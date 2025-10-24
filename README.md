When installing:
1) make a venv & install the requirements.txt as usual
1a) set the python to the venv python in VSCode
2) if you're on windows, you gotta make sure it supports JSONFields, as per https://code.djangoproject.com/wiki/JSON1Extension
3) DL the twee extension for VSCode
4) Get & run docker on port 6397 (docker run -p 6379:6379 -d redis)

Deployment:
Apparently just push to Heroku master...?

OK IF YOU GET THE SELF-SIGNED CERTIFICATE SSL ISSUE
apparently it's 'cuz Heroku forces TLS on but the redis kvs thing they use uses self-signed certs
so you need to add to the REDIS_URL ?ssl_cert_reqs=none to the REDIS_URL
but I think they rotate that! so later on I need to force it in the config resolution I think
aaaaaaaaa I wasted so much time on this