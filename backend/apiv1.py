from fastapi import FastAPI, UploadFile, File, HTTPException,Request
import yaml
import os

api = FastAPI()


# @api.get("/greeting")
# def greet():
#     name = os.environ.get("GREET_NAME", "")
#     return {"msg": f"Hello {name}!"}


@api.get("/",status_code=200)
def greet():
    return {"msg": "CWiCKS Assessment"}
   

@api.get("/cc",status_code=200)
def conv():
    return "POST to this endpoint with JSON to convert to YAML"


@api.post("/cc")
async def get_body(request: Request):
    try:
        req_info = await request.json()
        return {
            "status": "SUUCCESS",
            "data"  : req_info
        }
        return await request.json()
    except Exception as e:
        raise HTTPException(
            status_code=400, detail={"message": "Error", "detail": str(e)}
        )

    


