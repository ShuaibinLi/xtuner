import sys
from loguru import logger

from .auto import AutoConfig, AutoModelForCausalLM, AutoTokenizer
from .device import get_device, get_torch_device_module


_LOGGER = None

def log_format(debug=False):

    formatter = '[XTuner][{time:YYYY-MM-DD HH:mm:ss}][<level>{level}</level>]'

    if debug:
        formatter += '[<cyan>{name}</cyan>:'
        formatter += '<cyan>{function}</cyan>:'
        formatter += '<cyan>{line}</cyan>]'

    formatter += ' <level>{message}</level>'
    return formatter


def get_logger(level="INFO"):
    global _LOGGER
    if _LOGGER is None:
        # Remove the original logger in Python to prevent duplicate printing.
        logger.remove()
        logger.add(sys.stderr, level=level, format=log_format(debug=level=="DEBUG"))
        _LOGGER = logger
    return _LOGGER


__all__ = [
    'AutoConfig', 'AutoModelForCausalLM', 'AutoTokenizer', 'get_device',
    'get_torch_device_module'
]
