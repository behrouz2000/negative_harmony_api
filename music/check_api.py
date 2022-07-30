import check_negative

from fastapi import FastAPI

app = FastAPI()


@app.get("/negative/{chord}")
def get_negative_chord(chord: str):
    return check_negative.get_negative_chord(chord)



