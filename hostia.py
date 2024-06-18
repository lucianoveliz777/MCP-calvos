import time

def main():
    while True:
        try:
            hours = float(input("¿Cuántas horas deseas jugar? "))
            if hours <= 0:
                print("Por favor, introduce un número positivo.")
                continue
        except ValueError:
            print(" Por favor, introduce un número.")
            continue

        end_time = time.time() + hours * 3600

        while time.time() < end_time:
            print("hello da")
            time.sleep(60)  # Espera 1 minuto (60 segundos)

        while True:
            choice = input("¿Deseas continuar jugando? (s/n): ").strip().lower()
            if choice == 's':
                break
            elif choice == 'n':
                print("Finalizado.")
                return
            else:
                print("Entrada no válida. Por favor, responde 's' para si o 'n' para no.")

if __name__ == "__main__":
    main()