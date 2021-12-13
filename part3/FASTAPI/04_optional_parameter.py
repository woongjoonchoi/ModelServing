from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()

fake_db_items = {"pap" : "Foo" , "ssd" :  "BAR" , "qwer" : "modl"}

@app.get("/items/{item_id}")
def read_item(item_id  : str , q : Optional[str] = None ) :
    if item_id in fake_db_items.keys():
        if q :
            return {"item_id" : item_id , "q" : q}
        else :
            return {"item_id" : item_id}
    return {"key is not it the db"}


if __name__ == "__main__" :
    uvicorn.run(app, host = "0.0.0.0" , port = 8000)