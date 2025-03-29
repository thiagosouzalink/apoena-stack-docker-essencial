# 09 - Segurança e Monitoramento

## Comandos

1. **criando e executando os containers:**

```bash
docker run -d --name container1 busybox sh -c "while true; do sleep 1; done"
```

```bash
docker run -d --name container2 busybox sh -c "while true; do sleep 1; done"
```

```bash
docker run -d --name container3 busybox sh -c "while true; do echo $((2*30)) 1; done"
```

2. **Exibe informações de uso de recursos (CPU, memória, rede e disco) em tempo real para todos os containers.:**

```bash
docker stats
```

3. **exibe o uso de CPU de todos os containers em execução de forma personalizada:**

```bash
docker stats --format "{{.Container}}: {{.CPUPerc}}"
```

```bash
docker stats --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"
```

4. **Exibindo estatísticas de um container específico:**

```bash
docker stats container1
```

5. **Comandos curl com Docker API, acessando informações do Docker através do Unix socket (`/var/run/docker.sock`):**

- Requisição HTTP para a API do Docker e retorna uma lista de todos os containers em execução.

```bash
curl --unix-socket /var/run/docker.sock http://localhost/containers/json
```

- Retorna as estatísticas de uso em tempo real (streaming) para o container container2.

```bash
curl --unix-socket /var/run/docker.sock http://localhost/containers/container2/stats?stream=true
```

- Estatísticas retornadas apenas uma vez (não no modo de streaming), para o container container2.

```bash
curl --unix-socket /var/run/docker.sock http://localhost/containers/container2/stats?stream=false
```