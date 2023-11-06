import userMenuConsole
import commands

def start():
    while True:
        userMenuConsole.menu_console()
        user_input = input()
        if user_input == '1':
            commands.show("all")
        elif user_input == '2':
            commands.show("ID")
        elif user_input == '3':
            commands.show("date")
        elif user_input == '4':
            commands.show("all")
            commands.change_note()
        elif user_input == '5':
            commands.add_note()
        elif user_input == '6':
            commands.show("all")
            commands.del_notes()
        else:
            print("Программа Журнал заметок завершена")
            break
