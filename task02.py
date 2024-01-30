import turtle

def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order - 1, size / 3)
            turtle.left(angle)

def draw_koch_snowflake(turtle, order, size):
    for _ in range(3):
        koch_snowflake(turtle, order, size)
        turtle.right(120)

def main():
    # Запитуємо користувача про рівень рекурсії
    level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

    # Вікно для візуалізації сніжинки Коха
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Сніжинка Коха")

    # Створюємо черепашку
    fractal_turtle = turtle.Turtle()
    fractal_turtle.speed(1)

    # Переміщаємо черепашку в початкову позицію
    fractal_turtle.penup()
    fractal_turtle.goto(-150, -90)
    fractal_turtle.pendown()

    # Викликаємо функцію для створення сніжинки Коха
    draw_koch_snowflake(fractal_turtle, level, 300)

    # Завершуємо візуалізацію при кліку на вікно
    screen.exitonclick()

if __name__ == "__main__":
    main()
