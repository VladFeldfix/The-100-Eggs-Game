import random

class main:
    def __init__(self):
        # global vars
        self.win_counter = {}
        self.eggs = []
        self.console = []

        self.test()
        self.write()
    
    def test(self):
        test_x_times = 5
        self.win_counter = {"A": [], "B": [], "C": []}

        for i in range(test_x_times):
            self.set_up_board()
            self.strategy_A()
            self.strategy_B()
            self.strategy_C()
            self.print("\n"+"-"*119+"\n")
        
        self.display_results()
    
    def strategy_A(self):
        self.print("Strategy A ")
        
        step_counter = 0
        selected_card = -1
        x = 0
        while self.chosen_number != selected_card:
            step_counter += 1
            x += 1
            select_egg = self.eggs[x-1]
            selected_card = select_egg.inside_number
        self.win_counter["A"].append(step_counter)
        self.print("Found in: "+str(step_counter)+" steps\n")

    def strategy_B(self):
        self.print("Strategy B ")
        step_counter = 0
        selected_card = -1
        xx = []
        for i in range(1,101):
            xx.append(i)
        random.shuffle(xx)
        while self.chosen_number != selected_card:
            step_counter += 1
            x = xx.pop()
            select_egg = self.eggs[x-1]
            selected_card = select_egg.inside_number
        self.win_counter["B"].append(step_counter)
        self.print("Found in: "+str(step_counter)+" steps\n")

    def strategy_C(self):
        self.print("Strategy C ")
        step_counter = 0
        selected_card = -1
        x = self.chosen_number
        while self.chosen_number != selected_card:
            step_counter += 1
            select_egg = self.eggs[x-1]
            selected_card = select_egg.inside_number
            x = selected_card
        self.win_counter["C"].append(step_counter)
        self.print("Found in: "+str(step_counter)+" steps\n")

    def display_results(self):
        pass
    
    def set_up_board(self):
        # set up
        self.eggs = []
        all_numbers = []
        for i in range(1,101):
            all_numbers.append(i)
        random.shuffle(all_numbers)
        for i in range(1,101):
            egg_number = i
            inside_number = all_numbers.pop()
            self.eggs.append(node(egg_number,inside_number))
        
        # choose a golden card
        self.chosen_number = random.randint(1, 100)

        # display the board
        for egg in self.eggs:
            self.print(str(egg.egg_number).zfill(3)+" - "+str(egg.inside_number).zfill(3)+" | ")
            if egg.egg_number % 10 == 0:
                self.print("\n")
        self.print("\n")
        self.print("Chosen number: "+str(self.chosen_number)+str("\n"))
    
    def print(self, text):
        self.console.append(text)
    
    def write(self):
        file = open("log.txt", 'w')
        for line in self.console:
            file.write(line)
        file.close()

"""
class main:
    def __init__(self):
        self.test()
    
    def test(self):
        test_x_times = 10
        win_counter = {"A": [], "B": [], "C": []}
        
        for i in range(test_x_times):
            # set up
            eggs = []
            all_numbers = []
            for i in range(1,101):
                all_numbers.append(i)
            random.shuffle(all_numbers)
            for i in range(1,101):
                egg_number = i
                inside_number = all_numbers.pop()
                eggs.append(node(egg_number,inside_number))
            
            # choose a golden card
            chosen_number = random.randint(1, 100)

            # strategy A - search each egg one by one in a row
            step_counter = 0
            selected_card = -1
            x = 0
            while chosen_number != selected_card:
                step_counter += 1
                x += 1
                select_egg = eggs[x-1]
                selected_card = select_egg.inside_number
            win_counter["A"].append(step_counter)

            # strategy B - search by picking up a random egg
            step_counter = 0
            selected_card = -1
            xx = []
            for i in range(1,101):
                xx.append(i)
            random.shuffle(xx)
            while chosen_number != selected_card:
                step_counter += 1
                x = xx.pop()
                select_egg = eggs[x-1]
                selected_card = select_egg.inside_number
            win_counter["B"].append(step_counter)
            
            # strategy C
            step_counter = 0
            selected_card = -1
            x = chosen_number
            while chosen_number != selected_card:
                step_counter += 1
                select_egg = eggs[x-1]
                selected_card = select_egg.inside_number
                x = selected_card
            win_counter["C"].append(step_counter)

            # display eggs
            for egg in eggs:
                print(str(egg.egg_number) + " - " + str(egg.inside_number))

        print("Results:")
        #print(win_counter)
        print("Strategy A: " + str(sum(win_counter["A"])/test_x_times))
        print("Strategy B: " + str(sum(win_counter["B"])/test_x_times))
        print("Strategy C: " + str(sum(win_counter["C"])/test_x_times))
        input(">")
        self.test()
"""
class node:
    def __init__(self, egg_number, inside_number):
        self.egg_number = egg_number
        self.inside_number = inside_number
main()