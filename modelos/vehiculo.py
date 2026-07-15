class Vehiculo:
    def __init__(self, placa, marca, modelo, anio, id_cliente):
        self.id = None
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.id_cliente = id_cliente  
        
    def __str__(self):
        return f"[{self.id}] {self.marca.upper()} {self.modelo} | Placa: {self.placa.upper()} | Año: {self.anio} (Cliente ID: {self.id_cliente})"

    def to_dict(self):
        return {
            "id": self.id,
            "placa": self.placa,
            "marca": self.marca,
            "modelo": self.modelo,
            "anio": self.anio,
            "id_cliente": self.id_cliente
        }

    def from_dict(d):
        v = Vehiculo(d["placa"], d["marca"], d["modelo"], d["anio"], d["id_cliente"])
        v.id = d["id"]
        return v