from minecraftmonitoring import Client, logger

logger(True)

client = Client('auth_token')

servers = client.servers()

client.edit_server(
    servers['Pink Quartz'],
    forced_title='Politic Server'
)