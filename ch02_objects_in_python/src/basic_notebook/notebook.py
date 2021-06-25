from typing import List
from typing import Optional

from basic_notebook.note import Note


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags="") -> None:
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id) -> Optional[Note]:
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note

    def modify_memo(self, note_id, memo) -> bool:
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags) -> bool:
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def search(self, filter) -> List[Note]:
        return [note for note in self.notes if note.match(filter)]
