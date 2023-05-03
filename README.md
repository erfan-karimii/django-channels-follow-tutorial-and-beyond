# django-channels-read-docs-and-follow

this is my first time i want seriously follow django channels official docs 
oh and template is also by fuly coded by myself for the first time!?

## technologies

<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="./docs/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://git-scm.com/" target="_blank"> <img src="./docs/git-original.svg" alt="git" width="40" height="40"/> </a>
<a href="https://www.djangoproject.com/" target="_blank"> <img src="./docs/django-plain.svg" alt="django" width="40" height="40"/> </a>
<a href="https://redis.io/" target="_blank"> <img src="./docs/redis-original.svg" alt="redis" width="40" height="40"/> </a>
<a href="#" target="_blank"> <img src="./docs/html5-original.svg" alt="html" width="40" height="40"/> </a>
<a href="https://getbootstrap.com/" target="_blank"> <img src="./docs/bootstrap-original.svg" alt="bootstrap" width="40" height="40"/> </a>
<a href="https://sqlite.org/index.html" target="_blank"> <img src="./docs/sqlite-original.svg" alt="sqlite" width="40" height="40"/> </a>
</p>

## goals:

- learn more about ws 
- extend it to realworld use case 
- as always have fun:)

## how run this little project

```bash
git clone https://github.com/erfan-karimii/django-channels-follow-tutorial-and-beyond
cd django-channels-follow-tutorial-and-beyond
pip install -r requirment.txt
```
run redis with docker for ws:
```bash
docker pull redis
docker run redis -d -p 6379:6379 
```

and run project:
```bash
cd core
python manage.py runserver
```