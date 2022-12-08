import copy

day = int('08')
with open(f"inputs/input{day}.txt", "r") as f:
    raw_data = f.read()

with open(f"tests/test{day}.txt", "r") as t:
    test_data = t.read()


def solve(data):
    width = len(data[0])
    height = len(data)
    # pad data
    # pad = "".join(['0'] * (len(data[0]) + 2))
    # data = ['0' + l + '0' for l in data]
    # data.insert(0, pad)
    # data.append(pad)
    # for ll in data:
    #     print(ll)

    visible_matrix = [[0] * width for i in range(0, height)]
    # horizontal

    # left to right, right to left
    for y in range(height):
        mlr = -1
        mrl = -1
        for x in range(width):
            lr = data[y][x]
            if int(lr) > mlr:
                mlr = int(lr)
                visible_matrix[y][x] = 1
            rl = data[y][width - x - 1]
            if int(rl) > mrl:
                mrl = int(rl)
                visible_matrix[y][width - x - 1] = 1
    for x in range(width):
        mtd = -1
        mdt = -1
        for y in range(height):
            td = data[y][x]
            dt = data[height - y - 1][x]
            if int(td) > mtd:
                visible_matrix[y][x] = 1
                mtd = int(td)
            if int(dt) > mdt:
                visible_matrix[height - y - 1][x] = 1
                mdt = int(dt)

    print("pt1", sum([i for j in visible_matrix for i in j]))


def get_scenic_score(data, y, x):
    width = len(data[0])
    height = len(data)
    d = int(data[y][x])

    tv = 0
    rv = 0
    lv = 0
    bv = 0
    arr = copy.deepcopy(data[y][:x].split())
    arr = [int(i) for i in arr[0]]
    arr.reverse()
    for i in arr:
        lv += 1
        if i >= d:
            # print("found blocking tree to the left", lv, d)
            break

    arr = copy.deepcopy(data[y][x+1:].split())
    arr = [int(i) for i in arr[0]]
    # print("right: ", arr)
    for i in arr:
        rv += 1
        if i >= d:
            break
        # print(f"{i} is not bigger than {d}")

    arr = copy.deepcopy([int(data[yy][x]) for yy in range(y + 1, height)])
    # print("bot", arr)
    for i in arr:
        bv += 1
        if i >= d:
            # print("found blocking tree to the south", bv, d)
            break

    arr = copy.deepcopy([int(data[yy][x]) for yy in range(0, y)])
    arr.reverse()
    # print("top", arr)
    for i in arr:
        tv += 1
        if i >= d:
            # print("found blocking tree to the north", tv, d)
            break

    return tv * lv * rv * bv


def solve2(data):
    width = len(data[0])
    height = len(data)
    best_score = -1
    for y in range(1, height-1):
        for x in range(1, width-1):
            best_score = max(best_score, get_scenic_score(data, y, x))
    print("pt2", best_score)



solve(raw_data.split('\n'))

solve2(raw_data.split('\n'))
