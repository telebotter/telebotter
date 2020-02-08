import os
import logging
import logging.handlers




class GWTimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    """ A modified TimedRotatingFileHandler to create new logfiles with write
    permission for groups. Based on this example from SO:
    https://stackoverflow.com/a/6779307/7268121
    """

    def _open(self):
        prevumask=os.umask(0o002)
        rtv=logging.handlers.TimedRotatingFileHandler._open(self)
        os.umask(prevumask)
        return rtv
