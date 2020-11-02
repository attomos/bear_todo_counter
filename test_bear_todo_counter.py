from bear_todo_counter import append_todo_count


def test_simple_todo():
    txt = """\
Tasks
- [x] Task one
- [ ] Task two
- [ ] Task three"""
    actual = append_todo_count(txt)
    expected = """\
Tasks [1/3]
- [x] Task one
- [ ] Task two
- [ ] Task three"""
    assert actual == expected


def test_todo_with_emoji():
    txt = """\
Tasks 🐻
- [x] 🌈 Task
- [ ] Task two
- [ ] Task three"""
    actual = append_todo_count(txt)
    expected = """\
Tasks 🐻 [1/3]
- [x] 🌈 Task
- [ ] Task two
- [ ] Task three"""
    assert actual == expected


def test_todo_with_existing_todo_counter():
    txt = """\
Tasks 🐻 [1/3]
- [x] 🌈 Task
- [x] Task two
- [ ] Task three"""
    actual = append_todo_count(txt)
    expected = """\
Tasks 🐻 [2/3]
- [x] 🌈 Task
- [x] Task two
- [ ] Task three"""
    assert actual == expected


def test_todo_with_subtasks():
    txt = """\
Tasks 🐻
- [x] 🌈 Task
- [ ] Task two
- [ ] Task three
	- [ ] subtask 1
	- [ ] subtask 2"""
    actual = append_todo_count(txt)
    expected = """\
Tasks 🐻 [1/5]
- [x] 🌈 Task
- [ ] Task two
- [ ] Task three
	- [ ] subtask 1
	- [ ] subtask 2"""
    assert actual == expected


def test_empty_todo():
    txt = """\
Tasks 🙄
- [x] 
- [ ] 
- [ ] """  # noqa: W291
    actual = append_todo_count(txt)
    expected = """\
"""
    expected = """\
Tasks 🙄 [1/3]
- [x] 
- [ ] 
- [ ] """  # noqa: W291
    assert actual == expected


def test_todo_with_links():
    txt = """\
Tasks 👍
- [x] https://good-article.com/1
- [ ] https://good-article.com/main
	- [ ] https://good-article.com/sub1
	- [x] https://good-article.com/sub2
- [x] [Working With XML in Scala - DZone Java](https://dzone.com/articles/working-with-xml-in-scala)
- [x] [Amundsen — Lyft’s data discovery & metadata engine – Lyft Engineering](https://eng.lyft.com/amundsen-lyfts-data-discovery-metadata-engine-62d27254fbb9)"""  # noqa: E501
    actual = append_todo_count(txt)
    expected = """\
Tasks 👍 [4/6]
- [x] https://good-article.com/1
- [ ] https://good-article.com/main
	- [ ] https://good-article.com/sub1
	- [x] https://good-article.com/sub2
- [x] [Working With XML in Scala - DZone Java](https://dzone.com/articles/working-with-xml-in-scala)
- [x] [Amundsen — Lyft’s data discovery & metadata engine – Lyft Engineering](https://eng.lyft.com/amundsen-lyfts-data-discovery-metadata-engine-62d27254fbb9)"""  # noqa: E501
    assert actual == expected


def test_todo_with_dashes():
    txt = """\
Tasks with dashes 😂
- [ ] - in the beginning of a task
- [ ] let's see - in the middle of a task
- [ ] what about at the end -
- [ ] -
- [x] - in the beginning of a task
- [x] let's see - in the middle of a task
- [x] what about at the end -
- [x] -"""
    actual = append_todo_count(txt)
    expected = """\
Tasks with dashes 😂 [4/8]
- [ ] - in the beginning of a task
- [ ] let's see - in the middle of a task
- [ ] what about at the end -
- [ ] -
- [x] - in the beginning of a task
- [x] let's see - in the middle of a task
- [x] what about at the end -
- [x] -"""
    assert actual == expected


def test_todo_with_plus_signs():
    txt = """\
Tasks with plus signs 😂
- [ ] + in the beginning of a task
- [ ] let's see + in the middle of a task
- [ ] what about at the end +
- [ ] +
- [x] + in the beginning of a task
- [x] let's see + in the middle of a task
- [x] what about at the end +
- [x] +"""
    actual = append_todo_count(txt)
    expected = """\
Tasks with plus signs 😂 [4/8]
- [ ] + in the beginning of a task
- [ ] let's see + in the middle of a task
- [ ] what about at the end +
- [ ] +
- [x] + in the beginning of a task
- [x] let's see + in the middle of a task
- [x] what about at the end +
- [x] +"""
    assert actual == expected


def test_todo_with_line_separator():
    txt = """\
# tryme 🐻
- [ ] read this
- [ ] read this too
---
- [x] done 1
- [x] done 2"""
    actual = append_todo_count(txt)
    expected = """\
# tryme 🐻 [2/4]
- [ ] read this
- [ ] read this too
---
- [x] done 1
- [x] done 2"""
    assert actual == expected


def test_todo_with_mixed_cases():
    txt = """\
# x or X? Why not both
- [x] read this
- [X] read this too
- [ ] do this later
---
- [x] done 1
- [X] done 2"""
    actual = append_todo_count(txt)
    expected = """\
# x or X? Why not both [4/5]
- [x] read this
- [X] read this too
- [ ] do this later
---
- [x] done 1
- [X] done 2"""
    assert actual == expected


def test_empty_string():
    txt = ""
    expected = ""
    actual = append_todo_count(txt)
    assert actual == expected


def test_markdown_without_todo():
    txt = """\
# project name
Description..."""
    expected = """\
# project name
Description..."""
    actual = append_todo_count(txt)
    assert actual == expected
