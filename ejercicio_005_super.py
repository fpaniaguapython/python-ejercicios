class DarthVader:
    def saludar(self):
        print("Soy tu padre")

class Luke(DarthVader):
    def saludar(self):
        super().saludar()
        print("Soy Luke")

luke = Luke()
luke.saludar()