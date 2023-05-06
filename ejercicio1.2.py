import clase
def crear():
    print('Ingrese los siguientes datos:')
    idcuenta=input('ID de la cuenta:')
    dominio=input('Dominio:')
    tipodominio=input('Tipo del dominio:')
    contrasena=input('Contrasena:')
    email=Email(idcuenta,dominio,tipodominio,contrasena)
    return email