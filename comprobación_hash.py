import os
import hashlib

def calcular_hash(archivo, algoritmo='SHA256'):
    try:
        hash_func = getattr(hashlib, algoritmo.lower())()
        with open(archivo, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                hash_func.update(byte_block)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al calcular el hash del archivo '{archivo}': {e}")
        return None

def leer_archivo_hashes(archivo_hashes):
    hashes_esperados = {}
    try:
        with open(archivo_hashes, 'r') as f:
            for linea in f:
                try:
                    nombre, hash_value = linea.strip().split(':', maxsplit=1)
                    hashes_esperados[nombre.strip()] = hash_value.strip()
                except ValueError:
                    print(f"Error: Formato incorrecto en la línea '{linea.strip()}'.")
    except FileNotFoundError:
        print(f"Error: El archivo de hashes '{archivo_hashes}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo de hashes: {e}")
        return None
    return hashes_esperados

def comprobar_archivos_y_hashes(archivo_hashes, directorio_archivos='.'):
    hashes_esperados = leer_archivo_hashes(archivo_hashes)
    if hashes_esperados is None:
        return

    print("\nComprobación de archivos y hashes:")
    for nombre, hash_esperado in hashes_esperados.items():
        archivo = os.path.join(directorio_archivos, nombre)
        print(f"\nArchivo: {archivo}")
        if not os.path.exists(archivo):
            print(f"  Resultado: El archivo no existe.")
            continue

        hash_calculado = calcular_hash(archivo)
        if hash_calculado is None:
            continue

        print(f"  CALCULADO: {hash_calculado}")
        print(f"  ESPERADO:  {hash_esperado}")
        if hash_calculado == hash_esperado:
            print(f"  Resultado: El hash es correcto y coincide.")
        else:
            print(f"  Resultado: El hash no coincide.")

archivo_hashes = 'hashes_sha256.txt'  
directorio_archivos = 'E:\\Proyecto5_AF\\'
comprobar_archivos_y_hashes(archivo_hashes, directorio_archivos)