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
        output = stdout.read().decode('utf-8')  # Standard output
        error = stderr.read().decode('utf-8')   # Standard error

        if output:
            print(f"Command Output:\n{output}")
        if error:
            print(f"Error Output:\n{error}")

        # Close the SSH connection
        ssh_client.close()
        print("Connection closed.")

    except Exception as e:
        print(f"An error occurred: {e}")
if __name__=="__main__":
    # Usage example
    hostname = "tega.n2ip.ru"
    port = 22  # Default SSH port
    username = "sae"
    password = "or!on!sC21"
    command = "ls -l /usr/home/sae"  # Replace with your desired command

    execute_remote_command(hostname, port, username, password, command)