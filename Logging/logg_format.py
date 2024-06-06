import logging
from other import log_all

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created} секунд записала сообщение: {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.INFO)
logger = logging.getLogger('main')
logger.warning('Вызов функции из другого модуля.')
log_all()
