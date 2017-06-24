import socket
import ssl

__version__ = "0.1.0"


def check_pypi_name(pypi_package_name, pypi_registry_host=None):
    """
    Check if a package name exists on pypi.

    TODO: Document the Registry URL construction.
        It may not be obvious how pypi_package_name and pypi_registry_host are used
        I'm appending the simple HTTP API parts of the registry standard specification.

    It will return True if the package name, or any equivalent variation as defined by PEP 503 normalisation
     rules (https://www.python.org/dev/peps/pep-0503/#normalized-names) is registered in the PyPI registry.

    >>> check_pypi_name('pip')
    True
    >>> check_pypi_name('Pip')
    True

    It will return False if the package name, or any equivalent variation as defined by PEP 503 normalisation
     rules (https://www.python.org/dev/peps/pep-0503/#normalized-names) is not registered in the PyPI registry.

    >>> check_pypi_name('testy_mc-test_case-has.a.cousin_who_should_never_write_a_package')
    False

    :param pypi_package_name:
    :param pypi_registry_host:
    :return:
    """
    if pypi_registry_host is None:
        pypi_registry_host = 'pypi.python.org'

    # Just a helpful reminder why this bytearray size was chosen.
    #                            HTTP/1.1 200 OK
    #                            HTTP/1.1 404 Not Found
    receive_buffer = bytearray(b'------------')
    context = ssl.create_default_context()
    ssl_http_socket = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=pypi_registry_host)
    ssl_http_socket.connect((pypi_registry_host, 443))
    ssl_http_socket.send(b''.join([
        b"HEAD /simple/", pypi_package_name.encode('ascii'), b"/ HTTP/1.0", b"\r\n",
        b"Host: ", pypi_registry_host.encode('ascii'), b"\r\n",
        b"\r\n\r\n"
    ]))
    ssl_http_socket.recv_into(receive_buffer)

    ssl_http_socket.shutdown(1)
    ssl_http_socket.close()

    # Early return when possible.
    if b'HTTP/1.1 200' in receive_buffer:
        return True
    elif b'HTTP/1.1 404' in receive_buffer:
        return False

    remaining_bytes = ssl_http_socket.recv(1024)
    redirect_path_location_start = remaining_bytes.find(b'Location:') + 10
    redirect_path_location_end = remaining_bytes.find(b'\r\n', redirect_path_location_start)
    # Append the trailing slash to avoid a needless extra redirect.
    redirect_path = remaining_bytes[redirect_path_location_start:redirect_path_location_end] + b'/'

    ssl_http_socket.shutdown(1)
    ssl_http_socket.close()

    ssl_http_socket = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=pypi_registry_host)
    ssl_http_socket.connect((pypi_registry_host, 443))

    ssl_http_socket.send(b''.join([
        b"HEAD ", redirect_path, b" HTTP/1.0", b"\r\n",
        b"Host: ", pypi_registry_host.encode('ascii'), b"\r\n",
        b"\r\n\r\n"]))
    ssl_http_socket.recv_into(receive_buffer)

    if b'HTTP/1.1 200' in receive_buffer:
        return True
    elif b'HTTP/1.1 404' in receive_buffer:
        return False
    else:
        NotImplementedError('A definitive answer was not found by primary or secondary lookups.')
