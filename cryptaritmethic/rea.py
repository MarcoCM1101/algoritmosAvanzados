# ----------------------------------------------------------
# Lab #5: Cryptarithmetic with CSP
# General cryptarithmetic puzzle solver.
#
# Date: 13-Oct-2023
# Authors:
#           A01747327 Jorge Rea
#           A01753911 Oswaldo Hernández
# ----------------------------------------------------------


from csp import Constraint, CSP
from typing import Dict, List, Optional


class CryptarithmeticConstraint(Constraint[str, int]):
    def __init__(self, unique_letters: List[str], words: List[str], answer: str, max_word_length: int) -> None:
        super().__init__(unique_letters)
        self.unique_letters: List[str] = unique_letters
        self.words: List[str] = words
        self.answer: str = answer
        self.max_word_length: int = max_word_length

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        # Check for duplicate assignments
        if len(set(assignment.values())) < len(assignment):
            return False

        if len(assignment) != len(self.unique_letters):
            return True

        total_word_sum = 0
        for i in range(self.max_word_length):
            for word in self.words:
                if i < len(word):
                    index = len(word) - 1 - i
                    total_word_sum += assignment[word[index]] * 10 ** i

        total_answer_sum = 0
        for i in range(len(self.answer)):
            index = len(self.answer) - 1 - i
            total_answer_sum += assignment[self.answer[index]] * 10 ** i

        return total_word_sum == total_answer_sum


def solve_cryptarithmetic_puzzle(addends: List[str], answer: str) -> Optional[Dict[str, int]]:
    unique_letters = list(set("".join(addends + [answer])))
    unique_letters.sort()

    possible_digits = {letter: list(range(10)) for letter in unique_letters}

    csp = CSP(unique_letters, possible_digits)
    csp.add_constraint(CryptarithmeticConstraint(
        unique_letters, addends, answer, max(map(len, addends))))

    solution = csp.backtracking_search()

    if solution is None:
        return None
    else:
        upper_solution = {key.upper(): value for key,
                          value in solution.items()}
        return upper_solution


if __name__ == "__main__":
    print(solve_cryptarithmetic_puzzle(['SEND', 'MORE'], 'MONEY'))
