# File: fifteen_puzzle.py

# ----------------------------------------------------------
# Lab #4: A* Search Algorithm
# Solving the 15 puzzle.
#
# Date: 06-Oct-2023
# Authors:
#           A01753729 Marco Antonio Caudillo Morales
#           A01754412 Adolfo Sebastián González Mora
# ----------------------------------------------------------

from typing import Optional, List
from generic_search import astar, Node, node_to_path

Frame = tuple[tuple[int, ...], ...]


def goal_test(frame: Frame) -> bool:
    goal = (
        (1, 2, 3, 4),
        (5, 6, 7, 8),
        (9, 10, 11, 12),
        (13, 14, 15, 0)
    )
    return frame == goal


def successors(frame: Frame) -> List[Frame]:
    # Encuentra la ubicación del 0 (espacio no ocupado)
    row, col = None, None
    for i in range(4):
        for j in range(4):
            if frame[i][j] == 0:
                row, col = i, j
                break

    # Define los posibles movimientos: [Arriba, Abajo, Izquierda, Derecha]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    results = []

    for move in moves:
        new_row, new_col = row + move[0], col + move[1]

        # Verifica si el movimiento es válido (dentro del límite del frame)
        if 0 <= new_row < 4 and 0 <= new_col < 4:
            # Crea una copia del frame original y realiza el movimiento
            frame_list = [list(row) for row in frame]
            frame_list[row][col], frame_list[new_row][new_col] = frame_list[new_row][new_col], frame_list[row][col]

            # Añade el nuevo frame a los resultados
            results.append(tuple(tuple(row) for row in frame_list))

    return results


def heuristic(frame: Frame) -> float:
    goal = (
        (1, 2, 3, 4),
        (5, 6, 7, 8),
        (9, 10, 11, 12),
        (13, 14, 15, 0)
    )

    mismatch_count = 0
    for i in range(4):
        for j in range(4):
            if frame[i][j] != goal[i][j]:
                mismatch_count += 1

    return float(mismatch_count)


def solve_puzzle(frame: Frame) -> None:
    result: Optional[Node[Frame]] = astar(
        frame, goal_test, successors, heuristic)

    if result is None:
        print("Unfortunately, no solution was found.")
        return

    path = node_to_path(result)
    n_steps = len(path) - 1
    print(
        f"Solution requires {n_steps} step{'s' if n_steps != 1 else ''}")

    for i in range(1, len(path)):
        prev_zero_pos = [(ix, jx) for ix, row in enumerate(path[i-1])
                         for jx, val in enumerate(row) if val == 0][0]
        curr_zero_pos = [(ix, jx) for ix, row in enumerate(path[i])
                         for jx, val in enumerate(row) if val == 0][0]
        direction = "up" if curr_zero_pos[0] > prev_zero_pos[0] else "down" if curr_zero_pos[
            0] < prev_zero_pos[0] else "left" if curr_zero_pos[1] > prev_zero_pos[1] else "right"
        print(
            f"Step {i}: Move {path[i-1][curr_zero_pos[0]][curr_zero_pos[1]]} {direction}")
