# Para efectos de copatibilidad con ambos algoritmos se trabajara con bloques de 128 bits siempre
import sys

class fowardData:
    requiredvalues = {
        "algoritmo": str,
        "tamañobloque": int,
        "tipodepadding": str,
        "texto": str,
        "key": str,
        # Solo se permite modo CBC en este programa
        "iv": str,
    }
    def initialize(self, required):
        for key in self.requiredvalues:
            if key in required:
                try:
                    self.requiredvalues[key] = self.requiredvalues[key](input(f"Introduzca el valor de {key}: "))
                except ValueError:
                    print(f"El valor de {key} no es valido")
                    sys.exit(1)
        if "texto" in required:
            self.paddit()
        return 0

    def paddit(self):
        if self.requiredvalues["texto"] != "":
            if self.requiredvalues["tipodepadding"]=="PCKS":
                self.requiredvalues["texto"] = self.PCKS()
            elif self.requiredvalues["tipodepadding"]=="ISO":
                self.requiredvalues["texto"] = self.ISO()
            else:
                self.requiredvalues["texto"] = self.requiredvalues["texto"].encode()
                if len(self.requiredvalues["texto"])%self.requiredvalues["tamañobloque"]*8 != 0:
                    print("El texto no es multiplo del tamaño de bloque")
                    sys.exit(1)
                else:
                    print("Cifrando sin padding")
        # print("tamaño texto =" + str(len(self.requiredvalues["texto"]))) para checkear si esta bien.
        return 0    
    
    def PCKS(self):
        if len(self.requiredvalues["texto"])% self.requiredvalues["tamañobloque"] != 0:
            padding = self.requiredvalues["tamañobloque"]-len(self.requiredvalues["texto"])
            padding = chr(padding)
            while len(self.requiredvalues["texto"]) < self.requiredvalues["tamañobloque"]:
                self.requiredvalues["texto"] += padding
            self.requiredvalues["texto"] = self.requiredvalues["texto"]
        return self.requiredvalues["texto"]
    def ISO(self):
        self.requiredvalues["texto"] = self.requiredvalues["texto"] + bytes.fromhex("80").decode('latin1')
        while len(self.requiredvalues["texto"])%self.requiredvalues["tamañobloque"]*8 != 0:
            self.requiredvalues["texto"] += bytes.fromhex("00").decode('latin1')
        return self.requiredvalues["texto"]

                    
if __name__ == "__main__":
    print("Aquí se cifra DES, AES o 3DES")
    print("Rellenos PCKS o ISO")
    data = fowardData()
    required = {"tamañobloque","tipodepadding","texto"}
    data.initialize(required)
    print(data.requiredvalues)
    
    #if data.requiredvalues["algoritmo"] != ("DES" or "AES" or "3DES"):
    #    print("El algoritmo no es valido")
    #    sys.exit(1)


