from gattlib import GATTRequester
from time import sleep

req = GATTRequester("CF:EC:C9:D4:85:39", False)
req.connect(True, 'random')
sleep(2000.00)
req.write_by_handle(0x16, b"\x57\x01\x00")