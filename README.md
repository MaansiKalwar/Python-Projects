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
