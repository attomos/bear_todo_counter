import subprocess

from bear_todo_counter import append_todo_count


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
    write_to_clipboard(output)
