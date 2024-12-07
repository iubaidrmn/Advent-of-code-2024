import itertools
from time import perf_counter


def evaluate_equation(nums: list[int], ops: tuple[str, ...]):
    res = nums[0]
    current = 1
    for op in ops:
        if op == "+":
            res += nums[current]
        elif op == "*":
            res *= nums[current]
        else:
            res = int(str(res) + str(nums[current]))
        current += 1
    return res


def part_one(data: str) -> int:
    equations: list[tuple[int, list[int]]] = [(int(line.split(":")[0]), [int(num) for num in line.split(
        ":")[1].split()]) for line in data.splitlines()]
    # the stupid approach
    ops = "+*"
    res = 0
    for result, eqn in equations:
        # the result of multiplying two sets (i.e. every combination of the operators possible for result length tuples)
        possibilities = itertools.product(ops, repeat=len(eqn) - 1)
        for p in possibilities:
            if result == evaluate_equation(eqn, p):
                res += result
                break
    return res


def part_two(data: str) -> int:
    equations: list[tuple[int, list[int]]] = [(int(line.split(":")[0]), [int(num) for num in line.split(
        ":")[1].split()]) for line in data.splitlines()]
    # the even stupider approach
    ops = ('*', '+', '||')
    res = 0
    for result, eqn in equations:
        possibilities = itertools.product(ops, repeat=len(eqn) - 1)
        for p in possibilities:
            if result == evaluate_equation(eqn, p):
                res += result
                break
    return res


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()
        # p1_start = perf_counter()
        # print(f"Part One: {part_one(data)}")
        # p1_end = perf_counter()
        # p1_elapsed = p1_end - p1_start
        p2_start = perf_counter()
        print(f"Part Two: {part_two(data)}")
        # p2_end = perf_counter()
        # p2_elapsed = p2_end - p2_start
        # print(f"Elapsed Time (Part One): {p1_elapsed:0.2f}s")  # ~0.10s
        # print(f"Elapsed Time (Part Two): {p2_elapsed:0.2f}s")  # 10s
