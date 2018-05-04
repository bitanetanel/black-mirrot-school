from black_mirror.request_parser import RequestParser, InvalidMessageException


def test_parse_too_short():
    parser = RequestParser("short")
    parser.parse()
    assert not parser.is_valid