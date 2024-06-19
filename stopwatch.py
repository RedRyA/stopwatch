
import tkinter as tk

 

from datetime import datetime, timedelta
import time
 

class Stopwatch:

    def __init__(self, master):

        self.master = master

        self.running = False

        self.start_time = None

        self.elapsed_time = 0
        # array for file
        self.file_array = []
        # array for display
        self.gui_array = []

       
 
### MAKE SEPERATE FUNCTIONS FOR PROCESSES
       

 

 # Create UI

        self.label = tk.Label(master, text="00:00:00",

                             font=("Helvetica", 48))

        self.label.pack()

 
        # create start button
        self.start_button = tk.Button(master, text="Start",bg='white', command=self.start)

        self.start_button.pack(side="left")

 
 # create stop button
        self.stop_button = tk.Button(master, text="Stop",bg='white', command=self.stop)

        self.stop_button.pack(side="left")

 
 # create reset button
        self.reset_button = tk.Button(master, text="Reset",bg='white', command=self.reset)

        self.reset_button.pack(side="left")

 
# create Times: text
        self.time_label = tk.Label(master, text="Times: ")

        self.time_label.pack(side="bottom")

 
# create time display box
        self.times_listbox = tk.Listbox(master, height=10, width=30)

        self.times_listbox.pack(side="bottom")

# create comment text and comment text holder

        self.comment_label=tk.StringVar()
        self.comment_label.set("Comment")
        self.comment_holder=tk.Label(master,textvariable=self.comment_label)
        self.comment_holder.pack(side='left')


# create comment box
        self.comment_box=tk.Entry(master)

        self.comment_box.pack(side="bottom")

# opens and writes to file
    def file_write(self):
           
            global FILE
            FILE=open(r"time_saver.txt","a")

            date=datetime.now().strftime('%d:%m:%Y')

            FILE.writelines("DATE: "+ date)

            FILE.writelines('\n')
            if len(self.comment_box.get())>0:
                FILE.writelines('Comment: ' )
                FILE.writelines(self.file_array[0])
                FILE.writelines('\n')
                FILE.writelines(self.file_array[1])
            else:

             FILE.writelines(self.file_array)

             FILE.writelines('\n')

    def array_append(self):

        self.file_array.append(f"{self.comment_box.get()}")
        self.file_array.append(f"Start: {start_time_str} - Stop: {stop_time_str}")
           

        self.gui_array.append(f"{self.comment_box.get()}")
        self.gui_array.append(f"Start: {start_time_str} - Stop: {stop_time_str}")

# clear array and comment box
    def  clear_arrBox(self):
        
            self.comment_box.delete(0,tk.END)

            while len(self.file_array) >0:
                
                self.file_array.pop()

            if len(self.gui_array) > 10:

                self.gui_array.pop(0)

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
        # change color of start and stop buttons when stop is clicked
            self.start_button.configure(bg='white')

            self.stop_button.configure(bg='red')

            global  start_time_str
            global  stop_time_str

            start_time_str = self.start_time.strftime('%H:%M:%S')

            stop_time_str = datetime.now().strftime('%H:%M:%S')

            self.array_append()
            self.file_write()
            self.clear_arrBox()

        #clear comment box make a seperate function

            self.comment_box.delete(0,tk.END)

            while len(self.file_array) >0:
                
                self.file_array.pop()

            FILE.close()

    
            self.update_times_listbox()

   


    def update_times_listbox(self):

        self.times_listbox.delete(0, tk.END)

        for time in self.gui_array:

            self.times_listbox.insert(tk.END, time)

           

    def reset(self):

        self.running = False

        self.elapsed_time = 0
       
        
       
        self.label.config(text="00:00:00")

        self.comment_box.delete(0,tk.END)

        self.start_button.configure(bg='white')

        self.stop_button.configure(bg='white')

       


    
        


# Create main window

root = tk.Tk()

root.title("Stopwatch")

 

# Create stopwatch

stopwatch = Stopwatch(root)

 

# Run the application

root.mainloop()

 

 



