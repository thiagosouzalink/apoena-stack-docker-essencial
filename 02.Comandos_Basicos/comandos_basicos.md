# Comandos Básicos

## Comandos de Gestão de Imagens

- **Baixar imagens do Docker Hub**  
  `docker pull <nome_da_imagem>`

- **Listar imagens locais**  
  `docker images`

- **Remover imagens locais**  
  `docker rmi <nome_ou_ID_da_imagem>`

## Comandos de Gestão de Containers

- **Criar e iniciar containers**  
  `docker run --name <nome_do_container> -d <nome_da_imagem>`

- **Listar containers em execução**  
  `docker ps`

- **Parar containers em execução**  
  `docker stop <nome_ou_ID_do_container>`

- **Remover containers parados**  
  `docker rm <nome_ou_ID_do_container>`
