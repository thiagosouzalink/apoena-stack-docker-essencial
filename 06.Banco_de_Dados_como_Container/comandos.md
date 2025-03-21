# 06 -  Banco de Dados como Container 

## Comandos

### Criar imagem e container

```bash
docker build -t apoena-mysql .
```

```bash
docker run -d --name apoena-mysql -p 3307:3306 apoena-mysql
```

## Execução App Python

1. **Configurar variáveis de ambiente no `.env-example` e renomear para `.env`**

2. **Instação dos pacotes python necessários**

```bash
pip install -r requirements.txt    
```

3. **Execução do app**

```bash
python app.py
```
