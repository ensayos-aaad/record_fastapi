# record_fastapi
Ensayo que corre una pagina que graba desde el microfono

## Requerimientos

```
pip install fastapi
pip install "uvicorn[standard]"
```

## Entorno virtual


```
python -m venv env
.\env\Scripts\activate 
pip install -r requirements.txt
```

## Prueba

Para correr ejecute el comando:

```
uvicorn main:app
```

## Importante

El codigo del reproductor que se encuentra el directorio [static](static/) fue tomado del siguiente [repo](https://github.com/addpipe/simple-web-audio-recorder-demo?tab=readme-ov-file).

## TODO

- [x] Se corre el [index.html](static/index.html) del reproductor invocando las funciones de javascript.
- [ ] Los estilos CSS no cargan.

La salida en terminal al ejecutar la aplicacion se muestra a continuación:

```
(env) PS C:\Users\Usuario\Documents\camellos\xavier\repos\record_fastapi> uvicorn main:app
INFO:     Started server process [7520]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:57631 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:57631 - "GET /style.css HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:57632 - "GET /favicon.ico HTTP/1.1" 404 Not Found
```


