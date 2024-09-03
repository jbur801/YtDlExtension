
import sys
import select
import threading
import time

def log(message):
    print(message)
    with open('testLog.txt', 'a') as log_file:
        log_file.write(message + '\n')




def read_input():
    while True:
        input_data = sys.stdin.readline().strip()
        if input_data:
            log(f"Received input: {input_data}")

def main():
    log("Running... (Type something and press Enter)")

    # Start a thread to handle input
    input_thread = threading.Thread(target=read_input, daemon=True)
    input_thread.start()

    # Main loop to simulate doing other work
    while True:
        # Do other tasks here (simulate doing work with sleep)
        log("Doing other work...")
        time.sleep(1)  # Simulate work being done
if __name__ == "__main__":
    main()