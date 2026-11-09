import random
import math

def simular_montecarlo():
    print("=== PROGRAMA: INTERSECCIÓN ELIPSE E HIPÉRBOLE (MONTECARLO) ===")
    
    # Pedimos los datos iniciales al usuario
    a = float(input("Ingrese el valor de 'a' (elipse): "))
    b = float(input("Ingrese el valor de 'b' (elipse): "))
    c = float(input("Ingrese el valor de 'c' (hipérbole): "))
    d = float(input("Ingrese el valor de 'd' (hipérbole): "))
    N = int(input("Ingrese la cantidad de puntos aleatorios a generar: "))
    
    puntos_elipse = 0
    puntos_interseccion = 0
    
    # Calculamos el área teórica de la elipse usando la fórmula matemática
    area_elipse_teorica = math.pi * a * b
    
    # Generamos puntos aleatorios dentro de los límites de la caja (-a a a y -b a b)
    for _ in range(N):
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)
        
        # Revisamos si el punto cae dentro de la elipse
        dentro_elipse = (x**2 / a**2) + (y**2 / b**2) <= 1
        
        if dentro_elipse:
            puntos_elipse += 1
            
            # Si ya cayó en la elipse, comprobamos si también está dentro de la hipérbole
            dentro_hiperbole = (x**2 / c**2) - (y**2 / d**2) >= 1
            
            if dentro_hiperbole:
                puntos_interseccion += 1
                
    # Usamos proporciones para aproximar el área de la zona donde se cruzan
    if puntos_elipse > 0:
        area_interseccion = area_elipse_teorica * (puntos_interseccion / puntos_elipse)
    else:
        area_interseccion = 0.0
        
    # Mostramos los resultados finales en pantalla
    print("\n" + "="*40)
    print("RESULTADOS FINALES")
    print("="*40)
    print(f"* Cantidad de puntos aleatorios que cayeron dentro de la elipse: {puntos_elipse}")
    print(f"* Cantidad de puntos aleatorios que cayeron en la intersección: {puntos_interseccion}")
    print(f"* Área teórica de la elipse: {area_elipse_teorica:.4f}")
    print(f"* Área aproximada de la zona de la elipse que se interseca con la hipérbole: {area_interseccion:.4f}")

if __name__ == "__main__":
    simular_montecarlo()
