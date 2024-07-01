
''' Aqui se menciona y solicita por medio de esta variable el numero de ID del usuario el cual sera almacenado con valor numero debido al uso de INT a traves de Input '''
SolicitudID = str(input('Proporcionar tu numero de nomina: '))
''' Aqui se usa while para condicionar a que el numero de nomina sea alfanumerico a traves de isalnum lo cual valida si contiene lo valores solicitados'''
while not SolicitudID.isalnum():
        ''' En caso de que no cumpla arroja el siguiente print y despues nuevamente el input el cual debe cumplirse la condicion de cualquier manera '''
        print('Nómina en formato incorrecto. Debe capturar solo números y letras.')
        SolicitudID = str(input('Ingresa el correcto: '))

''' Aqui se menciona y solicita por medio de esta variable nombre del usuario el cual sera almacenado con valor string debido al uso de str '''
NombreUsuario = str(input('Proporcionar tu nombre: '))
''' Aqui se usa isalpha para validar que la condicion sean solo letras. De no ser asi arrojaria un nuevo input solicitandolo nuevamente'''
while not NombreUsuario.isalpha():
        ''' Se Muestra este print si la condicion de while no se cumple creando un nuevo input''' 
        print('Nombre de usuario en formato incorrecto. Debe capturar solo letras.')
        NombreUsuario = str(input('Ingresa tu nombre correctamente: '))
''' Aqui se menciona y solicita por medio de esta variable el numero de videos del usuario que subira el cual sera almacenado para posteriormente validarlo'''
NumeroDeVideos = int(input('Numeros de videos que subira: '))
''' Aqui usamos isdigit para validar que el input solo acepte numeros y no letras ''' 
while not NumeroDeVideos.is_integer():
        ''' En caso de no ser numero arrojaria este print y despues un nuevo input solicitaria el correcto numero de videos '''
        print('Cantidad de videos en formato incorrecto. Debe capturar solo números')
        NumeroDeVideos = int(input('Ingresa el correcto numeros de videos que subira: '))

''' Finalmente imprimimos lo que se capturo en las variables antes solicitadas por medio de inputs ''' 
print('Bienvenido,', NombreUsuario, ' tu número de nómina es', SolicitudID, 'y estás intentando subir', NumeroDeVideos, 'videos.')

''' Creamos una variable con inicio cero para evitar errores para despues solicitar un input de string que seria limitado por un si o no ''' 
OpcionSioNo = 0
OpcionSioNo = str(input('¿Es correcta la información? si/no.:' ))

''' La condicion arrojaria un for en caso de ser la respuesta si '''
if OpcionSioNo == 'si'or OpcionSioNo == 'Si' or OpcionSioNo == 'SI' or OpcionSioNo == 'sI':
    for NumeroDeVideo in range(NumeroDeVideos):
        TituloVideo = str(input('Titulo del video: '))
        if not TituloVideo.isalnum():
            print('Título del video en formato incorrecto. Debe capturar solo números y letras.')
            TituloVideo = str(input('Ingresa el Titulo del video correcto: '))  
        NombreDelVideo = str(input('Nombre del Video:'))
        if not NombreDelVideo.isalnum():
            print('Nombre del video en formato incorrecto. Debe capturar solo números y letras.')
            NombreDelVideo = str(input('Ingresa el Nombre del video correcto: '))  
        ExtensionDelVideo = str(input('Extension del video: '))
        if not ExtensionDelVideo.isalnum():
            print('Extensión del video en formato incorrecto. Debe capturar solo números y letras.')
            ExtensionDelVideo = str(input('Ingresa la extension del video correcta: '))  
        TamañoDelVideo = input('Tamaño del video en megas: ')
        if not int(TamañoDelVideo.isdigit()):
            print('Tamaño del video en formato incorrecto. Debe capturar solo números.')
            TamañoDelVideo = input('Ingrese el correcto formato y tamaño del video en megas: ')
        if int(TamañoDelVideo) > 3:
            print('El archivo no debe pesar más de 3 MB.')
            TamañoDelVideo = input('Ingrese el correcto tamaño del video en megas: ') 
elif OpcionSioNo == 'no' or OpcionSioNo == 'No' or OpcionSioNo == 'nO' or OpcionSioNo == 'NO':
    SalirDelSistema = str(input('Desea Salir del sistema? si/no: '))
    if SalirDelSistema == 'si':
        print('Muchas gracias por haber usado nuestro sistema, hasta pronto')
    if SalirDelSistema == 'no':
        SolicitudID = int(input('Proporcionar tu numero de nomina: '))
        ''' Aqui se menciona y solicita por medio de esta variable nombre del usuario el cual sera almacenado con valor string debido al uso de str '''
        NombreUsuario = str(input('Proporcionar tu nombre: '))
        ''' Aqui se menciona y solicita por medio de esta variable el numero de videos del usuario qeu subira el cual sera almacenado con valor numero debido al uso de INT '''
        NumeroDeVideos = int(input('Numeros de videos que subira: '))
while True:
    try:
        if OpcionSioNo != 'si'or OpcionSioNo != 'Si' or OpcionSioNo != 'SI' or OpcionSioNo != 'sI' or OpcionSioNo != 'no' or OpcionSioNo != 'No' or OpcionSioNo != 'nO' or OpcionSioNo != 'NO':
            break
      # Sale del bucle si todo está bien
    except ValueError:
        print("Error: Debes ingresar un si o no.")
    except Exception as e:
        print(f"Error inesperado: {e}")






    
   
