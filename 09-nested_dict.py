nested_dict = {
    "Persona1": {"Nombre": "Ricardo", "edad": 29, "Ciudad": "Ciudad de México"},
    "Persona2": {"Nombre": "Carlos", "edad": 31, "Ciudad": "Córdoba"},
    "Persona3": {"Nombre": "Carmen", "edad": 44, "Ciudad": "Gualajara"},
}

for key, value in nested_dict.items():
    print(f"{key}:")
    for sub_key, sub_value in value.items():
        print(f" {sub_key}: {sub_value}")
