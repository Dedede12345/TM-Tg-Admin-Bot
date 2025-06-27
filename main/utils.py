import time
from sys import stdin, stdout, stderr
import asyncio
import paramiko
import os

EC2_IP = '34.205.69.195'
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_PATH = os.path.join(SCRIPT_DIR, '..', 'secret', 'Flask-Web-Server-Key-New.pem')
USERNAME = 'admin'

def ssh_docker_command_sync(command: str) -> dict[str, str]:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(EC2_IP, username=USERNAME, key_filename=SECRET_PATH)

    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode().strip()
    error = stderr.read().decode().strip()

    stdout.channel.recv_exit_status()
    ssh.close()

    f"STDOUT:\n{output}\nSTDERR:\n{error}" if error else output
    return {"STDOUT" : f"{output}", "STDERR": f"{error}" if error else output}

async def ssh_docker_command(command: str) -> dict[str, str]:
    return await asyncio.to_thread(ssh_docker_command_sync, command)

async def start_flask_container() -> str:
    return (await ssh_docker_command('sudo docker compose up -d'))['STDERR']

async def stop_flask_container() -> str:
    return (await ssh_docker_command('sudo docker compose stop -t 3 && sudo docker compose rm -f'))['STDOUT']


async def main():
    # Start container
    res = await start_flask_container()
    print(res)

    time.sleep(5)

    res = await stop_flask_container()
    print(res)

if __name__ == '__main__':

   asyncio.run(main())

