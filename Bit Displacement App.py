import customtkinter as ctk
import tkinter as tk
import math

ctk.set_appearance_mode("light")


class App:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry("300x400")
        self.master.resizable(False, False)
        self.master.wm_title("Bit Displacement App")

        # Create Entry
        self.entry1 = ctk.CTkEntry(
            self.master,
            placeholder_text="BH to Bit Length",
            font=("Helvetica bold", 12),
        )
        self.entry1.place(relx=0.5, rely=0.2, anchor="center")

        self.entry2 = ctk.CTkEntry(
            self.master,
            placeholder_text="Motor BH Angle",
            font=("Helvetica bold", 12),
        )
        self.entry2.place(relx=0.5, rely=0.4, anchor="center")

        # Creating Label
        self.label1 = ctk.CTkLabel(self.master, text="", font=("Helvetica bold", 20))

        self.label2 = ctk.CTkLabel(self.master, text="", font=("Helvetica bold", 20))

        self.label3 = ctk.CTkLabel(
            self.master,
            text="* Enter Bit To Bend Lenght (ft)",
            font=("Helvetica bold", 12),
        )
        self.label3.place(relx=0.5, rely=0.3, anchor="center")

        self.label4 = ctk.CTkLabel(
            self.master, text="* Enter Bend Housing Angle", font=("Helvetica bold", 12)
        )
        self.label4.place(relx=0.5, rely=0.5, anchor="center")

        self.result = ctk.CTkLabel(self.master, text="", font=("Helvetica bold", 15))
        self.result.place(relx=0.5, rely=0.6, anchor="center")

        # Creating Button
        self.button = ctk.CTkButton(
            self.master, text="Calculate", command=self.calculate, corner_radius=20
        )
        self.button.place(relx=0.5, rely=0.7, anchor="center")

        self.reset_button: ctk.CTkButton | None = None

    def calculate(self):
        try:
            a = float(self.entry1.get())
            b = float(self.entry2.get())
            c = math.sin(math.radians(b))
            if a > 10 or b > 3.1:
                error_messagebox = tk.messagebox.showinfo(
                    "ERROR", message="Please enter a valid number"
                )  # Pop up messagebox
            else:
                displacement = round(12 * a * c, 2)
                displacement = self.result.configure(text=f"BD {displacement} in")

                if displacement == None:
                    self.reset_button = ctk.CTkButton(
                        self.master,
                        text="Reset",
                        command=self.reset,
                        corner_radius=20,
                        fg_color="red",
                        hover_color="darkred",
                    )
                    self.reset_button.place(relx=0.5, rely=0.8, anchor="center")
        except Exception as e:
            print("Error:", e)

    def reset(self):
        try:
            self.result == None
            self.entry1.delete(0, "end")
            self.entry2.delete(0, "end")

            self.reset_button.destroy()

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    app = ctk.CTk()
    gui = App(master=app)
    app.mainloop()
