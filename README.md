Python Practice Projects
------------------
Quiz Game
--------------
Key Points:

- The program greets the user with "Welcome to my computer quiz!" and asks if they want to play the quiz using input().
- The user's response is checked; if they don't respond with "yes" (case-insensitive), the program terminates using quit().
- If the user chooses to play, the game begins with a message, and the score variable is initialized to 0.
- The program asks six questions about computer-related acronyms (CPU, GPU, RAM, PSU, LAN, WAN).
- For each question, the user's answer is collected via input().
- Each answer is compared to the correct response (case-insensitive). If correct, "Correct!" is printed, and the score is incremented by 1; otherwise, "Incorrect!" is displayed.
- After all questions are answered, the program prints the total number of correct answers using print("You got " + str(score) + " questions correct!")
- The program calculates and prints the user's score as a percentage of total questions using print("You got " + str(score/6*100) + "%.").

OUTPUT:


![Screenshot 2024-08-11 143452](https://github.com/user-attachments/assets/2157db16-53ab-4f4e-945d-cb220615c1e6)

------------------------
Guessing Game
-----------------------
Key Points:

- The program prompts the user to enter a number (top_of_range). It checks if the input is a valid positive integer. If not, the program asks the user to input a valid number and exits.
- Once validated, the input is converted to an integer and stored as top_of_range. This number defines the upper limit of the range for the random number that will be generated.
- The program generates a random number between 0 and the top_of_range using random.randint(0, top_of_range) and stores it in random_number.
- The program enters an infinite loop where it prompts the user to guess the randomly generated number. It tracks the number of guesses with the guesses variable, which increments with each guess.
- For each guess, the program checks if the input is a number. If it is not, the user is asked to enter a valid number again. If the guess is correct, the program congratulates the user and breaks the loop. If 
  incorrect, it gives feedback on whether the guess was too high or too low.
- Once the user guesses the correct number, the program exits the loop and displays the total number of guesses it took for the user to find the correct number. 

OUTPUT:


![Screenshot 2024-08-12 225639](https://github.com/user-attachments/assets/b26ce502-a98a-4538-b81e-1144ffb33e73)
------------------------------------------------------------------
Rock, Paper and Scissor Game!
--------------------------------------------------------------
Key Points:

- The code continuously prompts the user to enter either "Rock," "Paper," "Scissors," or "Q" to quit. It uses a while True loop to keep the game running until the user decides to quit by typing "Q".
- The computer randomly picks an option ("rock," "paper," or "scissors") by generating a random number (0, 1, or 2) and selecting the corresponding element from the options list.
- The code compares the user's choice with the computer's choice. If the user's choice beats the computer's (according to the game rules), the user wins, and their win count (user_wins) is incremented. Otherwise, the computer wins, and the computer's win count (computer_wins) is incremented.
- When the user decides to quit (by typing "Q"), the game ends, and the code prints out the total number of wins for both the user and the computer before displaying a "Goodbye!" message.

OUTPUT:


![Screenshot 2024-08-13 222109](https://github.com/user-attachments/assets/8ca50c19-5f01-4f80-942b-e602452c8d98)
------------------------------------------------------------------------------------------------------------------
Adventure Game!
--------------------
Key Points:

- The code begins by asking the user for their name and then greets them by including their name in a welcome message.
- The user is presented with a choice to go left or right on a dirt road. Based on their choice, the adventure continues with different scenarios.
-  The code uses conditional statements (if, elif, else) to handle the user's decisions, leading to various outcomes (winning, losing, or invalid choices).
-  After the adventure concludes, the code thanks the user for participating by repeating their name.

  OUTPUT:


![Screenshot 2024-08-14 215608](https://github.com/user-attachments/assets/5a3f59e6-d78a-4d3f-91aa-6f9f866e3a27)
---------------------------------------------------------------------------------------------------------------
PIG !
----------------
Key Points:

- The `roll()` function generates a random number between 1 and 6, simulating a dice roll.
- The program prompts the user to input the number of players (between 2 and 4) and validates the input to ensure it's within the allowed range.
- The program creates a list `player_scores` to track each player's score, initialized to 0 for all players.
- The main game loop continues until one player's score reaches or exceeds the target score of 50 points.
- During each player's turn, they decide whether to roll the dice or end their turn. If they roll a 1, their turn ends and they score 0 for that round. Otherwise, their roll value is added to their current score.
- After each player's turn, their accumulated score for that round is added to their total score.
- Once a player's score reaches 50 or more, the game ends, and the player with the highest score is declared the winner.

  OUTPUT:


  ![Screenshot 2024-08-15 231443](https://github.com/user-attachments/assets/2d17c5ee-68f0-4608-abca-bc12544dc187)
  -----------------------------------------
Password Manager!
----------------------------------------------
Key Points:

- The code imports Fernet from the cryptography.fernet module to handle encryption and decryption.
- The load_key() function reads the encryption key from a file called key.key and returns it.
- The key is loaded using load_key(), and a Fernet object (fer) is created to handle cryptographic operations.
- The view() function reads the passwords.txt file, decrypts the stored passwords using fer, and prints out the usernames and passwords.
- The add() function takes an account name and password from the user, encrypts the password using fer, and writes the encrypted password to the passwords.txt file.
- The program runs in an infinite loop, prompting the user to either view existing passwords, add new passwords, or quit the program.
-  The loop breaks when the user inputs 'q', ending the program.
-  If the user inputs anything other than 'view', 'add', or 'q', the program prints "Invalid mode" and prompts again.
-   Passwords are stored in the file passwords.txt in an encrypted format to ensure security.
-   The program uses file operations to store and retrieve passwords, making the data persistent across different runs of the program.
-   -   This code provides basic functionality for a password manager, ensuring that sensitive information is securely encrypted and decrypted when needed​(Password Manager).



