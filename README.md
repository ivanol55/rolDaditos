# Cuentamuertes web
----

## Definición de proyecto
Este proyecto es un contador de muertes web-based orientado a personas que crean contenido en plataformas de streaming como Twitch, o que llevan una mesa de Roleplay a distancia y quieren un lugar centralizado donde lanzar unos dados justos de forma que no suponga mucho problema y no interrumpa la partida, y en el caso del streamer, utilizando poca carga de sistema gracias al diseño ligero de frontend, y facilidad de compartir estas tiradas gracias a la pestaña de dado autoactualizada

## A quién va dirigido
Este es un proyecto principalmente enfocado a personas que creen contenido de juegos de rol de mesa, como [Dungeons and Dragons](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons), sea para una audiencia en internet, o para una mesa personal con compañía pero sin estar en el foco de internet.

## Requisitos técnicos
Esta aplicación requiere:

- Tener instalado Python3 en la máquina que va a hacer de servidor
- Un servidor con sistema operativo `Debian 9` o superior o `Ubuntu 18.04` o superior.
- Tener instalado el webserver `Apache2`.
- Un dominio que apuntar a esta webApp.
- Tener instalada una instancia de `PostgreSQL` en este mismo servidor.
- Tener acceso a un usuario de PostgreSQL que pueda acceder por método remoto que pueda crar usuarios con permiso de `CREATEDB`.
- Tener acceso al usuario administrador del sistema, para poder ejecutar el script `installer.py` con el usuario `root`.

El script de instalación se ocupará del resto.

## Instalación
Una vez tengas todos los requisitos mencionados en la sección anterior, simplemente descarga el repositorio en el que se encuentra este documento, ejecuta `python3 installer.py` y el instalador te guiará a través del resto del proceso.

## Manual

### Selector de personaje
Una vez abras la página, lo primero que encontrarás será el selector de personaje, que indica con quién quieres jugar esta sesión. Si esta es la primera vez o es una campaña nueva, este desplegablee stará en blanco.

En tal caso, los formularios inferiores deben usarse. El formulario de la izquierda sirve para crear una campaña de juego nueva en la que posteriormente crearás personajes. El formulario de la derecha, en cambio, nos permite introducir en el campo de texto un nuevo personaje, pero éste debe ligarse a una partida, con lo cual debe crearse antes la partida a la que se ligará. En ambos casos, tras la creación, se devolverá al inicio para crear más personajes o elegir con el que jugar.

### Página principal
Una vez elijamos personaje, la web nos llevará automáticamente a la pagina principal, donde tenemos acceso a todo lo necesario para una partida. De arriba a abajo en orden de aparición veremos:

- El formulario de dados
- El log de resultados
- Los stats de dados
- Un extracto de texto con el último dado tirado
- Los stats por sesión de juego
- El último dado autoactualizado cada 3 segundos, para añadirlo como fuente de streaming

### El formulario de dados
Esta es la opción que más utilizarás de todo el programa. Te pedirá la sesión de juego en la que estás, en número, y el número de dados que quieres tirar. Para continuar, harás click en `tabla de dados`.

Tras esto, irás a una página donde tendrás que introducir el número de caras que tiene cada dado que has tirado y hacer click en "ver resultados"

Esto te llevará a una página donde verás una tabla con tus resultados de tiradas para cada dado, y un botón para volver al inicio.

### Log de resultados
En este apartado encontraremos un listado de la id, la fecha y hora, la sesión, las caras del dado, el resultado y el tirador de cada dado que se ha registrado en la base de datos.

### Stats de dados
En esta página veremos, de todos los personajes que existen en la base de datos, cuñantos dados ha tirado en total, y cuál es la media de resultados de esos dados.

### Stats por partida
En este apartado, tras hacer click en el botón, nos encontraremos con un desplegable. Con él podremos elegir de qué sesión queremos ver información general. Una vez elegido, cuando hagamos click en `Stats de partida` veremos una tabla con stats de dados generales de los jugadores, como quién ha tirado más o menos dados, quiénes han tenido las mejores o peores tiradas, o cuántos dados se han tirado por hora de juego de media.

### Último dado autoupdating
Cuando hagamos click a este botón se abrirá una web donde veremos la última tirada registrada en la base de datos, sin nada más, y esta página se actualiza cada 3 segundos automáticamente con la última tirada. Esto permite a un creador de contenido añadir de forma sencilla la última tirada al overlay del contenido sin tener que pelearse con formatos de página, como es el caso del resto de la web.

## Contribuciones
Por el momento las contribuciones a este web project personal están cerradas, pero siempre puedes abrir una Issue en GitHub si encuentras algún error que intentaré solucionar en la medida de lo posible.

## Licencia
Ver el archivo LICENSE de la repo, ahí está la licencia completa. Software licenciado bajo la licencia de software libre `GNU General Public License v3.0`.

