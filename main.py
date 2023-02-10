#finds perfect number
#Ella Mohanram
#February 2, 2023

#finds perfect number
#return: perfect number
class PerfectNumber:
    #constructor function that initializes instance variables
    def __init__(self):
        self.current_number = 0

    #checks if a given number is perfect
    #number: the number to check if perfect
    #return: true if perfect, else false
    def perfect_number(self, number):
        if number == 0:
            return False
        else:
            count = 0
            for num in range(1, number):
                if (number % num) == 0:
                    count += num
                else:
                    continue

            if count == number:
                return True
            else:
                return False

    #finds perfect number given maximum number
    #limit: integer that creates maximum number
    #returns: perfect number if such number exists
    def find_perfect(self, limit):
        upper_limit = 10 ** int(limit)
        stack = []

        root_point = 0
        stack.append(root_point)

        while len(stack) > 0:
            current_point = stack[-1]
            stack.pop(-1)
            print(current_point)

            if self.perfect_number(current_point) == True:
                self.current_number = current_point
                return current_point
            else:
                for i in range(0, 10):
                    new_number = (current_point * 10) + i
                    if new_number < upper_limit:
                        stack.append(new_number)

        return -1

    #runs class in terminal
    #returns: perfect number
    def run(self):
        iterative_deepening = input("Do you want to try iterative deepening? (Y/N): ")
        if iterative_deepening == "Y":
            for i in range(1, 6):
                self.find_perfect(i)
                print("perfect = " + str(self.current_number))
        else:
            limit = input("Enter limit: ")
            self.find_perfect(limit)
            print("perfect = " + str(self.current_number))

perfectNumber = PerfectNumber()
perfectNumber.run()
