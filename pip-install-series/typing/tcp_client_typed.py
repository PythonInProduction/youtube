import socket
from dataclasses import dataclass
from typing import Final

DEFAULT_BUFFER_SIZE: Final[int] = 4096

@dataclass(frozen=True, slots=True)
class TcpClientConfig:
    host: str
    port: int
    timeout_seconds: float = 5.0
    buffer_size: int = DEFAULT_BUFFER_SIZE

class TcpClient:
    def __init__(self, config: TcpClientConfig) -> None:
        self._config = config
        self._socket: socket.socket | None = None

    def connect(self) -> None:
        if self._socket is not None:
            return

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(self._config.timeout_seconds)
        sock.connect((self._config.host, self._config.port))
        self._socket = sock

    def send(self, data: bytes) -> None:
        if not data:
            raise ValueError("data must not be empty")

        self._require_socket().sendall(data)

    def receive(self) -> bytes:
        data = self._require_socket().recv(self._config.buffer_size)
        if data == b"":
            raise ConnectionError("Connection closed by remote host")
        return data

    def request(self, payload: bytes) -> bytes:
        self.send(payload)
        return self.receive()

    def close(self) -> None:
        if self._socket is not None:
            self._socket.close()
            self._socket = None

    def _require_socket(self) -> socket.socket:
        if self._socket is None:
            raise ConnectionError("Socket is not connected")
        return self._socket

    def __enter__(self) -> TcpClient:
        self.connect()
        return self

    def __exit__(self, exc_type: object, exc: object, tb: object) -> None:
        self.close()

def main() -> None:
    config = TcpClientConfig(host="127.0.0.1", port=5000)

    with TcpClient(config) as client:
        response: bytes = client.request(b"ping")
        print(response.decode("utf-8"))

if __name__ == "__main__":
    main()
