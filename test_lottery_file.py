from global_hw  import count_matching_numbers


list1 = list(map(int, input("Введите первые 10 чисел через пробел: ").split()))
list2 = list(map(int, input("Введите вторые 10 чисел через пробел: ").split()))

result = count_matching_numbers(list1, list2)

print("Количество совпадающих чисел:", result)


""" Этот файл создан для проверки написанного кода в файле <<global_hw.py>>  

    В этой программе сравниваются 2 и только 2 списка !!!  
    В этих списках должно быть только по 10 чисел в каждом
    
    ввод с клавиатуры : через пробел , после завершения нажать Enter 
    
    Good luck """