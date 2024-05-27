def filter_short_strings(input_array):
    # Создаем пустой массив для хранения строк длиной <= 3 символа
    result_array = []
    
    # Проходим по всем элементам исходного массива
    for string in input_array:
        # Если длина строки меньше или равна 3, добавляем её в результат
        if len(string) <= 3:
            result_array.append(string)
    
    return result_array

# Примеры использования функции
example1 = ["Hello", "2", "world", ":-)"]
example2 = ["1234", "1567", "-2", "computer science"]
example3 = ["Russia", "Denmark", "Kazan"]

print(filter_short_strings(example1))  # Ожидаемый результат: ["2", ":-)"]
print(filter_short_strings(example2))  # Ожидаемый результат: ["-2"]
print(filter_short_strings(example3))  # Ожидаемый результат: []
