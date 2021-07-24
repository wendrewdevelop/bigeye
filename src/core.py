from utils import file_exposed
from functions import *
from config import *
from services.container import (
    build_docker_file, 
    run_image_docker,
    getting_last_image_docker_by_id,
    getting_last_image_docker,
    create_container,
    exec_function_inside_container,
    creating_folder_inside_container,
    cp_file_to_container,
    removing_and_clear_all_registers
)


def main():
    '''
        that function group and execute
        another functions
    '''

    # getting image path
    console_log('INFO', "getting image path")
    path_union = file_exposed(
        filename='img.jpg'
    ).path_union()
    console_log('INFO', path_union)

    try:
        # build docker image
        build_docker_file()
        # getting name of image
        image_id = getting_last_image_docker_by_id('bigeye')
        # Run image as a container
        run_image_docker('bigeye')
        # Creating container
        create_container('bigeye')
        console_log('INFO', 'Container created')
        # Creating folder inside container
        console_log('INFO', 'Creating folder inside container')
        creating_folder_inside_container('bigeye')
        # Copy file inside docker
        console_log('INFO', 'Copying file inside container')
        cp_file_to_container('bigeye', str(path_union))
        # Scan folder with file
        console_log('INFO', 'Scan folder with file')
        exec_function_inside_container('bigeye')
        os.system('y') # removing data inside container
        os.system('y') # delete all container
        return 'Process finished, no errors reported'
    except Exception as error:
        return error
    finally:
        removing_and_clear_all_registers()


if __name__ == "__main__":
    main()