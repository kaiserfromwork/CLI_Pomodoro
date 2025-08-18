#!/home/kaiser/projects/CLI_Pomodoro/venv/bin/python

import sys
import time
import subprocess

from quotes import get_quote


def notify_user(message: str = "This is a notification.\n") -> None:
    try:
        subprocess.run(["notify-send", message], check=True, text=True)
    except Exception as error:
        print("an error occurred while trying to notify the user")
        print(f"error: {error}")


def count_down_timer(interval_time: int) -> None:
    for minutes in range(1, interval_time):
        time_left = f"{((interval_time - minutes) // 60)}:{((60 - minutes) % 60):02d}"
        sys.stdout.write(f"\rTime left: {time_left}")
        sys.stdout.flush()
        time.sleep(1)
    print("\rTime left: 0:00")


def check_digits(focused_interval: str, break_interval: str) -> bool:
    errors_list = []
    if not focused_interval.isdigit():
        errors_list.append("Please, enter only numbers for your focused time.\n")
    if not break_interval.isdigit():
        errors_list.append("Please, enter only numbers for  your break time.")

    is_valid = not errors_list
    return is_valid


def get_interval_times() -> tuple | None:
    focused_interval = input(
        "How long would you like to work for each time? (in minutes)\n"
    )
    break_interval = input(
        "How long would you like to break between sessions? After 3 focus session, next break will be longer.\n"
    )

    if not focused_interval.isdigit():
        print("Please, enter only numbers for your focused time.\n")
    if not break_interval.isdigit():
        print("Please, enter only numbers for  your break time.")

    return focused_interval, break_interval


def cli_pomodoro() -> None:
    seconds = 60
    counter = 0

    response = get_interval_times()
    if not response:
        print("Unable to get input from user!")
        return

    focused_interval, break_interval = response
    focused_time = int(focused_interval) * seconds
    short_break = int(break_interval) * seconds

    while True:
        print("\nFOCUSED TIME!")
        notify_user("Time to Focus!")
        count_down_timer(focused_time)
        print("\nYour Focused time is UP!\nYou can take a break now!\n")

        # response = get_quote()
        response = None
        if response:
            quote, author = response
            message = f"BREAK TIME\n\n{quote} - {author}"
            notify_user(message)
        else:
            notify_user("You should take a break now.")

        print("BREAK TIME!")
        count_down_timer(short_break)
        notify_user("Break time is over!\n")
        counter += 1
        print("")

        if counter == 2:
            short_break += short_break
            print("Your next break will be longer.")
        if counter > 2:
            is_done = input("Would you like to use Pomodoro some more?\n")
            if is_done not in ("yes", "y"):
                return
            else:
                counter = 0


if __name__ == "__main__":
    print("Starting CLI Pomodor Application!")
    cli_pomodoro()
    print("CLI Pomodoro Application is finished!")
