# Microservices_Docker_Deployment
NodeJS &amp; Python Microservice

Run Service:
```docker-compose up --build```

Basic Docker commands:
Start all services (build images if needed)
```docker-compose up```

## Start all services and rebuild images
```docker-compose up --build```

## Run services in the background (detached mode)
```docker-compose up -d```

## Stop and remove containers, networks, images, and volumes
```docker-compose down```

## View logs from all services
```docker-compose logs```

## List running containers managed by docker-compose
```docker-compose ps```

## Stop services without removing containers
```docker-compose stop```

## Restart services
```docker-compose restart```

```
Microservices_Docker_Deployment/
│── .github/
│   └── workflows/               # GitHub Actions workflows
│       ├── nodejs.yml           # CI/CD for Node.js Auth Service
│       └── python.yml           # CI/CD for Python Product Service
│
├── auth-service/                # Node.js Auth Service
│   ├── index.js                 # Express server (signup, login)
│   ├── package.json             # Node.js dependencies
│   └── Dockerfile               # Dockerfile for Node.js service
│
├── product-service/             # Python Flask Product Service
│   ├── app.py                   # Flask CRUD APIs (JWT protected)
│   ├── requirements.txt         # Python dependencies
│   └── Dockerfile               # Dockerfile for Flask service
│
├── docker-compose.yml           # Run all services together
└── README.md                    # Project documentation
```
