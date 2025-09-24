from parametros import (SOLES_INICIO, TEMP_INICIAL, RIEGO_1, RIEGO_2, POTENCIAL_SOLARETILLO_MIN,
POTENCIAL_SOLARETILLO_MAX, CONSTANTE_SOLES, AUMENTO_NUTRIENTE, ANTI_ROBO, AUM_POT_CIL,
AUM_AUM_CIL)
from random import randint
from abc import ABC, abstractmethod
class Jardin:
    def __init__(self, tablero: list):
        self.tablero = tablero
        self.inv_plantas = []
        self.soles = SOLES_INICIO
        self.temperatura = TEMP_INICIAL

    def cultivar_planta(self, planta: str, coords: str):
        coords = coords.split(",") #el formato de coords es x,y
        self.tablero[coords[0]][coords[1]] = planta

    def regar_plantas() -> None:
        numero_random = randint(0,1)
        if numero_random == 0:
            riego = RIEGO_1
        elif numero_random == 1:
            riego = RIEGO_2
        for planta in self.inv_plantas:
            planta.regarse(riego)
    def mutar(self, planta_1, planta_2):

        pass
    def presentarse(self):
        pass

class Plantas(ABC):
    def __init__(self, tipo: str, vida_maxima: int, vida: int,
                 resistencia: int, resistencia_term: int, altura: int) -> None:
        self.tipo = tipo
        self.vida_max = vida_maxima
        self._vida = vida
        self.res = resistencia
        self.res_term = resistencia_term
        self.congelacion = False
        self.altura = altura

    def __str__(self):
        
        return self.tipo

    def regarse(riego) -> None:
        if (self.vida + riego) > self.vida_max:
            self.vida = self.vida_max
        elif self.vida + riego <= self.vida_max:
            self.vida += riego
    @property
    def vida(self) -> int:
        vida = self._vida
        return vida
    @vida.setter
    @abstractmethod
    def vida(self, vida_restar) -> None:
        if vida_restar > self.vida:
            self.vida = 0
        else:
            self.vida -= vida_restar

class Solaretillo(Plantas):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.potencial = randint(POTENCIAL_SOLARETILLO_MIN, POTENCIAL_SOLARETILLO_MAX)
    
    def vida(self, vida_restar) -> None:
        if vida_restar > self.vida:
            self.vida = 0
        else:
            self.vida -= vida_restar

    def produccion_soles(temperatura, altura) -> float:
        prod = round(CONSTANTE_SOLES * self.potencial * (temperatura / 25) * (altura / 30))
        if prod < 0:
            return float(0)
        else:
            return prod

class Defensauce(Plantas):
    def __init__(self, armadura: int, *args, **kwargs) -> None:
        self.armadura = armadura
        super().__init__(*args, **kwargs)

    @property
    def vida(self) -> int:
        vida = self._vida
        return vida
    @vida.setter
    def vida(self, vida_restar) -> None:
        if vida_restar >= self.armadura:
            self.armadura = 0
            a_restar = abs(self.armadura - vida_restar)
            self.vida -= a_restar
        else: 
            self.armadura -= vida_restar

class Potencilantro(Plantas):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    def produccion_soles_pot(temperatura: int, altura: int) -> float:
        prod = round(CONSTANTE_SOLES * self.potencial * (temperatura / 25) * (altura / 30)
                     * (1 + AUMENTO_NUTRIENTE / 100))
        if prod < 0:
            return float(0)
        else:
            return prod

    
class Aresauce(Solaretillo, Defensauce):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    def anti_robo(self) -> float:
        anti_robo = ANTI_ROBO
        return ANTI_ROBO

class Cilantrillo(Solaretillo, Potencilantro):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    def produccion_soles_pot(temperatura: int, altura: int) -> float:
        prod = round(CONSTANTE_SOLES * (self.potencial + AUM_POT_CIL) * (temperatura / 25) 
                     * (altura / 30) * (1 + (AUMENTO_NUTRIENTE + AUM_AUM_CIL)/ 100))
        if prod < 0:
            return float(0)
        else:
            return prod

class Fensaulantro(Defensauce, Potencilantro):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def redux_ataque(self, nivel_zombie: int) -> float:
        nivel_final = nivel_zombie * (1 - RED_ATQ)
        return nivel_final
testeo_sol = Solaretillo("D", 20, 20, 20, 20, 20)

print(testeo_sol)
