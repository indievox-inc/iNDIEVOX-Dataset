# encoding=utf8

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import os
from gensim import corpora, models, similarities
from six import iteritems
import uniout

input_train_data_file = os.path.join(os.path.join(os.getcwd(), os.path.dirname(__file__)), 'dataset/lyrics.dataset')

dictionary = corpora.Dictionary(document.split() for document in open(input_train_data_file))
stoplist = set("我 你 妳 我們 在 了 都 不 的 是 有 沒有 要 不要 讓 也 人 說 就 著 這 他 她 祢 阮 攏 咱 那 啦 喔 啊 吧 嗎 嘩啦啦 會 能 卻 這樣 和 好 做 詞 曲 ㄟ % - ， ’ ( ) （ ） : ： . 。 ！ ! 、 ～ ~ / i you the to me my be don't it your and t a s oh go da la".split())
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
            if stopword in dictionary.token2id]
dictionary.filter_tokens(stop_ids)
dictionary.compactify()
dictionary.save('lyrics.dict')

texts = [[word for word in document.split() if word not in stoplist]
         for document in open(input_train_data_file)]

# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
         for text in texts]

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('lyrics.mm', corpus)

##################

if (os.path.exists("lyrics.dict")):
    dictionary = corpora.Dictionary.load('lyrics.dict')
    corpus = corpora.MmCorpus('lyrics.mm')
    print("Used files generated from first tutorial")
else:
    print("Please run first tutorial to generate data set")

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=10)
corpus_lsi = lsi[corpus_tfidf]

lsi.save('lyrics.lsi')
lsi = models.LsiModel.load('lyrics.lsi')

##################

dictionary = corpora.Dictionary.load('lyrics.dict')
corpus = corpora.MmCorpus('lyrics.mm')

lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=10)

doc = "望著 滿天星斗 的 塗鴉 好像 看見 自己 童年 的 模樣 總是 說 著 淘氣 浪漫 的 願望 夢想 能夠 飛往 燦爛 的 天堂 而 那天 真的 心願 正 溫柔 地 對 我 說 當你 陷入 絕望 中請 記得 我 用 美麗 的 幻想 讓 真心 永遠 純真 而 不變 當你 寂寞 的 時候 請 想念 我 用 單純 的 信仰 給 自己 溫暖 的 回答 閉上 雙眼 靜靜地 徜徉 彷彿 穿越時空 回到 了 過往 以為 銀河 就 在 不遠 的 前方 星星 月亮 都 在 我 面前 玩耍 而 那 微小 的 喜悅 正 溫柔 地 對 我 說 當你 陷入 絕望 中請 記得 我 用 美麗 的 幻想 讓 真心 永遠 純真 而 不變 當你 寂寞 的 時候 請 想念 我 用 單純 的 信仰 給 自己 溫暖 的 回答 ( 和 童 年時 無邪 的 希望 ) 親愛 的 我 親愛 的 我 願 你 永遠 像 我 一樣 帶著 勇氣 和 倔強 歲月 改變 你 的 模樣 無法 改變 你 的 去向"
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow]

index = similarities.MatrixSimilarity(lsi[corpus], num_features=500)
index.save('lyrics.index')

sims = index[vec_lsi]

sims = sorted(enumerate(sims), key=lambda item: -item[1])
print(sims[:10])
