from datetime import date

def solve(value):
    return (lambda w: {"year": w.year, "week": w.week, "weekday": w.weekday})(date.fromisoformat(value).isocalendar())
