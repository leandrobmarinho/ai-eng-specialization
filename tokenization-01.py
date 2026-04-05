import nltk

nltk.download("punkt_tab")

text = "Machine learning é um campo da inteligência artificial que permite que computadores aprendam padrões a partir de dados. Sem serem explicitamente programados."
work_tokens = nltk.word_tokenize(text)
print(work_tokens)

setence_tokens = nltk.sent_tokenize(text)
print(setence_tokens)


documents = [
    "Machine learning é o aprendizado automático de máquinas a partir de dados.",
    "Ele permite que sistemas façam previsões e decisões sem programação explícita.",
    "É usado em áreas como reconhecimento de voz, imagens e recomendação de conteúdo.",
]


def preprocess(text: str) -> list[str]:
    tokens = nltk.word_tokenize(text.lower())
    return [token for token in tokens if token.isalpha()]


documents
preprocessed_documents = [" ".join(preprocess(doc)) for doc in documents]
print(preprocessed_documents)
