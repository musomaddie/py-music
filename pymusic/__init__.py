import logging

import colorlog

from .update_globs import update_prefix

handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter(
        "%(log_color)s%(levelname)s%(reset)s | %(blue)s%(name)s:%(lineno)s%(reset)s >>> %(log_color)s%(message)s%("
        "reset)s"
    )
)
logging.basicConfig(
    level=logging.DEBUG, handlers=[handler]
)
