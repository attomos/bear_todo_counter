import re


def append_todo_count(txt):
    lines = txt.splitlines()
    complete = 0
    total = 0
    for line in lines:
        if re.match(r"^\s*\+\s+\[?\S*", line):
            complete += 1
        if re.match(r"^\s*[\+|-]\s+\[?\S*", line):
            total += 1
    todo_count = "[{}/{}]".format(complete, total)

    total_pattern = r"\[\d+/\d+\]"
    if re.search(total_pattern, lines[0]):
        lines[0] = re.sub(total_pattern, todo_count, lines[0])
    else:
        lines[0] += " {}".format(todo_count)
    return "\n".join(lines)
