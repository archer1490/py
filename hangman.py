pictures = [
    '',
    '-------',
    '''
    |   
    |   
    |   
    |   
    |
    -------
    ''',
    '''
    +---+
    |   
    |   
    |   
    |   
    |
    -------
    ''',
    '''
    +---+
    |   |
    |   
    |   
    |   
    |
    -------
    ''',
    '''
    +---+
    |   |
    |   O
    |   
    |   
    |
    -------
    ''',
    '''
    +---+
    |   |
    |   O
    |   |
    |   
    |
    -------
    ''',
    '''
    +---+
    |   |
    |   O
    |  /|
    |   
    |
    -------
    ''',
    '''
    +---+
    |   |
    |   O
    |  /|\\
    |   
    |
    -------
    ''',
    '''
    +---+
    |   |
    |   O
    |  /|\\
    |  / 
    |
    -------
    ''',
    '''
    +---+
    |   |
    |   O
    |  /|\\
    |  / \\
    |
    -------
    ''',
]


def getGuess(alreadyGuessed):
    while True:
        guess = input('Введите букву: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Введите пожалуйста ОДНУ букву')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, назовите БУКВУ')
        else:
            return guess

word = input('Введите слово: ')
correct_letters = set(word)
guessed_letters = []
missed_letters = []
gameOver = False
win = False

while not gameOver:
    letter = getGuess(guessed_letters + missed_letters)
    if letter in correct_letters:
        guessed_letters.append(letter)
    else:
        missed_letters.append(letter)

    if len(guessed_letters) == len(correct_letters):
        gameOver = True
        win = True
    elif len(missed_letters) == len(pictures) - 1:
        gameOver = True

    print('СЛОВО:')
    for letter in word:
        if(letter in guessed_letters):
            print(f'{letter} ', end = '')
        else:
            print('_ ', end = '')
    print('\n')
    print('Неверные буквы:')
    print(','.join(missed_letters))
    print('ВИСЕЛИЦА:')
    print(pictures[len(missed_letters)])

if win == True:
    print('ПОБЕДА')
else:
    print('ПРОИГРЫШ')