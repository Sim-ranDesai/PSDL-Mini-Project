



'''
            Programming Skills Development Laboratory Mini Project : Dice Rolling And Stone Paper Scissor Game
'''


'''
                Contributers :
                 --> Simran Desai
                 --> Sanika Deshpande
                 --> Gargee Dorle
                 --> Mayuri Gadhave
'''



print("*******************")
print("WELCOME TO THE GAMES : ")
print("*******************")


print("There are two games avaliable for you : ")
print("0. EXIT")
print("1. Random Dice Rolling Generator")
print("2. Tile Matching or Memory Game")

choice = int(input("Enter the choice : "))



# to exit the games alltogether
if choice == 0:
    exit()

# dice rolling game with two variations
if choice == 1:



    print("**********MENU**********")
    print("Welcome to Dice Rolling Random Number Generator")
    print("1. Tkinter GUI based")
    print("2. Console based")
    print("Enter your choice : ")
    ch = int(input())


    # for the GUI based
    if ch == 1:
                                                    ## RANDOM 2 DICE ROLLING GAME ##
        print("You are now playing rolling dice!!")
        from tkinter import *
        import random

        root = Tk()
        root.geometry("700x450")
        root.title("Roll Dice")
        root.config(background="#A569BD")

        label=Label(root,text="",font=("times",260))

        def roll():
            dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
            label.configure(text=f'{random.choice(dice)}{(random.choice(dice))}')
            label.pack()



        button=Button(root,text="Let the dice roll!",width=40,height=5,font=10,fg="#F5B041", bg="#58D68D",bd="2",command=roll)
        button.pack(padx=10,pady=10)
        root.mainloop()



                                                ## RANDOM MULTIPLE DICE ROLLING GAME ON CONSOLE##
    # Console based multiple 
    if ch == 2:
        
       
        import random
        # dice.py
        def generate_dice_faces_diagram(dice_values):
            
            """Return an ASCII diagram of dice faces from `dice_values`.

            The string returned contains an ASCII representation of each die.
            For example, if `dice_values = [4, 1, 3, 2]` then the string
            returned looks like this:

            ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
            ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
            │  *   *  │ │         │ │  *      │ │  *      │
            │         │ │    *    │ │    *    │ │         │
            │  *   *  │ │         │ │      *  │ │      *  │
            └─────────┘ └─────────┘ └─────────┘ └─────────┘
            """
            
            # Generate a list of dice faces from DICE_ART
            dice_faces = []
            for value in dice_values:
                dice_faces.append(DICE_ART[value])

            # Generate a list containing the dice faces rows
            dice_faces_rows = []
            for row_idx in range(DIE_HEIGHT):
                row_components = []
                for die in dice_faces:
                    row_components.append(die[row_idx])
                row_string = DIE_FACE_SEPARATOR.join(row_components)
                dice_faces_rows.append(row_string)

            # Generate header with the word "RESULTS" centered
            width = len(dice_faces_rows[0])
            diagram_header = " RESULTS ".center(width, "~")

            dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
            return dice_faces_diagram


        DICE_ART = {
            1: (
                "┌─────────┐",
                "│         │",
                "│    *    │",
                "│         │",
                "└─────────┘",
            ),
            2: (
                "┌─────────┐",
                "│  *      │",
                "│         │",
                "│      *  │",
                "└─────────┘",
            ),
            3: (
                "┌─────────┐",
                "│  *      │",
                "│    *    │",
                "│      *  │",
                "└─────────┘",
            ),
            4: (
                "┌─────────┐",
                "│  *   *  │",
                "│         │",
                "│  *   *  │",
                "└─────────┘",
            ),
            5: (
                "┌─────────┐",
                "│  *   *  │",
                "│    *    │",
                "│  *   *  │",
                "└─────────┘",
            ),
            6: (
                "┌─────────┐",
                "│  *   *  │",
                "│  *   *  │",
                "│  *   *  │",
                "└─────────┘",
            ),
        }
        DIE_HEIGHT = len(DICE_ART[1])
        DIE_WIDTH = len(DICE_ART[1][0])
        DIE_FACE_SEPARATOR = " "

        def roll_dice(num_dice):
            """Return a list of integers with length `num_dice`.

            Each integer in the returned list is a random number between
            1 and 6, inclusive.
            """
            roll_results = []
            for _ in range(num_dice):
                roll = random.randint(1, 6)
                roll_results.append(roll)
            return roll_results


        def parse_input(input_string):
            """Return `input_string` as an integer between 1 and 6.

            Check if `input_string` is an integer number between 1 and 6.
            If so, return an integer with the same value. Otherwise, tell
            the user to enter a valid number and quit the program.
            """
            if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
                return int(input_string)
            else:
                print("PLease enter a number between 1 to 6.")
                ans=int(input("\nWant to continue? Type 1 for yes, 0 for no"))
                if(ans==1):
                  num_dice_input = input("How many dice do you want to roll? [1-6] ")
                  num_dice = parse_input(num_dice_input)
                  roll_results = roll_dice(num_dice)
                  
                  print(roll_results)
                  dice_face_diagram = generate_dice_faces_diagram(roll_results)
                  print(f"\n{dice_face_diagram}")

                else:
                 exit()


        # ~~~ App's main code block ~~~
        # 1. Get and validate user's input

        num_dice_input = input("How many dice do you want to roll? [1-6] ")
        num_dice = parse_input(num_dice_input)

        # 2. Roll the dice
        roll_results = roll_dice(num_dice)

        print(roll_results)  # Remove this line after testing the app
        # 3. Generate the ASCII diagram of dice faces
        dice_face_diagram = generate_dice_faces_diagram(roll_results)
        # 4. Display the diagram
        print(f"\n{dice_face_diagram}")

            
       

