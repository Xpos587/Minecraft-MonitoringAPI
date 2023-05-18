from mmonitoring import Client, logger

logger(True)

client = Client('auth_token')

servers = client.servers()

for server in servers:
    client.remove_server(servers[server])

print('Old server list:', servers)
print('New server list:', client.servers())