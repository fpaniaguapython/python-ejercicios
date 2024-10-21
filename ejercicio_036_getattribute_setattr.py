from typing import Any
class Engendro:
    def __init__(self, nombre):
        self.nombre = nombre
    def __getattribute__(self, name: str):
        print("En el getattribute")
        return super().__getattribute__(name)
    def __setattr__(self, name: str, value: Any) -> None:
        print("Estoy en el setattr")
        super().__setattr__(name, value)
    
e = Engendro("Orco")#Estoy en el setattr, por la inicialización en __init__
print(e.nombre)#En el getattribute ; Orco
e.nombre = "Sauron"#Estoy en el setattr