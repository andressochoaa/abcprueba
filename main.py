from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get("/characters")
async def get_characters():
    url = "https://rickandmortyapi.com/api/character"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("...")
        raise HTTPException(status_code=response.status_code, detail="Error al obtener informacion de la API")
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5500)