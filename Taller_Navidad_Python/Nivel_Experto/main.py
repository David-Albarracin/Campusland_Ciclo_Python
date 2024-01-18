

import templates.menus as menu
import templates.reusable as reusable
import services.campers as sc
import services.notas as notas
import services.campusland as campus




if __name__ == '__main__':
    while (True):
        opMenu = input(menu.showMenu("home"))
        if (opMenu == "1"):
            sc.newCamper()
        elif (opMenu == "2"):
            notas.pruebaAdmision()
        elif(opMenu == "3"):
            campus.newArea()
        elif(opMenu == "4"):
            campus.newRuta()
        elif(opMenu == "5"):
            sc.matricular()
        elif(opMenu == "6"):
            notas.registrarNotas()
        elif(opMenu == "7"):
            campus.newTrainer()
        elif(opMenu == "8"):
            notas.moduloReportes()
        elif(opMenu == "9"):
            sc.delCamper()
        elif(opMenu == "10"):
            sc.editarCamper()
        elif(opMenu == "11"):
            reusable.showSuccess("Gracias Por usar el Sistema")
            break
        else:
            reusable.showError("Opcion No Valida Intentalo de Nuevo")


























"""
Nivel Experto
El departamento académico de campuslands desea crear un programa que le permita llevar el seguimiento
Académico de todos los campers que se encuentran matriculados en el programa intensivo de programación.
Usted es contratado para liderar el desarrollo del programa que debe cumplir con las siguientes
especificaciones:
1. Registro de campers : El programa debe permitir a las personas encargadas de procesar las inscripciones
a el programa; la información que se tiene por cada camper es la siguiente : nro de identificación, nombre,
Apellidos, dirección, acudiente, teléfonos de contacto(Nro celular y nro fijo),estado.
2. Campus cuenta con diferentes rutas de entrenamiento las cuales deben cumplir los candidatos que superen
La prueba inicial. Las rutas son: Ruta NodeJS, Ruta Java, Ruta NetCore.
3. Registro de prueba : La persona encargada de asignar las pruebas debe contar con una opción en el programa
Que le permita registrar la nota de los campers que se han registrado y tienen un estado de inscrito. La
Prueba es aprobada si el promedio entre la nota teórica y la nota practica es >=60.
4. Registro de áreas de entrenamiento : Campus cuenta con diferentes áreas de entrenamiento en la cuales
Los campers aprenden los diferentes stack etnológicos dependiendo de las rutas de entrenamiento. Por el
Momento se cuenta con tres áreas de entrenamiento con una capacidad máxima de 33 campers.

5. Creación de rutas de entrenamiento : La coordinación académica desea poder crear nuevas rutas
de entrenamiento las cuales contienen la siguiente información.

* Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)
* Programación Web (HTML, CSS y Bootstrap)
* Programación formal (Java, JavaScript, C#)
* Bases de datos (Mysql, MongoDb y Postgresql). Cada ruta tiene un SGDB principal y un alternativo.
* Backend (NetCore, Spring Boot, NodeJS y Express)

6. Los campers que pasaron de inscritos a aprobados podrán ser asignados a cualquiera de las rutas que se han
creado previamente. Se debe tener en cuenta que no se puede exceder la capacidad de cada una de las áreas
de entrenamiento.

7. CampusLands cuenta con Entrenadores expertos encargados de dirigir cada una de las rutas de entrenamiento.
es quiere decir que a cada entrenador se le podrán asignar diferentes rutas de entrenamiento teniendo en
cuenta su horario.

8. Gestor de matriculas. La coordinación académica desea contar con un modulo de matriculas que le permita
asignar los campers aprobados, experto encargado, ruta de entrenamiento asignada, fecha de inicio, fecha
finalizacion y salón de entrenamiento.
9. Periódicamente los campers son evaluados para conocer las habilidades adquiridas durante el proceso de
Entrenamiento, cuando finaliza cada modulo los campers deben presentar una prueba teórica y una prueba
Practica. Esta prueba es considerada como aprobada si el promedio de las dos dan un valor >=60.

La prueba teórica tiene un peso de 30%, la prueba practica tiene un peso del 60%. Durante el proceso el
Entrenador realiza quices, trabajos los cuales tienen un peso del 10%. Al finalizar el proceso de evaluación
Se considera aprobado el modulo si la nota final es > 60.
10. Estudiantes en riesgo. La coordinación académica cuando finaliza cada uno de los módulos de las rutas
evalúa el rendimiento de cada uno de los campers teniendo en cuenta la nota obtenida en cada modulo. Si la nota
Es <60 el camper queda en rendimiento bajo lo cual genera un llamado de atención por tal motivo
Se debe permitir consultar los campers en riesgo bajo.
11. Modulo de reportes.

a. Listar los campers que se encuentren en estado de inscrito.
b. Listar los campers que aprobaron el examen inicial.
c. Listar los entrenadores que se encuentran trabajando con campuslands.
d. Listar los estudiantes que cuentan con bajo rendimiento.
e. Listar los campers y entrenador que se encuentren asociados a una ruta de entrenamiento.
f. Mostrar cuantos campers perdieron y aprobaron cada uno de los modulos teniendo en cuenta
la ruta de entrenamiento y el entrenador encargado.

"""


