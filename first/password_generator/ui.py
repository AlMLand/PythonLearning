import tkinter as tk

from first.password_generator.generator import Generator


class GeneratorUI:

    def __init__(self):
        self.root = self._create_root()
        self.entry = self._create_entry()
        self.uppercase = self._create_checkbox("include uppercase letters?")
        self.lowercase = self._create_checkbox("include lowercase letters?")
        self.digits = self._create_checkbox("include digits?")
        self.special_chars = self._create_checkbox("include special chars?")
        self.result_text = self._create_text_area()

    @staticmethod
    def _create_root():
        root = tk.Tk()
        root.geometry("400x300")
        root.title("password generator")
        return root

    def start(self):
        self.root.mainloop()

    def _create_text_area(self):
        result_text = tk.Text(self.root, wrap="word", height=5, state="disabled")
        result_text.pack()
        return result_text

    def _create_checkbox(self, text):
        bool_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, text=text, variable=bool_var).pack()
        return bool_var

    def _calculate_work(self):
        length: int = int(self.entry.get())
        uppercase: bool = self.uppercase.get()
        lowercase: bool = self.lowercase.get()
        digits: bool = self.digits.get()
        special_chars: bool = self.special_chars.get()

        generator = Generator(length, uppercase, lowercase, digits, special_chars)
        password = generator.create_password()

        self._set_text(password)

    def _set_text(self, text: str):
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, text)
        self.result_text.config(state="disabled")

    def _create_entry(self):
        tk.Label(self.root, text="enter length").pack()

        entry = tk.Entry(self.root)
        entry.pack()

        tk.Button(self.root, text="get", command=self._calculate_work).pack()

        return entry
