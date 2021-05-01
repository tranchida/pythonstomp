import time

import stomp

conn = stomp.Connection()
conn.connect('admin', 'password', wait=True)
conn.send(body='Hello World', destination='/queue/test', content_type='plain/text', persistent='true')
time.sleep(2)
conn.disconnect()
print("done")