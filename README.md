# Tekton challenge
## Guillermo López Velarde González

### Instrucciones de uso
Para probar, envíar el siguiente JSON vía POST al siguiente endpoint:
https://maxareagetter-dvo4sj4zhq-uc.a.run.app/tekton/max_area_getter/1.0.0
{
    "heights": [1,8,6,2,5,4,8,3,7]
}

Si se desea desplegar el servicio localmente, correr los siguientes comandos, con docker instalado:
docker build -t dockerfile .
docker run -d -p 8080:8080 --name MaxAreaGetter dockerfile

y después, hacer la petición local a la URL:
http://127.0.0.1:8080/tekton/max_area_getter/1.0.0

### Instrucciones para correr las pruebas
Colocarse en el root del repositorio (afuera de src) y correr:
pipenv install --dev
pipenv run pytest

### Requerimientos:
Unit testing: 
https://github.com/GuillermoLvG/challenge/tree/feature/max_area_getter_service/test/bp
Any python version: Utilicé 3.8
Expose it as Rest API - Flask:
https://maxareagetter-dvo4sj4zhq-uc.a.run.app/tekton/max_area_getter/1.0.0
y el código en flask:
https://github.com/GuillermoLvG/challenge/blob/feature/max_area_getter_service/src/endpoints/api_controller.py

### Extras:
He agregado algunas cositas a la prueba:
- Continuous Integration
- Continuous Deployment
- Integration Tests

#### Continuous Integration:
El repositorio tiene 3 ramas:
- main
- develop
- feature/max_area_getter_service

He configurado en GCP que las pruebas (unitarias y de integración) se corran al momento de hacer un PR. En este paso podrían implementarse otros procesos como checar automaticamente buenas practicas en el código con algún pre-commit, o alguna otra cosa.
![image](https://user-images.githubusercontent.com/21270714/167958706-06b382de-0839-4f91-a7e9-28a19254ecf0.png)

#### Continuous Deployment:
Al hacer push en la rama main, se despliega automaticamente el servicio en GCP.
![image](https://user-images.githubusercontent.com/21270714/167958273-822f4225-f6dc-4e3d-b7c8-4f8224fba448.png)

### Integration Tests:
Hice una prueba de integración sencilla acá:
https://github.com/GuillermoLvG/challenge/tree/feature/max_area_getter_service/test/endpoints

Si tienen problemas usando el servicio mándenme un correo, lo voy a dejar arriba unos días.
