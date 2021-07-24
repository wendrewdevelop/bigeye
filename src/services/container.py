import os
import io
from pathlib import Path
from functions import *
import pandas as pd
import subprocess


def build_docker_file():
    '''
        build docker
    '''

    root_folder_path = Path()
    dockerfile_path = f'../{root_folder_path}'
    console_log('INFO', 'Starting docker build')
    try:
        return os.system(f'sudo docker build --tag bigeye {dockerfile_path}')
    except Exception as error:
        return error


def run_image_docker(image_name: str):
    '''
        run image inside container
    '''

    console_log('INFO', 'Running docker image as container')
    try:
        os.system(f'sudo docker run -d --name {image_name} {image_name}:latest sleep 60')
        
        return 'Running'
    except Exception as error:
        return error


def getting_last_image_docker(image_name: str):
    '''
        return the latest docker image
    '''
    
    console_log('INFO', 'Getting latest image docker')
    try:
        output = subprocess.check_output(f'sudo docker images {image_name}:latest', shell=True)
        return output
    except Exception as error:
        return error


def getting_last_image_docker_by_id(image_name: str):
    '''
        return the latest docker image
    '''
    
    console_log('INFO', 'Getting latest image docker')
    try:
        output = subprocess.check_output(f'sudo docker images {image_name}:latest -q', shell=True)
        return output
    except Exception as error:
        return error


def create_container(image_name: str):
    '''
        create container based on docker image id
    '''

    console_log('INFO', 'create container')
    try:
        output = os.system(f'sudo docker create --name {image_name} -p 5001:5001 {image_name}:latest')
        return output
    except Exception as error:
        return error


def exec_function_inside_container(image_name: str):
    '''
        execute function inside container
    '''

    console_log('INFO', 'running function')
    try:
        os.system('cd src/files/')
        exec = os.system(f'sudo docker exec -ti {image_name} clamscan -r filestoscan')
        return exec
    except Exception as error:
        return error


def creating_folder_inside_container(image_name: str):
    '''
        creating folder inside container
    '''

    console_log('INFO', 'running function')
    try:
        exec = os.system(f'sudo docker exec -ti {image_name} mkdir filestoscan')
        return exec
    except Exception as error:
        return error


def cp_file_to_container(image_name: str, file_name: str):
    '''
        Copy file to a container directory
    '''

    # docker cp <src-path> <container>:<dest-path> 
    console_log('INFO', 'Starting copy')
    try:
        output = os.system(f'sudo docker cp {file_name} {image_name}:filestoscan')
        return output
    except Exception as error:
        return error
        

def removing_and_clear_all_registers():
    '''
        removing and clear all registers
        from another container and file 
        created by that process.
    '''

    console_log('INFO', 'Clear all images and containers')
    try:
        os.system('sudo docker system prune')
        os.system('sudo docker system prune -a')
        return 'Cleared.'
    except Exception as error:
        return error