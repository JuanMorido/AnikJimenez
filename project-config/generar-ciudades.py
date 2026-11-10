#!/usr/bin/env python3
"""Genera ahoraestuturno/ciudades.json, la lista que usa el buscador de "Ciudad y país".

Fuente: GeoNames (https://www.geonames.org), licencia CC BY 4.0.
Uso:    python3 project-config/generar-ciudades.py
Descarga unos 215 MB a una carpeta temporal la primera vez.

Criterio: ciudades de más de 15.000 habitantes de todo el mundo y de más de 5.000
en los países de habla hispana, ordenadas de mayor a menor población. Cada entrada es
"Nombre|PAÍS" o "Nombre|PAÍS|Nombre original" cuando el nombre en español difiere del
de GeoNames (así "London" también encuentra "Londres").
"""
import collections
import io
import json
import pathlib
import tempfile
import urllib.request
import zipfile

BASE = "https://download.geonames.org/export/dump/"
CACHE = pathlib.Path(tempfile.gettempdir()) / "geonames"
SALIDA = pathlib.Path(__file__).resolve().parent.parent / "ahoraestuturno" / "ciudades.json"

HISPANOS = {
    "AR", "BO", "CL", "CO", "CR", "CU", "DO", "EC", "ES", "GQ", "GT", "HN",
    "MX", "NI", "PA", "PE", "PR", "PY", "SV", "UY", "VE",
}
# Nombres administrativos que GeoNames lista a veces como nombre en español de una ciudad
ADMINISTRATIVOS = ("Provincia", "Distrito", "Delegación", "Municipio", "Departamento", "Región")
CORRECCIONES = {
    ("Havana", "CU"): "La Habana",
    ("Panama City", "PA"): "Ciudad de Panamá",
}
# Países que GeoNames trae con su nombre oficial largo; se usa el nombre corriente
PAISES_CORREGIDOS = {
    "BQ": "Caribe neerlandés",
    "CU": "Cuba",
    "CW": "Curazao",
    "GQ": "Guinea Ecuatorial",
    "KR": "Corea del Sur",
    "MA": "Marruecos",
    "SS": "Sudán del Sur",
    "SX": "Sint Maarten",
}


def descargar(nombre):
    CACHE.mkdir(exist_ok=True)
    destino = CACHE / nombre
    if not destino.exists():
        print("Descargando", nombre)
        urllib.request.urlretrieve(BASE + nombre, destino)
    return destino


def lineas(nombre_zip, interno):
    with zipfile.ZipFile(descargar(nombre_zip)) as z, z.open(interno) as f:
        for linea in io.TextIOWrapper(f, encoding="utf-8"):
            yield linea.rstrip("\n").split("\t")


def main():
    ciudades = {}
    for archivo, solo in (("cities15000", None), ("cities5000", HISPANOS)):
        for f in lineas(archivo + ".zip", archivo + ".txt"):
            if solo is None or f[8] in solo:
                ciudades.setdefault(f[0], {"nombre": f[1], "pais": f[8], "poblacion": int(f[14])})

    paises = {}
    with urllib.request.urlopen(BASE + "countryInfo.txt") as f:
        for linea in io.TextIOWrapper(f, encoding="utf-8"):
            if not linea.startswith("#"):
                c = linea.rstrip("\n").split("\t")
                paises[c[16]] = {"codigo": c[0], "nombre": c[4]}

    alternos = collections.defaultdict(list)
    for f in lineas("alternateNamesV2.zip", "alternateNamesV2.txt"):
        if f[2] == "es" and (f[1] in ciudades or f[1] in paises):
            f += [""] * (8 - len(f))
            if f[6] != "1" and f[7] != "1":  # ni coloquial ni histórico
                alternos[f[1]].append((f[3], f[4] == "1"))

    def en_espanol(gid, c):
        fijo = CORRECCIONES.get((c["nombre"], c["pais"]))
        if fijo:
            return fijo
        opciones = [o for o in alternos.get(gid, []) if not o[0].startswith(ADMINISTRATIVOS)]
        nombres = [o[0] for o in opciones]
        if not opciones or c["nombre"] in nombres:
            return c["nombre"]
        preferidos = [o[0] for o in opciones if o[1]]
        if preferidos:
            return preferidos[0]
        # En países hispanos el nombre de GeoNames ya está en español, salvo los dobles ("A / B")
        if c["pais"] in HISPANOS and " / " not in c["nombre"]:
            return c["nombre"]
        return nombres[0]

    nombres_pais = {}
    for gid, p in paises.items():
        opciones = alternos.get(gid, [])
        preferidos = [o[0] for o in opciones if o[1]]
        nombres_pais[p["codigo"]] = (preferidos or [o[0] for o in opciones] or [p["nombre"]])[0]
    nombres_pais.update(PAISES_CORREGIDOS)

    vistos = set()
    entradas = []
    for gid, c in sorted(ciudades.items(), key=lambda kv: -kv[1]["poblacion"]):
        nombre = en_espanol(gid, c)
        if (nombre, c["pais"]) in vistos:
            continue
        vistos.add((nombre, c["pais"]))
        partes = [nombre, c["pais"]]
        if nombre != c["nombre"]:
            partes.append(c["nombre"])
        entradas.append("|".join(partes))

    usados = {e.split("|")[1] for e in entradas}
    datos = {
        "fuente": "GeoNames (geonames.org), CC BY 4.0",
        "paises": {k: v for k, v in sorted(nombres_pais.items()) if k in usados},
        "ciudades": entradas,
    }
    SALIDA.write_text(json.dumps(datos, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"{len(entradas)} ciudades, {len(datos['paises'])} países -> {SALIDA}")


if __name__ == "__main__":
    main()
