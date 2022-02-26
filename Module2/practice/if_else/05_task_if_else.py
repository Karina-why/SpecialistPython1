# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# TODO: your code here
month = int(input("month:"))  
if month==12 or month==1 or month==2:
    print("Зима")
elif month==3 or month==4 or month==5:
    print("Весна")
elif month==6 or month==7 or month==8:
    print("Лето")
else:
    print ("Осень")
