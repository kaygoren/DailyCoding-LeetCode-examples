#  Letter Combinations of a Phone Number#17 -- LeetCode

class LetterCombination:
    phoneKeys = {"2":["a","b","c"],
                 "3":["d","e","f"],
                 "4":["g","h","i"],
                 "5":["j","k","l"],
                 "6":["m","n","o"],
                 "7":["p","q","r","s"],
                 "8":["t","u","v"],
                 "9":["w","x","y","z"]}
    answer = []

    def letterCombination(self, digits):
        self.combination(digits, "")

    def combination(self, digits, str):
        if(len(digits) == 0):
            self.answer.append(str)
        else:
            for letter in self.phoneKeys[digits[0]]:
                self.combination(digits[1:], str+letter)

letterComb = LetterCombination()
letterComb.letterCombination("23")
print(letterComb.answer)
