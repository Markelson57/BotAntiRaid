# Bot Anti-Raid

El Bot Anti-Raid es una herramienta diseñada para proteger tu servidor Discord de comportamientos maliciosos y acciones no deseadas. A continuación se describen sus principales características:

## Funcionalidades:

1. **Eliminación de mensajes repetidos:** El bot monitorea los mensajes enviados en los canales del servidor y detecta si hay mensajes repetidos, en particular aquellos que mencionan a `@everyone`. Si se detecta un mensaje repetido en un corto período de tiempo, el bot automáticamente eliminará los mensajes duplicados para evitar el spam.

2. **Detección de canales repetidos:** Cuando se crea un nuevo canal en el servidor, el bot verifica si el nombre del canal ya existe en la lista de canales previamente creados. Si se detecta un nombre de canal repetido, el bot eliminará el canal recién creado para evitar la creación masiva de canales no deseados.

3. **Expulsión de miembros que crean canales repetidos:** Si un miembro se une al servidor y se detecta que ha creado canales repetidos, el bot tomará medidas para expulsar a ese miembro del servidor. Esto ayuda a mantener un entorno seguro y libre de abusos.

Recuerda que el bot Anti-Raid necesita tener los permisos adecuados en el servidor para poder realizar estas acciones de protección.

## Pasos para utilizar el Bot Anti-Raid

1. **Descargar el programa**: Descarga el archivo antiraid.py que contiene el código del Bot Anti-Raid en tu sistema.

2. **Instalar las dependencias**: Abre tu terminal y ejecuta el siguiente comando para instalar las dependencias requeridas:

   pip install discord

3. **Crear una aplicación y obtener el token del bot**: Crea una aplicación en el Portal de Desarrolladores de Discord, crea un bot y obtén el token del bot.

4. **Configurar el archivo antiraid.py**: Abre el archivo antiraid.py en tu editor de código y reemplaza 'INSERTA_AQUÍ_TU_TOKEN' en la línea `TOKEN = 'INSERTA_AQUÍ_TU_TOKEN'` con el token del bot obtenido en el paso anterior.

5. **Ejecutar el programa**: Guarda los cambios en el archivo antiraid.py y ejecuta el siguiente comando desde tu terminal:

   python antiraid.py

6. **Invitar al bot a tu servidor Discord**: Una vez que el programa esté en funcionamiento, obtendrás un enlace de invitación en la terminal. Copia el enlace e invita al bot a tu servidor Discord.

7. **Configurar los permisos del bot**: Asegúrate de asignar los permisos adecuados al bot en tu servidor Discord para que pueda realizar acciones como eliminar mensajes y expulsar a los infractores.

8. **Activar el bot**: Activa el Bot Anti-Raid en el canal donde deseas que monitoree y tome medidas contra actividades sospechosas.

9. **Proteger tu servidor**: El Bot Anti-Raid estará activo en tu servidor Discord, detectando y tomando medidas contra acciones no deseadas como creación masiva de canales, spam de mensajes y menciones repetidas.

Para obtener más información y contenido relacionado, te invitamos a visitar el canal de YouTube Markelson57.

## COMANDOS

1. **!scan**: Este es el unico comando de momento ya que eo se utiliza si el bot no pudo bloquer el raid. Lo que hace es escanear los canales repetidos y los elimina si es que puede, luego escanea los canales eliminados, para poder recuperarlo. Ademas, el bot con este comando puede recuperar los canales eliminados por el raid. **NOTA**: Si noo has usado el comando despues de 30 min, el server no se podrá recuperarlo.
