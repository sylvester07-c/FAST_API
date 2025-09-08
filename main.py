from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randint  

app = FastAPI()


class Post(BaseModel):
    title: str
    post: str
# class Post(BaseModel):
#     title: str
#     content: str
#     rating: Optional[int] = None

    

# my_posts = [{"title":"My Post 1", "content":"This is my post content 1", "id":1}, {"title":"My Post 2", "content":"This is my post content 2", "id":2}]

# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p 
        
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i


@app.get("/")
async def root():
    return {"Hello": "mum"}


@app.get("/posts")
def get_post():
    return {"message": my_posts}


@app.post("/newPost")
async def new_post(new_post: Post):
    print(new_post)
    return {
    "data": "new_post"
    }

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_post(post: Post):
#     post_dict = post.dict() # Convert Pydantic model to dictionary 
#     post_dict["id"] = randint(0, 1000000000000)  # Assign a random ID for the new post
#     my_posts.append(post_dict)
#     return {"data": post_dict}

# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts)-1]
#     return {"detail": post}  

# @app.get("/posts/{id}")
# def get_post(id: int):
#     post = find_post(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail=f"post with id: {id} was not found")
 
#     return {"post_detail": post}

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     index = find_index_post(id)

#     if index == None:
#         raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"post with id: {id} does not exist")
#     my_posts.pop(index)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}")
# def update_post(id: int, post:Post):
#     print(post)
#     return{'message': "update post"}
