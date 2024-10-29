import logging
from logging.config import dictConfig

from src.config import DevConfig, config

def obfuscation(email: str, obfuscation_length: int) -> str:
    characters = email[:obfuscation_length]
    first, last = email.split("@")
    return characters + ("*" * (len(first) - obfuscation_length)) + "@" + last

class EmailObfuscationFilter(logging.Filter):
    def __init__(self, name: str = "", obfuscation_length: int = 2) -> None:
        super().__init__(name)
        self.obfuscation_length = obfuscation_length

    def filter(self, record: logging.LogRecord) -> bool:
        if "email" in record.__dict__:
            record.email = obfuscation(record.email, self.obfuscation_length)
        return True


def configure_logging() -> None:
    dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {
            "correlation_id": {
                "()": "asgi_correlation_id.CorrelationIdFilter",
                "uuid_length": 8 if isinstance(config, DevConfig) else 32,
                "default_value": "-",
            },
            "email_obfuscation": {
                "()": EmailObfuscationFilter,
                "obfuscation_length": 2 if isinstance(config, DevConfig) else 0,
            }
        },
        "formatters": {
            "console": {
                "class": "logging.Formatter",
                "datefmt": "%y-%m-%d %H:%M:%S",
                "format": "(%(correlation_id)s) %(name)s:%(lineno)d - %(message)s",
            },
            "file": {
                "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
                "datefmt": "%y-%m-%d %H:%M:%S",
                "format": "%(asctime)s %(msecs)03dZ %(levelname)-8s %(correlation_id)s %(name)s %(lineno)d %(message)s",
            }
        },
        "handlers": {
            "default": {
                "class": "rich.logging.RichHandler",
                "level": "DEBUG",
                "formatter": "console",
                "filters": ["correlation_id", "email_obfuscation"],
            },
            "rotating_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "file",
                "filename": "streamSage.log",
                "maxBytes": 1024 * 1024, # 1MB
                "backupCount": 3,
                "encoding": "utf8",
                "filters": ["correlation_id", "email_obfuscation"],
            }
        },
        "loggers": {
            "uvicorn": {
                "handlers": ["default", "rotating_file"],
                "level": "INFO",
            },
            "src": {
                "handlers": ["default", "rotating_file"],
                "level": "DEBUG" if isinstance(config, DevConfig) else "INFO",
                "propagate": False,
            },
            "databases": {
                "handlers": ["default"],
                "level": "WARNING",
            },
            "aiosqlite": {
                "handlers": ["default"],
                "level": "WARNING",
            },
        },
    })
