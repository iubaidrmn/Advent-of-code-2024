from collections import defaultdict

FILENAME = "input.txt"
PRUNE = 16777216
ITERATIONS = 2000


def parse_input(filename):
    with open(filename) as input_file:
        return [int(num) for num in input_file.read().split("\n")]


def evolve(secret_number):
    secret_number = ((secret_number * 64) ^ secret_number) % PRUNE
    secret_number = ((secret_number // 32) ^ secret_number) % PRUNE
    secret_number = (secret_number * 2048 ^ secret_number) % PRUNE
    return secret_number


def generate_secret_numbers_and_changes(secret_numbers, iterations):
    final_numbers = []
    deltas = []
    for num in secret_numbers:
        prices = [num % 10]
        for _ in range(iterations):
            num = evolve(num)
            prices.append(num % 10)
        changes = [
            (second - first, second) for first, second in zip(prices, prices[1:])
        ]
        final_numbers.append(num)
        deltas.append(changes)
    return final_numbers, deltas


def part_one(final_secret_numbers):
    return sum(final_secret_numbers)


def part_two(deltas):
    bananas = defaultdict(int)
    for changes in deltas:
        seen = set()
        for i in range(len(changes) - 3):
            sequence = tuple(change[0] for change in changes[i : i + 4])
            if sequence not in seen:
                bananas[sequence] += changes[i + 3][1]
                seen.add(sequence)
    return max(bananas.values())


def main():
    secret_numbers = parse_input(FILENAME)
    final_secret_numbers, deltas = generate_secret_numbers_and_changes(
        secret_numbers, ITERATIONS
    )

    print(part_one(final_secret_numbers))
    print(part_two(deltas))


if __name__ == "__main__":
    main()
