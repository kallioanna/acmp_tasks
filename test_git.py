#
def max_ethanol_molecules(carbon_atoms, hydrogen_atoms, oxygen_atoms):
    # Определяем количество молекул спирта из каждого элемента
    max_from_carbon = carbon_atoms // 2  # 2 атома углерода на молекулу
    max_from_hydrogen = hydrogen_atoms // 6  # 6 атомов водорода на молекулу
    max_from_oxygen = oxygen_atoms // 1  # 1 атом кислорода на молекулу

    # Находим минимальное значение из трех расчетов
    return min(max_from_carbon, max_from_hydrogen, max_from_oxygen)

# Ввод данных от пользователя
carbon = int(input("Введите количество атомов углерода (C): "))
hydrogen = int(input("Введите количество атомов водорода (H): "))
oxygen = int(input("Введите количество атомов кислорода (O): "))

# Вычисляем максимальное количество молекул этилового спирта
result = max_ethanol_molecules(carbon, hydrogen, oxygen)

# Вывод результата
print(f"Максимально возможное количество молекул этилового спирта: {result}")