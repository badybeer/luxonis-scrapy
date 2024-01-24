# Luxonis Zadanie

Tento projekt predstavuje aplikáciu, ktorá používa Scrapy na stiahnutie dát o nehnuteľnostiach z webu sreality.cz a Flask server na ich zobrazenie.

## Spustenie projektu

Tento projekt je kontajnerizovaný pomocou Docker a Docker Compose, čo zjednodušuje spustenie projektu.

### Predpoklady

Pred spustením sa uistite, že máte nainštalované:

- Docker
- Docker Compose

### Spustenie

1. Naklonujte repozitár:

git clone https://github.com/tvoje-uzivatelske-meno/tvoj-repozitar.git

2. Prejdite do koreňového adresára projektu:

cd tvoj-projekt

3. Spustite Docker Compose:

4. Otvorte prehliadač a prejdite na `http://127.0.0.1:8080`, kde by ste mali vidieť bežiacu aplikáciu.

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

Tvoje meno

## Licencia

Tento projekt nie je licencovaný a je dostupný ako open-source.

