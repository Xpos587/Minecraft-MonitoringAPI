from minecraftmonitoring import (
    Client,
    logger,
    markdown,
    params
)

logger(True)

client = Client('auth_token')

response = client.add_server(
    address='play.pinkquartz.ru',
    server_version='1.19.4',
    forced_title='Pink Quartz',
    description=f'Топовый сервер для {markdown.bold("политики")}. Лучший из лучших!\n\nЛюбим всех!',
    lure='Политический сервер!',
    params=[params.Survival, params.Economy, params.Clans]
)

print(client.servers())