import numpy as np
number = np.random.randint(1,101)
count = 0

while True:
    predict_number=int(input('Угадай число от 1 до 100: '))
    count+=1
    if predict_number > number:
        print("Число должно быть меньше")
    elif predict_number < number:
        print("Число должно быть больше")
    else:
        print(f'Вы угадали число {predict_number} за {count} попыток')
        break
    