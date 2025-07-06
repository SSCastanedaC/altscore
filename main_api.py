from fastapi import FastAPI, status, HTTPException
from fastapi.responses import HTMLResponse

from e7 import systems, get_system
from e9 import get_volumes

app = FastAPI()

system = None

@app.get("/phase-change-diagram/")
def api_get_volumes(pressure: int):
    return get_volumes(pressure)

@app.get("/status/")
def api_get_system():
    global system
    system = get_system()
    return {
        "damaged_system": system
    }

@app.get("/repair-bay/")
def api_repair_bay():
    code = ""
    if system:
        print(system)
        code = systems[system]
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
        <div class="anchor-point">{code}</div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/teapot/")
def api_teapot():
    raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail="I'm a teapot.")
