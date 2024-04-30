Aby testować kod i sprawdzać dostępność aplikacji w ramach konfiguracji z Docker Compose oraz w pipeline GitLab CI, należy dodać odpowiednie skrypty testowe i usługi do monitorowania. Można to zrobić, implementując w pipeline etapy testowania, takie jak testy jednostkowe, integracyjne, akceptacyjne, a także weryfikacje dostępności serwisu.

### 1. Dodanie Testów do Docker Compose

Poniżej pokazano, jak można zintegrować testy do środowiska definiowanego przez `docker-compose.yml`. Użyjemy jako przykładu prostego serwisu webowego opartego na Flask.

**Dockerfile** (dla aplikacji Flask):

```Dockerfile
# Znajduje się w folderze projektu pod nazwą Dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
CMD ["flask", "run", "--host=0.0.0.0"]
```

**docker-compose.yml**:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
    depends_on:
      - db
  db:
    image: postgres
    environment:
      POSTGRES_DB: mojabaza
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - db-data:/var/lib/postgresql/data

  test:
    build: .
    command: pytest
    volumes:
      - .:/app
    depends_on:
      - web

volumes:
  db-data:
```

- **Test Service**: Tu dodano serwis `test`, który odpala pytest w kontekście aplikacji. Zależy on od serwisu `web` i ma za zadanie uruchomić testy po tym, jak aplikacja zostanie uruchomiona.

### 2. Dodanie Testów i Sprawdzania Działania w GitLab CI

Następnie modyfikujemy `.gitlab-ci.yml` by dodać etapy testowania i sprawdzania dostępności.

**.gitlab-ci.yml**:

```yaml
stages:
  - build
  - test
  - deploy

build:
  stage: build
  image: docker:19.03.12
  services:
    - docker:19.03.12-dind
  script:
    - docker-compose build

test:
  stage: test
  image: docker:19.03.12
  services:
    - docker:19.03.12-dind
  script:
    - docker-compose run test

deploy:
  stage: deploy
  image: docker:19.03.12
  services:
    - docker:19.03.12-dind
  script:
    - docker-compose up -d

```

W konfiguracji CI:
- **Build**: Buduje obrazy Docker oparte na `docker-compose.yml`.
- **Test**: Uruchamia kontenery testowe (`docker-compose run test`) definiowane w `docker-compose.yml`.
- **Deploy**: Wdraża aplikację w trybie detached.

### 3. Monitorowanie i Alerty

Do monitorowania działania aplikacji można wykorzystać narzędzia takie jak Prometheus i Grafana. Prometheus zbiera metryki z Twoich aplikacji, a Grafana służy do ich wizualizacji.

Aby zaimplementować monitoring, można dodać konfiguracje Prometheus i Grafana do `docker-compose.yml` i skonfigurować odpowiednie dashboardy w Grafana, które będą wyświetlały dostępność serwisów.

Przykład integracji monitoringu wymagałby znacznie bardziej rozbudowanego przykładu, włączając definiowanie endpointów metryk w aplikacji, konfigurację zapisu danych dla Prometheus, oraz uruchomienie Grafany.

To podejście pozwoli Ci nie tylko automatycznie testować i wdrażać kod, ale także monitorować jego działanie na produkcji.