import os
import time

#Aviso principal de los requisitos esperados
print("Instalador del tiradados rolDaditos basado en web")
print("Vas a instalar el sistema de tiradados rolDaditos. Este instalador asume: ")
print("		1. Que instalarás esto en una máquina Debian o Ubuntu.")
print("		2. Que utilizas Apache2.")
print("		3. Que tienes el dominio al que quieres asignar este virtualHost.")
print("		4. Que tu WebRoot es /var/www/.")
print("		5. Que la cuenta con la que has ejecutado este script tiene acceso de administrador, usando la cuenta root.")
print("		6. Que PostgreSQL está instalado en esta misma máquina.")
print("		7. Que tienes instalado y funcional un usuario de PostgreSQL capaz de crear bases de datos a base de conexión remota, no con el método de 'su'.")

#Comprobación de si se quiere continuar
seguro = input("Quieres continuar? [s/N]")
if seguro not in ["s", "S"]:
	exit()

#Si se quiere continuar, empieza el script
print("Se va a continuar con la instalación!")
time.sleep(2)
print("Primero comprobaremos que instalas todo lo necesario...")
time.sleep(2)

#Actualizar e instalar los paquetes necesarios
os.system("apt update")
os.system("apt install -y python3-psycopg2 php-pgsql php")
print("\nInstalado todo lo necesario! Ahora se recargará Apache2.")
time.sleep(2)
import psycopg2

#Reiniciar Apache2
os.system("service apache2 reload")
print("\nExtrayendo carpeta de contenidos.")
time.sleep(2)

#Extraer a su carpeta los archivos de la webApp
os.system("mkdir source/apache")
os.system("tar -xvzf source/files.tar.gz -C source/apache")

#Credeciales de la webApp en PostgreSQL
dbUser = input("\nEscribe el usuario que luego será dueño de la base de datos: ")
dbPassword = input("Contraseña que el usuario creado usará para que la web se comunique con PostgreSQL (CUIDADO: LA CONTRASEÑA ES VISIBLE EN ESTE PASO): ")
dbDatabase = input("Nombre de la base de datos que crearás, donde se guardarán los registros para la web: ")
vhostDomain = input("Dominio que estará en el vhost y que apuntará a esta web: ")
pageName = input("Nombre de quién lleva el contador, ejemplo escribir 'María' para establecer en la web 'Tiradados de María': ")
print("Todos los datos recogidos! Hagamos un par de cambios en los archivos para adaptarlos: ")
time.sleep(2)

#Replace con los datos recibidos para el backend
replaceUser = "sed -i 's/user=REPLACE/user=" + dbUser + "/g' source/apache/backend/creds/.my.cnf"
os.system(replaceUser)
replacePass = "sed -i 's/password=REPLACE/password=" + dbPassword + "/g' source/apache/backend/creds/.my.cnf"
os.system(replacePass)
replaceDB = "sed -i 's/database=REPLACE/database=" + dbDatabase + "/g' source/apache/backend/creds/.my.cnf"
os.system(replaceDB)
replacePageName = "sed -i 's/name=REPLACE/name=" + pageName + "/g' source/apache/backend/creds/.my.cnf"
os.system(replacePageName)

#Replace para el vHost de Apache2
replacevHost = "sed -i 's/    ServerName REPLACE/    ServerName " + vhostDomain + "/g' source/roldaditos.conf"
os.system(replacevHost)

#Replace en el script sql
replaceSQL = "sed -i 's/ALTER TABLE public.campaigns OWNER TO REPLACEONINSTALL;/ALTER TABLE public.campaigns OWNER TO " + dbUser + ";/g' source/db.sql"
os.system(replaceSQL)
replaceSQL = "sed -i 's/ALTER TABLE public.personajes OWNER TO REPLACEONINSTALL;/ALTER TABLE public.personajes OWNER TO " + dbUser + ";/g' source/db.sql"
os.system(replaceSQL)
replaceSQL = "sed -i 's/ALTER TABLE public.tiradas OWNER TO REPLACEONINSTALL;/ALTER TABLE public.tiradas OWNER TO " + dbUser + ";/g' source/db.sql"
os.system(replaceSQL)
replaceSQL = "sed -i 's/ALTER TABLE public.tiradas_id_seq OWNER TO REPLACEONINSTALL;/ALTER TABLE public.tiradas_id_seq OWNER TO " + dbUser + ";/g' source/db.sql"
os.system(replaceSQL)

#Credenciales de administrador de postgreSQL
print("\nAhora necesitamos los credenciales de acceso a la base de datos.")
dbAdminUser = input("Nombre del usuario que puede crear usuarios con permisos en el gestor de bases de datos: ")
dbAdminPass = input("Contraseña del usuario que puede crear usuarios con permisos en el gestor de bases de datos (CUIDADO: LA CONTRASEÑA ES VISIBLE EN ESTE PASO): ")
connString = "host='localhost' dbname='postgres' user='" + dbAdminUser + "' password='" + dbAdminPass + "'"
conn = psycopg2.connect(connString)
print("Conectado! Ahora el script ejecutará las tareas necesarias: ")
cursor = conn.cursor()

#Crea el usuario especificado par que sea dueño de la base de datos
print("Creando el usuario aislado...")
query = "CREATE USER " + dbUser + " WITH CREATEDB ENCRYPTED PASSWORD '" + dbPassword + "'"
cursor.execute(query)
conn.commit()
cursor.close()
conn.close()

#Crea la database donde se guardarán las muertes, por aislamiento 
print("Creando la base de datos...")
connString = "host='localhost' dbname='postgres' user='" + dbUser + "' password='" + dbPassword + "'"
conn = psycopg2.connect(connString)
cursor = conn.cursor()
conn.autocommit = True
query = "CREATE DATABASE " + dbDatabase
cursor.execute(query)
cursor.close()
conn.autocommit = False
conn.close()

#Lee el .sql de las tablas y lo ejecuta para crear las tablas con el owner correcto
print("Creando las tablas de la base de datos...")
connString = "host='localhost' dbname='" + dbDatabase + "' user='" + dbUser + "' password='" + dbPassword + "'"
conn = psycopg2.connect(connString)
cursor = conn.cursor()
cursor.execute(open("source/db.sql", "r").read())
conn.commit()
cursor.close()
conn.close()
print("Se han creado los elementos de bases de datos! Ahora lo moveremos todo a su sitio y podrás crear tu VirtualiHost de Apache2 con webroot en /var/www/roldaditos/frontend/, iniciarlo, y ya estará funcional.")
time.sleep(2)

#Mover todo a su lugar y cambiar los permisos a los correctos
os.system("mkdir /var/www/roldaditos")
os.system("mv source/apache/* /var/www/roldaditos/")
os.system("chown root:www-data -R /var/www/roldaditos/frontend/")
os.system("mv source/roldaditos.conf /etc/apache2/sites-available/")
os.system("a2ensite roldaditos")
print("Todo listo! Recargando apache2 para que el site esté activo...")
time.sleep(2)
os.system("service apache2 reload")
print("Listo! Que disfrutes del tiradados rolDaditos! ya puedes borrar esta carpeta de instalación si quieres")

