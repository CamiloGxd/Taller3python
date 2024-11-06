masa = {
    "tonelada": 1000,         
    "kilogramo": 1,           
    "gramo": 0.001,           
    "miligramo": 1e-6         
}
longitud = {
    "pulgada": 0.0254,        
    "pie": 0.3048,            
    "yarda": 0.9144,          
    "metro": 1               
}
print("\033[1m" "antes de proceder con la conversion debe asegurarse de que las unidades de conversion que se ingresen deben ser del mismo tipo" "\033[0m")
inicio = input("\033[1m" "Ingresar la unidad a converir \033[0m (tonelada, kilogramo, gramo, miligramo, pulgada, pie, yarda, metro): ")
fin = input("\033[1m" "Ingresar el tipo de unidad en la que se imprima la conversion \033[0m (tonelada, kilogramo, gramo, miligramo, pulgada, pie, yarda, metro): ")
dato = float(input("Ingrese el dato a convertir: "))

if inicio in masa and fin in masa:
    kg = dato * masa[inicio]       
    conversion = kg / masa[fin] 
    print(f"conversion: {dato} {inicio} es igual a {conversion} {fin}")

elif inicio in longitud and fin in longitud:
    metros = dato * longitud[inicio]      
    conversion = metros / longitud[fin] 
    print(f"conversion: {dato} {inicio} es igual a {conversion} {fin}")
else:
    print("\033[1m" "Esa conversion no esta asignada" "\033[0m")
