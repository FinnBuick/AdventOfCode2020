
with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]


bags = {}
for l in lines:
    bag, contains = l.split('contain')
    bag = bag.replace(' bags', '')
    bags[bag] = contains


def dfs(bag, bags):
    contains = []
    for b in bags:
        if bag in bags[b]:
            # Add b to our list
            contains.append(b)
            # Add all children to b in our list
            contains.extend(dfs(b, bags))
    # Remove duplicates
    return set(contains)


print("Part 1: ", len(dfs('shiny gold', bags)))


bags = {}
for l in lines:
    l = l.replace('bags', '').replace('bag', '').replace('.', '')
    bag, contains = l.split(" contain ")
    bag = bag.strip()

    if 'no other' in contains:
        bags[bag] = {}
        continue

    contains = contains.split(',')
    contains = [c.strip() for c in contains]
    inner_dict = {}
    for c in contains:
        amount = int(c[0])
        color = c[2:].strip()
        inner_dict[color] = amount
    bags[bag] = inner_dict


def rec_count(bag, bags):
    count = 1

    contained_bags = bags[bag]
    for c in contained_bags:
        factor = contained_bags[c]
        count += factor * rec_count(c, bags)

    return count


print("Part 2:", rec_count('shiny gold', bags))
