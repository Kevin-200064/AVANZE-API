from config.logger import Logger
class MecanicoNoEncontradoError(Exception):
    def __init__(self, mecanico_id):
        super().__init__(f"Mecánico ID={mecanico_id} no encontrado")
class MecanicoDAO:
    def __init__(self):
        self.__bd = []
        self.__cid = 1
        self.__log = Logger()
        
    def buscar_por_id(self, id):
        for m in self.__bd:
            if m.id == id: return m
        return None
        
    def insertar(self, mecanico):
        mecanico.id = self.__cid
        self.__cid += 1
        self.__bd.append(mecanico)
        self.__log.info(f"Mecánico agregado: {mecanico.nombre} {mecanico.apellido} (ID={mecanico.id})")
        return mecanico
        
    def obtener_todos(self):
        return sorted(self.__bd, key=lambda m: m.apellido)
        
    def actualizar(self, mecanico_id, especialidad=None):
        m = self.buscar_por_id(mecanico_id)
        if not m:
            self.__log.error(f"Actualizar fallido: Mecánico ID={mecanico_id} no existe")
            raise MecanicoNoEncontradoError(mecanico_id)
        if especialidad: m.especialidad = especialidad
        self.__log.info(f"Mecánico actualizado: ID={mecanico_id}")
        return m
        
    def eliminar(self, mecanico_id):
        m = self.buscar_por_id(mecanico_id)
        if not m:
            self.__log.error(f"Eliminar fallido: Mecánico ID={mecanico_id} no existe")
            raise MecanicoNoEncontradoError(mecanico_id)
        self.__bd.remove(m)
        self.__log.info(f"Mecánico eliminado: {m.nombre} (ID={mecanico_id})")
        return True
        
    def total(self):
        return len(self.__bd)