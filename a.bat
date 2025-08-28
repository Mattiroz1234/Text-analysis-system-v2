 docker compose up

cd .\retriever\

docker build -t docker-retriever:v1 .

docker run --name retriever-contaienier -d docker-retriever:v1


docker build -t docker-image-preprocessor:v1 .

docker run --name preprocessor-contaienier -d docker-image-preprocessor:v1



docker build -t docker-image-enricher:v1 .

docker run --name persister-contaienier -d docker-image-data-persister:v1

docker build -t docker-image-data-persister:v1 .

docker run --name persister-contaienier -d docker-image-data-persister:v1
