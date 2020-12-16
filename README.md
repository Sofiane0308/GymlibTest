#  Test Gymlib

# But

Nous voulons développer une API en charge de la gestion d'une file de chiffre (qu'on appellera job).

Cette API expose plusieurs routes:

- GET /jobs: renvoie le tableau des jobs (ex: [5,4,3,2,1])

- POST /jobs: accepte un JSON au format `{ "input": number }` et ajoute le chiffre dans la file **s'il n'est pas déjà présent à l'intérieur de la file** (ex: `{ "input": 12 }`)

- GET /job: renvoie le premier job de la file (et mets à jour la file) (ex: 12)

- DELETE /jobs: vide la file si la file est vide, on renvoie un status HTTP 204 et aucun output

# Instructions
Pour lancer l'API , allez sur le répertoire racine et lancer les commandes qui correspondent à l'environnement de votre choix:
## Sur Docker
- `export API_PORT=3111`
- `docker-compose up`
## Sur l'OS (python/pip)
- `pip install -r requirements.txt`
- `export API_PORT=3111`
- `python manage.py runserver 0.0.0.0:$API_PORT`
### Note: L'API écoute sur le port 3111

# Tests
## Tests unitaires intégrés (python/django)

    python manage.py test
 
## Test fournis (javascript/node)
Afin de tester l'API allez sur le répertoire /test et lancez la commande suivante (Nodejs):

    npm install && npm run test`

# Notes
Le projet inclut:
- Des tests unitaires dans */jobqueue/tests.py*.
- Un *Dockerfile* et un fichier *docker-compose.yml* pour le build et le run sur Docker.
- Un fichier de configuration .travis.yml pour l'intégration continue sur Travis CI.

# Concernant les tests fournis:
Dans la 2eme partie, on post la liste d'entiers sous Promise.all() qui bloque jusqu'à reception de toutes les réponses avant de verifier le resultat, sauf que les requêtes peuvent arriver en désordre à l'API ce qui ne donne pas le résulats attendu.
Je me suis permis donc de changer un petit peu cette partie en mettant l'appel fetch() dans une boucle en bloquant a chaque appel.
