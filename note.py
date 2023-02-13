from datetime import datetime
import json
from art import text2art


class Note:
    note_id = 1

    def __init__(self, header: str, body: str):
        self.note_id = Note.note_id
        Note.note_id += 1
        self.header = header
        self.body = body
        self.date = str(datetime.now())

    def __str__(self) -> str:
        n_id = text2art(str(self.note_id))
        header = '----- ' + self.header + ' -----\n\n'

        return str(self.date) + '\n' + n_id + header + self.body + '\n\n' + ('*' * 50)

    def __lt__(self, other):
        return self.date > other.date

    def __gt__(self, other):
        return self.date < other.date

    def __le__(self, other):
        return self.date >= other.date

    def __ge__(self, other):
        return self.date <= other.date

    def __eq__(self, other):
        return self.date == other.date

    def to_dict(self):
        return {'note_id': self.note_id, 'header': self.header, 'body': self.body, 'date': self.date}

    def editing(self, header: str, body: str):
        self.header = header
        self.body = body
        self.date = str(datetime.now())
