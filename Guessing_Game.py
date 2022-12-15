# Show the game levels
def show_levels():
    print(''' Game Levels: 
      (1) Easy: 
          * Limits: [1 - 10]  
          * Number of trials: 3
      
      (2) Intermediate: 
          * Limits: [1 - 100] 
          * Number of trials: 7
      
      (3) Hard:  
          * Limits: [1 - 1000] 
          * Number of trials: 15 ''')

# Ask the user for the game level
def game_level_choice():
    while True:
        game_level = input('Enter the game level: (1) Easy \t (2) Intermediate \t (3) Hard  ===>  ')
        if game_level in ['1', '2', '3']:
            game_level = int(game_level)
            break
        else:
            print('Invalid Choice! Please choose 1, 2, or 3')
            continue
    return game_level

# Set the game settings according to the game level
def set_game_setting(game_level):
    if game_level == 1:
        limits = range(1, 11)
        num_trials = 3
    elif game_level == 2:
        limits = range(1, 101)
        num_trials = 7
    else:
        limits = range(1, 1001)
        num_trials = 15
    return limits, num_trials

# Start Playing
def start_playing(limits, num_trials):
    import random
    hidden_num = random.choice(limits)
    user_trials = 0
    while user_trials < num_trials:
        guess = int(input("Enter the guess number  ===>  "))
        user_trials += 1
        if guess == hidden_num:
            print(f'You succeeded in {user_trials} trials')
            break
        else:
            if user_trials == num_trials:
                print(f"Unfortunately you lost, You tried {user_trials} trials. No more Trials!")
                print(f'The hidden number is  {hidden_num}')
            elif guess < hidden_num:
                print('No, Increase!')
            else:
                print('No, Decrease!')
            continue

# Play Again
def play_again():
    while True:
        play_again = input("To play again enter [1] and to not play again enter [0]  ===>  ")
        if play_again in ['0', '1']:
            play_again = int(play_again)
            break
        else:
            print('Invalid Choice! Please choose 0 or 1')
            continue
    return play_again

# Let's Play
def play():
    show_levels()
    while True:
        game_level = game_level_choice()
        limits, num_trials = set_game_setting(game_level)
        start_playing(limits, num_trials)
        if play_again() == 1:
            continue
        else:
            print('END')
            break

if __name__ == '__main__':
    play()







