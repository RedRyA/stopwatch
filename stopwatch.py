import tkinter as tk

import openpyxl

from datetime import datetime, timedelta

'''''

Possible SQL Server

 

SERVER = '99NETWORKING07'

DATABASE = 'Time_Clock'

USERNAME = 'IBC'

PASSWORD =' '

 

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};Trusted_Connection=no'

conn = pyodbc.connect(connectionString)

 

sql = "INSERT INTO dbo.time_store (date, comment) VALUES (%s, %s)"

val=("Monday","Test")

cursor=conn.cursor()

cursor.execute(sql,val)

'''

class Stopwatch:

 

    def __init__(self, master):

        self.master = master

        self.running = False

        self.start_time = None

        self.elapsed_time = 0

        self.file_arr = []

        self.gui_arr = []

 

       

 

        global wb

        wb = openpyxl.load_workbook('time_save.xlsx')

        global sheet

        sheet = wb.active

     

 # Create UI

        self.label = tk.Label(master, text="00:00:00",

                             font=("Helvetica", 48))

       

       

        self.label.pack()

 

        self.start_button = tk.Button(master, text="Start",bg='white', command=self.start)

        self.start_button.pack(side="left")

 

        self.stop_button = tk.Button(master, text="Stop",bg='white', command=self.stop)

        self.stop_button.pack(side="left")

 

        self.reset_button = tk.Button(master, text="Reset",bg='white', command=self.reset)

        self.reset_button.pack(side="left")

 

        self.time_label = tk.Label(master, text="Times: ")

        self.time_label.pack(side="bottom")

 

        self.times_listbox = tk.Listbox(master, height=10, width=30)

        self.times_listbox.pack(side="bottom")

 

        self.comment_text=tk.StringVar()

        self.comment_text.set("Comment")

        self.comment=tk.Label(master,textvariable=self.comment_text)

        self.comment.pack(side='left')

 

        self.comment_box=tk.Entry(master,width=30)

        self.comment_box.pack(side='bottom')

       

       

 

    def update(self):

        if self.running:

            now = datetime.now()

            self.elapsed_time = (now - self.start_time).total_seconds()

            self.label.config(text=self.format_time(self.elapsed_time))

            self.master.after(1000, self.update)

           

    def format_time(self, elapsed):

        hours, remainder = divmod(elapsed, 3600)

        minutes, seconds = divmod(remainder, 60)

        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

 

    def start(self):

        if not self.running:

            self.running = True

            self.start_time = datetime.now() - timedelta(seconds=self.elapsed_time)

            self.start_button.configure(bg='green')

            self.stop_button.configure(bg='white')

            self.update()

       

     

 

 

    def stop(self):

        if self.running:

            self.running = False

            self.start_button.configure(bg='white')

            self.stop_button.configure(bg='red')

 

            start_time_str = self.start_time.strftime('%H:%M:%S')

            stop_time_str = datetime.now().strftime('%H:%M:%S')

 

           # start_time =  self.file_arr.append(f"{start_time_str}")

            #stop_time = self.file_arr.append(f"{stop_time_str}")

            comment_add = f"{self.comment_box.get()}"

           

            self.gui_arr.append(f"{self.comment_box.get()}")

            self.gui_arr.append(f"Start: {start_time_str} - Stop: {stop_time_str}")

         

            #FILE=open(r"time_saver.txt","a")

       

            date=datetime.now().strftime('%d:%m:%Y')

            sheet.append([date,comment_add,start_time_str,stop_time_str])

           # FILE.writelines("DATE: "+ date)

            #FILE.writelines('\n')

            #FILE.writelines( self.file_arr)

            #FILE.writelines('\n')

           

            for time in self.file_arr:

                self.file_arr.pop()

            wb.save('time_save.xlsx')

           # FILE.close()

         

 

           

            # Keep only the last 10 times

            if len(self.gui_arr) > 10:

                self.gui_arr.pop(0)

           

            self.update_times_listbox()

 

    def update_times_listbox(self):

        self.times_listbox.delete(0, tk.END)

        for time in self.gui_arr:

            self.times_listbox.insert(tk.END, time)

           

    def reset(self):

        self.running = False

        self.elapsed_time = 0

        self.label.config(text="00:00:00")

        self.start_button.configure(bg='white')

        self.stop_button.configure(bg='white')




# Create main window

root = tk.Tk()

root.title("Stopwatch")

 

# Create stopwatch

stopwatch = Stopwatch(root)

 

# Run the application

root.mainloop()