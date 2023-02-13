from note import Note
from  notes_db import Notes_db


def add_note(db: Notes_db):
    header = input('Введите заголовок заметки: ')
    body = input('Введите тело заметки: ')
    db.add_note(Note(header, body))

def del_note(db: Notes_db):
    while True:
        try:
            note_id = int(input('Введите номер заметки для удаления: '))
        except ValueError:
            print("Не верно введена команда")
            continue
        break

    db.del_note(note_id)

def edit_note(db: Notes_db):
    while True:
        try:
            note_id = int(input('Введите номер заметки для редактирования: '))
        except ValueError:
            print("Не верно введена команда")
            continue
        break

    header = input('Введите заголовок заметки: ')
    body = input('Введите тело заметки: ')
    db.edit_note(note_id, header, body)

def exit_notes(db: Notes_db):
    db.save_notes()
    exit()

def read_note(db: Notes_db):
    while True:
        try:
            com = int(input('Введите номер заметки для просмотра, либо "0" для вывода всех заметок: '))
        except ValueError:
            print("Не верно введена команда либо заметки с таким номером не существует")
            continue
        break
    if com == 0:
        db.read_notes()
    else:
        if 0 < com <= len(db.notes):
            print(db.notes[com - 1])
        else:
            print("Не верно введена команда")
