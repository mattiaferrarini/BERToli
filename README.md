# BERToli 🎶🇮🇹

## About the model

BERToli is a BERT model for Italian song lyrics. It was obtained via continued pretraining of [`dbmdz/bert-base-italian-xxl-cased`](https://huggingface.co/dbmdz/bert-base-italian-xxl-cased) on ~106k Italian song lyrics from the [Genius Song Lyrics Dataset](https://www.kaggle.com/datasets/carlosgdcj/genius-song-lyrics-with-language-information).
The objective was Masked Language Modeling (MLM). 

The model is available on [Hugging Face](https://huggingface.co/mattiaferrarini/BERToli).

## Evaluation

The base model and the adapted model were tested on a held-out set of ~6k songs with the following results:

| Model | MLM Loss | Perplexity |
|----------|----------|----------|
| Base    | 1.94    | 6.95    |
| **BERToli**    | **1.45**    | **4.26**    |

**Evaluation of the learned representations will be made available in the future, once a suitable dataset has been created / identified.**

## Why BERToli?

[Pierangelo Bertoli](https://en.wikipedia.org/wiki/Pierangelo_Bertoli) (5 November 1942 – 7 October 2002) was an Italian singer-songwriter and poet.

## How to run the code

1. Clone the repository:
```
git clone https://github.com/mattiaferarrini/BERToli.git
```

2. Download the [Genius Song Lyrics Dataset](https://www.kaggle.com/datasets/carlosgdcj/genius-song-lyrics-with-language-information) in the folder and unzip it.

3. Filter and format the extracted CSV into a JSON file:
```
python cleaner.py song_lyrics.csv italian_songs.json
```

4. Split the songs into train, validation and test sets:
```
python splitter.py italian_songs.json
```

5. Run the `bertoli.ipynb` notebook to train and evaluate the model step by step.
