class Vehiculo:
    identificador = 0
    def __init__(self, rendimiento, marca, energia=111.5, *args, **kwargs) -> None:
        self.rendimiento = rendimiento
        self.marca = marca
        if energia < 0:
            self._energia = float(0)
        else:
            self._energia = round(float(energia), 1)
        self.identificador = Vehiculo.identificador
        Vehiculo.identificador += 1
    
    @property    
    def autonomia(self) -> float:
        energia = self._energia
        autonomia = energia * self.rendimiento
        return autonomia
    @property
    def energia(self) -> float:
        energia = self._energia
        return energia

    @energia.setter
    def energia(self, energia) -> None:
        if energia < 0:
            self._energia = float(0)
        else:
            self._energia = round(float(energia), 1)


class AutoBencina(Vehiculo):

    def __init__(self, bencina_favorita, *args, **kwargs) -> None:
        self.bencina_favorita = bencina_favorita
        super().__init__(*args, **kwargs)
    
    def recorrer(self, kilometros) -> str:
        autonomia = self.autonomia
        if kilometros > autonomia:
            recorrido = autonomia
            gasto = round(float(recorrido / self.rendimiento), 1)
            energia_inicial = self.energia
            nueva_energia = energia_inicial - gasto
            self.energia = nueva_energia

        else:
            recorrido = kilometros
            gasto = round(float(recorrido / self.rendimiento), 1)
            energia_inicial = self.energia
            nueva_energia = energia_inicial - gasto
            self.energia = nueva_energia
        a_retornar = f"Anduve {recorrido}Km y eso consume {gasto}L de bencina"
        return a_retornar
            
class AutoElectrico(Vehiculo):
    def __init__(self, vida_util_bateria, *args, **kwargs) -> None:
        self.vida_util_bateria = vida_util_bateria
        super().__init__(*args, **kwargs)

    def recorrer(self, kilometros) -> str:
        autonomia = self.autonomia
        if kilometros > autonomia:
            recorrido = autonomia
            gasto = round(float(recorrido / self.rendimiento), 1)
            energia_inicial = self.energia
            nueva_energia = energia_inicial - gasto
            self.energia = nueva_energia
            
        else:
            recorrido = kilometros
            gasto = round(float(recorrido / self.rendimiento), 1)
            energia_inicial = self.energia
            nueva_energia = energia_inicial - gasto
            self.energia = nueva_energia
            
        a_retornar = f"Anduve {recorrido}Km y eso consume {gasto}W de energia electrica"
        return a_retornar

    
class Camioneta(Vehiculo):
    def __init__(self, capacidad_maleta, *args, **kwargs) -> None:
        self.capacidad_maleta = capacidad_maleta
        super().__init__(*args, **kwargs)
    

class Telsa(AutoElectrico):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def recorrer(self, kilometros) -> str:
        retornado = super().recorrer(kilometros)
        a_retornar = retornado + " de forma muy inteligente"
        return a_retornar

class FaitHibrido(AutoBencina, AutoElectrico):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(vida_util_bateria=5, *args, **kwargs)
    def recorrer(self, kilometros):
        if kilometros > 10.0:
            kilometros_restantes = kilometros - 10.0
            retorno_bencina = AutoBencina.recorrer(self, 10.0)
            retorno_electrico = AutoElectrico.recorrer(self, kilometros_restantes)
            a_retornar = retorno_bencina + " " + retorno_electrico 
            return a_retornar 
        elif kilometros <= 10.0:
            retorno_electrico = AutoElectrico.recorrer(self, kilometros)
            return retorno_electrico





