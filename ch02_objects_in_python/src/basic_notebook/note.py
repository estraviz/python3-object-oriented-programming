from datetime import date

# Store the next available id for all new notes
last_id: int = 0


class Note:
    def __init__(self, memo, tags=""):
        self.memo: str = memo
        self.tags: str = tags
        self.creation_date: date = date.today()
        global last_id
        last_id += 1
        self.id: int = last_id

    def match(self, filter):
        return filter in self.memo or filter in self.tags
