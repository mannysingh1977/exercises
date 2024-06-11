import pytest
from datetime import date, timedelta
from calendars import CalendarStub
from tasks import Task, Tasklist

def test_creation():
    today = date(2000, 1, 1)
    calendar = CalendarStub(today)

    sut = Tasklist(calendar)

    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks

def test_adding_task_with_due_day_in_future():
    today = date(2000, 1, 1)
    tomorrow = today + timedelta(days=1)
    calendar = CalendarStub(today)
    task = Task('programming', tomorrow)
    sut = Tasklist(calendar)

    sut.add_task(task)

    assert 1 == len(sut)
    assert [task] == sut.due_tasks

def test_adding_task_with_due_day_in_past():
    today = date(2000, 1, 1)
    yesterday  = today - timedelta(days=1)
    calendar = CalendarStub(today)
    task = Task('programming 1', yesterday)
    sut = Tasklist(calendar)

    with pytest.raises(RuntimeError):
        sut.add_task(task)
    
    assert 0 == len(sut)

def test_task_becomes_finished():
    today = date(2000, 1, 1)
    tomorrow = today + timedelta(days=1)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    sut = Tasklist(calendar)
    sut.add_task(task)

    task.finished = True

    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
