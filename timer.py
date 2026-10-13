#COUNT DOWN TIMER PYTHON CODE

import time


def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        print(f"{remaining}...", flush=True)
        time.sleep(1)
    print("Time's up!")


def main():
    seconds = int(input("Enter countdown duration in seconds: "))

    if seconds <= 0:
        print("Duration must be greater than zero.")
        return

    countdown(seconds)


if __name__ == "__main__":
    main()
