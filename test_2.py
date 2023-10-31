import random

def roll_dice(num_dice):
    """Бросает указанное количество костей и возвращает результат"""
    dice = []
    for _ in range(num_dice):
        dice.append(random.randint(1, 6))
    return dice

def make_bet(previous_bet):
    """Получает ставку предыдущего игрока и возвращает новую ставку"""
    new_bet = input("Сделайте свою ставку (значение (от 1го до 6) и количество кубиков): ")

    # Проверить корректность ввода и вернуть новую ставку
    while True:
        try:
            count, value = new_bet.split()
            count = int(count)
            value = int(value)
            if count > num_dice_1 and count > num_dice_2:  # Проверяем обе руки
                raise ValueError
            if previous_bet is not None:
                prev_count, prev_value = previous_bet.split()
                prev_count = int(prev_count)
                prev_value = int(prev_value)
                if count <= prev_count and value <= prev_value:
                    raise ValueError
            break
        except ValueError:
            print("Некорректный ввод! Попробуйте еще раз.")
            new_bet = input("Сделайте свою ставку (число и номинал): ")

    return new_bet

def count_dice(dice, value):
    """Подсчитывает количество костей с указанным значением"""
    count = 0
    for die in dice:
        if die == value:
            count += 1
    return count

def play_round(num_dice_1, num_dice_2):
    """Играет один раунд игры"""
    # Бросаем кости
    global new_bet
    dice_1 = roll_dice(num_dice_1)
    dice_2 = roll_dice(num_dice_2)
    print("Выпавшие значения костей первого игрока:", dice_1)
    print("Выпавшие значения костей второго игрока:", dice_2)

    # Первый игрок делает ставку
    bet = make_bet(None)

    # Второй игрок выбирает действие
    action = input("Выберите действие (1 - 'не верю', 2 - сделать ставку): ")

    # Проверяем выбор второго игрока
    if action == '1':
        # Игрок не верит предыдущей ставке
        previous_value = int(bet.split()[1])
        count_1 = count_dice(dice_1, previous_value)
        count_2 = count_dice(dice_2, previous_value)
        if count_1 + count_2 < int(bet.split()[0]):
            # Первый игрок проиграл
            print("Первый игрок проиграл!")
            # Обновить количество кубиков у первого игрока
            num_dice_1 -= 1
        else:
            # Второй игрок проиграл
            print("Второй игрок проиграл!")
            # Обновить количество кубиков у второго игрока
            num_dice_2 -= 1
    elif action == '2':
        # Игрок делает свою ставку
        new_bet = make_bet(bet)
        previous_value = int(bet.split()[1])
        previous_count = int(bet.split()[0])
        new_value = int(new_bet.split()[1])
        new_count = int(new_bet.split()[0])
        if new_count <= previous_count and new_value <= previous_value:
            print("Ставка должна быть выше предыдущей!")
            return
        if new_count > num_dice_1 or new_count > num_dice_2:
            print("Ставка превышает количество кубиков!")
            return
        # Сравнить новую ставку с предыдущей и определить победителя и проигравшего
        if new_count >= previous_count and new_value >= previous_value:
            print("Первый игрок проиграл!")
            num_dice_1 -= 1
        else:
            print("Второй игрок проиграл!")
            num_dice_2 -= 1

    # Повысить ставку или завершить игру, если достигнут предел
    if num_dice_1 > 0 and num_dice_2 > 0:
        if action == '2':
            action = input("Выберите действие (1 - 'не верю', 2 - сделать ставку): ")
            if action == '1':
                # Игрок не верит ставке после повышения
                previous_value = int(new_bet.split()[1])
                count_1 = count_dice(dice_1, previous_value)
                count_2 = count_dice(dice_2, previous_value)
                if count_1 + count_2 < int(new_bet.split()[0]):
                    # Первый игрок проиграл
                    print("Первый игрок проиграл!")
                    # Обновить количество кубиков у первого игрока
                    num_dice_1 -= 1
                else:
                    # Второй игрок проиграл
                    print("Второй игрок проиграл!")
                    # Обновить количество кубиков у второго игрока
                    num_dice_2 -= 1
            elif action == '2':
                # Игрок повышает ставку
                new_bet = make_bet(new_bet)

        if num_dice_1 > 0 and num_dice_2 > 0:
            play_round(num_dice_1, num_dice_2)

    # Объявить победителя игры
    if num_dice_1 == 0 and num_dice_2 == 0:
        print("Игра окончена. Ничья!")
    elif num_dice_1 == 0:
        print("Игра окончена. Победил первый игрок!")
    else:
        print("Игра окончена. Победил второй игрок!")

num_dice_1 = 5
num_dice_2 = 5
play_round(num_dice_1, num_dice_2)