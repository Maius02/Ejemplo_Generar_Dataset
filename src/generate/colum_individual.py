import csv

def generate_column_CH04_str(path_individual):
    """Se traduce los valores CH04 numéricos a "Masculino" y "Femenino" según corresponda. El resultado se debe 
    almacenar en una nueva columna llamada CH04_str. """

    with open(path_individual, 'r', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo, delimiter=';')
        data = list(reader)
        header = reader.fieldnames + ["CH04_str"]
        
    # modifico las filas, agrego nuevas columnas
    for file in data:
        file["CH04_str"] = 'Masculino' if file['CH04'] == '1' else 'Femenino'
    
    # Escribimos de nuevo el mismo archivo, con la columna nueva
    with open(path_individual, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames = header, delimiter = ';')
        writer.writeheader()
        writer.writerows(data)
