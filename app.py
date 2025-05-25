from fastapi import FastAPI
from sozlarmanosi import sozlar_manosi

app = FastAPI(
    title="So'zlar Manosi API",
    description="So'zlar Manosi API",
    version="1.0.0",
    docs_url='/',
    redoc_url='/docs',
)

@app.get("/api/v1/so'zlarmanosi/{soz}", tags=["So'zlar Manosi"])
async def manosi(soz: str):
    return await sozlar_manosi(soz)
