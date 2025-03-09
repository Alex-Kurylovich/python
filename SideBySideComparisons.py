class SideBySideComparisons:

    def get_stairs(self, input):
        print("Bild steps for " + str(len(input)) + " " +  str(input))
        output = []
        index = 0
        steps = 1
        while index + steps <= len(input) :
            stairs = input[index : index + steps]
            output.append(stairs)
            steps += 1
            index += steps - 1
        if index < len(input) :
            result = "False"
        else :
            result  = output
        return result



if __name__ == '__main__':

    my_stares = SideBySideComparisons()

    input1 = [1, 2, 3, 4, 5, 6]
    print("Steps " + str(my_stares.get_stairs(input1)))

    input2 = [1, 2, 3, 4, 5, 6, 7]
    print("Steps " + str(my_stares.get_stairs(input2)))

    input3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Steps " + str(my_stares.get_stairs(input3)))
