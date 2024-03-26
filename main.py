from fastapi import FastAPI, Request, Response,Header,HTTPException

app = FastAPI()

API_KEY = "KOCAK"

@app.get('/')

def getHome():
    return{"message": "this is my place,welcome"
           }

@app.get('/see-headers')
def readHeaders(request:Request):
    headers = request.headers

    return{ "message":"isi headers",
           "headers":headers.get("user-agent")
           }

@app.get("/example")
def read_example_headers(request: Request):
    headers = request.headers
    # Access specific header values
    user_agent = headers.get("user-agent")
    authorization = headers.get("authorization")
    custom_header = headers.get("custom-header")

    return {
        "User-Agent": user_agent,
        "Authorization": authorization,
        "Custom-Header": custom_header
    }

@app.get("/example2")
def example_endpoint():
    content = "Hello, this is the response content."

    # Create a Response object and set custom headers
    response = Response(content=content)
    response.headers["X-Custom-Header"] = "This is custom value"
    response.headers["Authorization"] = "pass_token_1234"

    return response

@app.get("/protected")
def protect(api_key: str = Header(None)):

  if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

  return {"message":"This endpoint is protected by API Token Key.",
          "data":{"1":{"username":"fahmi","password":"1234"},
                  "2":{"username":"raka","password":"abcd123"},
                  "3":{"username":"rachman","password":"h8teacher"}
                 }
          }