from decouple import config

class Config():
    """Base configuration."""
    SECRET_KEY = config('SECRET_KEY')
    SCHEDULER_API_ENABLED = True


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True


config = {
    'development': DevelopmentConfig
}
