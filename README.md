# fastapi-with-mongodb
Try using FastAPI with MongoDB

### References
- MongoDB - [Getting Started with MongoDB and FastAPI](https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/)
  - Source code: [`mongodb-with-fastapi`](https://github.com/mongodb-developer/mongodb-with-fastapi) 
- testdriven.io - [Building a CRUD App with FastAPI and MongoDB](https://testdriven.io/blog/fastapi-mongo/)

### Set up
```bash
# Set MONGODB_URL environment variable:
export MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

# Start the service:
uvicorn main:app --reload
```
