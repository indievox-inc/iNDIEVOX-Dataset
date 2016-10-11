![iNDIEVOX](https://raw.githubusercontent.com/indievox-inc/iNDIEVOX-Dataset/master/image/logo.png)

## Intro

iNDIEVOX open datasets, you can play machine learning algorithms with these datasets.

## Datasets

You can check out and listen to the music by song id, using the url format like: `https://www.indievox.com/song/song_id`. for example: [https://www.indievox.com/song/1](https://www.indievox.com/song/1)

### Music Valence-Arousal Datasets

* [Valence-Arousal Dataset Training Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/va_train_song_id.dataset)
* [Valence-Arousal Dataset Testing Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/va_test_song_id.dataset)
* [Valence Training Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/valence_train.dataset) - The 1 - 68 columns are audio features(use pyaudio) and the last column is valence value.
* [Valence Testing Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/valence_test.dataset) - The 1 - 68 columns are audio features(use pyaudio) and the last column is valence value.
* [Arousal Training Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/arousal_train.dataset) - The 1 - 68 columns are audio features(use pyaudio) and the last column is arousal value.
* [Arousal Testing Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/arousal_test.dataset) - The 1 - 68 columns are audio features(use pyaudio) and the last column is arousal value.

### Music Emotion Classification Datasets

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
* [Emotion Combine Training Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_combine_song_train.dataset) - The 1 - 68 columns are audio features(use pyaudio) and the last column is emotion category number.
* [Emotion Combine Testing Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_combine_song_test.dataset) - The 1 - 68 columns are audio features(use pyaudio) and the last column is emotion category number.
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

### Buy Together Datasets

* [Buy Together Discs](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/buy_together_disc.dataset) - Each row is transaction that discs buys together, each column is the disc id number.
* [Buy Together Songs](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/buy_together_song.dataset) - Each row is transaction that songs buys together, each column is the song id number.

## Algorithms and Feature Extraction

We play algorithms like [Gaussian SVM](https://en.wikipedia.org/wiki/Support_vector_machine) and [Ridge Regression](https://en.wikipedia.org/wiki/Tikhonov_regularization) to train ML models from the datasets. The algorithm library we use is [Fuku-ML](https://github.com/fukuball/fuku-ml), and feature extraction library is [PyAudio](https://github.com/jleb/pyaudio).

## Made From These Datasets

## [VA Radio](https://www.indievox.com/radio/va) - Use Music Valence-Arousal Datasets

![VA Radio](https://raw.githubusercontent.com/indievox-inc/iNDIEVOX-Dataset/master/image/va_radio_demo.png)

---

## [Emotion Radio](https://www.indievox.com/radio/emotion/relax) - Use Music Emotion Classification Datasets

![Emotion Radio](https://raw.githubusercontent.com/indievox-inc/iNDIEVOX-Dataset/master/image/emotion_radio_demo.png)

---

## [Buy Together](https://www.indievox.com/disc/10586) - Use Buy Together Datasets

![Buy Together](https://raw.githubusercontent.com/indievox-inc/iNDIEVOX-Dataset/master/image/buy_together_demo.png)

---
