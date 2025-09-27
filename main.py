import numpy as np
import matplotlib.pyplot as plt


# --- 1. ФУНКЦИЯ ПРИНАДЛЕЖНОСТИ (ТРЕУГОЛЬНАЯ) ---

def triangular_membership(x, a, m, b):
    """
    Треугольная функция принадлежности (trimf).
    a - нижняя граница, m - пик, b - верхняя граница.
    x - четкий объект (значение BMI).
    """
    if x <= a or x >= b:
        return 0.0
    elif a <= x <= m:
        # Линейный рост от 0 до 1
        return (x - a) / (m - a)
    elif m < x <= b:
        # Линейное падение от 1 до 0
        return (b - x) / (b - m)
    else:
        return 0.0


# --- 2. ОПЕРАЦИЯ ДОПОЛНЕНИЯ ---

def complement_fuzzy_set(membership_value):
    """
    Операция дополнения (NOT).
    μ_A_bar(x) = 1 - μ_A(x)
    """
    # Если входное значение не находится в диапазоне [0, 1],
    # функция просто возвращает 1 - значение, как это принято в нечеткой логике.
    return 1.0 - membership_value


# --- 3. ПРИМЕР: НЕЧЕТКОЕ МНОЖЕСТВО "НОРМАЛЬНЫЙ ВЕС" (BMI) ---

# Параметры для нечеткого множества "Нормальный вес" по BMI:
# (a) - нижняя граница (где принадлежность равна 0)
# (m) - пик (где принадлежность равна 1)
# (b) - верхняя граница (где принадлежность равна 0)
# Согласно ВОЗ, нормальный вес находится в диапазоне BMI 18.5 – 24.9.
# Мы выберем пик в 21.5 для симметрии и более плавные границы.
A = 16.0  # a: Начинается от 0
M = 21.5  # m: Пик принадлежности (идеальный BMI)
B = 27.0  # b: Заканчивается на 0


# --- 4. ОСНОВНОЙ СКРИПТ ---

def run_complement_operation():
    print("--- Операция дополнения нечеткого множества (BMI) ---")
    print(f"Нечеткое множество A: 'Нормальный вес' (Параметры: a={A}, m={M}, b={B})")

    # Ввод четких объектов множества (значений BMI)
    try:
        input_bmis = input("Введите несколько значений BMI (через запятую): ")
        # Преобразование строки в список чисел
        crisp_objects = [float(x.strip()) for x in input_bmis.split(',')]
    except ValueError:
        print("Ошибка ввода. Введите числа через запятую.")
        return

    print("\n| BMI (Четкий объект) | μ_A(x) (Принадлежность) | μ_A_bar(x) (Дополнение) |")
    print("|---------------------|-------------------------|-------------------------|")

    # Таблица результатов
    for bmi in crisp_objects:
        # 1. Вычисляем принадлежность к исходному множеству 'Нормальный вес'
        mu_A = triangular_membership(bmi, A, M, B)

        # 2. Вычисляем принадлежность к дополнению
        mu_A_bar = complement_fuzzy_set(mu_A)

        print(f"| {bmi:19.1f} | {mu_A:23.4f} | {mu_A_bar:23.4f} |")

    # --- ВИЗУАЛИЗАЦИЯ РЕЗУЛЬТАТОВ ---
    x_range = np.linspace(10, 35, 300)

    # 1. Принадлежность к множеству A
    mu_A_values = [triangular_membership(x, A, M, B) for x in x_range]

    # 2. Принадлежность к дополнению A
    mu_A_bar_values = [complement_fuzzy_set(mu_A) for mu_A in mu_A_values]

    plt.figure(figsize=(10, 6))
    plt.plot(x_range, mu_A_values, label='A: Нормальный вес ($\mu_A(x)$)', color='blue')
    plt.plot(x_range, mu_A_bar_values, label='¬A: Дополнение Нормального веса ($\mu_{\overline{A}}(x)$)', color='red',
             linestyle='--')

    # Отмечаем точки, введенные пользователем
    for bmi in crisp_objects:
        mu_A = triangular_membership(bmi, A, M, B)
        mu_A_bar = complement_fuzzy_set(mu_A)
        plt.plot(bmi, mu_A, 'go', markersize=8, label=f'μ_A({bmi:.1f})={mu_A:.2f}' if bmi == crisp_objects[0] else None)
        plt.plot(bmi, mu_A_bar, 'rs', markersize=8,
                 label=f'μ_¬A({bmi:.1f})={mu_A_bar:.2f}' if bmi == crisp_objects[0] else None)

    plt.title('Операция дополнения для нечеткого множества "Нормальный вес" (BMI)')
    plt.xlabel('Индекс массы тела (BMI)')
    plt.ylabel('Степень принадлежности')
    plt.grid(True)
    plt.legend()
    plt.show()


# Запуск основной функции
if __name__ == "__main__":
    run_complement_operation()
