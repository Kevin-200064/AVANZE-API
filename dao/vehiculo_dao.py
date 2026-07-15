from config.logger import Logger

class VehiculoNoEncontradoError(Exception):
    def __init__(self, vehiculo_id):
        super().__init__(f"Vehículo ID={vehiculo_id} no encontrado")

class PlacaDuplicadaError(Exception):
    def __init__(self, placa):
        super().__init__(f"Placa '{placa}' ya registrada")
class VehiculoDAO:
    def __init__(self):
        self.__bd = []
        self.__cid = 1
        self.__log = Logger()
        
    def buscar_por_placa(self, placa):
        for v in self.__bd:
            if v.placa.lower() == placa.lower(): return v
        return None
        
    def buscar_por_id(self, id):
        for v in self.__bd:
            if v.id == id: return v
        return None
        
    def insertar(self, vehiculo):
        if self.buscar_por_placa(vehiculo.placa):
            self.__log.warning(f"Placa duplicada: {vehiculo.placa}")
            raise PlacaDuplicadaError(vehiculo.placa)
        vehiculo.id = self.__cid
        self.__cid += 1
        self.__bd.append(vehiculo)
        self.__log.info(f"Vehículo agregado: {vehiculo.marca} {vehiculo.modelo} (ID={vehiculo.id})")
        return vehiculo
        
    def obtener_todos(self):
        return sorted(self.__bd, key=lambda v: v.placa)
        
    def actualizar(self, vehiculo_id, marca=None, modelo=None, anio=None):
        v = self.buscar_por_id(vehiculo_id)
        if not v:
            self.__log.error(f"Actualizar fallido: Vehículo ID={vehiculo_id} no existe")
            raise VehiculoNoEncontradoError(vehiculo_id)
        if marca: v.marca = marca
        if modelo: v.modelo = modelo
        if anio: v.anio = anio
        self.__log.info(f"Vehículo actualizado: ID={vehiculo_id}")
        return v
        
    def eliminar(self, vehiculo_id):
        v = self.buscar_por_id(vehiculo_id)
        if not v:
            self.__log.error(f"Eliminar fallido: Vehículo ID={vehiculo_id} no existe")
            raise VehiculoNoEncontradoError(vehiculo_id)
        self.__bd.remove(v)
        self.__log.info(f"Vehículo eliminado: Placa {v.placa} (ID={vehiculo_id})")
        return True
        
    def total(self):
        return len(self.__bd)