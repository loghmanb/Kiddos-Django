import os
from pathlib import Path
from dotenv import load_dotenv


def load_custom_environment_variables():
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    usr_project_folder = os.path.expanduser('~/'+BASE_DIR.name)
    for project_folder in [BASE_DIR, usr_project_folder]:
        load_dotenv(os.path.join(project_folder, '.env'))