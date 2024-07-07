import random


def get_secret_word():
    word_list_file_path = '/Users/umamahc/capstone_project/real_wordles_2315.txt'
    with open(word_list_file_path, 'r') as f:
        words = f.read().splitlines()
    secret_word = random.choice(words).upper()
    return secret_word


def get_clues(guess, word):
    green = '\U0001F7E9'
    yellow = '\U0001F7E8'
    red = '\U0001F7E5'
    clues = []
    non_grn_lett_guess = []
    non_grn_lett_word = []
    zipped = zip(guess, word)
    for words in zipped:
        if words[0] == words[1]:
            clues.append(green)
            non_grn_lett_guess.append(' ')
            non_grn_lett_word.append(' ')
        else:
            clues.append(' ')
            non_grn_lett_guess.append(words[0])
            non_grn_lett_word.append(words[1])
    count_dict = {}
    for i in range(len(guess)):
        if not non_grn_lett_guess[i].isalpha():
            continue
        elif non_grn_lett_guess[i] in non_grn_lett_word:
            if non_grn_lett_guess[i] not in count_dict:
                count_dict[non_grn_lett_guess[i]] = 1
            else:
                count_dict[non_grn_lett_guess[i]] += 1
            dict_occurrence = count_dict[non_grn_lett_guess[i]]
            if dict_occurrence <= non_grn_lett_word.count(non_grn_lett_guess[i]):
                clues[i] = yellow
            else:
                clues[i] = red
        else:
            clues[i] = red
    clue_string = ' '.join(clues)
    guess_string = ''
    for lett in guess:
        guess_string += lett
        guess_string += '  '
    return f'{guess_string}\n{clue_string}'


num_lett = 5
max_guess = 6


def main():
    print(f'''I am thinking of a {num_lett} letter word. You have {max_guess} guesses to figure out the secret word. 
I will give you some clues after each guess.
If a letter returns \U0001F7E5 it is not in the secret word.
If a letter returns \U0001F7E8 it is in the secret word but not in the correct position.
If a letter returns \U0001F7E9 it is in the secret word and in the right position. Good luck!''')

    while True:
        word = get_secret_word()
        guesses_so_far = 1
        while max_guess >= guesses_so_far:
            guess = ''
            while len(guess) != num_lett or ' ' in guess:
                guess = input(f'Guess #{guesses_so_far}: ').upper()
            clues = get_clues(guess, word)
            print(clues)
            guesses_so_far += 1
            if guess == word:
                print('You got it!')
                break
            if guesses_so_far > max_guess:
                print(
                    f'You have run out of guesses. The secret word was {word}')
                break
        continue_playing = input(
            'Do you want to play again? (Yes/No): ').upper()
        if not continue_playing.startswith('Y'):
            break
    print('Thank you for playing!')


if __name__ == '__main__':
    main()
