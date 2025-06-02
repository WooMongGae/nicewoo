# nicewoo

> 텍스트 전처리, 키워드 추출, 요약, 언어 감지 기능을 제공하는 Python 패키지

## ✨ 주요 기능

- `remove_stopwords(text, lang='en')`: NLTK 기반 불용어 제거
- `extract_keywords(text, top_n=5)`: TF-IDF 기반 키워드 추출
- `summarize(text, ratio=0.2)`: Gensim 또는 Sumy 기반 텍스트 요약
- `detect_language(text)`: langdetect 기반 언어 감지

## 📦 설치 방법

```bash
pip install nicewoo
