## To implement
- Protect the api with nginx.

## Comment structure
- Comments that are obvious after the first read of the code should not be kept in the code augmenting the cognetive load and the time spent reading the code of the developers.
    They can be kept in this file.

## Investigating the docker image

- https://pythonspeed.com/articles/base-image-python-docker-images/
- It's investigated to take advantange of a previous investigation. Where i updated all the versions (from the SO base image to all the versions in requirements.txt).
- I realize that the python images come from debian but again i choose ubuntu because the community is bigger and the errors are fixed faster because of that. More importantly i have previously solved various bugs in the ubuntu machine which will help alocating resources(time) in the problem at hand.
- The building of the image may be slower but this in a real world example will be optimized by creating a base image with everything we need and uploading that to a registry of our own.
- The version of the base image is 18.04 and not 20.04 to take advantange of the longer release/debugging time passed in the community.

## Building image / [Dockerfile](./Dockerfile)
- To fix Python.h includes and compilations when including packages that need to be compiled.
        `RUN apt-get -y install python3.8-dev`

- Python 3.8 is currently being improved (https://devguide.python.org/#status-of-python-branches) and have a longer possible life (https://endoflife.date/python) whitout being too new.
    `RUN apt-get -y install python3.8`

-  The directory of the project it's defined as the default directory of vagrant; from the source (/) so;
        `(ENV BASE_DIR=/mopokemon)`
    - Even if the Operating System changes the structure of the project is kept.
    - Also is not directed to home(~) to make paths shorter and not dependant on a particular user

## Using the image / docker-compose

- The code is shared, not copied, to the container to:
    - speed the build of the image for development(now the code is small and is not a problem look at assumptions)
    - Being able to use the IDE of your choice in the host Operating System.

## Choosed names
- mopokemon is choosed as a project name to slighly protect the anonimity of the project and that it's not easily copied.

## Documentation
- The style is choosen from pep 257 https://www.python.org/dev/peps/pep-0257#multi-line-docstrings

## Design decisions
- https://pokemondb.net/pokebase/270377/what-pokemon-has-the-longest-name longest name for models.Pokemon.name data type

- SaveChainEvolution (from [_private_save_evolution_chain.py](./pokemon/management/commands/_private_save_evolution_chain.py))does not need to be a Object but it looks cleaner and in my opinion "More extensible" for modification (https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle)

- PokemonRetrieveViewSet (from [views.py](./pokemon/api/views.py)) is implemented as a viewset because it shows a greater knowledge of Django Rest Framework, a simple ApiView could sufice but it's always better to write less code and to rely on code that has been tested more.

## Debug

### Debug the command
You need to run Visual Studio Code with the remote extension (https://code.visualstudio.com/docs/remote/remote-overview) in the mopokemon_rest-service container, in the /mopokemon directory. Make sure you have put your breakpoints (https://code.visualstudio.com/docs/editor/debugging). Then run inside the container the command:

    $ python -m debugpy --wait-for-client --listen 0.0.0.0:5678 ./manage.py save_evolution_chain_data --force --traceback 1

And start the debugger from the menu that Visual Studio Code provides.

### Debug the Rest Service
Each time the django server starts it uses ptvsd to allow Visual Studio Code debug to attach and start to debug, so when you run:
    `$ docker-compose up`
You can go to the debugging menu pick "Django: debug" and start debugging.