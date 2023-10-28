# app_ide
Messing around with some barebones constructs required in an IDE.

![build status](https://github.com/praisetompane-toy-applications/app_ide/actions/workflows/app_ide.yaml/badge.svg)


## setup instructions:
1. install `python 3.11` or higher.
    - [Python Download]: (https://www.python.org/downloads/)

2. clone repo:
    ```shell
    git clone git@github.com:praisetompane-toy-applications/app_ide.git
    ```

## package management:
- install pipenv: https://pypi.org/project/pipenv/
## run program:
- install packages into local environment using pipenv[**only required for first run**]:
    ```shell
    pipenv install
    ```
- to start system run:
    ```shell
    ./start_system.sh
    ```

## testing:
### unit tests:
- to run tests:
    - activate environment
    ```shell
    pipenv shell
    ```
    - run tests
    ```shell
    pytest
    ```