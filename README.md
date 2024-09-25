# Todo List Application Using Tkinter

## 1. Overview
This application is a Todo List Manager built using Python and Tkinter for the graphical user interface (GUI). It allows users to:
- Add tasks
- Mark tasks as completed
- Edit existing tasks
- Delete selected tasks

The app offers a simple, user-friendly interface with task management features such as scrolling and interactive buttons.

## 2. Key Features

### 1. Task Addition
- Users can enter tasks through a text input box.
- Tasks are displayed dynamically, and pressing Enter or clicking the Add button will add them to the list.

### 2. Task Completion
- Each task has a checkbox that allows users to mark it as completed.
- Completed tasks are displayed with a strikethrough, and the background changes to green, indicating that the task is done.

### 3. Task Editing
- Users can edit a task by first selecting it (via the checkbox), then clicking the Edit button.
- A dialog box appears, allowing users to update the task's description.

### 4. Task Deletion
- Selected tasks can be deleted by clicking the Delete button.
- A confirmation message appears to ensure tasks aren't accidentally removed.

## 3. User Interface
- **Scroll-Enabled Task List:** The application supports an unlimited number of tasks with a scrollable frame.
- **Minimalist Design:** The background is styled in a calm blue-grey color (#646683), keeping the focus on tasks.
- **Interactive Buttons:** Users can add, edit, and delete tasks via buttons or keyboard shortcuts, making it efficient to use.

## 4. Detailed Walkthrough

### 1. Adding a Task
When a user enters a task and presses Add, it is:
- Displayed in a new task frame with a checkbox and a label.
- Stored internally for future actions (edit/delete).

### 2. Completing a Task
By clicking the checkbox, a task is marked as completed:
- The task's text is crossed out (via strikethrough styling).
- The background changes to green, providing visual feedback.

### 3. Editing a Task
After checking a task, the Edit button allows the user to change its text.
- A popup dialog appears where the user can edit the task.
- Once edited, the task’s checkbox is automatically unchecked.

### 4. Deleting a Task
By selecting one or more tasks and pressing Delete, the user is asked to confirm the action via a dialog box.
- Upon confirmation, the selected tasks are removed from both the display and the internal storage.

## 5. Technical Highlights
- **Tkinter Framework:** Used for building the entire GUI.
- **Canvas and Scrollbar:** The app uses a scrollable canvas to manage multiple tasks within the same window.
- **Dynamic UI Updates:** Tasks are dynamically added, edited, or removed in real-time without needing to restart the application.
- **Event Binding:** The Enter key is bound to the task addition feature, enhancing user interaction.

## 6. Conclusion
This **Todo List application** provides a simple yet powerful way to manage tasks efficiently. It leverages Python's Tkinter library for a clean user interface and features robust task management capabilities like adding, editing, completing, and deleting tasks—all within a responsive and scrollable design.
