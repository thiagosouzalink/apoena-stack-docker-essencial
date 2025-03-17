# 05 - Networking

## Comandos Sinatxe

`docker network create --driver bridge <nome_da_rede>`

`docker build -t <nome_da_imagem>:<tag> -f <nome_do_dockfile> <caminho_do_dockerfile>`

`docker run --name <nome_do_container> --network <nome_da_rede> <nome_da_imagem>`

`docker logs <nome_do_container>`

## Prática - Bridged

```bash
docker network create --driver bridge apoena-network
```

```bash
docker build -t apoena-server -f Dockerfile.server .
```

```bash
docker build -t apoena-client -f Dockerfile.client .
```

```bash
docker run --name apoena-server --network apoena-network apoena-server
```

```bash
docker run --name apoena-client --network apoena-network apoena-client
```

```bash
docker logs apoena-server
```
