from fastapi import FastAPI, HTTPException
from manager_retrieval import ManagerRetrieval

app = FastAPI()
manager = ManagerRetrieval()

@app.get("/")
def get_root():
    return {'Hello':'World'}


#Read
#All antisemitic
@app.get("/get_antisemitic")
async def get_antisemitic():
    try:
        res = manager.get_all_data("antisemitic")
        return {"result":res}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail={"error": str(e)})

#Read
#All ont_antisemitic
@app.get("/get_not_antisemitic")
async def get_antisemitic():
    try:
        res = manager.get_all_data("not_antisemitic")
        return {"result":res}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail={"error": str(e)})