import asyncio
import json
import websockets

# Endereço do servidor WebSocket
SERVER_URI = "ws://localhost:8000"

class Client:
    def __init__(self, app):
        self.app = app

    async def connect(self):
        async with websockets.connect(SERVER_URI) as websocket:
            while True:
                try:
                    # Obtém a localização atual do usuário do aplicativo Kivy
                    location = self.app.gps_location.split("=")[1]

                    # Cria uma mensagem JSON com a localização e o tipo de mensagem
                    message = json.dumps({
                        "type": "location",
                        "location": location
                    })

                    # Envia a mensagem para o servidor
                    await websocket.send(message)

                except Exception as e:
                    print(f"Erro ao enviar mensagem: {e}")
                    break

                # Espera um segundo antes de enviar a próxima mensagem
                await asyncio.sleep(1)

    async def run(self):
        while True:
            try:
                # Tenta conectar com o servidor
                await self.connect()

            except Exception as e:
                print(f"Erro ao conectar com o servidor: {e}")

            # Espera 10 segundos antes de tentar conectar novamente
            await asyncio.sleep(10)
