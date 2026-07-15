from config.logger import Logger

class OrdenNoEncontradaError(Exception):
    def __init__(self, orden_id):
        super().__init__(f"Orden de Trabajo ID={orden_id} no encontrada")

class OrdenTrabajoDAO:
    def __init__(self):
        self.__bd = []
        self.__cid = 1
        self.__log = Logger()
        
    def buscar_por_id(self, id):
        for o in self.__bd:
            if o.id == id: return o
        return None
        
    def insertar(self, orden):
        orden.id = self.__cid
        self.__cid += 1
        self.__bd.append(orden)
        self.__log.info(f"Orden agregada: Vehículo ID={orden.id_vehiculo} (ID={orden.id})")
        return orden
        
    def obtener_todos(self):
        return sorted(self.__bd, key=lambda o: o.id)
        
    def actualizar(self, orden_id, estado=None, costototal=None, id_mecanico=None):
        o = self.buscar_por_id(orden_id)
        if not o:
            self.__log.error(f"Actualizar fallido: Orden ID={orden_id} no existe")
            raise OrdenNoEncontradaError(orden_id)
        if estado: o.estado = estado
        if costototal is not None: o.costototal = costototal
        if id_mecanico is not None: o.id_mecanico = id_mecanico
        self.__log.info(f"Orden actualizada: ID={orden_id}")
        return o
        
    def eliminar(self, orden_id):
        o = self.buscar_por_id(orden_id)
        if not o:
            self.__log.error(f"Eliminar fallido: Orden ID={orden_id} no existe")
            raise OrdenNoEncontradaError(orden_id)
        self.__bd.remove(o)
        self.__log.info(f"Orden eliminada: ID={orden_id}")
        return True
        
    def total(self):
        return len(self.__bd)