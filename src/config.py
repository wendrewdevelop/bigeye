import io
import os
import pathlib
from pathlib import Path
from services.container import build_docker_file


# getting absolute folder path
absolute_files_path = pathlib.Path().resolve()