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
