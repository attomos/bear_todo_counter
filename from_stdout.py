import fileinput

from bear_todo_counter import append_todo_count


def main():
    lines = []
    for line in fileinput.input():
        lines.append(line.rstrip("\n"))
    txt = "\n".join(lines)
    output = append_todo_count(txt)
    print(output)


if __name__ == "__main__":
    main()
