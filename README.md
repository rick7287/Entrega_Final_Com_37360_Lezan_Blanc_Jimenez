# Entrega_Final_Com_37360_Lezan_Blanc_Jimenez
Entrega del proyecto final de la comision 37360, curo de Python de CoderOuse

En este link puedes ver el video de la pagina en operacion.
<https://www.youtube.com/watch?v=jsI5otXLU5A>

Este viseo complementario muestra un cambio de ultima hora en el modulo de registro
<https://www.youtube.com/watch?v=Rk9PnT6GmhA>


Los archivos del proyecto estan en la rama 'master' de este repositorio

Integrantes:

Paula Lezan: Encargada de la app de mensajeria, 'Message'. Se creo una app que permite a los usuarios mandar mesnajes a otros usuarios registrados. Consta de un inbox donde se muestran los 'hilos' de conversacion que se tiene con algun usuario. Al hacer click al vinculo con el nombre del usuario, se muestran los mensajes que hay entre ese usuario y la persona loggeada.


Ricardo Jimenez: Encargado de la app 'Blog' y 'comun': Se creo la App para el manejo del Blog. Incluye un CRUD completo para crear, editar, borrar y ver entradas de blog. Se incluyo el uso del editor de texto enriquecido de Django CKeditor para el template de creacion y edicion de publicaciones del blog. En la app 'comun' simplemente se crearon las vistas para mandar llamar a la pagina de inicio (/) y acerca de (/about), las cuales se hicieron en html basico.


Ramon Blanc: Encargado de la app de manejo de usuarios, 'accounts'
La consruccion fue de la siguiente manera:
Primeramente, uso el modelo User de Django, al usar el UserCreationForm para creacion de usuarios, y las funciones asociadas (como por ej. is_authenticated). Esto me garantiza un login, signup y logout solidos y seguros, ya que utilizo los propios de Django. 
Luego, creo el modelo propio Perfil, estableciendo una relacion OneToOne en el atributo user,  lo cual permite poder usar todos los metodos y atributos de User, pero ademas pudiendo agregar los atributos requeridos por consigna ( link, imagen, y descripcion, este ultimo en formato TextField). 
Ademas, defino en models.py, mediante el uso de signals (post_save, sender), la funcion create_user_perfil, que me crea automaticamente, un objecto perfil asociado a cada user (creado al hacer el signup). 
En cuanto a las vistas, signup y login_request no tienen ninguna novedad, pero si la vista editar_perfil, que junta dos formularios en una sola vista, permitiendo editar/guardar, de una sola vez, los atributos de Perfil y User, siendo muy comodo para el usuario manejar su informacion de Perfil. 
La aplicacion es muy sencilla de usar, pudiendo realizar todas las acciones mediante botones bien visibles para el usuario. Incluso permite eliminar totalmente el perfil.

Por ultimo, desde la ruta  /admin, podemos ver y editar todos los modelos  del Proyecto. Solo necesitamos haber creado un superuser, pudiendo hacerlo ingresando, en la ventana de comandos,  ‘python manage.py createsuperuser’. Estar seguros de estar en el directorio del Proyecto antes de hacer esto.





