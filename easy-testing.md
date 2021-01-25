## staring the service

1) First try to do -> `docker-compose up -d`

## Testing the command
1) To run the command just do -> `docker-compose exec rest-service python manage.py save_evolution_chain_data --force --traceback 1`
2) In general the command can be run with -> `docker-compose exec rest-service python manage.py save_evolution_chain_data CHAIN_ID`
    - Where CHAIN_ID is an integer that identifies an evolution chain.
3) If you want to see the manual of the command use -> `docker-compose exec rest-service python manage.py save_evolution_chain_data`


## Testing the api rest
* The database is added to the repository (db.sqlite3) for fast testing, the command has been run with CHAIN_ID=1 and CHAIN_ID=2 so charmander/bulbasaur and their evolutions have been added.
1) Make sure you have curl installed in the host machine and then run -> `curl https://ec2-34-229-95-181.compute-1.amazonaws.com:8000/api/v1/pokemon/ivysaur`

2) If you want to test in a more visual manner here is the url to the project in postman -> https://documenter.getpostman.com/view/7547562/TW6tMAnE
    - You can also see some examples of the urls.