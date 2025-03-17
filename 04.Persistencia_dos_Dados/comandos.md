# 04 - Persistências dos Dados

## Comandos Sintaxe

```bash
docker build -t <nome_da_imagem>:<tag> <caminho_do_dockerfile>
```

```bash
docker run --name <nome_do_container> -v <diretorio_local>:/<diretorio_no_container> <nome_da_imagem>
```

```bash
docker volume create <nome_do_volume>
```

## Prática Binds - Write

```bash
docker build -t apoena-iss-tracker-bind-mount .
```

``` bash
docker run --name apoena-iss-container-bind-mount -v <diretorio_local_bind_mount>:/app/data apoena-iss-tracker-bind-mount
```

## Prática Binds - Read

```bash
docker build -t apoena-iss-data-reader .
```

```bash
docker run --name apoena-iss-data-reader -v <diretorio_local_bind_mount>:/app/data apoena-iss-data-reader
```

## Prática Volumes

```bash
docker build -t apoena-sqlite-database .
```

```bash
docker volume create apoena-sqlite-db-python
```

```bash
docker run --name apoena-sqlite-python -it -v apoena-sqlite-db-python:/app/data apoena-sqlite-database
```
