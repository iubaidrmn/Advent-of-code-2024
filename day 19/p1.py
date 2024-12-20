def can_form_design(patterns, design):
    """Recursive helper function to determine if a design can be formed from patterns."""
    if not design:
        return True
    for pattern in patterns:
        if design.startswith(pattern):
            if can_form_design(patterns, design[len(pattern):]):
                return True
    return False

def count_possible_designs(patterns, designs):
    """Counts how many designs can be formed using the given patterns."""
    count = 0
    for design in designs:
        if can_form_design(patterns, design):
            count += 1
    return count

def main():
    with open('input.txt', 'r') as file:
        content = file.read()
    
    # Split input into patterns and designs
    patterns_section, designs_section = content.split("\n\n")
    patterns = patterns_section.split(", ")
    designs = designs_section.split("\n")
    
    # Count how many designs can be formed
    result = count_possible_designs(patterns, designs)
    print(f"Number of possible designs: {result}")

if __name__ == "__main__":
    main()
