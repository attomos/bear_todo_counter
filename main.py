import re
import subprocess


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


# https://stackoverflow.com/a/25802742/606355
def write_to_clipboard(output):
    process = subprocess.Popen(
        "pbcopy", env={"LANG": "en_US.UTF-8"}, stdin=subprocess.PIPE
    )
    process.communicate(output.encode("utf-8"))


def read_from_clipboard():
    return subprocess.check_output("pbpaste", env={"LANG": "en_US.UTF-8"}).decode(
        "utf-8"
    )


if __name__ == "__main__":
    txt = read_from_clipboard()
    output = append_todo_count(txt)
    print(output.split("\n")[0])
    write_to_clipboard(output)
