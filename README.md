# Microservices_Docker_Deployment
NodeJS &amp; Python Microservice

Run Service:
docker-compose up --build

Basic Docker commands:
Start all services (build images if needed)
docker-compose up

##Start all services and rebuild images
docker-compose up --build

##Run services in the background (detached mode)
docker-compose up -d

##Stop and remove containers, networks, images, and volumes
docker-compose down

##View logs from all services
docker-compose logs

##List running containers managed by docker-compose
docker-compose ps

##Stop services without removing containers
docker-compose stop

##Restart services
docker-compose restart