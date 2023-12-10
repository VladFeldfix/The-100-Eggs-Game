import random

class main:
    def __init__(self):

        
        #for i in eggs:
        #    print(str(i.egg_number) + " - " + str(i.inside_number))
        self.test()
    
    def test(self):
        test_x_times = 10000
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

        print("Results:")
        #print(win_counter)
        print("Strategy A: " + str(sum(win_counter["A"])/test_x_times))
        print("Strategy B: " + str(sum(win_counter["B"])/test_x_times))
        print("Strategy C: " + str(sum(win_counter["C"])/test_x_times))
        input(">")
        self.test()

class node:
    def __init__(self, egg_number, inside_number):
        self.egg_number = egg_number
        self.inside_number = inside_number
main()