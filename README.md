## Backend

### Clonar proyecto
```bash
git clone  git@github.com:jmaresm/FlaskAPIProducts.git
```

### Entrar al directorio del proyecto
```bash
cd FlaskAPIProducts/
```

### Installation
Instalar dependencias 
```bash
python3 -m pip install -r requirements.txt
```


## Docker
### Levantar las BD
```bash
docker-compose up -d
``` 

## API
### Correr api 
```bash
python3 entrypoint.py
``` 



## API documentation
### Swagger docs
Introduce la URL en un browser
```
http://127.0.0.1:5001/swagger/
```

## Unit Test

```bash
cd test/
python3 pytest
```