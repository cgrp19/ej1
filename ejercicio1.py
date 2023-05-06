class Email:
    __idcuenta=''
    __dominio=''
    __tipodominio=''
    __contrasena=''
    def __init__(self,idcuenta,dominio,tipodominio,contrasena):
        self.__idcuenta=idcuenta
        self.__dominio=dominio
        self.__tipodominio=tipodominio
        self.__contrasena=contrasena
    def retornaemail(self):
        print('{}@{}.{}'.format(self.__idcuenta,self.__dominio,self.__tipodominio,self.__tipodominio))
    def getdominio(self):
        return 'El dominio es: '.format(self.__dominio)
    def crearcuenta(self):
        print('Ingrese un email para crear la cuenta:')