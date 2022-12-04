import string


def read_file(filename):
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]
    output = []
    for line in lines:
        n_elems = len(line) // 2
        output.append((line[:n_elems], line[n_elems:]))
    return output


def get_priority_dictionary():
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)

    combos = [x[0] for x in list(zip(enumerate(lowercase, start=1)))]
    d_lower = {y: x for x, y in combos}

    combos = [x[0] for x in list(zip(enumerate(uppercase, start=27)))]
    d_upper = {y: x for x, y in combos}

    dict_priorities = d_lower | d_upper
    return dict_priorities


def problem_one(data):
    priority = 0
    priority_dictionary = get_priority_dictionary()
    for rucksack in data:
        common_element = set(rucksack[0]).intersection(set(rucksack[1]))
        assert len(common_element) == 1
        common_element = list(common_element)[0]
        priority += priority_dictionary[common_element]
    return priority


def problem_two(data):
    priority = 0
    data = [x[0]+x[1] for x in data]
    priority_dictionary = get_priority_dictionary()
    assert len(data) % 3 == 0
    for i in range(0, len(data), 3):
        common = set(data[i]).intersection(set(data[i+1])).intersection(set(data[i+2]))
        assert len(common) == 1
        common = list(common)[0]
        priority += priority_dictionary[common]
    return priority


if __name__ == "__main__":
    data = read_file('./data/day_three.txt')
    print(problem_one(data))
    print(problem_two(data))
