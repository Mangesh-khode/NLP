import numpy as np
def get_vec(embeddings,word):
    m=len(words)
    x=np.zeroes((1,300))
    for word in words:
        english=word
        eng_emb=embeddings([english])
        x=np.row_stack((x,eng_emb))
    x=x[1: , : ]
    return x