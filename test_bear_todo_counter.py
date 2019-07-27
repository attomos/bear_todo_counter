from bear_todo_counter import append_todo_count


def test_simple_todo():
    txt = """\
Tasks
+ Task one
- Task two
- Task three"""
    actual = append_todo_count(txt)
    expected = """\
Tasks [1/3]
+ Task one
- Task two
- Task three"""
    assert actual == expected


def test_todo_with_emoji():
    txt = """\
Tasks 🐻
+ 🌈 Task
- Task two
- Task three"""
    actual = append_todo_count(txt)
    expected = """\
Tasks 🐻 [1/3]
+ 🌈 Task
- Task two
- Task three"""
    assert actual == expected


def test_todo_with_subtasks():
    txt = """\
Tasks 🐻
+ 🌈 Task
- Task two
- Task three
	- subtask 1
	- subtask 2"""
    actual = append_todo_count(txt)
    expected = """\
Tasks 🐻 [1/5]
+ 🌈 Task
- Task two
- Task three
	- subtask 1
	- subtask 2"""
    assert actual == expected


def test_empty_todo():
    txt = """\
Tasks 🙄
+ 
- 
- """  # noqa: W291
    actual = append_todo_count(txt)
    expected = """\
"""
    expected = """\
Tasks 🙄 [1/3]
+ 
- 
- """  # noqa: W291
    assert actual == expected


def test_todo_with_links():
    txt = """\
Tasks 👍
+ https://good-article.com/1
- https://good-article.com/main
	- https://good-article.com/sub1
	+ https://good-article.com/sub2
+ [Working With XML in Scala - DZone Java](https://dzone.com/articles/working-with-xml-in-scala)
+ [Amundsen — Lyft’s data discovery & metadata engine – Lyft Engineering](https://eng.lyft.com/amundsen-lyfts-data-discovery-metadata-engine-62d27254fbb9)"""  # noqa: E501
    actual = append_todo_count(txt)
    expected = """\
Tasks 👍 [4/6]
+ https://good-article.com/1
- https://good-article.com/main
	- https://good-article.com/sub1
	+ https://good-article.com/sub2
+ [Working With XML in Scala - DZone Java](https://dzone.com/articles/working-with-xml-in-scala)
+ [Amundsen — Lyft’s data discovery & metadata engine – Lyft Engineering](https://eng.lyft.com/amundsen-lyfts-data-discovery-metadata-engine-62d27254fbb9)"""  # noqa: E501
    assert actual == expected


def test_todo_with_dashes():
    txt = """\
Tasks with dashes 😂
- - in the beginning of a task
- let's see - in the middle of a task
- what about at the end -
- -
+ - in the beginning of a task
+ let's see - in the middle of a task
+ what about at the end -
+ -"""
    actual = append_todo_count(txt)
    expected = """\
Tasks with dashes 😂 [4/8]
- - in the beginning of a task
- let's see - in the middle of a task
- what about at the end -
- -
+ - in the beginning of a task
+ let's see - in the middle of a task
+ what about at the end -
+ -"""
    assert actual == expected


def test_todo_with_plus_signs():
    txt = """\
Tasks with plus signs 😂
- + in the beginning of a task
- let's see + in the middle of a task
- what about at the end +
- +
+ + in the beginning of a task
+ let's see + in the middle of a task
+ what about at the end +
+ +"""
    actual = append_todo_count(txt)
    expected = """\
Tasks with plus signs 😂 [4/8]
- + in the beginning of a task
- let's see + in the middle of a task
- what about at the end +
- +
+ + in the beginning of a task
+ let's see + in the middle of a task
+ what about at the end +
+ +"""
    assert actual == expected
