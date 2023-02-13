from note import Note
import json


class Notes_db:
    def __init__(self):
        self.notes = []

    def sort_notes_by_date(self):
        self.notes.sort()

    def add_note(self, note: Note):
        self.notes.append(note)

    def del_note(self, note_id: int):
        if 0 <= note_id <= len(self.notes):
            self.notes.pop(note_id - 1)  # because id starts to one
        else:
            print("Заметки с таким номером нет!")

    def read_notes(self):
        if len(self.notes) != 0:
            self.sort_notes_by_date()
            for note in self.notes:
                print(note)
        else:
            print("В базе нет заметок!")

    def save_notes(self):
        dict_notes = []
        for i in self.notes:
            dict_notes.append(i.to_dict())
        with open("data_notes.json", "w") as dn:
            json.dump(dict_notes, dn)

    def load_notes(self):
        try:
            with open("data_notes.json", "r") as dn:
                dict_notes = json.load(dn)
        except FileNotFoundError:
            return

        for dict_note in dict_notes:
            nt = Note(dict_note["header"], dict_note["body"])
            nt.note_id = dict_note["note_id"]
            nt.date = dict_note["date"]
            self.notes.append(nt)

    def edit_note(self, note_id: int, header, body):
        if 0 <= note_id <= len(self.notes):
            self.notes[note_id - 1].editing(header, body)  # because id starts to one
        else:
            print("Заметки с таким номером нет!")
