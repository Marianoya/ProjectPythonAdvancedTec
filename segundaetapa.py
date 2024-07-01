class Persona:
      __nombre = 'Sin Nombre Identificado'
      __id = 0

  #Constructor
      def __init__(self, nombre, id):
          self.__nombre = nombre
          self.__id= id
      
      def CapturarNombre(self):
        self.__nombre= input('Ingresa el Nombre: ')
      
      def CapturarID(self):
        self.__id = int(input('Ingresa el ID: '))

      def imprimirNombre(self):
        print(f'Nombre: {self.__nombre}')

      def imprimirId(self):
        print(f'ID: {self.__id}')


class Videos: 
      __nombreDelVideo = 'Sin Nombre Identificado'
      __ExtensionDelVideo = 'Sin extension Identificada'
      __TamañoDelVideo = 0

  #Constructor
      def __init__(self, nombreDelVideo, ExtensionDelVideo, TamañoDelVideo):
          self.__nombreDelVideo = nombreDelVideo
          self.__ExtensionDelVideo = ExtensionDelVideo
          self.__TamañoDelVideo = TamañoDelVideo

      def CapturarNombredelVideo(self):
        self.nombreDelVideo = input('Ingresa el Nombre del Video: ')
      
      def CapturarExtensiondelVideo(self):
        self.ExtensionDelVideo = input('Ingresa la extension del video: ')
        
      def CapturarTamañodelVideo(self):
        self.TamañoDelVideo = int(input('Ingresa el tamaño del video: '))
        
      def imprimirNombredelVideo(self):
        print(f'Nombre del Video: {self.__nombreDelVideo}')

      def imprimirExtensiondelVideo(self):
        print(f'Extension del video: {self.__ExtensionDelVideo}')

      def imprimirTamañodelVideo(self):
        print(f'Tamaño del Video: {self.__TamañoDelVideo}')

ObjetoPersona = Persona("Mariano", 1)

ObjetoPersona.CapturarNombre()
ObjetoPersona.CapturarID()
ObjetoPersona.imprimirNombre()
ObjetoPersona.imprimirId()

ObjetoVideos = Videos("PruebaVideo", "mp4", 3)

ObjetoVideos.CapturarNombredelVideo()
ObjetoVideos.CapturarExtensiondelVideo()
ObjetoVideos.CapturarTamañodelVideo()
ObjetoVideos.imprimirNombredelVideo()
ObjetoVideos.imprimirExtensiondelVideo()
ObjetoVideos.imprimirTamañodelVideo()
