# app_ide
![build status](https://github.com/praisetompane/app_ide/actions/workflows/app_ide.yaml/badge.svg)


## Objectives
A plain Python IDE to explore barebones constructs required in an IDE.

## Project Structure
- docs: Project documentation lives in here.
- src: production code lives in folder and is divided in the modules below:
    - app_ide: Project package.
        - linting:
            - Text linting lives in this module.
        - model:
            - The domain logic of the application lives in this module.
        - text_editor:
            - Text editing live in this module.
        - app.py:
            Entry point to startup the application
- tests: Test code lives in folder.
    The tests are intentionally separated from production code.
    - benefits:
        - Tests can run against an installed version after executing `pip install .`.
        - Tests can run against the local copy with an editable install after executing `pip install --edit`.
        - When using Docker, the entire app_etl folder can be copied without needing to exclude tests, which we don't release to PROD.
    - more in depth discussion here: https://docs.pytest.org/en/latest/explanation/goodpractices.html#choosing-a-test-layout-import-rules

- utilities: Any useful scripts, such as curl & postman requests, JSON payloads, software installations, etc.


## Dependencies
- [python 3.12+](https://www.python.org/downloads/)

## Setup Instructions
- The repository is configured to use [devcontainers](https://containers.dev) for development.
    - [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers)
    
## Run Program
- Start system run
    ```shell
    ./start_system.sh
    ```

## Testing
- Run unit and integration tests
    ```shell
    pytest
    ```
- End to End tests
    - Not Implemented

## Git Conventions
- **NB:** The main is locked and all changes must come through a Pull Request.
- Commit Messages:
    - Provide concise commit messages that describe what you have done.
        ```shell
        # example:
        git commit -m "feat(core): algorithm" -m"implement my new shiny faster algorithm"
        ```
    - References:
        - https://www.conventionalcommits.org/en/v1.0.0/
        - https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/

**Disclaimer**: This is still work in progress.