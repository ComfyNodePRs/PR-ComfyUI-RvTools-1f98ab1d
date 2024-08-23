
from ..core import CATEGORY, any, logger
from ..core import SAMPLERS_COMFY, SAMPLERS_RESTART, SCHEDULERS_COMFY, SCHEDULERS_IMPACT, SCHEDULERS_EFFICIENT, SCHEDULERS_RESTART

#---------------------------------------------------------------------------------------------------------------------#
#grabbed from ImageSaver and altered
class RSamplerSelector:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "sampler_name": (SAMPLERS_COMFY,),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SELECTOR.value

    RETURN_TYPES = (SAMPLERS_COMFY,)
    RETURN_NAMES = ("sampler_name",)

    FUNCTION = "execute"

    def execute(self, sampler_name):
        return (sampler_name,)

    @classmethod
    def VALIDATE_INPUTS(self, sampler_name):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSamplerSelector_Restart:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "sampler_name": (SAMPLERS_RESTART,),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (SAMPLERS_RESTART,)
    RETURN_NAMES = ("sampler_name",)

    FUNCTION = "execute"

    def execute(self, sampler_name):
        return (sampler_name,)

    @classmethod
    def VALIDATE_INPUTS(self, sampler_name):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSchedulerSelector_ComfyUI:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "scheduler_comfy": (SCHEDULERS_COMFY,),
                }
            }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (SCHEDULERS_COMFY,)
    RETURN_NAMES = ("scheduler_comfy",)

    FUNCTION = "execute"

    def execute(self, scheduler_comfy):
        return (scheduler_comfy,)

    @classmethod
    def VALIDATE_INPUTS(self, scheduler_comfy):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSchedulerSelector_Efficient:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "scheduler_efficient": (SCHEDULERS_EFFICIENT,),
                }
            }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (SCHEDULERS_EFFICIENT,)
    RETURN_NAMES = ("scheduler_efficient",)

    FUNCTION = "execute"

    def execute(self, scheduler_efficient):
        return (scheduler_efficient,)    

    @classmethod
    def VALIDATE_INPUTS(self, scheduler_efficient):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSchedulerSelector_Impact:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "scheduler_impact": (SCHEDULERS_IMPACT,),
                }
            }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (SCHEDULERS_IMPACT,)
    RETURN_NAMES = ("scheduler_impact",)

    FUNCTION = "execute"

    def execute(self, scheduler_impact):
        return (scheduler_impact,)    

    @classmethod
    def VALIDATE_INPUTS(self, scheduler_impact):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSchedulerSelector_Restart:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "scheduler_restart": (SCHEDULERS_RESTART,),
                }
            }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (SCHEDULERS_RESTART,)
    RETURN_NAMES = ("scheduler_restart",)

    FUNCTION = "execute"

    def execute(self, scheduler_restart):
        return (scheduler_restart,)

    @classmethod
    def VALIDATE_INPUTS(self, scheduler_restart):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSchedulerSelector_ComfyUI_Impact:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "scheduler_comfy": (SCHEDULERS_COMFY,),
                "scheduler_impact": (SCHEDULERS_IMPACT,),
                }
            }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (
        SCHEDULERS_COMFY,
        SCHEDULERS_IMPACT,)
    RETURN_NAMES = ("scheduler_comfy", "scheduler_impact",)

    FUNCTION = "execute"

    def execute(self, scheduler_comfy, scheduler_impact):
        return (scheduler_comfy, scheduler_impact,)

    @classmethod
    def VALIDATE_INPUTS(self, scheduler_comfy):
        return True
#---------------------------------------------------------------------------------------------------------------------#
class RSchedulerSelector_Efficient_Impact:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "scheduler_efficient": (SCHEDULERS_EFFICIENT,),
                "scheduler_impact": (SCHEDULERS_IMPACT,),
                }
            }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (
        SCHEDULERS_EFFICIENT,
        SCHEDULERS_IMPACT,)
    RETURN_NAMES = ("scheduler_efficient", "scheduler_impact",)

    FUNCTION = "execute"

    def execute(self, scheduler_efficient, scheduler_impact):
        return (scheduler_efficient, scheduler_impact,)

    @classmethod
    def VALIDATE_INPUTS(self, scheduler_efficient):
        return True

#---------------------------------------------------------------------------------------------------------------------#
