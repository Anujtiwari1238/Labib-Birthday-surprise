import tkinter as tk
import random

BG_PINK = "#FFC0CB"
BG_GOLD = "#FFD700"
RIBBON_COLOR = "#8B0000"
TEXT_COLOR = "#4B0082"
UNWRAPPED_COLOR = "#FF69B4"

class BirthdayPresentGame(tk.Tk):
    def __init__(self, recipient_name="Labib"):
        super().__init__()
        self.recipient_name = recipient_name
        self.title(f"🎁 A Special Gift for {self.recipient_name}! 🎁")
        self.geometry("750x550")
        self.config(bg=BG_PINK)
        self.resizable(False, False)

        self.center_window()

        self.winning_sections = set(random.sample(range(12), 3))
        self.unwrapped_sections = set()
        self.is_won = False

        self.create_widgets()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'+{x}+{y}')

    def create_widgets(self):
        tk.Label(
            self,
            text=f"Happy Birthday, {self.recipient_name}! Unwrap the Present!",
            font=("Georgia", 22, "bold italic"),
            bg=BG_GOLD,
            fg="white",
            relief=tk.RAISED,
            bd=5
        ).pack(fill='x', ipady=10)

        self.progress_label = tk.Label(
            self,
            text="Ribbon Pieces Unwrapped: 0 of 3",
            font=("Arial", 16),
            bg=BG_PINK,
            fg=TEXT_COLOR
        )
        self.progress_label.pack(pady=15)

        grid_frame = tk.Frame(self, bg=BG_PINK)
        grid_frame.pack(pady=10)

        self.buttons = []
        for i in range(12):
            btn = tk.Button(
                grid_frame,
                text="🎀 Unwrap 🎀",
                font=("Arial", 10, "bold"),
                width=12,
                height=4,
                bg=RIBBON_COLOR,
                fg="white",
                activebackground=UNWRAPPED_COLOR,
                command=lambda i=i: self.section_click(i)
            )
            row = i // 4
            col = i % 4
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(btn)

    def section_click(self, section_id):
        if self.is_won:
            return

        if section_id in self.winning_sections and section_id not in self.unwrapped_sections:
            self.unwrapped_sections.add(section_id)
            self.buttons[section_id].config(
                text="UNWRAPPED! ✨",
                bg=BG_GOLD,
                fg=TEXT_COLOR,
                relief=tk.SUNKEN,
                state=tk.DISABLED
            )
            self.update_progress()

            if len(self.unwrapped_sections) == 3:
                self.is_won = True
                self.show_winning_popup()

        elif section_id not in self.unwrapped_sections:
            self.buttons[section_id].config(text="Try Again!", bg="#FFDAB9")
            self.buttons[section_id].after(700, lambda: self.buttons[section_id].config(text="🎀 Unwrap 🎀", bg=RIBBON_COLOR))

    def update_progress(self):
        count = len(self.unwrapped_sections)
        self.progress_label.config(text=f"Ribbon Pieces Unwrapped: {count} of 3")

    def show_winning_popup(self):
        self.withdraw()

        winner_window = tk.Toplevel(self)
        winner_window.title("HAPPY BIRTHDAY!!!")
        winner_window.attributes('-fullscreen', True)
        winner_window.config(bg=UNWRAPPED_COLOR)

        tk.Label(
            winner_window,
            text=f"CONGRATULATIONS, {self.recipient_name}!",
            font=("Arial", 35, "bold"),
            bg=UNWRAPPED_COLOR,
            fg="white"
        ).pack(pady=(100, 20))

        tk.Label(
            winner_window,
            text="✨🎊 HAPPY BIRTHDAY! 🎊✨",
            font=("Script MT Bold", 70, "bold"),
            bg=UNWRAPPED_COLOR,
            fg=BG_GOLD
        ).pack(pady=20)

        tk.Label(
            winner_window,
            text="You're the most amazing gift in my life.",
            font=("Times New Roman", 25, "italic"),
            bg=UNWRAPPED_COLOR,
            fg="white"
        ).pack(pady=10)

        tk.Label(
            winner_window,
            text="I love you! 🥰",
            font=("Comic Sans MS", 50, "bold"),
            bg=UNWRAPPED_COLOR,
            fg=BG_PINK
        ).pack(pady=30)

        tk.Button(
            winner_window,
            text="Close & Let's Celebrate! 🎉",
            font=("Arial", 18, "bold"),
            command=self.quit,
            bg="white",
            fg=TEXT_COLOR,
            relief=tk.RAISED,
            bd=5
        ).pack(pady=80)

if __name__ == "__main__":
    app = BirthdayPresentGame(recipient_name="Labib")
    app.mainloop()