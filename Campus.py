
class Campus:
    # Constructor
    def __init__(self, __campusNit:int, __campusName: str, __campusPhone: str,
                __campusAddreess: str, __parking:bool, __sizeParking: int, __technicalService: bool, __user:User):
        # Datos de entrada
        self._campusNit = __campusNit
        self._campusName = __campusName
        self._campusPhone = __campusPhone
        self._campusAddreess = __campusAddreess
        self._parking = __parking
        self._sizeParking = __sizeParking
        self._technicalService = __technicalService
        #self._item = Proveedor(122324, 'Colchoneta', '6068848484', 'holi@example.com')   # Composición Item

    # Getter and Setter

    def __str__(self):
        return f"Nombre= {self.__campusName},Telefono= {self.__campusPhone},Dirección= {self.__campusAddreess}"

    def getCampusName(self):
        return self.__campusName
    def getCampusPhone(self):
        return self.__campusPhone
    def getCampusAddress(self):
        return self.__campusAddreess
    def setCampusName(self,__campusName):
        self.__campusName = __campusName
    def setCampusPhone(self,__campusPhone):
        self.__campusPhone = __campusPhone
    def setCampusAddreess(self,__campusAddreess):
        self.__campusAddreess = __campusAddreess


    campus:list=[]
    campus1 = Campus("900712196", "European Hardcore", "Chipre", "cualquier cosa", True, 13, False, optUser())
    campus.append(campus1)
    campus2 = Campus("800206239", "MMA Training", "La Sultana", "cualquier otra cosa", False, 0, True, optUser())
    campus.append(campus2)