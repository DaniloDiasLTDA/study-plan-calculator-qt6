import json
import logging

from pathlib import Path
import asyncio
from aiohttp import web

ROOT_PATH = Path('.')

logger = logging.getLogger(__name__)

def find_json_file(file_name):
    """
    Encontra o caminho completo de um arquivo JSON dentro da pasta 'data'.

    Args:
        nome_arquivo (str): O nome do arquivo JSON a ser encontrado.

    Returns:
        pathlib.Path ou None: O objeto Path do arquivo JSON se encontrado,
                                None caso contrário.
    """

    data_file = ROOT_PATH / 'data'

    file_path = data_file / file_name
    if file_path.exists() and file_path.is_file() and file_path.suffix == '.json':
        return file_path
    else:
        return None


async def open_clients():
    file_path = find_json_file('clientes.json')
    with open(file_path, 'r') as f:
          return json.load(f)

async def reader_client(request):
    client_id = request.match_info.get('cliente_id')
    if not client_id:
        return web.json_response({"erro": "ID do cliente não fornecido"}, status=400)

    try:
        data = await open_clients()
    except FileNotFoundError:
        return web.json_response({"erro": "Arquivo clientes.json não encontrado"}, status=404)

    client = data.get(client_id)
    if client:
        return web.json_response(client)
    else:
        return web.json_response({"erro": f"Cliente com ID {client_id} não encontrado"}, status=404)

async def reader_email(request):
    client_id = request.match_info.get('cliente_id')
    if not client_id:
        return web.json_response({"erro": "ID do cliente não fornecido"}, status=400)

    try:
        data = await open_clients()
    except FileNotFoundError:
        return web.json_response({"erro": "Arquivo clientes.json não encontrado"}, status=404)

    client = data.get(client_id)
    if client:
        return web.json_response(client['email'])
    else:
        return web.json_response({"erro": f"Cliente com ID {client_id} não encontrado"}, status=404)   
    
async def main():
    app = web.Application()
    app.add_routes([web.get('/clientes/{cliente_id}', reader_client)])
    app.add_routes([web.get('/clientes/email/{cliente_id}', reader_email)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    logger.info("Servidor rodando em http://localhost:8080")
    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Servidor interrompido.")