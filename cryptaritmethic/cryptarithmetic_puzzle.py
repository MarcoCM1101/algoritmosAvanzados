# ----------------------------------------------------------
# Lab #5: Cryptarithmetic with CSP
# General cryptarithmetic puzzle solver.
#
# Date: 13-Oct-2023
# Authors:
#           A01753729 Marco Antonio Caudillo Morales
#           A01754412 Adolfo Sebastián González Mora
# ----------------------------------------------------------

from csp import Constraint, CSP
from typing import Dict, List, Optional


class CryptoarithmeticConstraint(Constraint[str, int]):
    def __init__(self, letters: List[str], words: List[str], answer: str, max_len: int) -> None:
        super().__init__(letters)
        self.letters = letters
        self.words = words
        self.answer = answer
        self.max_len = max_len

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        # No duplicate values
        if len(set(assignment.values())) < len(assignment):
            return False

        if len(assignment) == len(self.letters):
            sum_words = sum(
                assignment[word[i]] * 10 ** (len(word) - 1 - i)
                for word in self.words
                for i in range(len(word))
            )
            sum_answer = sum(
                assignment[self.answer[i]] * 10 ** (len(self.answer) - 1 - i)
                for i in range(len(self.answer))
            )
            return sum_words == sum_answer

        return True


def solve_cryptarithmetic_puzzle(addends: List[str], result: str) -> Optional[Dict[str, int]]:
    unique_letters: List[str] = list(
        sorted(set("".join(addends + [result])))
    )
    max_word_length: int = max(map(len, addends + [result]))

    possible_values: Dict[str, List[int]] = {
        letter: list(range(10)) for letter in unique_letters
    }

    constraint_problem: CSP[str, int] = CSP(unique_letters, possible_values)
    constraint_problem.add_constraint(
        CryptoarithmeticConstraint(
            unique_letters, addends, result, max_word_length)
    )

    solution: Optional[Dict[str, int]
                       ] = constraint_problem.backtracking_search()

    return {k.upper(): v for k, v in solution.items()} if solution else None


if __name__ == "__main__":
    print(solve_cryptarithmetic_puzzle(['x', 'y', 'z'], 'xx'))
