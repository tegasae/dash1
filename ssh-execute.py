import asyncio
from datetime import datetime

import paramiko


def execute_remote_command(hostname, port, username, password, command):
    try:
        # Initialize SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add host keys

        # Connect to the remote host
        ssh_client.connect(hostname, port=port, username=username, password=password)
        print(f"Connected to {hostname}.")

        # Execute the command
        stdin, stdout, stderr = ssh_client.exec_command(command)

        # Read and print the output
        output = stdout.read()  # Standard output
        error = stderr.read().decode('utf-8')  # Standard error

        # if output:
        #    print(f"Command Output:\n{output}")
        if error:
            print(f"Error Output:\n{error}")

        # Close the SSH connection
        ssh_client.close()
        print("Connection closed.")
        return output

    except Exception as e:
        print(f"An error occurred: {e}")


def get_data(hostname, username, password):
    command = "docker exec work_http-app sqlite3 /app/data/telebot.db '.backup /tmp/backup.db' && docker exec work_http-app cat /tmp/backup.db"
    output = execute_remote_command(hostname, 22, username, password, command)
    with open(f"telebot.db", "wb") as file:
        file.write(output)

async def periodic_task(interval_seconds):
    while True:
        print("Executing async task...")
        get_data("192.168.100.147","tega","chfh178")
        await asyncio.sleep(interval_seconds)

async def main():
    # Start the periodic task
    await asyncio.create_task(periodic_task(300))

    # Keep the main function running (or perform other tasks if needed)
    await asyncio.Event().wait()


#if __name__ == "__main__":
    # Usage example
    # date_file=date_now=datetime.today().strftime('%Y-%M-%d-%H:%m')
    # hostname = "192.168.100.147"
    # port = 22  # Default SSH port
    # username = "tega"
    # password = "chfh178"
    ##command = "ls -l /usr/home/sae"  # Replace with your desired command
    # command="docker exec work_http-app sqlite3 /app/data/telebot.db '.backup /tmp/backup.db' && docker exec work_http-app cat /tmp/backup.db"
    # output=execute_remote_command(hostname, port, username, password, command)
    # with open(f"backup-{date_file}.db", "wb") as file:
    #    file.write(output)

    # with open(f"telebot.db", "wb") as file:
    #    file.write(output)
    #get_data("192.168.100.147", "tega", "chfh178")
if __name__ == "__main__":
    asyncio.run(main())