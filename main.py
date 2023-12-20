# Ver: https://code-maven.com/slides/python/fastapi-static-files-javascript
# Solucion en: https://github.com/tiangolo/fastapi/issues/4989 
#              https://fastapi.tiangolo.com/advanced/templates/#templates-and-static-files
#              https://github.com/JarroVGIT/fastapi-github-issues/tree/master/4989
#              https://stackoverflow.com/questions/61641514/css-not-recognized-when-served-with-fastapi


""" 
RUN: 
- uvicorn main:app
- uvicorn main:app --reload
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/record/static", StaticFiles(directory="webpages/record/static"), name="static")
app.mount("/js", StaticFiles(directory="webpages/record/js"), name="js")

templates = Jinja2Templates(directory="webpages")


@app.get("/", response_class=HTMLResponse)
async def coming_soon(request: Request):
    return templates.TemplateResponse("record/index.html", {"request": request})