#Lib's
import uvicorn
#Classes
from routes import app

app = app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)