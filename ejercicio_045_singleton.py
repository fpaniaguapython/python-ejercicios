class Motor:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def get_motor(cls):
        if (hasattr(cls,'_Motor__motor')):
            print("Ya tiene motor")
            return cls.__motor
        else:
            print("Creando motor")
            cls.__motor = Motor()
            return cls.__motor

motor1 = Motor.get_motor()
motor2 = Motor.get_motor()
print(motor1==motor2)