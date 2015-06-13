# -*- coding: utf-8 -*-
import os, sys

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(PROJECT_ROOT, os.pardir))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__), '../')))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__), '../../')))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..')))
sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__), '../../../..')))

from base.settings import load_django_settings
load_django_settings('m-app-exchange.app', )
from redis_model.queue import Worker
from base.core.dateutils import *
import json


def do_sync_favorite(data):
    print "**Recieve data: ", data

    game_ids_str = data["game_ids"]
    device_id = data["device_id"]
    #......


if __name__ == "__main__":
    worker = Worker("device_info.sync.favorite")
    try:
        worker.register(do_sync_favorite)
        worker.start()
    except KeyboardInterrupt:
        worker.stop()
        print "exited cleanly"
        sys.exit(1)
    except Exception, e:
        print e
