
from src.utils.constants import DATA_PATH, DATA_OUT_PATH

import csv

def join_data(encuesta):
    """genera un único archivo csv, puede ser de hogares o individuos"""

    # generar path al archivo único e identificar que escuesta estoy unificando
    if encuesta == "hogar":
        path_archivo_unico = DATA_OUT_PATH / "usu_hogar.csv"
        tipo = "usu_hogar_*"
    else:
        path_archivo_unico = DATA_OUT_PATH / "usu_individual.csv"
        tipo = "usu_individual_*"
    
    # Para controlar que el encabezado se escriba una sola vez
    se_escribio_encabezado = False  

    # abro el archivo único para escribirlo
    with path_archivo_unico.open('w', newline="", encoding = "utf-8") as archivo_unico_csv:

        writer = csv.writer(archivo_unico_csv)

        #recorro las carpetas que contiene data_eph
        for path_trimestre in DATA_PATH.iterdir():
            
            #recorro archivos de un trimestre, solo los que quiero unir --> tipo = hogar || individual
            for path_archivo in path_trimestre.glob(tipo):
                
                # abro el csv a copiar 
                with path_archivo.open('r', encoding='utf-8') as archivo_csv:
                    
                    csv_reader = csv.reader(archivo_csv, delimiter=';') #genero iterable

                    header, data = next(csv_reader), list(csv_reader)
                
                if not se_escribio_encabezado:
                    writer.writerow(header)
                    se_escribio_encabezado = True

                for line in data:
                    writer.writerow(line)


