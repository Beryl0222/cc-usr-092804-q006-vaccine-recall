"""儿童接种提醒和门诊回执。"""
from dataclasses import dataclass
from datetime import date
@dataclass
class Visit: child: str; visit_date: date; completed: bool; receipt_id: str
class ReminderBook:
    def __init__(self): self.visits = {}; self.sent = set()
    def import_receipt(self, visit): self.visits[visit.receipt_id] = visit
    def next_action(self, child, today):
        rows = [v for v in self.visits.values() if v.child == child]
        if any(v.completed for v in rows): return {'action': 'none', 'reason': '已完成'}
        due = min((v.visit_date for v in rows), default=today)
        return {'action': 'remind', 'due': due.isoformat()}
    def pending(self, today): return [self.next_action(c,today) for c in sorted({v.child for v in self.visits.values()})]
