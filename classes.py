class Vehiculo:
    def __init__(self, color, placa, marca):
        self.color = color
        self.placa = placa
        self.marca = marca

    def verificarEstado(self, fabricacion):
        return f'Vehículo {self.color} fabricado en el año {fabricacion}'

    def concatenarCaracteristicas(self):
        return f'Vehículo con placa {self.placa} y de color {self.color} es de marca {self.marca}'

vehiculo = Vehiculo('rojo', 'v22-444', 'Honda')

print(vehiculo.verificarEstado(2023))
print(vehiculo.concatenarCaracteristicas())
