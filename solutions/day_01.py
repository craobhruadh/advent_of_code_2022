import heapq


def read_input(filename, numeric=True):
    with open(filename) as f:
        data = [x.strip() for x in f.readlines()]

    elves = []
    lunchbox = []
    for d in data:
        if d == '':
            if lunchbox:
                elves.append(lunchbox)
                lunchbox = []
        else:
            lunchbox.append(int(d))
    if lunchbox:
        elves.append(lunchbox)

    return elves


def problem_one(elves):
    current_max = float("-inf")
    for elf in elves:
        current_max = max(
            current_max,
            sum(elf)
        )
    return current_max


def problem_two(elves):
    heap = []
    for elf in elves:
        current = sum(elf)
        heapq.heappush(heap, -current)
    
    total = 0
    for _ in range(3):
        total += abs(heapq.heappop(heap))
    return total


if __name__ == "__main__":
    elves = read_input('./data/day_one.txt', numeric=False)
    result_one = problem_one(elves)
    print(result_one)

    result_two = problem_two(elves)
    print(result_two)
