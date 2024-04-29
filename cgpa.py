from tkinter import Tk, Button, Label, LabelFrame,END, Entry, messagebox
from tkinter import ttk

class main_code:
    def __init__(self,root):
        self.root = root
        self.heading()
        self.regulation_frame()
        self.result_entry()
        self.show_result_frame()
        self.reset_data()

    def heading(self):
        header = Label(self.root, text="CGPA \n Calculator", font='helvetica 20')
        header.grid(row=0, column=0, sticky='ewns')
    
    def regulation_frame(self):
        regulation = LabelFrame(self.root,text="Regulation")
        regulation.grid(row=1,column=0)
        self.regulation_combobox = ttk.Combobox(regulation, values=[2010,2016,2022])
        self.regulation_combobox.grid(row=0,column=0, padx=5,pady=5, sticky='ewns')

    def result_entry(self):
        self.result_entry_frame = LabelFrame(self.root)
        self.result_entry_frame.grid(row=2,column=0, padx=10,pady=10)
        self.first_semester = Label(self.result_entry_frame,text="1st semester GPA: ")
        self.first_semester.grid(row=0, column=0)
        self.first_semester_entry = Entry(self.result_entry_frame)
        self.first_semester_entry.grid(row=0,column=1)

        self.second_semester = Label(self.result_entry_frame,text="2nd semester GPA: ")
        self.second_semester.grid(row=1, column=0)
        self.second_semester_entry = Entry(self.result_entry_frame)
        self.second_semester_entry.grid(row=1,column=1)

        self.third_semester = Label(self.result_entry_frame,text="3rd semester GPA: ")
        self.third_semester.grid(row=2, column=0)
        self.third_semester_entry = Entry(self.result_entry_frame)
        self.third_semester_entry.grid(row=2,column=1)

        self.fourth_semester = Label(self.result_entry_frame,text="4th semester GPA: ")
        self.fourth_semester.grid(row=3, column=0)
        self.fourth_semester_entry = Entry(self.result_entry_frame)
        self.fourth_semester_entry.grid(row=3,column=1)

        self.fifth_semester = Label(self.result_entry_frame,text="5th semester GPA: ")
        self.fifth_semester.grid(row=4, column=0)
        self.fifth_semester_entry = Entry(self.result_entry_frame)
        self.fifth_semester_entry.grid(row=4,column=1)

        self.sixth_semester = Label(self.result_entry_frame,text="6th semester GPA: ")
        self.sixth_semester.grid(row=5, column=0)
        self.sixth_semester_entry = Entry(self.result_entry_frame)
        self.sixth_semester_entry.grid(row=5,column=1)

        self.seventh_semester = Label(self.result_entry_frame,text="7th semester GPA: ")
        self.seventh_semester.grid(row=6, column=0)
        self.seventh_semester_entry = Entry(self.result_entry_frame)
        self.seventh_semester_entry.grid(row=6,column=1)

        self.eighth_semester = Label(self.result_entry_frame,text="8th semester GPA: ")
        self.eighth_semester.grid(row=7, column=0)
        self.eighth_semester_entry = Entry(self.result_entry_frame)
        self.eighth_semester_entry.grid(row=7,column=1)

        for widget in self.result_entry_frame.winfo_children():
            widget.grid_configure(padx=5,pady=3)

        Button(self.result_entry_frame, text="CALCULATE",bg='light green',font="halvetica 10",command=self.regulation_validation).grid(row=8, column=0,sticky='news',pady=5)
        Button(self.result_entry_frame, text="RESET", bg="red",font="halvetica 12", command=self.reset_data).grid(row=9, column=0, sticky='news')


    def show_result_frame(self):
        self.show_result= Label(self.result_entry_frame,text='',fg='dark green',font="halvetica 14")
        self.show_result.grid(row= 8,column=1, sticky='news')

    def regulation_validation(self):
        if self.regulation_combobox.get():
            if self.regulation_combobox.get() =="2010" or self.regulation_combobox.get() ==  "2016" or self.regulation_combobox.get() == "2022":
                self.result_validation()
            else:
                messagebox.showwarning(title='Error', message='Please select a valid regulation.')
        else:
            messagebox.showwarning(title='Error', message='You have must select regulation.')

    
    def result_validation(self):
        self.first_semester_entry.get()
        self.second_semester_entry.get()
        self.third_semester_entry.get()
        self.fourth_semester_entry.get()
        self.fifth_semester_entry.get()
        self.sixth_semester_entry.get()
        self.seventh_semester_entry.get()
        self.eighth_semester_entry.get()
    
        if self.first_semester_entry.get() and self.second_semester_entry.get() and self.third_semester_entry.get() and self.fourth_semester_entry.get() and self.fifth_semester_entry.get() and self.sixth_semester_entry.get() and self.seventh_semester_entry.get() and self.eighth_semester_entry.get():
            def check_final_result(result):
                characters_in_result = 0
                numbers = 0
                special_character_in_result = 0
                for i in range(0,len(result)):
                        if (result[i]>= 'a' and result[i]<= 'z' )or (result[i]>= 'A' and result[i]<= 'Z') :
                                characters_in_result = characters_in_result + 1
                        elif result[i]>= '0' and result[i]<= '9' or result[i] == '.':
                                numbers = numbers + 1
                        else:
                                special_character_in_result = special_character_in_result +1
                        i = i+1
                if characters_in_result > 0 or special_character_in_result >0:
                        return 1
                else:
                        return 0
            if check_final_result(self.first_semester_entry.get()) == 1:
                messagebox.showwarning(title="Error", message="First semester result is invalid.")
            elif check_final_result(self.second_semester_entry.get()) == 1:
                messagebox.showwarning(title="Error", message="Second semester result is invalid.")
            elif check_final_result(self.third_semester_entry.get()) == 1:
                messagebox.showwarning(title="Error", message="third semester result is invalid.")
            elif check_final_result(self.fourth_semester_entry.get()) == 1:
                messagebox.showwarning(title="Error", message="fourth semester result is invalid.")
            elif check_final_result(self.fifth_semester_entry.get()) == 1:
                messagebox.showwarning(title="Error", message="Fifth semester result is invalid.")
            elif check_final_result(self.sixth_semester_entry.get()) == 1:
                messagebox.showwarning(title="Error", message="Sixth semester result is invalid.")
            elif check_final_result(self.seventh_semester_entry.get()) == 1:
                messagebox.showwarning(title="Error", message="Seventh semester result is invalid.")
            elif check_final_result(self.eighth_semester_entry.get()) == 1:
                messagebox.showwarning(title="Error", message="Eighth semester result is invalid.")
            else:
                self.first_semester_result = float(self.first_semester_entry.get())
                self.second_semester_result = float(self.second_semester_entry.get())
                self.third_semester_result = float(self.third_semester_entry.get())
                self.fourth_semester_result = float(self.fourth_semester_entry.get())
                self.fifth_semester_result = float(self.fifth_semester_entry.get())
                self.sixth_semester_result = float(self.sixth_semester_entry.get())
                self.seventh_semester_result = float(self.seventh_semester_entry.get())
                self.eighth_semester_result = float(self.eighth_semester_entry.get())
                if (self.first_semester_result<0 or self.first_semester_result>4.00):
                    messagebox.showwarning(title="Error", message="First semester result is invalid.")
                elif self.second_semester_result<0 or self.second_semester_result>4.00:
                    messagebox.showwarning(title="Error", message="Second semester result is invalid.")
                elif self.third_semester_result<0 or self.third_semester_result>4.00:
                    messagebox.showwarning(title="Error", message="Third semester result is invalid.")
                elif self.fourth_semester_result<0 or self.fourth_semester_result>4.00:
                    messagebox.showwarning(title="Error", message="Fourth semester result is invalid.")
                elif self.fifth_semester_result<0 or self.fifth_semester_result>4.00:
                    messagebox.showwarning(title="Error", message="Fifth semester result is invalid.")
                elif self.sixth_semester_result<0 or self.sixth_semester_result>4.00:
                    messagebox.showwarning(title="Error", message="Sixth semester result is invalid.")
                elif self.seventh_semester_result<0 or self.seventh_semester_result>4.00:
                    messagebox.showwarning(title="Error", message="Seventh semester result is invalid.")
                elif self.eighth_semester_result<0 or self.eighth_semester_result>4.00:
                    messagebox.showwarning(title="Error", message="Eighth semester result is invalid.") 
                else:
                    self.calculate_cgpa()
        else: 
            messagebox.showwarning(title="Error",message="Please fill up all semesters result.")    

    def calculate_cgpa(self):
        self.final_result_for_2010 = (self.first_semester_result *(5/100)) + (self.second_semester_result *(5/100)) + (self.third_semester_result *(5/100)) + (self.fourth_semester_result * (15/100)) + (self.fifth_semester_result * (15/100)) + (self.sixth_semester_result *(20/100)) + (self.seventh_semester_result * (25/100)) + (self.eighth_semester_result * (10/100))
        self.final_result_for_2016 = (self.first_semester_result *(5/100)) + (self.second_semester_result *(5/100)) + (self.third_semester_result *(5/100)) + (self.fourth_semester_result * (10/100)) + (self.fifth_semester_result * (15/100)) + (self.sixth_semester_result *(20/100)) + (self.seventh_semester_result * (25/100)) + (self.eighth_semester_result * (15/100))
        self.final_result_for_2022 = (self.first_semester_result *(5/100)) + (self.second_semester_result *(5/100)) + (self.third_semester_result *(10/100)) + (self.fourth_semester_result * (10/100)) + (self.fifth_semester_result * (20/100)) + (self.sixth_semester_result *(20/100)) + (self.seventh_semester_result * (20/100)) + (self.eighth_semester_result * (10/100))
        if self.regulation_combobox.get() == "2010":
            self.show_result['text'] = "CGPA = {}".format(round(self.final_result_for_2010,2))
        elif self.regulation_combobox.get() == "2016":
            self.show_result['text'] = "CGPA = {}".format(round(self.final_result_for_2016,2))
        elif self.regulation_combobox.get() == "2022":
            self.show_result['text'] = "CGPA = {}".format(round(self.final_result_for_2022,2))

    def reset_data(self):
        self.first_semester_entry.delete(0, END)
        self.second_semester_entry.delete(0,END)
        self.third_semester_entry.delete(0,END)
        self.fourth_semester_entry.delete(0, END)
        self.fifth_semester_entry.delete(0,END)
        self.sixth_semester_entry.delete(0,END)
        self.seventh_semester_entry.delete(0,END)
        self.eighth_semester_entry.delete(0,END)
        self.show_result['text'] = ""
        
if __name__ == '__main__':
    root = Tk()
    root.title("CGPA Calculator")
    root.resizable(height=False,width=False)
    application = main_code(root)
    root.mainloop()