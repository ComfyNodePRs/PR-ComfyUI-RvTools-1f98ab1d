import numpy as np

import torch
import torch.nn.functional as F
import torchvision.transforms.v2 as T

from ..core import CATEGORY, any, logger, tensor2pil, pil2tensor, p, pb, make_3d_mask

#---------------------------------------------------------------------------------------------------------------------#
# IMAGES TO RGB (WAS Node)
class RImagesToRGB:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)

    FUNCTION = "execute"

    def execute(self, images):

        if len(images) > 1:
            tensors = []
            for image in images:
                tensors.append(pil2tensor(tensor2pil(image).convert('RGB')))
            tensors = torch.cat(tensors, dim=0)
            return (tensors, )
        else:
            return (pil2tensor(tensor2pil(images).convert("RGB")), )

#---------------------------------------------------------------------------------------------------------------------#        
#from comfy essentials
class RImageListToBatch:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("images",)
    INPUT_IS_LIST = True

    FUNCTION = "execute"

    def execute(self, images):
        shape = images[0].shape[1:3]
        out = []

        for i in range(len(images)):
            img = p(images[i])
            if images[i].shape[1:3] != shape:
                transforms = T.Compose([
                    T.CenterCrop(min(img.shape[2], img.shape[3])),
                    T.Resize((shape[0], shape[1]), interpolation=T.InterpolationMode.BICUBIC),
                ])
                img = transforms(img)
            out.append(pb(img))
            #image[i] = pb(transforms(img))

        out = torch.cat(out, dim=0)

        return (out,)        

#---------------------------------------------------------------------------------------------------------------------#
#from impact
class RImageBatchToList:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"images": ("IMAGE",), }}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("images",)
    OUTPUT_IS_LIST = (True,)
    
    FUNCTION = "execute"

    def execute(self, images):
        iimages = [images[i:i + 1, ...] for i in range(images.shape[0])]
        return (iimages, )

#---------------------------------------------------------------------------------------------------------------------#
#from impact
class RMaskBatchToList:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                        "masks": ("MASK", ),
                      }
                }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ("MASK", )
    OUTPUT_IS_LIST = (True, )

    FUNCTION = "execute"

    def execute(self, masks):
        if masks is None:
            empty_mask = torch.zeros((64, 64), dtype=torch.float32, device="cpu")
            return ([empty_mask], )

        res = []

        for mask in masks:
            res.append(mask)

        print(f"mask len: {len(res)}")

        res = [make_3d_mask(x) for x in res]

        return (res, )

#---------------------------------------------------------------------------------------------------------------------#
#from impact
class RMaskListToBatch:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                        "mask": ("MASK", ),
                      }
                }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ("MASK", )
    INPUT_IS_LIST = True

    FUNCTION = "execute"

    def execute(self, mask):
        if len(mask) == 1:
            mask = make_3d_mask(mask[0])
            return (mask,)
        elif len(mask) > 1:
            mask1 = make_3d_mask(mask[0])

            for mask2 in mask[1:]:
                mask2 = make_3d_mask(mask2)
                if mask1.shape[1:] != mask2.shape[1:]:
                    mask2 = comfy.utils.common_upscale(mask2.movedim(-1, 1), mask1.shape[2], mask1.shape[1], "lanczos", "center").movedim(1, -1)
                mask1 = torch.cat((mask1, mask2), dim=0)

            return (mask1,)
        else:
            empty_mask = torch.zeros((1, 64, 64), dtype=torch.float32, device="cpu").unsqueeze(0)
            return (empty_mask,)
