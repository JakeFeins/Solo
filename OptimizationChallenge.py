import numpy as np
if __name__ == "__main__":


    def sum_of_squares_of_odds(nums):
        #square each entry in nums
        nums = np.array(nums)
        nums = nums**2
        #sum numbers that aren't divisble by 4
        nums = nums[nums%4 != 0]
        return sum(nums)
        

    print(sum_of_squares_of_odds([1, 2, 3, 4, 5])) # should return 35 (1^2 + 3^2 + 5^2)
    print(sum_of_squares_of_odds([10, 11, 12, 13, 14, 15])) # should return 515 (11^2 + 13^2 + 15^2)
    print(sum_of_squares_of_odds([-1, -2, 3, -4, 5])) # should return 35 (-1^2 + 3^2 + 5^2)

    