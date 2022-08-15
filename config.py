from dotenv import load_dotenv
import dotenv
import os

dotenv_file_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_file_path):
    load_dotenv(dotenv_file_path)

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopementConfig(Config):
    ENV = 'developement'
    SQLALCHEMY_DATABASE_URI = "mysql+pymsql://root:root@localhost:3306/dog"

class ProductionConfig(Config):
    pass
