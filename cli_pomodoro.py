import sys
import time
import subprocess


def notify_user(message: str = "This is a notification.\n"):
    try:
        print("Notifying user.")
        subprocess.run(["notify-send", message], check=True, text=True)
    except Exception as error:
        print("an error occurred while trying to notify the user")
        print(f"error: {error}")


def count_down_timer(interval_time: int):
    for minutes in range(1, interval_time):
        time_left = f"{((interval_time - minutes) // 60)}:{((60 - minutes) % 60):02d}"
        sys.stdout.write(f"\rTime left: {time_left}\n")
        sys.stdout.flush()
        time.sleep(1)


def check_digits(focused_interval: str, break_interval: str) -> bool:
    errors_list = []
    if not focused_interval.isdigit():
        errors_list.append("Please, enter only numbers for your focused time.\n")
    if not break_interval.isdigit():
        errors_list.append("Please, enter only numbers for  your break time.")

    is_valid = not errors_list
    return is_valid


def cli_pomodoro():
    focused_interval = input(
        "How long would you like to work for each time? (in minutes)"
    )
    break_interval = input(
        "How long would you like to break between sessions? After 2 focus session you will have a longer break."
    )

    if not focused_interval.isdigit():
        print("Please, enter only numbers for your focused time.\n")
    if not break_interval.isdigit():
        print("Please, enter only numbers for  your break time.")

    seconds = 60
    focused_time = int(focused_interval) * seconds
    short_break = int(break_interval) * seconds
    counter = 0

    while True:
        if counter == 2:
            short_break = +short_break
            counter = 0
        else:
            short_break = short_break
        count_down_timer(focused_time)
        print("\nYour Focused time is UP!.\nYou can take a short break now!\n")
        notify_user()
        print("BREAK TIME!")
        count_down_timer(short_break)
        counter = +1


if __name__ == "__main__":
    print("Starting CLI Pomodor Application!")
    cli_pomodoro()
    print("CLI Pomodoro Application is finished!")
