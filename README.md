# To-Do List (Python)

A command-line to-do list built in Python. You can add, remove, view and search tasks, and your list is saved to a text file so it is still there the next time you run the program.

## Features

- Add and remove tasks from a numbered list
- View your tasks in a clean table
- Search tasks by keyword (not case-sensitive)
- Save and quit, or quit without saving
- Your list reloads automatically when you start the program
- Handles bad input, like empty tasks or typing letters when a number is expected

## Built with

- Python 3
- [Rich](https://github.com/Textualize/rich) for the styled menus and tables
- File I/O to save the list in `YourTodoList.txt`

## How to run

1. Install Python 3.
2. Install Rich:
   ```
   pip install rich
   ```
3. Run the program:
   ```
   python todo.py
   ```

## Example

```
╭───────────────╮
│ MY TO-DO LIST │
╰───────────────╯
Welcome back! You have 2 items in your list.

What would you like to do?
  [1] Add an item
  [2] Remove an item
  [3] View your list
  [4] Search your list
  [5] Save and quit
  [6] Quit without saving
```

## What I learned

- Working with lists, loops and functions in Python
- Reading and writing files so data stays between runs
- Checking user input so the program does not crash
- Using a library (Rich) to improve a terminal interface

## Next steps

- Add a Tkinter window so it can be used without the terminal
- Mark tasks as done instead of only removing them
