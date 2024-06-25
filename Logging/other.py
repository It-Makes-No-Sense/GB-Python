import logging

logger = logging.getLogger(__name__)


def log_all():
    logger.debug('Подробная отладочная инфа. Замена мнж-ва принтов')
    logger.info('Information')
    logger.warning('Предупреждение')
    logger.error('Тут ошибка')
    logger.critical('Крит')


if __name__ == '__main__':
    log_all()
