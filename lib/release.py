import os
import signal

for alias in os.listdir('loops'):
    with open("loops/{}/.play_pid".format(alias),"r") as pidfile:
        pid = pidfile.read()
    try:
        pid = int(pid)
        os.killpg(pid, signal.SIGTERM)
    except ProcessLookupError as e:
        pass
