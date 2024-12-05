from collections import defaultdict, deque

def parse_rules_and_updates(filename):
    """Parse ordering rules and updates from input.txt."""
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')
    
    ordering_rules = []
    updates = []

    for line in lines:
        line = line.strip()  # Remove extra whitespace
        if not line:
            continue  # Skip blank lines
        if "|" in line:
            ordering_rules.append(line)
        else:
            updates.append([int(num) for num in line.split(',') if num.strip()])
    
    return ordering_rules, updates

def parse_rules(rules):
    """Convert ordering rules into a directed graph."""
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for rule in rules:
        X, Y = map(int, rule.split('|'))
        graph[X].append(Y)
        in_degree[Y] += 1
        in_degree[X] += 0  # Ensure X exists in in_degree even if no incoming edges
    
    return graph, in_degree

def is_valid_update(update, graph, in_degree):
    """Check if the update order satisfies the graph rules."""
    # Create a subgraph for the pages in this update
    subgraph = defaultdict(list)
    sub_in_degree = defaultdict(int)
    for page in update:
        if page in graph:
            for neighbor in graph[page]:
                if neighbor in update:
                    subgraph[page].append(neighbor)
                    sub_in_degree[neighbor] += 1
            sub_in_degree[page] += 0  # Ensure page exists in in_degree
    
    # Topological sort to check for valid order
    queue = deque([node for node in update if sub_in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in subgraph[current]:
            sub_in_degree[neighbor] -= 1
            if sub_in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If the sorted order matches the update, it is valid
    return sorted_order == update, sorted_order

def find_middle(page_list):
    """Find the middle page of a list."""
    n = len(page_list)
    return page_list[n // 2] if n % 2 != 0 else page_list[(n - 1) // 2]

def process_updates(filename):
    """Main function to process updates and calculate result."""
    ordering_rules, updates = parse_rules_and_updates(filename)
    graph, in_degree = parse_rules(ordering_rules)

    incorrect_updates = []
    middle_pages = []

    for update in updates:
        is_valid, sorted_order = is_valid_update(update, graph, in_degree)
        if not is_valid:
            incorrect_updates.append(sorted_order)
            middle_pages.append(find_middle(sorted_order))
    
    # Sum the middle pages of incorrectly ordered updates
    return sum(middle_pages)

# Input file
filename = 'input.txt'
result = process_updates(filename)
print("Result:", result)