if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    second_max_grade = sorted(set([ele[1] for ele in records]))[1]

    sorted_named = sorted([items[0] for items in records if items[1] == second_max_grade])
    for _ in sorted_named:
        print(_)
