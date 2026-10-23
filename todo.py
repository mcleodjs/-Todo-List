

from pathlib import Path

from rich.console import Console
from rich.markup import escape
from rich.panel import Panel
from rich.table import Table

console = Console()

# The list is saved in a text file next to this script, one task per line.
FILE_PATH = Path(__file__).with_name("YourTodoList.txt")

MENU = """
[bold]What would you like to do?[/bold]
  [cyan][1][/cyan] Add an item
  [cyan][2][/cyan] Remove an item
  [cyan][3][/cyan] View your list
  [cyan][4][/cyan] Search your list
  [cyan][5][/cyan] Save and quit
  [cyan][6][/cyan] Quit without saving
"""


def load_list():
    """Return the saved tasks, or an empty list if there is no save file yet."""
    if not FILE_PATH.exists():
        return []
    with open(FILE_PATH, "r") as file:
        return [line.strip() for line in file if line.strip()]


def save_list(todolist):
    """Write every task to the save file, one per line."""
    with open(FILE_PATH, "w") as file:
        for item in todolist:
            file.write(f"{item}\n")


def show_list(todolist, title="Your list"):
    """Print the tasks as a numbered table."""
    table = Table(title=title, title_style="bold blue")
    table.add_column("#", justify="right", style="cyan")
    table.add_column("Task")
    for number, item in enumerate(todolist, 1):
        table.add_row(str(number), escape(item))
    console.print(table)


def ask_for_number(prompt, highest):
    """Keep asking until the user types a whole number from 1 to highest."""
    while True:
        answer = input(prompt)
        if answer.isdigit() and 1 <= int(answer) <= highest:
            return int(answer)
        console.print(f"[red]Please enter a number from 1 to {highest}.[/red]")


def add_item(todolist):
    item = input("Add item: ").strip()
    if not item:
        console.print("[red]Nothing was added because the item was empty.[/red]")
        return
    todolist.append(item)
    console.print(f"[green]✓ '{escape(item)}' added![/green]")


def remove_item(todolist):
    if not todolist:
        console.print("[yellow]Your list is empty, nothing to remove![/yellow]")
        return
    show_list(todolist)
    number = ask_for_number("\nEnter the number of the item to remove: ", len(todolist))
    removed = todolist.pop(number - 1)
    console.print(f"[green]✓ '{escape(removed)}' removed![/green]")


def search_items(todolist):
    search = input("What are you searching for? ").strip().lower()
    matches = [item for item in todolist if search in item.lower()]
    if matches:
        show_list(matches, title=f"Results for '{escape(search)}'")
    else:
        console.print("[yellow]Task not found.[/yellow]")


def main():
    console.print(Panel("[bold blue]MY TO-DO LIST[/bold blue]", expand=False))

    todolist = load_list()
    if todolist:
        count = len(todolist)
        console.print(f"Welcome back! You have {count} item{'s' if count != 1 else ''} in your list.")
    else:
        console.print("Starting a fresh list!")

    while True:
        console.print(MENU)
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_item(todolist)
        elif choice == "2":
            remove_item(todolist)
        elif choice == "3":
            if todolist:
                show_list(todolist)
            else:
                console.print("[yellow]Your list is empty![/yellow]")
        elif choice == "4":
            search_items(todolist)
        elif choice == "5":
            save_list(todolist)
            console.print("[green]Your list has been saved! Goodbye![/green]")
            break
        elif choice == "6":
            console.print("Goodbye! Your list was NOT saved.")
            break
        else:
            console.print("[red]Please choose a number from 1 to 6.[/red]")


if __name__ == "__main__":
    main()
