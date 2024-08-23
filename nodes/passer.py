from ..core import CATEGORY, any, SAMPLERS_COMFY, SAMPLERS_RESTART, SCHEDULERS_COMFY, SCHEDULERS_IMPACT, SCHEDULERS_EFFICIENT, SCHEDULERS_RESTART

#---------------------------------------------------------------------------------------------------------------------#
class RPassAudio:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "audio": ("AUDIO",),
            },
        }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("AUDIO",)
    FUNCTION = "passthrough"

    def passthrough(self, audio):
        return audio,
    
    @classmethod
    def VALIDATE_INPUTS(self, audio):
        return True

#---------------------------------------------------------------------------------------------------------------------#
class RPassClip:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "clip": ("CLIP",),
            },
        }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("CLIP",)
    FUNCTION = "passthrough"

    def passthrough(self, clip):
        return clip,

    @classmethod
    def VALIDATE_INPUTS(self, clip):
        return True

#---------------------------------------------------------------------------------------------------------------------#
class RPassConditioning:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "conditioning": ("CONDITIONING",),
            },
        }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "passthrough"

    def passthrough(self, conditioning):
        return conditioning,

    @classmethod
    def VALIDATE_INPUTS(self, conditioning):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RPassFloat:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "flt": ("FLOAT", {"forceInput": True}),
            },
        }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "passthrough"

    def passthrough(self, flt):
        return flt,

    @classmethod
    def VALIDATE_INPUTS(self, flt):
        return True

#---------------------------------------------------------------------------------------------------------------------#
#from KJNodes
class RPassImages:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "passthrough"

    def passthrough(self, image):
        return image,

    @classmethod
    def VALIDATE_INPUTS(self, image):
        return True

#---------------------------------------------------------------------------------------------------------------------#
class RPassInteger:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "int1": ("INT", {"forceInput": True}),
            },
        }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("INT",)
    FUNCTION = "passthrough"

    def passthrough(self, int1):
        return int1,

    @classmethod
    def VALIDATE_INPUTS(self, int1):
        return True

#---------------------------------------------------------------------------------------------------------------------#
class RPassLatent:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "latent": ("LATENT",),
            },
        }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "passthrough"

    def passthrough(self, latent):
        return latent,

    @classmethod
    def VALIDATE_INPUTS(self, latent):
        return True

#---------------------------------------------------------------------------------------------------------------------#
class RPassMasks:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "mask": ("MASK",),
            },
        }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("MASK",)
    FUNCTION = "passthrough"

    def passthrough(self, mask):
        return mask,

    @classmethod
    def VALIDATE_INPUTS(self, mask):
        return True

#---------------------------------------------------------------------------------------------------------------------#
class RPassModel:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
            },
        }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("MODEL",)
    FUNCTION = "passthrough"

    def passthrough(self, model):
        return model,

    @classmethod
    def VALIDATE_INPUTS(self, model):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RPassBasicPipe:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "pipe": ("BASIC_PIPE",),
            },
        }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("BASIC_PIPE",)
    FUNCTION = "passthrough"

    def passthrough(self, pipe):
        return pipe,

    @classmethod
    def VALIDATE_INPUTS(self, pipe):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RPassDetailerPipe:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "pipe": ("DETAILER_PIPE",),
            },
        }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("DETAILER_PIPE",)
    FUNCTION = "passthrough"

    def passthrough(self, pipe):
        return pipe,

    @classmethod
    def VALIDATE_INPUTS(self, pipe):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RPassPipeLine:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "pipe": ("PIPE_LINE",),
            },
        }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("PIPE_LINE",)
    FUNCTION = "passthrough"

    def passthrough(self, pipe):
        return pipe,

    @classmethod
    def VALIDATE_INPUTS(self, pipe):
        return True

#---------------------------------------------------------------------------------------------------------------------#
class RPassString:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"forceInput": True}),
            },

        }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("STRING",)
    FUNCTION = "passthrough"

    def passthrough(self, string):
        return string,

    @classmethod
    def VALIDATE_INPUTS(self, string):
        return True

#---------------------------------------------------------------------------------------------------------------------#
class RPassSampler:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "sampler_name": (SAMPLERS_COMFY, {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value

    RETURN_TYPES = (SAMPLERS_COMFY,)
    RETURN_NAMES = ("sampler_name",)

    FUNCTION = "passthrough"

    def passthrough(self, sampler_name):
        return (sampler_name,)

    @classmethod
    def VALIDATE_INPUTS(self, sampler_name):
        return True

#---------------------------------------------------------------------------------------------------------------------#
class RPassSamplerRestart:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "sampler_name": (SAMPLERS_RESTART, {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value

    RETURN_TYPES = (SAMPLERS_RESTART,)
    RETURN_NAMES = ("sampler_name",)

    FUNCTION = "passthrough"

    def passthrough(self, sampler_name):
        return (sampler_name,)

    @classmethod
    def VALIDATE_INPUTS(self, sampler_name):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RPassScheduler_ComfyIU:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "scheduler": (SCHEDULERS_COMFY, {"forceInput": True}),
                }
            }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = (SCHEDULERS_COMFY,)
    RETURN_NAMES = ("scheduler",)

    FUNCTION = "passthrough"

    def passthrough(self, scheduler):
        return (scheduler,)    

    @classmethod
    def VALIDATE_INPUTS(self, scheduler):
        return True

#---------------------------------------------------------------------------------------------------------------------#
class RPassScheduler_Impact:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "scheduler": (SCHEDULERS_IMPACT, {"forceInput": True}),
                }
            }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = (SCHEDULERS_IMPACT,)
    RETURN_NAMES = ("scheduler",)

    FUNCTION = "passthrough"

    def passthrough(self, scheduler):
        return (scheduler,)    

    @classmethod
    def VALIDATE_INPUTS(self, scheduler):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RPassScheduler_Efficient:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "scheduler": (SCHEDULERS_EFFICIENT, {"forceInput": True}),
                }
            }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = (SCHEDULERS_EFFICIENT,)
    RETURN_NAMES = ("scheduler",)

    FUNCTION = "passthrough"

    def passthrough(self, scheduler):
        return (scheduler,)    

    @classmethod
    def VALIDATE_INPUTS(self, scheduler):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RPassScheduler_Restart:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "scheduler": (SCHEDULERS_RESTART, {"forceInput": True}),
                }
            }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = (SCHEDULERS_RESTART,)
    RETURN_NAMES = ("scheduler",)

    FUNCTION = "passthrough"

    def passthrough(self, scheduler):
        return (scheduler,)    

    @classmethod
    def VALIDATE_INPUTS(self, scheduler):
        return True
#---------------------------------------------------------------------------------------------------------------------#
