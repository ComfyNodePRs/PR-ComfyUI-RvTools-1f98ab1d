import folder_paths
import os

from ..core.common import format_datetime, format_date_time, format_variables
from ..core import CATEGORY, any, logger

#---------------------------------------------------------------------------------------------------------------------#
#altered from CreateRootFolder from path-helper
class RProjectFolder:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "project_root_name": ("STRING", {"multiline": False, "default": "MyProject"}),
                "date_time_format": ("STRING", {"multiline": False, "default": "%Y-%m-%d"}),
                "add_date_time": (["disable", "prefix", "postfix"],),
                "create_batch_folder": (["enable", "disable"],),
                "batch_folder_name": ("STRING", {"multiline": False, "default": "batch_{}"}),                
                "output_path_generation": (["relative", "absolute"],)
            },
            "optional": {
                "batch_no": (any, {"forceInput": True})
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.FOLDER.value
    RETURN_TYPES = ("STRING",)
    
    FUNCTION = "execute"
    
    def execute(self, project_root_name, add_date_time, date_time_format, output_path_generation, create_batch_folder, batch_folder_name, batch_no=None):
        logger.debug("Project Folder: " + str(project_root_name))

        mDate = format_datetime(date_time_format)
        new_path = project_root_name

        if add_date_time == "prefix":
            new_path = os.path.join(mDate, project_root_name)
        elif add_date_time == "postfix":
            new_path = os.path.join(project_root_name, mDate)

        if create_batch_folder == "enable":
           folder_name_parsed = format_variables(batch_folder_name, batch_no)
           new_path = os.path.join(new_path, folder_name_parsed)

        if output_path_generation == "relative":
            return ("./" + new_path,)
        elif output_path_generation == "absolute":
            return (os.path.join(self.output_dir, new_path),)
    
    @classmethod
    def VALIDATE_INPUTS(self, project_root_name):
        return True
        
#---------------------------------------------------------------------------------------------------------------------#
class RFolderAdd:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {"forceInput": True}),
                #"path": ("PATH",),
                "folder_name": ("STRING", {"multiline": False, "default": "SubFolder"})
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.FOLDER.value
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)    
    
    FUNCTION = "execute"

    def execute(self, path, folder_name):
        logger.debug("Add Folder: " + str(folder_name))

        new_path = os.path.join(path, folder_name)
        return (new_path,)

    @classmethod
    def VALIDATE_INPUTS(self, path):
        return True

#---------------------------------------------------------------------------------------------------------------------#
class RFileNamePrefixAdd:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {"forceInput": True}),
                "file_name_prefix": ("STRING", {"multiline": False, "default": "image"}),
                "add_date_time": (["disable", "prefix", "postfix"],),
                "date_time_format": ("STRING", {"multiline": False, "default": "%Y-%m-%d_%H:%M:%S"}),
            },
            "optional": {
                "input_variables": (any,)
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.FOLDER.value
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)

    FUNCTION = "execute"

    def execute(self, path, file_name_prefix, add_date_time, date_time_format, input_variables=None):
        logger.debug("Add Filename Prefix: " + str(file_name_prefix))

        filename_name_parsed = format_variables(file_name_prefix, input_variables)
        if add_date_time == "disable":
            new_path = os.path.join(path, filename_name_parsed)
        else:
            new_path = os.path.join(path, format_date_time(filename_name_parsed, add_date_time, date_time_format))
        return (new_path,)

    @classmethod
    def VALIDATE_INPUTS(self, path):
        return True


#---------------------------------------------------------------------------------------------------------------------#