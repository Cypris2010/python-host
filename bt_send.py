from gattlib import GATTRequester

req = GATTRequester("00:11:22:33:44:55")
req.write_by_handle(0x16, b'\x57\x01\x00')