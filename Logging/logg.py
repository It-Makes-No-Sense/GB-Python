import logging
from other import log_all

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
logger.warning('Вызов функции из другого файла')
log_all()
