from datetime import date
from calendars import CalendarStub
from tasks import Task, Tasklist

def test_task_becomes_overdue():
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1 ,2)
    next_week = date(2000, 1, 8)
    calendar = CalendarStub(today)
    task = Task('finish programming 2', tomorrow)
    task_list = Tasklist(calendar)

    task_list.add_task(task)
    calendar.today = next_week

    assert [task] == task_list.overdue_tasks