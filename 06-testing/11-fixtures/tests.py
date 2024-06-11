import pytest
from datetime import date, timedelta
from calendars import CalendarStub
from tasks import Task, Tasklist

@pytest.fixture
def today():
    return date(2000, 1, 1)

@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)

@pytest.fixture
def yesterday(today):
    return today - timedelta(days=1)

@pytest.fixture
def calendar(today):
    return CalendarStub(today)

@pytest.fixture
def sut(calendar):
    return Tasklist(calendar)

def test_creation(sut):
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks

def test_adding_task_with_due_day_in_future(sut, tomorrow):

    task = Task('programming', tomorrow)

    sut.add_task(task)

    assert 1 == len(sut)
    assert [task] == sut.due_tasks

def test_adding_task_with_due_day_in_past(sut, yesterday):

    task = Task('programming 1', yesterday)

    with pytest.raises(RuntimeError):
        sut.add_task(task)
    
    assert 0 == len(sut)

def test_task_becomes_finished(sut, tomorrow):
    task = Task('description', tomorrow)
    sut.add_task(task)

    task.finished = True

    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
