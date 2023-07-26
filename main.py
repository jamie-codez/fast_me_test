from uvicorn import run

if __name__ == "__main__":
    run("app.posts:app", host="0.0.0.0", port=8001, reload=True)
