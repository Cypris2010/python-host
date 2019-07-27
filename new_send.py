from blesuite.connection_manager import BLEConnectionManager
import gevent
import time

adapter = 0
role = 'central'
timeout_seconds = 10

peer_device_address = "CF:EC:C9:D4:85:39"
peer_address_type = "public"

with BLEConnectionManager(adapter, role) as connection_manager:
    # initialize BLEConnection object
    connection = connection_manager.init_connection(peer_device_address, peer_address_type)

    # create connection
    connection_manager.connect(connection)

    # write to handle 0x0b
    #write_request = connection_manager.gatt_write_handle_async(connection, 0x16, b"\x57\x01\x00")
    
    # write to handle 0x0b
    write_request = connection_manager.gatt_write_handle(connection, 0x16, b"\x57\x01\x00")
    if write_request.has_error():
        print "Got error:", write_request.get_error_message()
    elif write_request.has_response():
        print "Got response:", write_request.response.data, "from handle", hex(write_request.handle)

