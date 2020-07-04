# Searx Instance ScrAPI
Experimental scrapping API to getting informations from Searx instances.

## Supported versions
+ 0.16.0

## Functions
- [x] List all engines and shortcuts. `/engines/all`
- [x] Show info about engine by name (currently shortcut only). `/engines/?name=%s`
- [ ] Show default categories.
- [x] List default settings in "general" category. `/general/default`
- [ ] Specify instance in query (also .onion instances).

## Development
+ Clone repo.
```
$ git clone https://git.samedamci.me/samedamci/searx-instance-scrapi && \
	cd searx-instance-scrapi
```
+ Create virtual environment.
```
# PyPy
$ virtualenv -p pypy3 .
```
```
# CPython
$ virtualenv .
```
+ Activate virtual environment.
```
$ source bin/activate
```
+ Install requirements.
```
$ pip3 install -r requirements.txt
```
+ Run development server.
```
# PyPy
$ pypy3 run.py
```
```
# CPython
$ python3 run.py
```

## Production
### Gunicorn
Gunicorn server can be runned with NGINX reverse proxy. This is recommended way
to run production servers because this is very easy way to enable HTTPS and other
specific WWW server settings.

[More informations](https://gunicorn.org/#deployment).
