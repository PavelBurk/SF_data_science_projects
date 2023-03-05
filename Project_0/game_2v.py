""" Компьютер сам загадывает и угадывает число"""
import numpy as np
def random_predict(number:int=1) ->int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    count = 0
    while True:
        count+=1
        predict_number = np.random.randint(1,101) #число от 1 до 100
        if predict_number == number:
            break
    return count

def score_game(random_predict) ->int:
    """За какое количество попыток в серднем угадывает число

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: количество попыток
    """
    count_ls = []
    np.random.seed(1) #фиксация сида для воспроизводимости
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    
    print(f'Ваш алогоритм угадывает число в среднем за {score} попыток')
    return score

#RUN
if __name__ == '__main__':
    score_game(random_predict)
    