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
Rock, Ppaer and Scissor Game!
--------------------------------------------------------------
Key Points:

- The code continuously prompts the user to enter either "Rock," "Paper," "Scissors," or "Q" to quit. It uses a while True loop to keep the game running until the user decides to quit by typing "Q".
- The computer randomly picks an option ("rock," "paper," or "scissors") by generating a random number (0, 1, or 2) and selecting the corresponding element from the options list.
- The code compares the user's choice with the computer's choice. If the user's choice beats the computer's (according to the game rules), the user wins, and their win count (user_wins) is incremented. Otherwise, the computer wins, and the computer's win count (computer_wins) is incremented.
- When the user decides to quit (by typing "Q"), the game ends, and the code prints out the total number of wins for both the user and the computer before displaying a "Goodbye!" message.

OUTPUT:


![Screenshot 2024-08-13 222109](https://github.com/user-attachments/assets/8ca50c19-5f01-4f80-942b-e602452c8d98)

