import socket

from workerthread import WorkerThread


class WebServer:
    """
    Webサーバーを表すクラス
    """

    def serve(self):
        """
        サーバーを起動する
        """

        print("=== Server: サーバーを起動します ===")

        try:
            server_socket = self.create_server_socket()

            while True:
                print("=== Server: クライアントからの接続を待ちます ===")
                (client_socket, address) = server_socket.accept()
                print(f"=== Server: クライアントとの接続が完了しました remote_address: {address} ===")

                WorkerThread(client_socket, address).start()

        finally:
            print("=== Server: サーバーを停止します。 ===")

    def create_server_socket(self) -> socket:
        """
        通信を待ち受けるためのserver_socketを生成する
        :return:
        """

        server_socket = socket.socket()
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind((socket.gethostname(), 8080))
        server_socket.listen(10)
        return server_socket


if __name__ == "__main__":
    server = WebServer()
    server.serve()
