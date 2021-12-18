# Simple API with FastAPI

This project is a simple example API with FastAPI

## Installing

To install and execution the API In your local machine, you will need to:

```
a) Clone the project, and entry on folder of API:

git clone https://github.com/RicardoTurco/FastAPI_YT.git && cd FastAPI_YT/


b) Create and activate one "virtualenv" (SO Linux):

python3 -m venv venv
source venv/bin/activate


c) Install the dependences of project:

pip install -r requirements.txt


d) Run the project:

uvicorn main:app --reload


e) Accessing the API e receiving message of wellcome:

localhost:8000/ (on your browser)
```

## Swagger

After the application goes up, open your browser on `localhost:8000/docs` to see the self-documented interactive API.


## Files

* `.gitignore` - Lists files and directories which should not be added to git repository.
* `README.md` - Instructions and informations to run this project locally.
* `requirements.txt` - All project dependencies.
* `main.py` - The Application entrypoint.