# 07 - Processamento de Dados

## Comandos

1. **iniciar os serviços definidos em um arquivo `docker-compose.yaml`:**

```bash
docker-compose up -d
```

2. **Copiar arquivos ou diretórios do sistema local para dentro de um container Docker em execução. O parâmetro -L garante que o Docker copie o arquivo real, mesmo se houver links simbólicos.**

```bash
docker cp -L pyspark_job.py <nome_container>:/opt/bitnami/spark/pyspark_job.py
```

3. **Executar um comando (script Python com Spark) dentro do container:**

```bash
docker exec <nome_container> spark-submit --master spark://<id_container>:7077 pyspark_job.py
```

4. **Limpar o ambiente (remove todos os containers e redes) após a execução:**

```bash
docker-compose down
```
