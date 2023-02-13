# Напишите проект, содержащий функционал работы с заметками. Программа должна уметь создавать заметку, сохранять её,
# читать список заметок, редактировать заметку, удалять заметку.

import view
from notes_db import Notes_db
import controller as ctr


if __name__ == '__main__':
    ndb = Notes_db()
    ndb.load_notes()

    while True:
        view.print_start_menu()
        com = int(input('Введите команду: '))

        if com == 1:
            ctr.add_note(ndb)
        elif com == 2:
            ctr.del_note(ndb)
        elif com == 3:
            ctr.read_note(ndb)
        elif com == 4:
            ctr.edit_note(ndb)
        elif com == 5:
            ndb.save_notes()
        elif com == 0:
            ctr.exit_notes(ndb)
        else:
            print("Не верно введена команда")