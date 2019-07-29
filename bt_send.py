from gattlib import GATTRequester
from time import sleep

sleep(2.0)
req = GATTRequester("F0:18:98:A6:FC:73", False)
req.connect(True, 'random')
req.write_by_handle(0x16, b"\x57\x01\x00")
