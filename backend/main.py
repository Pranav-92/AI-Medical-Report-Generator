from fastapi import FastAPI
from routes.analyze import router as analyze_router
from routes.explain import router as explain_router

app = FastAPI(title="Medical Report AI")

app.include_router(analyze_router)
app.include_router(explain_router)

@app.get("/")
def root():
    return {"status": "Medical AI Backend Running"}
