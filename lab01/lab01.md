![image](https://github.com/what-the-fawk/network/assets/90683415/ab8c8a94-3e17-414b-9629-966946eefb60)

Топология воссоздана как показано на схеме. SwitchMiddle является корнем для двух VLAN - 10 и 20. Между Switch1 и Switch2 заблокированное соединение - trunk с "allowed vlan none". Между маршрутизатором и коммутатором уровня распределения тоже trunk - для соединения двух VLAN-ов с клиентов. Для первого используется gateway 192.168.10.3, для второго - 192.168.20.3.

Для обеспечения отказоустойчивости в коммутаторе SwitchMiddle настроена опция ip routing - для первого клиента gateway 192.168.10.2, для второго - 192.168.20.2. Если отключить маршрутизатор, то связность клиентов не нарушится тк перебрасыванием пакетов между VLAN'ами занимается коммутатор. Если бы он этого не делал, то клиенты бы могли связаться друг с другом через gateway'и указанные в первом параграфе.

IP клиентов: 192.168.10.1 (Client1), 192.168.20.1(Client2)

Gateways:
для Client1 - 192.168.10.2 (switch), 192.168.10.3 (router)
для Client2 - 192.168.20.2 (switch), 192.168.20.3 (router)

Дефолтный gateway - switch, чтобы при отключении коммутатора клиенты не теряли связность. Если поменять gateway клиенты будут друг друга искать через роутер. 

К сожалению конфиги не выгружались, поэтому я закинул целиком лабу (рядом с readme лежит)

Скрины:

Пинги со включенным роутером:
![image](https://github.com/what-the-fawk/network/assets/90683415/64d2d0a9-5758-4a89-a246-bab4347a8f66)

Пинги с выключенным роутером:
![image](https://github.com/what-the-fawk/network/assets/90683415/f0e4ffeb-cfc0-49a8-864e-9d0040cfcaf1)

Конфиг VLAN Switch(1-2):
![image](https://github.com/what-the-fawk/network/assets/90683415/1b70e1b8-3db9-4ba6-b869-1a1ff0199846)

Конфиг SwitchMiddle:
![image](https://github.com/what-the-fawk/network/assets/90683415/533de259-69d8-4429-b666-5b10f7197ae5)
![image](https://github.com/what-the-fawk/network/assets/90683415/32a1b7ee-fb0f-4594-bfa0-bfad4101e058)

Конфиг Router'a:
![image](https://github.com/what-the-fawk/network/assets/90683415/a02736b7-017e-4544-b965-fe7551942526)






