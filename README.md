# assets-app-api
Assets api for managing and maintaining assest


## Command to Build Docker image
```
docker build -t tag .
```

## Command to build docker-compose
```
docker-compose build 
```

## docker-compose run linting 
```
docker-compose run --rm app sh -c "flake8"
```

## docker-compose create django project
```
docker-compose run --rm app sh -c "django-admin startproject app ."
```

## docker-compose start application
```
docker-compose up
```

## docker-compose run tests
```
docker-compose run --rm app sh -c "python manage.py test"
```