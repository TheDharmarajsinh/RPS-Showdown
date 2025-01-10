import random

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "Rock" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissor" and computer_choice == "Paper"):
        return "user"
    else:
        return "computer"

def display_scores(player_name, user_score, computer_score):
    print("\n" + "-" * 30)
    print(f"Scoreboard:")
    print(f"{player_name}: {user_score}")
    print(f"Computer: {computer_score}")
    print("-" * 30 + "\n")

def play_game():
    print("\nWelcome to Rock, Paper, Scissors!")
    print("-" * 30)
    
    player_name = input("Enter your name: ").strip().capitalize()
    if not player_name:
        player_name = "Player"
    print(f"Hello, {player_name}! Let's play!\n")
    
    rounds = int(input("How many rounds would you like to play? (e.g., 3): "))
    user_score = 0
    computer_score = 0
    available_choices = ["Rock", "Paper", "Scissor"]
    
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num} of {rounds}")
        print("-" * 30)
        
        user_choice = input("Enter your choice (Rock, Paper, Scissor): ").capitalize()
        if user_choice not in available_choices:
            print("Invalid choice. Please try again!")
            continue
        
        computer_choice = random.choice(available_choices)
        print(f"\n{player_name} chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = get_winner(user_choice, computer_choice)
        if result == "draw":
            print("It's a Draw!")
        elif result == "user":
            print(f"Great job, {player_name}! You Win this round!")
            user_score += 1
        else:
            print("Computer Wins this round!")
            computer_score += 1
        
        display_scores(player_name, user_score, computer_score)
    
    print("\n" + "=" * 30)
    print("Game Over!")
    if user_score > computer_score:
        print(f"Congratulations, {player_name}! You are the overall winner!")
    elif user_score < computer_score:
        print("Better luck next time! The computer wins!")
    else:
        print("It's a tie overall!")
    print("=" * 30)

def main():
    while True:
        play_game()
        replay = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
