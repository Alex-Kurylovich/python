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

    def create_staircase1(self, nums):
      while len(nums) != 0:
        step = 1
        subsets = []
        if len(nums) >= step:
          subsets.append(nums[0:step])
          nums = nums[step:]
          step += 1
        else:
          return False
      return subsets

    def create_staircase2(self, nums):
        step = 1
        subsets = []
        while len(nums) != 0:
            if len(nums) >= step:
                subsets.append(nums[0:step])
                nums = nums[step:]
                step += 1
            else:
                return False
        return subsets

if __name__ == '__main__':

    my_stares = SideBySideComparisons()

    print("my_stares")
    input1 = [1, 2, 3, 4, 5, 6]
    print("Steps " + str(my_stares.get_stairs(input1)))
    input2 = [1, 2, 3, 4, 5, 6, 7]
    print("Steps " + str(my_stares.get_stairs(input2)))
    input3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Steps " + str(my_stares.get_stairs(input3)))
    print()

    print("create_staircase1")
    input1 = [1, 2, 3, 4, 5, 6]
    print("Steps " + str(my_stares.create_staircase1(input1)))
    input2 = [1, 2, 3, 4, 5, 6, 7]
    print("Steps " + str(my_stares.create_staircase1(input2)))
    input3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Steps " + str(my_stares.create_staircase1(input3)))
    print()

    print("create_staircase2")
    input1 = [1, 2, 3, 4, 5, 6]
    print("Steps " + str(my_stares.create_staircase2(input1)))
    input2 = [1, 2, 3, 4, 5, 6, 7]
    print("Steps " + str(my_stares.create_staircase2(input2)))
    input3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Steps " + str(my_stares.create_staircase2(input3)))


