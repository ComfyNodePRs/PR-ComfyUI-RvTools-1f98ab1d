from ..core import BOOLEAN, STRING, CATEGORY, any, logger, SAMPLERS_COMFY, SAMPLERS_RESTART, SCHEDULERS_COMFY,SCHEDULERS_IMPACT,SCHEDULERS_EFFICIENT,SCHEDULERS_RESTART
from ._names import CLASSES

class RSwitchAudio:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "audio1": ("AUDIO", {"forceInput": True}),
                "audio2": ("AUDIO", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("AUDIO",)   
    
    FUNCTION = "execute"

    def execute(self, Input, audio1=None, audio2=None,):
        logger.debug("Audio Switch: " + str(Input))

        if Input == 1:
            return (audio1,)
        else:
            return (audio2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchBus:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "pipe1": (CLASSES.RBUS_ANY_TYPE.value, {"forceInput": True}),
                "pipe2": (CLASSES.RBUS_ANY_TYPE.value, {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = (CLASSES.RBUS_ANY_TYPE.value,) 
    
    FUNCTION = "execute"

    def execute(self, Input, pipe1=None, pipe2=None,):
        logger.debug("Bus Switch: " + str(Input))

        if Input == 1:
            return (pipe1,)
        else:
            return (pipe2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchClip:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("CLIP", {"forceInput": True}),
                "input2": ("CLIP", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("CLIP",)   
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Clip Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchConditioning:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("CONDITIONING", {"forceInput": True}),
                "input2": ("CONDITIONING", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("CONDITIONING",)  
    RETURN_NAMES = ("c",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Conditioning Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchControlNet:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("CONTROL_NET", {"forceInput": True}),
                "input2": ("CONTROL_NET", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("CONTROL_NET",)  
    RETURN_NAMES = ("cn",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("ControlNet Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchFloat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("FLOAT", {"forceInput": True}),
                "input2": ("FLOAT", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("FLOAT",)  
    RETURN_NAMES = ("float",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Float Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchGuider:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("GUIDER", {"forceInput": True}),
                "input2": ("GUIDER", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("GUIDER",)  
    RETURN_NAMES = ("guider",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Guider Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchImage:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("IMAGE", {"forceInput": True}),
                "input2": ("IMAGE", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("IMAGE",)  
    RETURN_NAMES = ("image",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Image Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchInteger:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("INT", {"forceInput": True}),
                "input2": ("INT", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("INT",)  
    RETURN_NAMES = ("int",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Integer Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchLatent:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("LATENT", {"forceInput": True}),
                "input2": ("LATENT", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("LATENT",)  
    RETURN_NAMES = ("latent",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Latent Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchMask:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("MASK", {"forceInput": True}),
                "input2": ("MASK", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("MASK",)  
    RETURN_NAMES = ("mask",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Mask Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchModel:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("MODEL", {"forceInput": True}),
                "input2": ("MODEL", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("MODEL",)  
    RETURN_NAMES = ("model",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Model Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchBasicPipe:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("BASIC_PIPE", {"forceInput": True}),
                "input2": ("BASIC_PIPE", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("BASIC_PIPE",)  
    RETURN_NAMES = ("pipe",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Pipe Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchDetailerPipe:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("DETAILER_PIPE", {"forceInput": True}),
                "input2": ("DETAILER_PIPE", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("DETAILER_PIPE",)  
    RETURN_NAMES = ("pipe",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Detailer Pipe Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("STRING", {"forceInput": True}),
                "input2": ("STRING", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("STRING",)  
    RETURN_NAMES = ("string",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("String Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchVAE:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("VAE", {"forceInput": True}),
                "input2": ("VAE", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("VAE",)  
    RETURN_NAMES = ("vae",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("VAE Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchSampler:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": (any, {"default": [], "forceInput": True}),
                "input2": (any, {"default": [], "forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (SAMPLERS_COMFY,) 
    RETURN_NAMES = ("sampler_name",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Sampler Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchSampler_Restart:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": (any, {"default": [], "forceInput": True}),
                "input2": (any, {"default": [], "forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (SAMPLERS_RESTART,) 
    RETURN_NAMES = ("sampler_name",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Sampler Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchScheduler:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": (any, {"default": [], "forceInput": True}),
                "input2": (any, {"default": [], "forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (SCHEDULERS_COMFY,) 
    RETURN_NAMES = ("scheduler",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Scheduler Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchScheduler_Impact:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": (any, {"default": [], "forceInput": True}),
                "input2": (any, {"default": [], "forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (SCHEDULERS_IMPACT,) 
    RETURN_NAMES = ("scheduler",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Scheduler Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchScheduler_Efficient:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": (any, {"default": [], "forceInput": True}),
                "input2": (any, {"default": [], "forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (SCHEDULERS_EFFICIENT,) 
    RETURN_NAMES = ("scheduler",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Scheduler Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSwitchScheduler_Restart:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": (any, {"default": [], "forceInput": True}),
                "input2": (any, {"default": [], "forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (SCHEDULERS_RESTART,) 
    RETURN_NAMES = ("scheduler",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):
        logger.debug("Scheduler Switch: " + str(Input))

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True
#---------------------------------------------------------------------------------------------------------------------#  
class RMultiSwitch_Model:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "input1": ("MODEL", {"forceInput": True}),
                "input2": ("MODEL", {"forceInput": True}),
                "input3": ("MODEL", {"forceInput": True}),
                "input4": ("MODEL", {"forceInput": True}),
                "input5": ("MODEL", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("model",)

    FUNCTION = "execute"

    def execute(self, input1=None, input2=None, input3=None, input4=None, input5=None):
        

        if input1 != None:
            return (input1,)
        elif input2 != None:
            return (input2,)
        elif input3 != None:
            return (input3,)
        elif input4 != None:
            return (input4,)
        elif input5 != None:
            return (input5,)

        else:
            raise ValueError("Missing Input: Multi Model Switch has no active Input.")

#---------------------------------------------------------------------------------------------------------------------#  
class RMultiSwitch_CLIP:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "input1": ("CLIP", {"forceInput": True}),
                "input2": ("CLIP", {"forceInput": True}),
                "input3": ("CLIP", {"forceInput": True}),
                "input4": ("CLIP", {"forceInput": True}),
                "input5": ("CLIP", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("CLIP",)
    RETURN_NAMES = ("clip",)

    FUNCTION = "execute"

    def execute(self, input1=None, input2=None, input3=None, input4=None, input5=None):
        

        if input1 != None:
            return (input1,)
        elif input2 != None:
            return (input2,)
        elif input3 != None:
            return (input3,)
        elif input4 != None:
            return (input4,)
        elif input5 != None:
            return (input5,)
        else:
            raise ValueError("Missing Input: Multi CLIP Switch has no active Input")

#---------------------------------------------------------------------------------------------------------------------#  
class RMultiSwitch_VAE:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "input1": ("VAE", {"forceInput": True}),
                "input2": ("VAE", {"forceInput": True}),
                "input3": ("VAE", {"forceInput": True}),
                "input4": ("VAE", {"forceInput": True}),
                "input5": ("VAE", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("VAE",)
    RETURN_NAMES = ("vae",)

    FUNCTION = "execute"

    def execute(self, input1=None, input2=None, input3=None, input4=None, input5=None):
        

        if input1 != None:
            return (input1,)
        elif input2 != None:
            return (input2,)
        elif input3 != None:
            return (input3,)
        elif input4 != None:
            return (input4,)
        elif input5 != None:
            return (input5,)
        else:
            raise ValueError("Missing Input: Multi VAE Switch has no active Input")

#---------------------------------------------------------------------------------------------------------------------#  
class RMultiSwitch_Latent:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "input1": ("LATENT", {"forceInput": True}),
                "input2": ("LATENT", {"forceInput": True}),
                "input3": ("LATENT", {"forceInput": True}),
                "input4": ("LATENT", {"forceInput": True}),
                "input5": ("LATENT", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)

    FUNCTION = "execute"

    def execute(self, input1=None, input2=None, input3=None, input4=None, input5=None):
        

        if input1 != None:
            return (input1,)
        elif input2 != None:
            return (input2,)
        elif input3 != None:
            return (input3,)
        elif input4 != None:
            return (input4,)
        elif input5 != None:
            return (input5,)
        else:
            raise ValueError("Missing Input: Multi Latent Switch has no active Input")
#---------------------------------------------------------------------------------------------------------------------#

