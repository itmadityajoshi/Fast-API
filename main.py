from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {'detail':{'name':'masis'}}


@app.get("/about")
def about():
    return{'Name':"This about API from FastAPI."}