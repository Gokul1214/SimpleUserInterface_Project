import os
import pygubu
from names_show import ShowGender, Names

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "NAMES.ui")


class NamesApp:
    def __init__(self, parent):
        self.start_ui(parent)
        self.setup_gender_combo()
        self.setup_tree()

    def start_ui(self, parent):
        builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('top_frame', parent)
        builder.connect_callbacks(self)

        self._builder = builder
        self._name_entry = builder.get_object("name_entry", parent)
        self._gender_combo = builder.get_object("gender_combo", parent)
        self._tree = builder.get_object("names_table", parent)

    def setup_tree(self):
        tree = self._tree

        tree.configure(columns = (0, 1, 2, 3, 4))

        tree.heading(0, text='Name', anchor = tk.W)
        tree.heading(1, text = 'Year')
        tree.heading(2, text = 'Gender')
        tree.heading(3, text = 'NameCount')
        tree.heading(4, text = 'Total')

        tree.column(0, width = 250)
        tree.column(1, width = 100)
        tree.column(2, width = 100)
        tree.column(3, width = 100)
        tree.column(4, width = 100)

    def setup_gender_combo(self):
        genders = ShowGender.fetch_gender()
        self._gender_combo['values'] = [ShowGender.GENDER] + [gender.get_gender() for gender in genders]
        self._gender_combo.current(0)

    def gender_selected(self, event):
        print("Gender changed:", self._gender_combo.get())
        self.fetch_names()

    @classmethod
    def names_to_tuple(self, name):
        return (
            name.get_name(),
            name.get_year(),
            name.get_gender(),
            name.get_nameCount(),
            name.get_total()
        )

    def name_change(self, event):
        print("Name changed:", self._name_entry.get())
        self.fetch_names()

    def fetch_names(self):
        gender = self._gender_combo.get()
        name_entry = self._name_entry.get()

        names = Names.fetch_names(gender, name_entry)

        for i in self._tree.get_children():
            self._tree.delete(i)

        for i in range(len(names)):
            val = names[i]
            self._tree.insert('', 'end', values = NamesApp.names_to_tuple(val))
    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.title("Names manager")
    app = NamesApp(root)
    app.run()