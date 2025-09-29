def get_identificador() -> str:
    return "triángulo"

def get_area(base:int, altura:int) -> float:
    return (base*altura)/2

def get_perimetro(lado_a:int, lado_b:int, lado_c:int) -> float:
    return lado_a + lado_b + lado_c
