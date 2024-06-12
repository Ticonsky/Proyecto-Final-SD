# Clase que representa un tipo de propiedad
class propertyType:
    def __init__(self, name, description):
        # Constructor de la clase propertyType, inicializa los atributos del tipo de propiedad
        self.name = name  # Nombre del tipo de propiedad
        self.description = description  # Descripción del tipo de propiedad

    # Métodos getter y setter para cada atributo de la clase propertyType

    # Getter para name
    def get_name(self):
        return self.name

    # Setter para name
    def set_name(self, name):
        self.name = name

    # Getter para description
    def get_description(self):
        return self.description

    # Setter para description
    def set_description(self, description):
        self.description = description
