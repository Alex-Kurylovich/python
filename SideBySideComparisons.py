def get_staircase1(input):
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


def get_staircase2(nums):
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


def get_staircase3(nums):
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

    input11 = [1, 2, 3, 4, 5, 6]
    input22 = [1, 2, 3, 4, 5, 6, 7]
    input33 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Steps Input 1: " + str([1, 2, 3, 4, 5, 6]))
    print("Steps Input 2: " + str([1, 2, 3, 4, 5, 6, 7]))
    print("Steps Input 3: " + str([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print()

    print("my_stares")
    print("Steps " + str(get_staircase1(input11)))
    print("Steps " + str(get_staircase1(input22)))
    print("Steps " + str(get_staircase1(input33)))
    print()

    print("get_staircase2")
    print("Steps " + str(get_staircase2(input11)))
    print("Steps " + str(get_staircase2(input22)))
    print("Steps " + str(get_staircase2(input33)))
    print()

    print("get_staircase3")
    print("Steps " + str(get_staircase3(input11)))
    print("Steps " + str(get_staircase3(input22)))
    print("Steps " + str(get_staircase3(input33)))


