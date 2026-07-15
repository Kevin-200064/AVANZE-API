import json
import os
from modelos.cliente import Cliente
from modelos.vehiculo import Vehiculo
from modelos.mecanico import Mecanico
from modelos.orden_trabajo import OrdenTrabajo

_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARCHIVO_CLIENTES = os.path.join(_BASE, "datos_clientes.json")
ARCHIVO_VEHICULOS = os.path.join(_BASE, "datos_vehiculos.json")
ARCHIVO_MECANICOS = os.path.join(_BASE, "datos_mecanicos.json")
ARCHIVO_ORDENES = os.path.join(_BASE, "datos_ordenes.json")

# --- CLIENTES ---
def guardar_clientes(cdao):
    datos = [c.to_dict() for c in cdao.obtener_todos()]
    with open(ARCHIVO_CLIENTES, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print(f" OK Clientes guardados en '{ARCHIVO_CLIENTES}'")

def cargar_clientes(cdao):
    try:
        with open(ARCHIVO_CLIENTES, "r", encoding="utf-8") as f:
            datos = json.load(f)
        for d in datos:
            cliente = Cliente.from_dict(d)
            cdao._ClienteDAO__bd.append(cliente)
            if cliente.id >= cdao._ClienteDAO__cid:
                cdao._ClienteDAO__cid = cliente.id + 1
        print(f" OK {len(datos)} clientes cargados desde '{ARCHIVO_CLIENTES}'")
    except FileNotFoundError:
        print(f" AVISO: No existe '{ARCHIVO_CLIENTES}', se empieza desde cero")

# --- VEHÍCULOS ---
def guardar_vehiculos(vdao):
    datos = [v.to_dict() for v in vdao.obtener_todos()]
    with open(ARCHIVO_VEHICULOS, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print(f" OK Vehículos guardados en '{ARCHIVO_VEHICULOS}'")

def cargar_vehiculos(vdao):
    try:
        with open(ARCHIVO_VEHICULOS, "r", encoding="utf-8") as f:
            datos = json.load(f)
        for d in datos:
            vehiculo = Vehiculo.from_dict(d)
            vdao._VehiculoDAO__bd.append(vehiculo)
            if vehiculo.id >= vdao._VehiculoDAO__cid:
                vdao._VehiculoDAO__cid = vehiculo.id + 1
        print(f" OK {len(datos)} vehículos cargados desde '{ARCHIVO_VEHICULOS}'")
    except FileNotFoundError:
        print(f" AVISO: No existe '{ARCHIVO_VEHICULOS}', se empieza desde cero")

# --- MECÁNICOS ---
def guardar_mecanicos(mdao):
    datos = [m.to_dict() for m in mdao.obtener_todos()]
    with open(ARCHIVO_MECANICOS, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print(f" OK Mecánicos guardados en '{ARCHIVO_MECANICOS}'")

def cargar_mecanicos(mdao):
    try:
        with open(ARCHIVO_MECANICOS, "r", encoding="utf-8") as f:
            datos = json.load(f)
        for d in datos:
            mecanico = Mecanico.from_dict(d)
            mdao._MecanicoDAO__bd.append(mecanico)
            if mecanico.id >= mdao._MecanicoDAO__cid:
                mdao._MecanicoDAO__cid = mecanico.id + 1
        print(f" OK {len(datos)} mecánicos cargados desde '{ARCHIVO_MECANICOS}'")
    except FileNotFoundError:
        print(f" AVISO: No existe '{ARCHIVO_MECANICOS}', se empieza desde cero")

# --- ÓRDENES DE TRABAJO ---
def guardar_ordenes(odao):
    datos = [o.to_dict() for o in odao.obtener_todos()]
    with open(ARCHIVO_ORDENES, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print(f" OK Órdenes guardadas en '{ARCHIVO_ORDENES}'")

def cargar_ordenes(odao):
    try:
        with open(ARCHIVO_ORDENES, "r", encoding="utf-8") as f:
            datos = json.load(f)
        for d in datos:
            orden = OrdenTrabajo.from_dict(d)
            odao._OrdenTrabajoDAO__bd.append(orden)
            if orden.id >= odao._OrdenTrabajoDAO__cid:
                odao._OrdenTrabajoDAO__cid = orden.id + 1
        print(f" OK {len(datos)} órdenes cargadas desde '{ARCHIVO_ORDENES}'")
    except FileNotFoundError:
        print(f" AVISO: No existe '{ARCHIVO_ORDENES}', se empieza desde cero")
    


