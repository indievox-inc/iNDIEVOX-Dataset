![iNDIEVOX](https://raw.githubusercontent.com/indievox-inc/iNDIEVOX-Dataset/master/image/logo.png)

## Intro

[iNDIEVOX](https://www.indievox.com) open datasets, you can play machine learning algorithms with these datasets.

## Datasets

You can check out and listen to the music by song id, using the url format like: `https://www.indievox.com/song/song_id`. for example: [https://www.indievox.com/song/1](https://www.indievox.com/song/1)

### Buy Together Datasets

* [Buy Together Discs Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/buy_together_disc.dataset)
  * Each row is transaction that discs buys together, each column is the disc id number.
* [Buy Together Songs Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/buy_together_song.dataset)
  * Each row is transaction that songs buys together, each column is the song id number.

### Music Valence-Arousal Datasets

* [Valence Training Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/valence_train.dataset)
* [Valence Testing Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/valence_test.dataset)
  * The 1 - 68 columns are audio features(use PyAudio) and the last column is valence value.
* [Arousal Training Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/arousal_train.dataset)
* [Arousal Testing Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/arousal_test.dataset)
  * The 1 - 68 columns are audio features(use PyAudio) and the last column is arousal value.
* [Valence-Arousal Dataset Training Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/va_train_song_id.dataset)
* [Valence-Arousal Dataset Testing Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/va_test_song_id.dataset)

### Music Emotion Classification Datasets

* [Emotion Combine Training Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_combine_song_train.dataset)
* [Emotion Combine Testing Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_combine_song_test.dataset)
* [Relax Training Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_01_relax_train.dataset)
* [Relax Testing Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_01_relax_test.dataset)
* [Happy Training Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_02_happy_train.dataset)
* [Happy Testing Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_02_happy_test.dataset)
* [Excited Training Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_03_excited_train.dataset)
* [Exccited Testing Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_03_excited_test.dataset)
* [Blue Training Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_04_blue_train.dataset)
* [Blue Testing Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_04_blue_test.dataset)
* [Sad Training Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_05_sad_train.dataset)
* [Sad Testing Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_05_sad_test.dataset)
* [Angry Training Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_06_angry_train.dataset)
* [Angry Testing Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_06_angry_test.dataset)
    * The 1 - 68 columns are audio features(use PyAudio) and the last column is emotion category number.
* [Relax Training Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_01_relax_train_song_id.dataset)
* [Relax Testing Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_01_relax_test_song_id.dataset)
* [Happy Training Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_02_happy_train_song_id.dataset)
* [Happy Testing Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_02_happy_test_song_id.dataset)
* [Excited Training Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_03_excited_train_song_id.dataset)
* [Exccited Testing Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_03_excited_test_song_id.dataset)
* [Blue Training Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_04_blue_train_song_id.dataset)
* [Blue Testing Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_04_blue_test_song_id.dataset)
* [Sad Training Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_05_sad_train_song_id.dataset)
* [Sad Testing Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_05_sad_test_song_id.dataset)
* [Angry Training Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_06_angry_train_song_id.dataset)
* [Angry Testing Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_06_angry_test_song_id.dataset)

## Cool Things Made From These Datasets

## [VA Radio](https://www.indievox.com/radio/va) - Use Music Valence-Arousal Datasets

![VA Radio](https://raw.githubusercontent.com/indievox-inc/iNDIEVOX-Dataset/master/image/va_radio_demo.png)

---

## [Emotion Radio](https://www.indievox.com/radio/emotion/relax) - Use Music Emotion Classification Datasets

![Emotion Radio](https://raw.githubusercontent.com/indievox-inc/iNDIEVOX-Dataset/master/image/emotion_radio_demo.png)

---

## [Buy Together](https://www.indievox.com/disc/10586) - Use Buy Together Datasets

![Buy Together](https://raw.githubusercontent.com/indievox-inc/iNDIEVOX-Dataset/master/image/buy_together_demo.png)

---

## Algorithms and Feature Extraction

We play algorithms like [Gaussian SVM](https://en.wikipedia.org/wiki/Support_vector_machine) and [Ridge Regression](https://en.wikipedia.org/wiki/Tikhonov_regularization) to train ML models from the datasets. The algorithm library we use is [Fuku-ML](https://github.com/fukuball/fuku-ml), and feature extraction library is [PyAudio](https://github.com/jleb/pyaudio).

## iNDIEVOX MIR Open API

You can check out some data by using iNDIEVOX MIR Open API:

### Disc Profile API

* End Point: `https://www.indievox.com/api/mir/disc/profile/disc_id`
* HTTP Method: GET
* Example: https://www.indievox.com/api/mir/disc/profile/1?app_id=P300000045&app_secret=9bdecdb004682865260c9d2a5cc71f0d
* Response:

```json
{
    "response": {
        "status": {
            "version": "0.1",
            "code": "0",
            "error_type": "success",
            "message": "Success",
            "parameter": {
                "none": "none"
            }
        },
        "id": "1",
        "title": "感官駕馭",
        "description": "音樂人‧伍佰 夢幻而華麗的狂舞，激流般令人動容的氣度，讓人忍不住要站起來為他們鼓掌…… 樂評人‧翁嘉銘 不看歌詞，聽echo的《感官駕馭》，讓我驚豔。各器樂的的表現和技術都十分夠水準，品質很高，錄音及混色處理得很漂亮，音色純淨，且與情緒相貼，唱腔與吉他的關係是敵是友，是愛是恨，是靈肉的離離合合；編曲功力很強，每一首都有叫我忍不住要讚嘆的地方，好屌！ 序曲「It’s time to sing ; It’s time to get out」，人聲的吟哦、美語口白、吉他音牆等等營造超現實的迷離、奇幻，引人走向異境夢土。「限度」、「感官駕馭」衝勁十足，像是朗朗乾坤下的高速飛奔，光明的夢！「木雕輪盤」改為重鼻音的唱腔，是對世界旋轉與變幻的嘲弄與自我昏眩。「我將死去」、「剖（續繞）」，華麗的死亡歌德。「剖（續繞）」尾聲的鋼琴獨奏，讓我深感悽切。長達十分多鐘的「晚宴」，憂鬱的口白，多變的唱腔，加英倫搖滾狂飆，及教我耳朵飄舞的吉他彈奏，是場不肯散去的鬼魅夜宴！ 暫停我個人主觀的聽覺與想像力的飛馳及沉溺，echo的《感官駕馭》仍是我近來聽過最優的年輕滾搖樂團。儘管會想起是否受Radiohead、 Suede的影響，但在國內年輕樂團中，不以流行搖滾為尚，而以Grunge、Post-punk、Gothic、Black-metal為特色及意識主題的樂團，非常罕見！同時echo又擁有堅實的演出天分和音樂製作能力，帶給人迷幻、唯美的聽覺享受，是支風格獨卓，又令人迷戀的樂團。 1976主唱‧阿凱 「感官駕馭」這首暢快直接的4-5-6進行的搖滾，是第一次得見ECHO的音樂，這首歌以mp3格式傳遞，於是這個年輕的樂團開始在網路上被討論，他們當時的錄音器材是一台Roland880、練習的場地是清大成功湖旁邊的社團教室，平均年齡只有21歲，有驚人詞曲平衡和器樂演奏的技術，以上這些是物理的介紹，不足以形容我聽到這張專輯時的感動，在你將她放入CD PLAYER前，我要作這樣的預告，她的聲音優雅、墮落、龐大、而語言裡充滿這個世代對慘綠青春的迷惘和對物質跟形式主義的耽戀。從「木雕輪盤」開始，吉他手冠文跟鍵盤手新逸聯手鋪排在整張專輯中充斥的華美音牆。在「傾慕」裡直線進行的樂音，捕捉稍縱即逝的甜美，最愛的「我將死去」，柏蒼的文字跟從低沉到高亢的寬廣音域唱著對美的執著，在這麼多懷疑恐懼的每一天裡，只有不需要辯證的華美可以相信，為美心碎、為美而死，而我興奮的享受著這迷幻旅程帶來的窒息。 閃靈樂團主唱、TRA全國搖滾聯盟‧Freddy 絕大多數時間，我還是想當一個單純樂迷的角色，只因他們從99年至今，從未停止給我感動。 1999年六月，TRA在新竹某戶外廣場辦了一場「震盪風城」演唱會，據說那是新竹市第一次創作樂團的校外露天演唱會，演唱樂團邀請了「Echo」、「Freebird」、「亂黨」。 亂黨的歌曲收錄已於DIY合輯「夏恩的秘密」，Freebird，則曾在其他活動中看過他們演出。對於Echo，當時的我與當時的台北，沒聽過他們的音樂、不知道他們的來歷、不認識他們的名字。用很「倫理」的方式排了表演順序，不知名的Echo唱第一團。我，如往常為了活動忙進忙出。 一不小心，多聽了Echo幾分鐘，就停下腳步拒絕離開了。 當時Echo雖然許多環節都仍然生澀，風格也還未定型（我還記得他們當時給我的自我介紹表示，因為學校社團的多元走向，Echo什麼樂風都玩），然而他們作品中豐富而不矯揉的情感、流暢成熟的曲式構思，是難以埋沒，甚至震懾人的。 終於，發現了Echo，我開始主動邀請他們上台北演出，安排Echo參加1999年的野台開唱，他們雖一度遲疑，但我用斬釘截鐵的意志展現了誠意。台北搖滾圈不能代表台灣的搖滾樂團，但是台北的搖滾樂迷有權力聽到Echo的音樂。 1999～2001野台開唱、2001反中國併吞…等大大小小的演唱會，我開始不停止地安排Echo演出，而Echo的成熟、定型，亦讓我看得目不轉睛。喜歡Echo的人越來越多，Echo也開始著手進行越來越清楚的音樂計畫，我在旁偶有參與，但絕大多數時間，我還是想當一個單純樂迷的角色，只因他們從99年至今，從未停止給我感動。 一直到現在Echo的「感官駕馭」專輯，感動只會持續，不會停止… 四分衛‧虎神 有一種在黑夜中才能釋放的能量 不斷地流出 我無法在白天去面對祂 現代人已慢慢失去自省的本能 我欣賞柏蒼帶著懷疑 不安 失望的唱腔和用詞 而我 於是 是否 卻已 或許 依然……等 在在地透露對這繽紛的人世有著不凡的思緒 或許失望也是希望的開始吧 我的感官正敞開著 而你呢？趁著天未亮 進來Echo的世界吧！ 流氓樂團主唱‧阿德 如果，讓我他媽的再年輕個十歲，我是做不到這個樣子的音樂的。就算是現在的我，也可能會做得要死的辛苦。音樂進行到一首都還沒有結束時，我就知道我必須低下我一直高仰著的頭，衷心而誠懇的這麼告訴所有的人。 ECHO，幹！讓我汗顏。 很屌噢！?他媽的超屌喲。我說。 我知道你一定會想要問我：「屌在哪裡？」 呃！我必須承認，那是我這張屁眼似的嘴，所無法一一道盡的。不如，讓那些形容力比較強的人來為你解說哪。至於我跟你，就這樣吧；閉上我們只會放屁的屁眼，安靜而認真的，聽聽這張屌到不行的音樂吧！",
        "url": "https://www.indievox.com/disc/1",
        "icon_s": "https://d5cofyxrs7j5g.cloudfront.net/indievox_music/mp3/30000/1/1180X180.jpg?1476284342",
        "icon_m": "https://d5cofyxrs7j5g.cloudfront.net/indievox_music/mp3/30000/1/1480X480.jpg?1476284342",
        "icon_o": "https://d5cofyxrs7j5g.cloudfront.net/indievox_music/mp3/30000/1/1.jpg?1476284342",
        "release_date": "2002-01-11 00:00:00",
        "artist": "回聲樂團",
        "label": "回聲樂團",
        "type": "專輯",
        "genre": "另類",
        "play_num": "39813",
        "favorite_num": "33",
        "songs": [
            {
                "id": "2",
                "title": "It's Time To Sing, It's Time To Get Out",
                "order": "1",
                "artist_name": "回聲樂團"
            },
            {
                "id": "10",
                "title": "限度",
                "order": "2",
                "artist_name": "回聲樂團"
            },
            {
                "id": "11",
                "title": "感官駕馭",
                "order": "3",
                "artist_name": "回聲樂團"
            },
            {
                "id": "12",
                "title": "木雕輪盤",
                "order": "4",
                "artist_name": "回聲樂團"
            },
            {
                "id": "13",
                "title": "我將死去",
                "order": "5",
                "artist_name": "回聲樂團"
            },
            {
                "id": "14",
                "title": "錯置的共鳴",
                "order": "6",
                "artist_name": "回聲樂團"
            },
            {
                "id": "15",
                "title": "剖（續繞）",
                "order": "7",
                "artist_name": "回聲樂團"
            },
            {
                "id": "18",
                "title": "傾慕",
                "order": "8",
                "artist_name": "回聲樂團"
            },
            {
                "id": "23",
                "title": "晚宴",
                "order": "9",
                "artist_name": "回聲樂團"
            },
            {
                "id": "25",
                "title": "競逐孤寂",
                "order": "10",
                "artist_name": "回聲樂團"
            }
        ]
    }
}
```

### Song Profile API

* End Point: `https://www.indievox.com/api/mir/song/profile/song_id`
* HTTP Method: GET
* Example: https://www.indievox.com/api/mir/song/profile/11?app_id=P300000045&app_secret=9bdecdb004682865260c9d2a5cc71f0d
* Response:

```json
{
    "response": {
        "status": {
            "version": "0.1",
            "code": "0",
            "error_type": "success",
            "message": "Success",
            "parameter": {
                "none": "none"
            }
        },
        "id": "11",
        "title": "感官駕馭",
        "description": "",
        "lyric": "驀然間我又再次捲入這莫名的哀愁 迷樣的眼透露你的冷漠憔悴而雍容 蟄伏的心卻不知該如何掙脫 終究是個錯 於是我的在這失眠的夜仰望著星空 昏暗的天沒有一絲星火只剩無盡的沉默 寂靜的夜凝滯了我一身創痛 不願再追究 多少次我幻想這世界眩化成了夢 舉目所及的一切不過只是胡亂的拼湊 而一切 思緒交錯 情感煽動 只是知覺的暫留 是否 這是種錯 是否 是種淪落 是否 人們一直在尋求靈魂的解脫 驀然間我又再次捲入這莫名的哀愁 舉目所及的一切不過只是胡亂的拼湊 而一切 思緒交錯 情感煽動 只是知覺的暫留 是否 這是種錯 是否 是種淪落 是否 人們一直在尋求靈魂的解脫",
        "distribution_lyric": "感官駕馭 詞：柏蒼　曲：Echo回聲樂團 編曲：Echo回聲樂團　製作：Echo回聲樂團 驀然間我又再次捲入這莫名的哀愁 迷樣的眼透露你的冷漠憔悴而雍容 蟄伏的心卻不知該如何掙脫 終究是個錯 於是我的在這失眠的夜仰望著夜空 昏暗的天沒有一絲星火只剩無境的沉默 寂靜的夜凝滯了我一身創痛 不願再追究 多少次我幻想這世界眩化成了夢 舉目所及的一切不過只是胡亂的拼湊 而一切 思緒交錯 情感煽動 只是知覺的暫留 是否 這是種錯 是否 是種淪落 是否 人們一直在尋求靈魂的解脫 驀然間我又再次捲入這莫名的哀愁 舉目所及的一切不過只是胡亂的拼湊 而一切 思緒交錯 情感煽動 只是知覺的暫留 是否 這是種錯 是否 是種淪落 是否 人們一直在尋求靈魂的解脫 多少次我幻想這世界眩化成了夢 舉目所及的一切不過只是胡亂的拼湊 而一切 思緒交錯 情感煽動 只是知覺的暫留 是否 這是種錯 是否 是種淪落 是否 人們一直在尋求靈魂的解脫 ",
        "disc_id": "1",
        "disc_title": "感官駕馭",
        "url": "https://www.indievox.com/song/11",
        "icon_s": "https://d5cofyxrs7j5g.cloudfront.net/indievox_music/mp3/30000/1/1180X180.jpg?1476284342",
        "icon_m": "https://d5cofyxrs7j5g.cloudfront.net/indievox_music/mp3/30000/1/1480X480.jpg?1476284342",
        "icon_o": "https://d5cofyxrs7j5g.cloudfront.net/indievox_music/mp3/30000/1/1.jpg?1476284342",
        "release_date": "2002-01-11 00:00:00",
        "artist": "回聲樂團",
        "label": "",
        "genre": "另類",
        "order": "3",
        "play_num": "8485",
        "favorite_num": "24"
    }
}
```

### Song Feature API

* End Point: `https://www.indievox.com/api/mir/song/feature/song_id`
* HTTP Method: GET
* Example: https://www.indievox.com/api/mir/song/feature/11?app_id=P300000045&app_secret=9bdecdb004682865260c9d2a5cc71f0d
* Response:

```json
{
    "response": {
        "status": {
            "version": "0.1",
            "code": "0",
            "error_type": "success",
            "message": "Success",
            "parameter": {
                "none": "none"
            }
        },
        "pyaudio_features": {
            "all_features": "0.0971759507135 0.0522725538704 3.17837362526 0.169258223221 0.17761035192 0.956228257289 0.00502509712693 0.15608936237 -23.6492579746 1.07222239967 0.336302239542 0.346820087768 0.267659221286 0.283131088133 0.0937656447511 0.190683174147 0.0362026961856 0.0154396113281 -0.080628347938 -0.0335169517947 -0.0172362351962 0.00933555817031 0.00440588436309 0.0226880679292 0.00346651693534 0.00848391347293 0.0387006059329 0.00285731291516 0.0075745323209 0.0113387577205 0.00312870958828 0.0630765949414 0.00539453270726 0.0234939667419 0.0388878660983 0.032719504648 0.0973890238214 0.0310548057682 0.0207616842225 0.360788439164 0.0039994659012 0.0732569790969 0.606494590366 0.396489250405 0.377790168339 0.340543113059 0.318868500154 0.296211429293 0.288706367957 0.291934277393 0.2817686425 0.267312934278 0.276718296308 0.262986572635 0.239627809016 0.00821930036552 0.00426701380194 0.0151380889354 0.00356899202712 0.00880067083913 0.0253754848463 0.00266806262546 0.00760638100511 0.00953443383664 0.00379062135346 0.0356637684404 0.00530143698976 0.00834938484723",
            "beat_per_minute": "240",
            "zero_crossing_rate_avg": "0.097175950713526",
            "energy_avg": "0.052272553870389",
            "entropy_energy_avg": "3.1783736252579",
            "spectral_centroid_avg": "0.16925822322053",
            "spectral_spread_avg": "0.17761035192008",
            "spectral_entropy_avg": "0.95622825728928",
            "spectral_flux_avg": "0.0050250971269303",
            "spectral_rolloff_avg": "0.15608936236969",
            "mfcc_avg": "-23.6492579746 1.07222239967 0.336302239542 0.346820087768 0.267659221286 0.283131088133 0.0937656447511 0.190683174147 0.0362026961856 0.0154396113281 -0.080628347938 -0.0335169517947 -0.0172362351962",
            "chroma_avg": "0.00933555817031 0.00440588436309 0.0226880679292 0.00346651693534 0.00848391347293 0.0387006059329 0.00285731291516 0.0075745323209 0.0113387577205 0.00312870958828 0.0630765949414 0.00539453270726",
            "chroma_deviation_avg": "0.023493966741931",
            "zero_crossing_rate_std": "0.038887866098328",
            "energy_std": "0.032719504647986",
            "entropy_energy_std": "0.097389023821389",
            "spectral_centroid_std": "0.031054805768216",
            "spectral_spread_std": "0.020761684222522",
            "spectral_entropy_std": "0.36078843916354",
            "spectral_flux_std": "0.0039994659011968",
            "spectral_rolloff_std": "0.073256979096945",
            "mfcc_std": "0.606494590366 0.396489250405 0.377790168339 0.340543113059 0.318868500154 0.296211429293 0.288706367957 0.291934277393 0.2817686425 0.267312934278 0.276718296308 0.262986572635 0.239627809016",
            "chroma_std": "0.00821930036552 0.00426701380194 0.0151380889354 0.00356899202712 0.00880067083913 0.0253754848463 0.00266806262546 0.00760638100511 0.00953443383664 0.00379062135346 0.0356637684404 0.00530143698976",
            "chroma_deviation_std": "0.0083493848472264",
            "valence": "0.524623981184",
            "arousal": "0.944871467253"
        },
        "echonest_features": {
            "music_key": "4",
            "music_key_conf": "0.57",
            "mode": "0",
            "mode_conf": "0.532",
            "tempo": "127.193",
            "tempo_conf": "0.839",
            "time_signature": "4",
            "time_signature_conf": "1",
            "second": "317",
            "timbre_avg_vector": "53.000708571429,83.903382857143,19.652016190476,-11.481799047619,14.575156190476,-31.027503809524,-3.5456333333333,4.0158438095238,-6.6611504761905,0.90558190476191,-6.555819047619,-6.0241523809524",
            "timbre_std_vector": "2.2437992019662,30.054924824431,20.511796781874,20.711084167386,20.256416531608,14.588555782638,17.403297106063,19.008881610459,13.303719162048,14.424715695816,9.1276936356043,10.218610937897",
            "pitch_avg_vector": "0.42659428571429,0.3667019047619,0.43713523809524,0.35160666666667,0.4679419047619,0.20341904761905,0.2689419047619,0.38015142857143,0.24760476190476,0.35445619047619,0.2417,0.3813219047619",
            "pitch_std_vector": "0.31850753181427,0.26307702876906,0.3204293187711,0.25355598835566,0.35199192329784,0.15828669076054,0.20466488095161,0.29735452727863,0.19290104986564,0.28384826315557,0.19360720236703,0.28206205024254",
            "valence": "0.51938513171414",
            "arousal": "0.91460427926648",
            "liveness": "0.30945348815736",
            "acousticness": "0.0017703628769506",
            "loudness": "-5.457",
            "speechiness": "0.036107564685294"
        }
    }
}
```

## How to extract features from your songs?

If you don't know how to extract features by using [PyAudio](https://github.com/jleb/pyaudio), you can use iNDIEVOX to extract features for you. But before uploading songs to iNDIEVOX, **you should make sure that you have the rights to upload the songs**.

#### Step 1. Upload your songs on [iNDIEVOX](https://www.indievox.com).

#### Step 2. Set the songs public.

#### Step 3. Wait 1 - 3 days for iNDIEVOX to extract features.

#### Step 4. Done, you can use [iNDIEVOX MIR Open API](https://github.com/indievox-inc/iNDIEVOX-Dataset#indievox-mir-open-api) to check out the resul

## How to contribute?

All the data are labeled by experts, and you can be one of the experts. Just contribute!

#### Step 1. Listen to the music on [iNDIEVOX](https://www.indievox.com).

#### Step 2. Label the song in mind.

For emotion, int value from 1 - 6, 1 stands for relax, 2 stands for happy, 3 stands for excited, 4 stands for blue, 5 stands for sad, 6 stands for angry.

For valence, float value from 0 - 1, 0 means very negative mood, 1 means very positive mood, so if you feel a little happy, you can label 0.68.

For arousal, float value from 0 - 1, 0 means very low energy mood, 1 means very high engergy mood, so if you feel excited, you can label 0.89.

#### Step 3. Put data into dataset.

Find the song id on url and find the song feature using [iNDIEVOX MIR Open API](https://github.com/indievox-inc/iNDIEVOX-Dataset#indievox-mir-open-api), then put the data into the right dataset you labeled in your mind.

#### Step 4. Send pull request.

## Credits

These guys below contributed with content and more. Come join us and put yourself down below ;)

- [@fukeball](https://github.com/fukuball)
- [@JudyTai](https://github.com/JudyTai)
