import socket
import struct
import constants
from request_parser import RequestParser


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((constants.TCP_IP, constants.TCP_PORT))
    s.listen(5)
    print "Listening to {}:{}".format(constants.TCP_IP, constants.TCP_PORT)
    try:
        while 1:
            conn, addr = s.accept()
            data = conn.recv(constants.BUFFER_SIZE)
            if data:
                print "Got a message: {}".format(data)
                message_parser = RequestParser(data).parse()
                if not message_parser.is_valid:
                    conn.send(struct.pack("b", -1))
                else:
                    conn.send(data)
            conn.close()
    except Exception, e:
        pass
    finally:
        print "closing"
        conn.close()
        s.close()


if __name__ == "__main__":
    main()