def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def main():
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    print(f"El mínimo común múltiplo de {num1} y {num2} es {lcm(num1, num2)}")

if __name__ == "__main__":
    main()