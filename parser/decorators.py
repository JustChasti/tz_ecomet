from loguru import logger


# страндартный декоратор, чтобы при ошибке, сервис мог продолжать работу
def default_decorator(errormessage):
    def iternal_decorator(function):
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except Exception as e:
                logger.exception(e)
                return {'message': errormessage}
        return wrapper
    return iternal_decorator
