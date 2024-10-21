from typing import Any

class Comando:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("Soy el comando y me estoy ejecutando...")

comando = Comando()
comando()
