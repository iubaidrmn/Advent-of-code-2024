from functools import lru_cache

def count_ways(patterns, design):
    """Counts the number of ways to form a design using patterns."""
    @lru_cache(None)
    def helper(remaining_design):
        if not remaining_design:
            return 1  # Found one way to complete the design

        ways = 0
        for pattern in patterns:
            if remaining_design.startswith(pattern):
                ways += helper(remaining_design[len(pattern):])
        return ways

    return helper(design)

def total_arrangements(patterns, designs):
    """Calculates the total number of arrangements for all designs."""
    total_ways = 0
    for design in designs:
        total_ways += count_ways(tuple(patterns), design)
    return total_ways

def main():
    with open('input.txt', 'r') as file:
        content = file.read()

    # Split input into patterns and designs
    patterns_section, designs_section = content.split("\n\n")
    patterns = patterns_section.split(", ")
    designs = designs_section.strip().split("\n")

    # Calculate the total number of arrangements
    result = total_arrangements(patterns, designs)
    print(f"Total number of arrangements: {result}")

if __name__ == "__main__":
    main()
