# Luxonis Task

This project is an application that uses Scrapy to download real estate data from sreality.cz and Flask server to display it.

## Starting the project

This project is containerized using Docker and Docker Compose, which makes it easier to run.

### Prerequisites

Before starting, make sure you have the following installed:

- Docker
- Docker Compose

### Getting Started

1. **Clone the repository:**

`git clone https://github.com/badybeer/luxonis-scrapy.git`

2. **Go to the root directory of the project:**

`cd luxonis-scrapy`

3. **Starting Docker Compose:**

`docker-compose up`

4. **Connect to PostgresDB in the new terminal:**

`psql -h localhost -p 5432 -U admin -d sreality `
The test password is `admin`.

5. **Creating the database structure:**

`CREATE TABLE flats (
    title TEXT,
    image_url TEXT
);`

6. ** Restarting Docker Compose:**

`docker-compose up`

7. **Opening the application:**

Navigate to `http://127.0.0.1:8080` in your browser where you should see the application running.

## Project structure

The project contains the following main components:

- `docker-compose.yml`: A Docker Compose file that defines and binds the services needed to run the application.
- `Dockerfile`: Dockerfile for the Scrapy project.
- `Dockerfile.flask`: Dockerfile for the Flask server.
- `luxonis_task/`: The directory containing the Scrapy project and the Flask application.
- `luxonis_task/app.py`: The main file of the Flask application.
- `luxonis_task/spiders/`: Directory containing the Scrapy spiders.
- `luxonis_task/templates/`: Templates for the Flask application.
- `luxonis_task/static/`: Static files for Flask, such as CSS.

## Author

Jozef Badár

## License

This project is not licensed and is available as open-source.





# Luxonis Zadanie

Tento projekt predstavuje aplikáciu, ktorá používa Scrapy na stiahnutie dát o nehnuteľnostiach z webu sreality.cz a Flask server na ich zobrazenie.

## Spustenie projektu

Tento projekt je kontajnerizovaný pomocou Docker a Docker Compose, čo zjednodušuje jeho spustenie.

### Predpoklady

Pred spustením sa uistite, že máte nainštalované:

- Docker
- Docker Compose

### Spustenie

1. **Naklonovanie repozitára:**

`git clone https://github.com/badybeer/luxonis-scrapy.git`

2. **Prechod do koreňového adresára projektu:**

`cd luxonis-scrapy`

3. **Spustenie Docker Compose:**

`docker-compose up`

4. **Pripojenie k PostgresDB v novom termináli:**

`psql -h localhost -p 5432 -U admin -d sreality  `
Testovacie heslo je `admin`.

5. **Vytvorenie štruktúry databázy:**

`CREATE TABLE flats (
    title TEXT,
    image_url TEXT
);`

6. **Reštartovanie Docker Compose:**

`docker-compose up`

7. **Otvorenie aplikácie:**

Prejdite na `http://127.0.0.1:8080` vo vašom prehliadači, kde by ste mali vidieť bežiacu aplikáciu.

## Štruktúra projektu

Projekt obsahuje nasledujúce hlavné komponenty:

- `docker-compose.yml`: Súbor Docker Compose, ktorý definuje a spája služby potrebné na spustenie aplikácie.
- `Dockerfile`: Dockerfile pre Scrapy projekt.
- `Dockerfile.flask`: Dockerfile pre Flask server.
- `luxonis_zadanie/`: Adresár obsahujúci Scrapy projekt a Flask aplikáciu.
- `luxonis_zadanie/app.py`: Hlavný súbor Flask aplikácie.
- `luxonis_zadanie/spiders/`: Adresár obsahujúci Scrapy pavúkov.
- `luxonis_zadanie/templates/`: Šablóny pre Flask aplikáciu.
- `luxonis_zadanie/static/`: Statické súbory pre Flask, ako je CSS.

## Autor

Jozef Badár

## Licencia

Tento projekt nie je licencovaný a je dostupný ako open-source.

