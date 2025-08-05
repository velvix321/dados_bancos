from fastapi import FastAPI
import random

app = FastAPI()

frases= [
    "acredite em você"
    "cada dia e uma nova chance!"
    "você e mais forte do que imagina"
    "persistencia e o caminho do sucesso"
    "nao desista ate se orgulhar"
]
@app.get("/frase")
def get_frase():
    frase_aleatoria = random.choice(frases)
    return{"frase": frase_aleatoria}