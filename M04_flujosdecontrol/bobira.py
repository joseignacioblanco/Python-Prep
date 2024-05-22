import turtle
import random

# Define la clase Serpiente
class Serpiente(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed(0)
        self.segments = []

    def mover(self, direccion):
        self.setheading(direccion)
        self.forward(10)

    def agregar_segmento(self):
        self.segments.append(self.clone())

    def detectar_colision(self):
        # Comprueba si la serpiente choca con los bordes de la ventana
        if self.xcor() > ancho or self.xcor() < -ancho:
            return True
        elif self.ycor() > alto or self.ycor() < -alto:
            return True

        # Comprueba si la serpiente choca consigo misma
        for segmento in self.segments[:-1]:
            if segmento.distance(self) < 20:
                return True
        return False

# Define las variables globales
ancho = 600
alto = 400

serpiente = Serpiente()
comida = turtle.Turtle()
comida.shape("circle")
comida.penup()

# Define la función para generar nueva comida
def generar_comida():
    # Comprueba si la comida está demasiado cerca de la serpiente
    for segmento in serpiente.segments:
        if segmento.distance(comida) < 20:
            return

    # Genera una nueva posición para la comida
    comida.setposition(random.randint(-ancho // 2, ancho // 2), random.randint(-alto // 2, alto // 2))

# Define la función principal
def main():
    # Inicializa la ventana
    ventana = turtle.Screen()
    ventana.setup(ancho, alto)
    ventana.title("Juego de la serpiente")

    # Bucle principal del juego
    while True:
        # Obtiene la entrada del usuario
        tecla = ventana.window.getkey()

        # Mueve la serpiente
        serpiente.mover(tecla)

        # Detecta colisiones
        if serpiente.detectar_colision():
            print("Perdiste!")
            break

        # Genera nueva comida si la serpiente se come la comida actual
        if serpiente.segments[0].distance(comida) < 20:
            generar_comida()
            serpiente.agregar_segmento()

    # Cierra la ventana
    ventana.bye()

# Llama a la función principal
if __name__ == "__main__":
    main()
