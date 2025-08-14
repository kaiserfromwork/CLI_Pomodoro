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


def cli_pomodoro():
    seconds = 60
    focused_time = 5 * seconds
    short_break = 2 * seconds

    while True:
        count_down_timer(focused_time)
        print("\nYour Focused time is UP!.\nYou can take a short break now!\n")
        notify_user()
        print("BREAK TIME!")
        count_down_timer(short_break)


if __name__ == "__main__":
    print("Starting CLI Pomodor Application!")
    cli_pomodoro()
    print("CLI Pomodoro Application is finished!")
