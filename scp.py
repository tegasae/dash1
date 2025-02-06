import paramiko

def copy_file_from_remote(hostname, port, username, password, remote_path, local_path):
    try:
        # Initialize SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote host
        ssh_client.connect(hostname, port=port, username=username, password=password)
        print("Connected to the remote host.")

        # Use SFTP to copy the file
        sftp = ssh_client.open_sftp()
        sftp.get(remote_path, local_path)  # Download file from remote to local
        print(f"File copied from {remote_path} to {local_path}")

        # Close the SFTP session and SSH connection
        sftp.close()
        ssh_client.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__=="__main__":
    # Usage example
    hostname = "tega.n2ip.ru"
    port = 22  # Default SSH port
    username = "sae"
    password = "or!on!sC21"
    remote_path = "/home/sae/1.txt"
    local_path = "/tmp/1.txt"

    copy_file_from_remote(hostname, port, username, password, remote_path, local_path)