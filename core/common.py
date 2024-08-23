import os
import numpy as np
import torch

from PIL import Image
from datetime import datetime

#---------------------------------------------------------------------------------------------------------------------#
# just a helper function to set the widget values (or clear them)
def setWidgetValues(value=None, unique_id=None, extra_pnginfo=None) -> None:
    if unique_id and extra_pnginfo:
        workflow = extra_pnginfo["workflow"]
        node = next((x for x in workflow["nodes"] if str(x["id"]) == unique_id), None)

        if node:
            node["widgets_values"] = value

    return None

#---------------------------------------------------------------------------------------------------------------------#
# return x and y resolution of an image (torch tensor)
def getResolutionByTensor(image=None) -> dict:
    res = {"x": 0, "y": 0}

    if image is not None:
        img = image.movedim(-1, 1)

        res["x"] = img.shape[3]
        res["y"] = img.shape[2]

    return res

#---------------------------------------------------------------------------------------------------------------------#
# by https://stackoverflow.com/questions/6080477/how-to-get-the-size-of-tar-gz-in-mb-file-in-python
def get_size(path):
    size = os.path.getsize(path)
    if size < 1024:
        return f"{size} bytes"
    elif size < pow(1024, 2):
        return f"{round(size / 1024, 2)} KB"
    elif size < pow(1024, 3):
        return f"{round(size / (pow(1024, 2)), 2)} MB"
    elif size < pow(1024, 4):
        return f"{round(size / (pow(1024, 3)), 2)} GB"

#---------------------------------------------------------------------------------------------------------------------#
def format_datetime(datetime_format):
    today = datetime.now()
    return f"{today.strftime(datetime_format)}"

#---------------------------------------------------------------------------------------------------------------------#
#imported from path-helper
def format_date_time(string, position, datetime_format):
    today = datetime.now()
    if position == "prefix":
        return f"{today.strftime(datetime_format)}_{string}"
    if position == "postfix":
        return f"{string}_{today.strftime(datetime_format)}"

#---------------------------------------------------------------------------------------------------------------------#
def format_variables(string, input_variables):
    if input_variables:
        variables = str(input_variables).split(",")
        return string.format(*variables)
    else:
        return string
#---------------------------------------------------------------------------------------------------------------------#
#comfy essentials
def p(image):
    return image.permute([0,3,1,2])
def pb(image):
    return image.permute([0,2,3,1])

# Tensor to PIL (WAS Node)
def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

# PIL to Tensor (WAS Node)
def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

def make_3d_mask(mask):
    if len(mask.shape) == 4:
        return mask.squeeze(0)

    elif len(mask.shape) == 2:
        return mask.unsqueeze(0)

    return mask