# for second game
if choice == 2:
                                                     ## MATCHING TILES GAMES ##
    print("You are now playing the matching tiles games!!")
    from tkinter import *
    import random
    import time
    from tkinter import messagebox

    #### GLOBAL VARIABLES ######

    # data list contains the data in the cards
    data = ["@", "#", "$", "%", "^", "&", "*", "!"]
    data_length = len(data)

    # to check if the game ends, No more available cards
    game_end = 0

    # dictionary stores buttons(keys) and their texts(values)
    dict_cards = {}

    # to check how many cards clicked if 2, stop and check similarity
    clicked_cards = 0

    # fst_ refers to first clicked card
    fst_ = ""

    # scnd_ refers to second clicked card
    scnd_ = ""

    # store the moment when the game starts
    start = time.time()

    # initialize or initiate our root(window)
    root = Tk()
    root.resizable(False, False)
    root.title("Memory Game")
    root.config(background="green")

    # first frame_

    f1 = Frame(root)
    f1.pack()

    # fonts
    fonts = ['Helvetica', '20', 'bold']

    bt1 = Button(f1, font=(fonts), width="3", height="1", command=lambda: bttn_clicked(bt1))
    bt1.grid(row=0, column=0, padx=20, pady=40)
    dict_cards[bt1] = ""

    bt2 = Button(f1, font=(fonts), width="3", height="1", command=lambda: bttn_clicked(bt2))
    bt2.grid(row=0, column=1, padx=20, pady=40)
    dict_cards[bt2] = ""

    bt3 = Button(f1, font=(fonts), width="3", height="1", command=lambda: bttn_clicked(bt3))
    bt3.grid(row=0, column=2, padx=20, pady=40)
    dict_cards[bt3] = ""

    bt4 = Button(f1, font=(fonts), width="3", height="1", command=lambda: bttn_clicked(bt4))
    bt4.grid(row=0, column=3, padx=20, pady=40)
    dict_cards[bt4] = ""

    # second frame_

    f2 = Frame(root)
    f2.pack()

    bt5 = Button(f2, font=(fonts), width="3", height="1", command=lambda: bttn_clicked(bt5))
    bt5.grid(row=1, column=0, padx=20, pady=40)
    dict_cards[bt5] = ""

    bt6 = Button(f2, font=(fonts), width="3", height="1", command=lambda: bttn_clicked(bt6))
    bt6.grid(row=1, column=1, padx=20, pady=40)
    dict_cards[bt6] = ""

    bt7 = Button(f2, font=(fonts), width="3", height="1", command=lambda: bttn_clicked(bt7))
    bt7.grid(row=1, column=2, padx=20, pady=40)
    dict_cards[bt7] = ""

    bt8 = Button(f2, font=(fonts), width="3", height="1", command=lambda: bttn_clicked(bt8))
    bt8.grid(row=1, column=3, padx=20, pady=40)
    dict_cards[bt8] = ""

    # third frame_

    f3 = Frame(root)
    f3.pack()

    bt9 = Button(f3, font=(fonts), width="3", height="1", command=lambda: bttn_clicked(bt9))
    bt9.grid(row=1, column=0, padx=20, pady=40)
    dict_cards[bt9] = ""

    bt10 = Button(f3, font=(fonts), width="3", height="1", command=lambda: bttn_clicked(bt10))
    bt10.grid(row=1, column=1, padx=20, pady=40)
    dict_cards[bt10] = ""

    bt11 = Button(f3, font=(fonts), width="3", height="1", command=lambda: bttn_clicked(bt11))
    bt11.grid(row=1, column=2, padx=20, pady=40)
    dict_cards[bt11] = ""

    bt12 = Button(f3, font=(fonts), width="3", height="1", command=lambda: bttn_clicked(bt12))
    bt12.grid(row=1, column=3, padx=20, pady=40)
    dict_cards[bt12] = ""

    # forth frame_

    f4 = Frame(root)
    f4.pack()

    bt13 = Button(f4, font=(fonts), width="3", height="1", command=lambda: bttn_clicked(bt13))
    bt13.grid(row=1, column=0, padx=20, pady=40)
    dict_cards[bt13] = ""

    bt14 = Button(f4, font=(fonts), width="3", height="1", command=lambda: bttn_clicked(bt14))
    bt14.grid(row=1, column=1, padx=20, pady=40)
    dict_cards[bt14] = ""

    bt15 = Button(f4, font=(fonts), width="3", height="1", command=lambda: bttn_clicked(bt15))
    bt15.grid(row=1, column=2, padx=20, pady=40)
    dict_cards[bt15] = ""

    bt16 = Button(f4, font=(fonts), width="3", height="1", command=lambda: bttn_clicked(bt16))
    bt16.grid(row=1, column=3, padx=20, pady=40)
    dict_cards[bt16] = ""   
    
    
    ######### USED FUNCTIONS #########
    
    
    # this function to set random data to our cards
    def random_text():
        # record if the data has occured twice
        occurances = {"@": 0, "#": 0, "$": 0, "%": 0, "^": 0, "&": 0, "*": 0, "!": 0}

        for bttn in dict_cards:
    
            if len(data) > 0:
                random.shuffle(data)
                x = data[0]
                dict_cards[bttn] = x
                occurances[x] = occurances[x] + 1
                
                if occurances[x] == 2:
                    data.remove(x)
                
                
    # this function is called when we click a card
    def bttn_clicked(btn):
        global clicked_cards
        global fst_
        global scnd_

        clicked_cards = clicked_cards + 1

        if clicked_cards == 1:
            fst_ = btn
            btn.configure(text=dict_cards[btn], state=DISABLED)

        if clicked_cards == 2:
            scnd_ = btn
            btn.configure(text=dict_cards[btn], state=DISABLED)

            root.after(500, check_same)
    
    
    # this function to check if the two cards are similar
    def check_same():
        global clicked_cards
        global fst_
        global scnd_
        global game_end
        global data_length

        if scnd_['text'] != fst_['text']:
            fst_.configure(text="", state="normal")
            scnd_.configure(text="", state="normal")
        else:
            game_end = game_end + 1

        if game_end == data_length:
            messagebox.showinfo("MEMORY GAME", "You have spent " + str(int(time.time() - start)) + " sec!")
            root.destroy()

        clicked_cards = 0


    # calling the function random_text
    random_text()

    # run out window
    root.mainloop()


   
print("Thank you for playing!!")
print("Visit again :)")



'''
End of code
'''








