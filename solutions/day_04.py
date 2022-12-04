

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    output = []
    for line in lines:
        first, second = line.split(',')
        first = [int(x) for x in first.split('-')]
        second = [int(x) for x in second.split('-')]
        output.append((first, second))
    return output


def problem_one(data):
    count = 0
    for first, second in data:
        if first[0] >= second[0] and first[1] <= second[1]:
            count += 1
        elif first[0] <= second[0] and first[1] >= second[1]:
            count += 1
    return count


def problem_two(data):
    count = 0
    for first, second in data:
        first = sorted(first)
        second = sorted(second)
        if first[1] < second[0] or second[1] < first[0]:
            continue
        else:
            count += 1
    return count


if __name__ == "__main__":
    data = read_file('./data/day_04.txt')
    print(problem_one(data))
    print(problem_two(data))
