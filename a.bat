 docker compose up

cd .\retriever\

docker build -t docker-retriever:v1 .

docker run --name retriever-contaienier -d docker-retriever:v1

