from config import *


class ValidateFile:
    '''
        Class to validate received file.
    '''

    def __init__(self, filename) -> None:
        '''
            constructor function

            args: 
                [filename](str): 
                    representing the file name.
        '''

        self.filename = filename
        self.abs_path = absolute_files_path

    def path_union(self):
        '''
            this function group full file path
        '''

        file_path = f'{self.abs_path}/files/{self.filename}'
        
        return file_path