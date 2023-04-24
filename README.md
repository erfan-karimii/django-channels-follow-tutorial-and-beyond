# django-channels-read-docs-and-follow

 this is my first time i want seriously follow django channels official docs 
 
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