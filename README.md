![iNDIEVOX](https://raw.githubusercontent.com/indievox-inc/iNDIEVOX-Dataset/master/image/logo.png)

## Intro

iNDIEVOX open datasets, you can play machine learning algorithms with these datasets.

## Datasets

You can check out and listen to the music by song id, using the url format like: `https://www.indievox.com/song/song_id`. for example: [https://www.indievox.com/song/1](https://www.indievox.com/song/1)

### Music Valence-Arousal Datasets

* [Valence-Arousal Dataset Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/va_song_id.dataset) - Top 200 song ids are for testing and the other 800 song ids are for training.
* [Valence Training Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/valence_train.dataset) - Top 68 columns are audio features(use pyaudio) and the last column is valence value.
* [Valence Testing Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/valence_test.dataset) - Top 68 columns are audio features(use pyaudio) and the last column is valence value.
* [Arousal Training Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/arousal_train.dataset) - Top 68 columns are audio features(use pyaudio) and the last column is arousal value.
* [Arousal Testing Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/arousal_test.dataset) - Top 68 columns are audio features(use pyaudio) and the last column is arousal value.

### Music Classification Datasets

* [Relax Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_01_relax_song_id.dataset) - Top 10 song ids are for testing and the other 60 song ids are for training.
* [Happy Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_02_happy_song_id.dataset) - Top 10 song ids are for testing and the other 60 song ids are for training.
* [Excited Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_03_excited_song_id.dataset) - Top 10 song ids are for testing and the other 60 song ids are for training.
* [Blue Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_04_blue_song_id.dataset) - Top 10 song ids are for testing and the other 60 song ids are for training.
* [Sad Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_05_sad_song_id.dataset) - Top 10 song ids are for testing and the other 60 song ids are for training.
* [Angry Song ID List](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_06_angry_song_id.dataset) - Top 10 song ids are for testing and the other 60 song ids are for training.
* [Emotion Training Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_song_train.dataset) - Top 68 columns are audio features(use pyaudio) and the last column is emotion category number.
* [Emotion Testing Dataset](https://github.com/indievox-inc/iNDIEVOX-Dataset/blob/master/dataset/emotion_song_test.dataset) - Top 68 columns are audio features(use pyaudio) and the last column is emotion category number.

## Algorithms and Feature Extraction

We play algorithms like [Gaussian SVM](https://en.wikipedia.org/wiki/Support_vector_machine) and [Ridge Regression](https://en.wikipedia.org/wiki/Tikhonov_regularization) to train data from the datasets. The algorithm library we use is [Fuku-ML](https://github.com/fukuball/fuku-ml), and feature extraction library is [PyAudio](https://github.com/jleb/pyaudio).

## Made From These Datasets
