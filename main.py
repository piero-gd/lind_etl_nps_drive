from src.controller.main_controller import MainController
from src.config.env_config import FILE_ID

if __name__ == '__main__':
    controller = MainController(FILE_ID)
    controller.run()
