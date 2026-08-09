from Evtx.Evtx import Evtx

with Evtx("manager.evtx") as log:
    for r in log.records():
        print(r.xml())
