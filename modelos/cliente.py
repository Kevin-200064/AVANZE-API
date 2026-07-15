class Cliente:                                         
    def __init__(self, nombre, apellido, telefono, email):  
        self.id = None      
        self.nombre = nombre    
        self.apellido = apellido       
        self.telefono = telefono  
        self.email = email     
    
    def __str__(self):            
        return f"[{self.id}] {self.apellido}, {self.nombre} | Tel: {self.telefono} | {self.email}"

    def to_dict(self):
        return 
        {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
            "email": self.email
        }

    def from_dict(d):
        c = Cliente(d["nombre"], d["apellido"], d["telefono"], d["email"])
        c.id = d["id"]
        return c