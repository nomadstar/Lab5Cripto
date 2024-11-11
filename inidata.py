# Para efectos de copatibilidad con ambos algoritmos se trabajara con bloques de 128 bits siempre
import sys, pycryptodome
class fowardData:
    requiredvalues = {
        "algoritmo": str,
        "tamañobloque": int,
        "padding": str,
        "texto": str,
        "key": str,
        # Solo se permite modo CBC en este programa
        "iv": None,
    }
    def initialize(self, required):
        for key in self.requiredvalues:
            if key in required:
                try:
                    self.requiredvalues[key] = self.requiredvalues[key](input(f"Introduzca el valor de {key}: "))
                except ValueError:
                    print(f"El valor de {key} no es valido")
                    sys.exit(1)
        return True
                    
if __name__ == "__main__":
    data = fowardData()
    required = {"algoritmo", "tamañobloque", "padding", "texto", "key"}
    data.initialize(required)
    print(data.requiredvalues)
    input("Presione enter para continuar... de lo contrario presione ")

                


