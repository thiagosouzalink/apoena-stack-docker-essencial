# 06 - Docker Compose

## Comandos

1. **Navegar até a raiz do projeto, onde está o arquivo `docker-compose.yaml`**

2. **Iniciar os serviços definidos no arquivo `docker-compose.yaml` através do comando:**

```bash
docker-compose up
```

3. **Caso precise fazer alteração no código `Dockerfile` ou `app.py`, execute o comando abaixo:**

```bash
docker-compose build --no-cache
```

Este comando é utilizado para construir a imagem Docker para os serviços definidos no docker-compose.yaml.
A opção --no-cache força a reconstrução da imagem sem usar o cache de camadas anteriores.

4. **Para parar e remover os contêineres, redes, volumes e imagens associadas aos serviços definidos no `docker-compose.yml` utilize o comando:**

```bash
docker-compose down -v --rmi all
```
