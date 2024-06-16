import subprocess
import sys
import ipaddress
import click

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def get_platform():
    if sys.platform.startswith("win"):
        return "win"
    elif sys.platform.startswith("linux"):
        return "linux"
    elif sys.platform.startswith("darwin"):
        return "mac"
    else:
        return None

def perform_ping(ip):
    platform = get_platform()
    args = ["ping", ip, "-c", "1"] if platform != "win" else ["ping", ip, "-n", "1"]
    try:
        subprocess.check_output(args, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def find_mtu(ip, min_mtu, max_mtu, step):
    if not is_valid_ip(ip):
        click.echo("Неверный IP-адрес.")
        return

    if not perform_ping(ip):
        click.echo("Назначение недоступно.")
        return
    
    if min_mtu < 0 or max_mtu < 0 or step <= 0:
        click.echo("Значения MTU должны быть положительными.")
        return
    
    if min_mtu > max_mtu:
        click.echo("Минимальное значение MTU не может быть больше максимального.")
        return

    good_mtu = 0
    platform = get_platform()
    for mtu in range(min_mtu, max_mtu + 1, step):
        args = ["ping", ip, "-c", "1"] if platform != "win" else ["ping", ip, "-n", "1"]
        if platform == "win":
            args.extend(["-f", "-l", str(mtu)])
        elif platform == "linux":
            args.extend(["-s", str(mtu), "-M", "do"])
        elif platform == "mac":
            args.extend(["-D", "-s", str(mtu)])
        try:
            subprocess.check_output(args, stderr=subprocess.DEVNULL)
            good_mtu = mtu
        except subprocess.CalledProcessError:
            break
    if good_mtu:
        click.echo(f"Максимальное значение MTU: {good_mtu}")
    else:
        click.echo("Не удалось найти значение MTU.")

@click.command()
@click.option('--ip', default='127.0.0.1', help='IP-адрес назначения')
@click.option('--min', 'min_mtu', default=500, help='Минимальное значение MTU для проверки', type=int)
@click.option('--max', 'max_mtu', default=1500, help='Максимальное значение MTU для проверки', type=int)
@click.option('--step', default=10, help='Шаг значения', type=int)
def main(ip, min_mtu, max_mtu, step):
    find_mtu(ip, min_mtu, max_mtu, step)

if __name__ == "__main__":
    main()
