import os
import random
import json

def clear_screen():
    os.system('clear')

def show_disclaimer():
    clear_screen()
    print('''
*Disclaimer*
          "Welcome to Rock, Paper, Scissors Game, version 1.5!
           We're excited to launch this new game, and we're committed to continuously improving and expanding its features. Currently, you can enjoy a simple yet engaging game of Rock, Paper, Scissors. However, we have big plans for future updates!
           Stay tuned for new features, game modes, and surprises that will enhance your gaming experience. Our goal is to make this game more enjoyable and challenging with each update.
           
*Some upcoming features to look forward to*
- Multiplayer mode: Compete with friends and other players online
- Tournament mode: Participate in tournaments and win rewards
- Customization options: Personalize your game with different themes, avatars, and more
- Leaderboards: Climb the ranks and become the ultimate Rock, Paper, Scissors champion

We appreciate your feedback and suggestions. Your input will help shape the future of this game.
Thank you for playing, and get ready for an exciting journey with Rock, Paper, Scissors Game!
New updates coming soon!

*Created by: Debajit.KTY*
''')
    input("Press Enter to continue...")
    clear_screen()    

def load_balance():
    """Load the user's balance from a file."""
    try:
        with open('balance.json', 'r') as f:
            data = json.load(f)
            return data.get('balance', 10)  # Default to 10 if no balance is found
    except FileNotFoundError:
        return 10  # Default balance if file does not exist

def save_balance(balance):
    """Save the user's balance to a file."""
    with open('balance.json', 'w') as f:
        json.dump({'balance': balance}, f)

def play_game():
    """Main function to play the Rock, Paper, Scissors game."""
    user_balance = load_balance()  # Load balance from file

    while True:
        clear_screen()
        print(f"Your current balance: ${user_balance}")
        
        if user_balance <= 0:
            print("You do not have enough money to play. Please contact: +91 9999999999 to add funds.")
            break
        
        print(''' 
               [VERSION: 1.5]
        ''')
        print("Type 'disclaimer' to view the game's disclaimer.")
        
        # Ask the user how much they want to wager
        while True:
            try:
                wager = int(input("How much do you want to wager for each match? (1 to your balance): "))
                if 1 <= wager <= user_balance:
                    break
                else:
                    print(f"Please enter a valid amount between 1 and {user_balance}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        choices = ["rock", "paper", "scissors"]
        score = {"User      ": 0, "Computer": 0}
        
        for i in range(5):
            Computer = random.choice(choices)
            User = input(f"Round {i+1}: Do you choose rock, paper or scissors? (or type 'disclaimer'): ").lower()
            
            if User == "disclaimer":
                show_disclaimer()
                continue
            
            while User not in choices:
                User = input("Invalid choice. Please enter rock, paper or scissors: ").lower()
                
            print(f"\nComputer chose: {Computer}")
            
            if User == Computer:
                print("WOW! 😊 Same with me hahhaa~😅")
            elif (User     == "rock" and Computer == "scissors") or (User     == "scissors" and Computer == "paper") or (User     == "paper" and Computer == "rock"):
                print("You win this round!")
                score["User      "] += 1
                user_balance += wager  # Add wager amount for winning
            else:
                print("You lose this round!")
                score["Computer"] += 1
                user_balance -= wager  # Deduct wager amount for losing
                
            print(f"\nScore: User - {score['User      ']}, Computer - {score['Computer']}")
            print(f"Current balance: ${user_balance}\n")
            
        print("Final Score:")
        print(f"User      - {score['User      ']}, Computer - {score['Computer']}")
        
        if score["User      "] > score["Computer"]:
            print("You win the series!")
        elif score["User      "] < score["Computer"]:
            print("You lose the series!")
        else:
            print("Hahaha~😅 Same Score nice!")
        
        print(f"Your balance after this series: ${user_balance}\n")
        
        save_balance(user_balance)  # Save balance to file after each game
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    show_disclaimer()
    play_game()