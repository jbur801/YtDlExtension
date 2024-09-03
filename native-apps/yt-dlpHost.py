import sys
import json


def log(message):
    print(message)
    with open('log.txt', 'a') as log_file:
        log_file.write(message + '\n')

def read_message():
    log('reading')
    # Read the length prefix (4 bytes)
    raw_length = sys.stdin.buffer.read(4)
    if len(raw_length) < 4:
        log("Error: Insufficient data read for message length")
        return None
    log(f"Raw length data: {repr(raw_length)}")
    message_length = int.from_bytes(raw_length, 'little')
    log(f"Message length: {message_length}")
    
    # Read the actual message
    message = sys.stdin.buffer.read(message_length)
    if len(message) < message_length:
        log("Error: Insufficient data read for message")
        return None
    log(f"Received message: {message.decode('utf-8')}")
    return message.decode('utf-8')

def write_message(message):
    # Convert message to bytes and write to stdout
    message_bytes = message.encode('utf-8')
    sys.stdout.write(f"{len(message_bytes):<4}")
    sys.stdout.write(message_bytes.decode('utf-8'))
    sys.stdout.flush()

def main():
    log("Native messaging host started")
    message = read_message()
    if message is None:
        log("No message received or read failed")
        log("exiting...")
        return
    log(f"Processing message: {message}")
    try:
        # Assuming the message is a JSON string
        received_data = json.loads(message)
        response = {"status": "success", "received": received_data}
    except json.JSONDecodeError as e:
        response = {"status": "error", "message": f"Invalid JSON: {str(e)}"}
    write_message(json.dumps(response))
    log(f"Response sent: {json.dumps(response)}")
    log("Native messaging host finished")

if __name__ == "__main__":
    main()