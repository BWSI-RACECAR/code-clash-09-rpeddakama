"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #9 - License Plate (licenseplate.py)


Author: Wonjun Lee

Difficulty Level: 5/10

Prompt: Jon was speeding on the highway with his RACECAR, and the highway camera has taken a picture 
of the RACECAR’s number plate. However, some characters on the plate are blurry. Please write a function 
that returns the number of possible combinations of the number plate. The number plate for his RACECAR
consists of 7 distinct characters, starting with 3 distinct alphabets and ending with 4 distinct numbers. 
The input will be passed as a string and any blurred characters will be written as ‘.’

Test Cases: 
Input: “ABC123.” ; Output: 7
Input: “.ON0123” ; Output: 24
Input: “.BC.234” ; Output: 168
"""


class Solution:
    def licensePlate(self, str):
        # type str: string
        # return: int
        letters = []
        numbers = []
        l_dotcount = 0
        n_dotcount = 0

        for i in range(3):
            if str[i] != ".":
                letters.append(str[i])
            else:
                l_dotcount += 1
        for i in range(3, len(str)):
            if str[i] != ".":
                numbers.append(str[i])
            else:
                n_dotcount += 1

        if n_dotcount + l_dotcount == 0:
            return 0

        ans = 1
        for i in range(l_dotcount):
            ans = ans * (26 - (len(letters) - (i)))
        for i in range(n_dotcount):
            ans = ans * (10 - (len(numbers) - (i)))

        return ans


def main():
    string1 = input()
    tc1 = Solution()
    ans = tc1.licensePlate(string1)
    print(ans)


if __name__ == "__main__":
    main()
