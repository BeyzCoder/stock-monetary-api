import os

DB_CONFIG = [
    os.getenv('DB_USER'),
    os.getenv('DB_PASSWORD'),
    os.getenv('HOST'),
    os.getenv('PORT'),
    os.getenv('DB_NAME'),
]
