class Server:
    """для описания работы серверов в сети"""

    def __init__(self) -> None:
        self.ip_address = id(self)
        self.buffer = []

    def send_data(self, data):
        router.buffer.append(data)

    def get_data(self):
        data_list = self.buffer.copy()
        self.buffer = []
        return data_list

    def get_ip(self):
        return self.ip_address


class Router:
    """для описания работы роутеров в сети(в данной задаче полагается один роутер)"""
    
    def __init__(self) -> None:
        self.connected_servers = []
        self.buffer = []
    
    def link(self, server):
        """Присоединение сервера к роутеру"""
        self.connected_servers.append(server)
    
    def unlink(self, server):
        """Отсоединение сервера server (объекта класса Server) от роутера"""
        if server in self.connected_servers:
            self.connected_servers.remove(server)
    
    def send_data(self):
        """Отправка всех пакетов из буфера роутера соответствующим серверам"""
        for data_packet in self.buffer:
            destination_ip = data_packet.ip # Получение ip адреса назначения из текущего пакета данных
            for server in self.connected_servers:
                if server.ip_address == destination_ip:
                    server.buffer.append(data_packet)
                    break

        self.buffer = [] # очистка буфера


class Data:
    """для описания пакета информации"""

    def __init__(self, data, ip) -> None:
        self.data = data
        self.ip = ip





router = Router()  # экземпляр класса роутер
sv_from = Server()  # Именованный экземпляр класса сервер № 1
sv_from2 = Server()  # Именованный экземпляр класса сервер № 2
router.link(sv_from)  # Присоединение сервера № 1 к роутеру
router.link(sv_from2)  # Присоединение сервера № 2 к роутеру
router.link(Server())  # Присоединение сервера № 3 ('безымянного') к роутеру
router.link(Server())  # Присоединение сервера № 4 ('безымянного') к роутеру
sv_to = Server()  # Именованный экземпляр класса сервер № 5
router.link(sv_to)  # Присоединение сервера № 5 к роутеру
sv_from.send_data(Data("Hello", sv_to.get_ip()))  # Отправка строки 'Hello'  1->5
sv_from2.send_data(Data("Hello", sv_to.get_ip()))  # Отправка строки 'Hello'  2->5
sv_to.send_data(Data("Hi", sv_from.get_ip()))  # Отправка строки 'Hi' 5->1
router.send_data()  # Отправка всех данных из буфера по адресам
msg_lst_from = sv_from.get_data()  # Список всех принятых пактов сервером 1

msg_lst_to = sv_to.get_data()  # Список всех принятых пактов сервером 5
print(msg_lst_to)
for data_packet in msg_lst_to:
    print(f"Data: {data_packet.data}, Destination_IP: {data_packet.ip}")