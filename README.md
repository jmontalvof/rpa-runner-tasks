# Rpa Runner Tasks

Repositorio de tareas ejecutables para Robocorp Runner API.

Este proyecto almacena scripts Python que pueden ser sincronizados automáticamente mediante git-sync y ejecutados remotamente desde la API de ejecución.

## Arquitectura

text GitHub    |    v git-sync    |    v Robocorp Runner API    |    v Python Tasks 

Cada script ubicado en la carpeta actions/ puede ser ejecutado mediante una llamada HTTP al endpoint /run.



