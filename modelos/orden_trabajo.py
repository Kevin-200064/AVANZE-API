class OrdenTrabajo:
    def __init__(self, descripcionfalla, estado, costototal, id_vehiculo, id_mecanico=None):
        self.id = None
        self.descripcionfalla = descripcionfalla
        self.estado = estado  
        self.costototal = costototal
        self.id_vehiculo = id_vehiculo
        self.id_mecanico = id_mecanico  
        
    def __str__(self):
        mecanico_str = f"Mecánico ID: {self.id_mecanico}" if self.id_mecanico else "Sin asignar"
        return f"[{self.id}] Vehículo ID: {self.id_vehiculo} | Falla: {self.descripcionfalla} | Estado: {self.estado.upper()} | Costo: S/.{self.costototal:.2f} | {mecanico_str}"

    def to_dict(self):
        return {
            "id": self.id,
            "descripcionfalla": self.descripcionfalla,
            "estado": self.estado,
            "costototal": self.costototal,
            "id_vehiculo": self.id_vehiculo,
            "id_mecanico": self.id_mecanico
        }

    def from_dict(d):
        o = OrdenTrabajo(d["descripcionfalla"], d["estado"], d["costototal"], d["id_vehiculo"], d["id_mecanico"])
        o.id = d["id"]
        return o