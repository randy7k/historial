# Historial de usuario

## Contexto
El proceso de Gestión Humana de nuestra empresa está diseñando un sistema de medición/compensación de sus colaboradores por cumplimiento de objetivos.  A principio de año la dirección socializa los lineamientos estratégicos con toda la organización y el equipo ejecutivo estructura los objetivos en que trabajará cada área para encaminar a la organización hacia el cumplimiento de los lineamientos estratégicos.  Los objetivos se clasifican en perspectivas y pueden responder a necesidades Financieras, de Procesos Internos, de Clientes y de Educación/Aprendizaje de los colaboradores.

## Requerimiento
Como dirección de Gestión Humana se necesita medir el resultado de los objetivos de los colaboradores y asignarles un porcentaje de cumplimiento o logro según la meta alcanzada para entregarles una remuneración.

### Comentario
Un objetivo tiene las siguientes características:
  - Descripción [150 caracteres alfanuméricos]
  - Métrica [30 caracteres alfanumericos]
  - Tabla de consecución
    - Meta (X0 - Xn) [Numérico de punto flotante]
    - Descripción de meta (X0 - Xn) [30 caracteres alfanumericos]
    - Porcentaje de consecución (Y0 - Yn) [Numérico de punto flotante]

# Criterios de aceptación
1) Los valores de la tabla de consecución pueden introducirse en orden ascendente o descendente dependiendo de la naturaleza de la métrica.  Esto puede significar que la meta sea directa o inversamente proporcional a su consecución. (Ver ejemplos de objetivos)
2) Los campos de la meta y la consecución solo aceptan valores numéricos. 
3) El resultado de un objetivo se evaluará contra los parámetros de la meta (X0 - Xn) y se mostrará el porcentaje de consecución (Y0 - Yn) correspondiente.
4) En una lista de valores de meta ascendentes si el resultado es inferior al valor de meta mínimo la consecución será cero (0).
5) En una lista de valores de meta ascendentes si el resultado es superior al valor de meta máximo la consecución será 100%.
6) En una lista de valores de meta descendentes si el resultado es superior al valor de meta máximo la consecución será cero (0).
7) En una lista de valores de meta descendentes si el resultado es inferior al valor de meta mínimo la consecución será 100%.
8) La tabla de consecución debe tener al menos 2 valores de meta y porcentaje de consecución.

# Entregables
1) Una herramienta donde se pruebe la funcionalidad detallada en el punto 2.
2) Desarrollado en Python(Django framework).
3) Escribir tests.
4) Entregar código en bitbucket y desplegar en el servicio de su elección.

