import struct
import socket
from black_mirror import constants


def test_connect_to_tcp():
    """Make sure the connection is not raising an error"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((constants.TCP_IP, constants.TCP_PORT))
    s.close()


def test_send_invalid_message():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((constants.TCP_IP, constants.TCP_PORT))
    s.send("invalid")
    response = s.recv(constants.BUFFER_SIZE)
    assert struct.unpack("b", response[0])[0] == -1
    s.close()