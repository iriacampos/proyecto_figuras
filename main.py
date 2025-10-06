from lib import cuadrado, rectangulo, triangulo, circunferencia
print("Proyecto figuras")
print(cuadrado.get_identificador())
lado = 4
print(f"El area de un {cuadrado.get_identificador()} de lado {lado} es: {cuadrado.get_area(lado)} y el perímetro es {cuadrado.get_perimetro(lado)}")

base=4
altura=2
print(rectangulo.get_identificador())
print(f"El area de un {rectangulo.get_identificador()} de base {base} y altura {altura} es: {rectangulo.get_area(base, altura)} y el perímetro es {rectangulo.get_perimetro(base, altura)}")
print(triangulo.get_identificador())
print(f"El area de un {triangulo.get_identificador()} de base {base} y altura {altura} es: {triangulo.get_area(base, altura)} y el perímetro es {triangulo.get_perimetro(base, base, base)}")

radio=2
print("circunferencia")
print(f"El area de una circunferencia de radio {radio} es: {circunferencia.get_area(radio)}")