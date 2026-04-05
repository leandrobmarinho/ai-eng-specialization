import nltk

nltk.download("punkt_tab")

text = "Hello, how are you? I'm fine, thank you."
tokens = nltk.word_tokenize(text)
print(tokens)