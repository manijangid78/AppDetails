from fastapi import FastAPI
from authentication.routers import auth

articles = []
app = FastAPI()

app.include_router(auth.router, prefix="/auth")

# @app.get("/articles", response_model=List[Article])
# async def read_articles():
#     return articles
#
# @app.post("/articles", response_model=Article)
# async def create_article(article: Article):
#     articles.append(article)
#     return article
#
# @app.put("/articles/{article_id}", response_model=Article)
# async def update_article(article_id:int, article:Article):
#     articles[article_id] = article
#     return article
#
# @app.delete("/article/{article_id}")
# async def deleteArticle(article_id:int):
#     del articles[article_id]
#     return {"message": "Article deleted"}

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}