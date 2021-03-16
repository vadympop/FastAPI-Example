import uvicorn

if __name__ == "__main__":
    uvicorn.run("fae.api.v1.app.main:app", port=5000, reload=True)