from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {'detail':{'name':'masis'}}


@app.get("/about")
def about():
    return{'Name':"This about API from FastAPI."}


@app.get('/show'/{id})
def show(id:int):
    return {'data':{id}}


@app.get('/blog/{id}')
def particular_blog(id:int):
    return {'data':{'blog':id}}


@app.get('blog/comments/{id}')
def particular_blog(id:int):
    return {'data':{'blog':{'comment':{id}}}}