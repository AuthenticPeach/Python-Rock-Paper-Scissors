import random

def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Let's play Rock-paper-Scissors!")
    user_score = 0
    computer_score = 0
    while user_score < 2 and computer_score < 2:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

    if user_score > computer_score:
        print("Congratulations! You won the game!")
    else:
        print("The computer won the game.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    while play_again not in ['yes', 'no']:
        print("Invalid choice. Please try again.")
        play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again == 'yes':
        play_game()
    else:
        print("Thank you for playing!")

play_game()
