When installing:
1) make a venv & install the requirements.txt as usual
1a) set the python to the venv python in VSCode
2) if you're on windows, you gotta make sure it supports JSONFields, as per https://code.djangoproject.com/wiki/JSON1Extension
3) DL the twee extension for VSCode
4) Get & run docker on port 6397 (docker run -p 6379:6379 -d redis)