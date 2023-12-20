# record_fastapi
Ensayo que corre una pagina que graba desde el microfono

## Requerimientos

```
pip install fastapi
pip install "uvicorn[standard]"
pip install jinja2
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

El codigo del reproductor que se encuentra el directorio [webpages/record/](webpages/record/) fue tomado del siguiente [repo](https://github.com/addpipe/simple-web-audio-recorder-demo?tab=readme-ov-file).

## TODO

- [x] Se corre el [index.html](webpages/record/index.html) del reproductor invocando las funciones de javascript.
- [x] Los estilos CSS no cargan.

## Referencias principales

### Punto de partida de la parte de javascript

* https://code-maven.com/slides/python/fastapi-static-files-javascript

### Solicion para cargar los archivos CSS

* https://github.com/tiangolo/fastapi/issues/4989 
* https://fastapi.tiangolo.com/advanced/templates/#templates-and-static-files
* https://github.com/JarroVGIT/fastapi-github-issues/tree/master/4989
* https://stackoverflow.com/questions/61641514/css-not-recognized-when-served-with-fastapi

