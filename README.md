# Aplicación de clasificación de noticias

## Instrucciones
- Copiar noticia en campo de texto (está configurado para idioma español)
- Seleccionar el modelo (entre SVM, NaiveBayes, Logistic y Random Forest)
- Hacer click en "Predecir"
- La predicción consiste en una etiqueta que podrá ser: 

{'Tecnología': 0,
 'Entretenimiento': 1,
 'Deportes': 2,
 'Salud': 3,
 'Medio ambiente': 4,
 'Política': 5,
 'Ciencia': 6}
 
 
 - 

Desplegado en: http://flask-heroku-jorgecif.herokuapp.com/


# Pasos deploy en Heroku con Flask

-	Creo carpeta nueva
-	Creo entorno virtual
o	Instalo virtualenv si no lo tengo: pip instal virtualenv
o	Creo entorno: virtualenv [nombreentorno]
o	Ejecuto entorno creado: . [nombreentorno]/Scripts/actívate
o	Para manejar en vscode ir a command palette y abrir python interpreter para seleccionar el nuevo entorno (archivo Python.exe en carpeta creada del entorno)
-	Instalo paquetes en mi entorno virtual
o	Flask: pip install flask
o	Gunicorn: pip install gunicorn
-	Entro a carpeta del entorno y creo carpeta de proyecto, ejemplo: Project
-	Creo el archivo Python: main.py
-	Pruebo corriendo el archivo
-	Cambiamos el puerto a 5000 y la bandera debug en false
-	Creo archivo requirements.txt
o	Pip freeze (para ver listado de requerimientos)
o	pip freeze > requirements.txt
-	Creo archivo Procfile
o	web: gunicorn main:app
-	Deploy en heroku
o	Instalar Heroku
o	Logion
	Heroku login
o	Crear aplicación
	Heroku create [nombre app] 
	Si entro a la aplicación y voy a pestaña “deploy” salen los comandos
o	Inicializo repositorio
	git init
o	Apunto repositorio a aplicación en heroku
	Heroku git:remote -a [nombre app]
o	Deploy
	Git add  . 
	Git commit -am “comentario”
	Git push heroku master
o	Abro 
	Heroku open


