from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"mensagem": "Servidor FastAPI no Render está rodando!"}

@app.post("/webhook/kommo")
async def kommo_webhook(request: Request):
    data = await request.json()
    print("Webhook recebido do Kommo:", data)

    # depois a gente trata isso (IA + resposta pro cliente)
    return {"status": "ok"}
