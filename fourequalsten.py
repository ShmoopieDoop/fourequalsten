GOAL_NUMBER = 10


def generate_combos(l) -> list[tuple[int]]:
    combos = []

    def h(l: list[int], *c):
        if len(l) == 1:
            combos.append((*c, *l))
            return
        else:
            for i in l:
                t = l[:]
                t.remove(i)
                h(t, *c, i)

    h(l)
    return combos


def generate_op_combos(n):
    ops = ["+", "-", "*", "/"]
    combos = []

    def h(*c):
        if len(c) == n:
            combos.append(c)
            return
        else:
            for i in ops:
                h(*c, i)

    h()
    return combos


def add_ops(combo, ops):
    e = []
    for i in range(len(ops)):
        e.append(combo[i])
        e.append(ops[i])
    e.append(combo[-1])
    return e


def bracket_combos(e):
    es = []
    for i in range(0, len(e) - 2, 2):
        for j in range(i + 2, len(e), 2):
            e1 = e[:i] + ["("] + e[i : j + 1] + [")"] + e[j + 1 :]
            es.append(e1)
    return es


def run_combo(e):
    s = "".join(e)
    try:
        if eval(s) == GOAL_NUMBER:
            print(f"{s} = {GOAL_NUMBER}")
    except ZeroDivisionError:
        pass


def check_ops(combos, op_combos):
    for c in combos:
        for o in op_combos:
            e = add_ops(c, o)
            b_co = bracket_combos(e)
            for b in b_co:
                run_combo(b)


def main():
    n = 5181
    l = list(str(n))
    combos = generate_combos(l)
    op_combos = generate_op_combos(len(l) - 1)
    check_ops(combos, op_combos)


if __name__ == "__main__":
    main()
