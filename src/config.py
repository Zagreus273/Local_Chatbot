import os
PROMPT_TEMPLATE= """
If the question is related to the content of the provided CSV document, use the following context to answer concisely and accurately. If the question is not related to the CSV content, answer based on your general knowledge:

{context}

---

Answer the question based on the above context in a brief: {question}
"""


class CONFIG:
    # "mxbai-embed-large"
    EMBEDDING_MODEL = "nomic-embed-text"
    script_dir = os.path.dirname(os.path.abspath(__file__))

    DATA_PDF_PATH = script_dir + "/data/"
    CHROMA_PATH = script_dir + "/chroma"
    OLLAMA_RESPONSE_MODEL = "qwen3:4b"
    TOP_K = 3
    
