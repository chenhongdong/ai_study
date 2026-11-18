TORTOISE_ORM = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql', # MySQL
            'credentials': {
                'host': '127.0.0.1',
                'port': '3306',
                'user': 'root',
                'password': '123456',
                'database': 'fastapi',
                'minsize': 1,
                'maxsize': 5,
                'echo': True
            }
        }
    },
    'apps': {
        'models': {
            'models': ['models', 'aaerich.models'],
            'default+connection': 'default'
        }
    },
    'use_tz': Fasle,
    'timezone': 'Asia/Shanghai'
}