import customtkinter as ctk

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('bek calculator')
        self.geometry('320x460')
        self.configure(bg_color='#000000')  

        self.font = ctk.CTkFont('Helvetica', 26, weight='bold')
        self.expr = ''

        self.entry = ctk.CTkEntry(
            self, state=ctk.DISABLED, font=self.font,
            text_color='white', bg_color='#000000', fg_color='#1C1C1E',
            justify='right'
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=12, pady=(15, 10), sticky='we')

        self.create_buttons()

    def create_buttons(self):
        layout = [
            [('7',), ('8',), ('9',), ('+', True)],
            [('4',), ('5',), ('6',), ('-', True)],
            [('1',), ('2',), ('3',), ('/', True)],
            [('CE', False, '#A5A5A5', 'black', self.clear),
             ('0',), ('=', True, '#FF9500', 'white', self.equal),
             ('*', True)],
        ]

        for r, row in enumerate(layout, start=1):
            for c, data in enumerate(row):
                text = data[0]
                is_act = data[1] if len(data) > 1 else False
                bg = data[2] if len(data) > 2 else None
                fg = data[3] if len(data) > 3 else 'white'
                cmd = data[4] if len(data) > 4 else None

                self.add_btn(r, c, text, is_act, bg, fg, cmd)

    def add_btn(self, row, column, text, is_act=False, bg=None, fg='white', command=None):
        # Цвета
        if bg is None:
            bg = '#FF9500' if is_act else '#505050'

        if command is None:
            command = lambda: self.insert(text)

        button = ctk.CTkButton(
            self, text=text, command=command,
            font=self.font, text_color=fg,
            fg_color=bg, hover_color='#FFA733',
            width=70, height=70, corner_radius=35 
        )
        button.grid(row=row, column=column, padx=6, pady=6)

    def insert(self, text):
        operators = '+-*/'
        if text in operators:
            if not self.expr or self.expr[-1] in operators:
                return
        self.entry.configure(state=ctk.NORMAL)
        self.expr += text
        self.entry.delete(0, ctk.END)
        self.entry.insert(0, self.expr)
        self.entry.configure(state=ctk.DISABLED)

    def clear(self):
        self.entry.configure(state=ctk.NORMAL)
        self.entry.delete(0, ctk.END)
        self.expr = ''
        self.entry.configure(state=ctk.DISABLED)

    def equal(self):
        self.entry.configure(state=ctk.NORMAL)
        self.entry.delete(0, ctk.END)
        try:
            result = eval(self.expr)
            self.expr = str(result)
        except:
            self.expr = ''
            result = 'ERROR'
        self.entry.insert(0, str(result))
        self.entry.configure(state=ctk.DISABLED)


if __name__ == '__main__':
    ctk.set_appearance_mode("dark")  
    app = Main()
    app.mainloop()
