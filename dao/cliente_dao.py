from config.logger import Logger

class ClienteNoEncontradoError(Exception):
    def __init__(self, cliente_id):
        super().__init__(f"Cliente ID={cliente_id} no encontrado")

class RUCDuplicadoError(Exception):
    def __init__(self, ruc):
        super().__init__(f"RUC '{ruc}' ya registrado")

class ClienteDAO:
    def __init__(self):
        self.__bd = []
        self.__cid = 1
        self.__log = Logger()
    
    def buscar_por_ruc(self, ruc):
        for c in self.__bd:
            if c.ruc == ruc: return c
        return None
    
    def buscar_por_id(self, id):
        for c in self.__bd:
            if c.id == id: return c
        return None
    
    def insertar(self, cliente):
        if self.buscar_por_ruc(cliente.ruc):
            self.__log.warning(f"RUC duplicado: {cliente.ruc}")
            raise RUCDuplicadoError(cliente.ruc)
        cliente.id = self.__cid
        self.__cid += 1
        self.__bd.append(cliente)
        self.__log.info(f"Cliente agregado: {cliente.nombre} (ID={cliente.id})")
        return cliente
    
    def obtener_todos(self):
        return sorted(self.__bd, key=lambda c: c.nombre)
    
    def actualizar(self, cliente_id, nombre=None, email=None, telefono=None):
        c = self.buscar_por_id(cliente_id)
        if not c:
            self.__log.error(f"Actualizar fallido: Cliente ID={cliente_id} no existe")
            raise ClienteNoEncontradoError(cliente_id)
        if nombre: c.nombre = nombre
        if email: c.email = email
        if telefono: c.telefono = telefono    
        self.__log.info(f"Cliente actualizado: ID={cliente_id}")
        return c
    
    def eliminar(self, cliente_id):
        c = self.buscar_por_id(cliente_id)
        if not c:
            self.__log.error(f"Eliminar fallido: Cliente ID={cliente_id} no existe")
            raise ClienteNoEncontradoError(cliente_id)
        self.__bd.remove(c)
        self.__log.info(f"Cliente eliminado: {c.nombre} (ID={cliente_id})")
        return True
    
    def total(self):
        return len(self.__bd)