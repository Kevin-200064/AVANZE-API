class Mecanico:
    def __init__(self, nombre, apellido, especialidad):
        self.id = None
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        
    def __str__(self):
        return f"[{self.id}] {self.apellido}, {self.nombre} | Especialidad: {self.especialidad}"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "especialidad": self.especialidad
        }

    def from_dict(d):
        m = Mecanico(d["nombre"], d["apellido"], d["especialidad"])
        m.id = d["id"]
        return m