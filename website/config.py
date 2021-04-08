import os


class Config:
    SECRET_KEY = '5791134cc0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'rohanPanigrahi96@gmail.com'
    MAIL_PASSWORD = 'VUkgTw62LqcHwPN'
