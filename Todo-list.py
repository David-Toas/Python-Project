from tkinter import *
from tkinter import simpledialog, messagebox

"""Initialize the main window"""
root = Tk()
root.title("Python Project - Todo List")
root.geometry("500x500")

"""Set the background color for the root window"""
root.configure(bg="#646683")


"""Frame for tasks and scrollbar"""
task_frame = Frame(root,  bg="#646683")
task_frame.pack(pady=10, padx=5, fill=BOTH, expand=True)

"""Canvas and scrollbar for scrolling tasks"""
canvas = Canvas(task_frame, bg="#646683")
scrollbar = Scrollbar(task_frame, orient="vertical", command=canvas.yview, bg="#646683")
scrollable_frame = Frame(canvas, bg="#646683")

"""Bind the scrollable frame to adjust the scroll region"""
scrollable_frame.bind(
    "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

"""Create a window within the canvas to hold the tasks"""
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

"""Pack the canvas and scrollbar"""
canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

"""Entry box for adding new tasks"""
entry_box = Entry(root, font=("Roboto", 10), width=25, )
entry_box.pack(pady=10)

"""List to store tasks"""
tasks = []

"""Function to add a task"""
def add_task():
    """Get and strip task input"""
    task = entry_box.get().strip()
    """Only proceed if task is not empty"""
    if task:
        """Create a frame to hold the task"""
        task_frame = Frame(scrollable_frame, bg="#646683", pady=5)
        task_frame.pack(fill=X)
        """Create a checkbox for the task completion"""
        var = IntVar()
        check = Checkbutton(task_frame, variable=var,
                            command=lambda: update_task_style(label, var), bg="#646683")
        check.pack(side=LEFT)
        """Create a label for the task text"""
        label = Label(task_frame, text=task, font=(
            "Roboto", 15), bg="#646683", wraplength=400)
        label.pack(side=LEFT, fill=X, expand=True)
        """Add the task to the tasks list"""
        tasks.insert(0,(task_frame, var, label))
        """Clear the input box after adding"""
        entry_box.delete(0, END)


"""Function to update the task's style (strikethrough when completed)"""
def update_task_style(label, var):
    """Update the task's appearance when its checkbox is toggled."""
    label.config(
        fg="white" if var.get() else "black",
        bg="green" if var.get() else "#646683",
        font=("Roboto", 15, "overstrike" if var.get() else "normal")
    )


"""function to delete task"""
def delete_task():
    """Delete checked tasks after confirmation."""
    checked_tasks = [task for task in tasks if task[1].get()]
    if checked_tasks:
        # Proceed only if tasks are checked
        if len(checked_tasks) == 1:
            message = f"Are you sure you want to delete the task: '{checked_tasks[0][2]['text']}'?"
        else:
            message = f"Are you sure you want to delete {len(checked_tasks)} tasks?"
        
        # Confirm before deleting
        if messagebox.askyesno("Delete Task(s)", message):
            for task_frame, var, label in checked_tasks:
                # Remove the task from the UI
                task_frame.destroy()
                # Remove it from the list
                tasks.remove((task_frame, var, label))
    else:
        messagebox.showinfo("No Tasks Selected", "Please select a task to delete.")


"""Function to edit a checked task"""
def edit_task():
    for task_frame, var, label in tasks:
        """Only allow editing if task is checked"""
        if var.get():
            old_text = label.cget("text")
            new_text = simpledialog.askstring(
                "Edit Task", "Edit your task:", initialvalue=old_text)

            if new_text:
                """Update the task with new text"""
                label.config(text=new_text)
                """Uncheck after editing"""
            var.set(0)
            update_task_style(label, var)
            """Stop after the first checked task is edited"""
            break


"""Button frame for holding action buttons"""
button_frame = Frame(root, bg="#646683")
button_frame.pack(pady=20)

"""Add task, delete task, and edit task buttons"""
Button(button_frame, text="Add", command=add_task,
       bg="green", fg="white").grid(row=0, column=0, padx=5)
Button(button_frame, text="Delete", command=delete_task,
       bg="red", fg="white").grid(row=0, column=1, padx=5)
Button(button_frame, text="Edit", command=edit_task,
       bg="#ffbf00", fg="black").grid(row=0, column=2, padx=5)

"""Bind the Enter key to trigger the add_task function"""
entry_box.bind('<Return>', lambda e: add_task())

"""Start the main loop"""
root.mainloop()


"""Final Project: Todo List Application
 Objective:

 Develop a Todo List application with a focus on creating an intuitive and user-friendly interface. The application should allow users to manage their tasks effectively.

 Requirements:

 1. Task Management:
 - Add Tasks: Users should be able to add new tasks to their list. ✅
 - Edit Tasks: Users should be able to edit existing tasks.✅
 - Delete Tasks: Users should be able to remove tasks from their list.✅
 - Mark Tasks: Users should be able to mark tasks as completed or pending.

 2. User Interface:
 - Design: Create a clean, organized, and visually appealing UI.✅
 - Libraries: Use UI libraries such as Tkinter to build your interface.✅
 - Elements: Include essential UI elements such as buttons ✅, text entry fields ✅, and checkboxes✅.

 3. Additional Features (Optional but encouraged):
 - Task Categories: Allow users to categorize tasks (e.g., Work, Personal).
 - Due Dates: Provide functionality to set and view due dates for tasks.
 - Search Functionality: Implement a search feature to find tasks quickly.
 - Data Persistence: Save tasks to a file or database so that they persist between sessions.

 Evaluation Criteria:
 - Functionality: The application should meet the basic requirements and handle edge cases effectively.✅
 - Usability: The user interface should be intuitive and easy to navigate.✅
 - Design: Pay attention to visual design and user experience.✅
 - Code Quality: Write clean, readable, and well-documented code. ✅"""
