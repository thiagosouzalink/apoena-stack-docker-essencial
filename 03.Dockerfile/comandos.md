# 03 - Dockerfile

## Build

Para construir uma imagem Docker a partir de um Dockerfile, use o seguinte comando:

```bash
docker build -t <nome_da_imagem>:<tag> <caminho_do_dockerfile>
```

## Run

Para rodar um container a partir de uma imagem, use o comando:

````bash
docker run --name <nome_do_container> <nome_da_imagem>
````

## Exemplo

``` bash
docker build -t apoena_iss_data_app .
```

```bash
docker run --name apoena-iss_data_app apoena_iss_data_app
```
