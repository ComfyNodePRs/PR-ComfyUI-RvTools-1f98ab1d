import sys
import comfy


FLOAT = ("FLOAT", {"default": 1,
                   "min": -sys.float_info.max,
                   "max": sys.float_info.max,
                   "step": 0.01})

BOOLEAN = ("BOOLEAN", {"default": True})
BOOLEAN_FALSE = ("BOOLEAN", {"default": False})

INT = ("INT", {"default": 1,
               "min": -sys.maxsize,
               "max": sys.maxsize,
               "step": 1})

STRING = ("STRING", {"default": ""})

STRING_ML = ("STRING", {"multiline": True, "default": ""})

STRING_WIDGET = ("STRING", {"forceInput": True})

JSON_WIDGET = ("JSON", {"forceInput": True})

class AnyType(str):
    """A special class that is always equal in not equal comparisons. Credit to pythongosssss"""

    def __eq__(self, _) -> bool:
        return True

    def __ne__(self, __value: object) -> bool:
        return False


any = AnyType("*")

SCHEDULERS_COMFY = comfy.samplers.KSampler.SCHEDULERS
SCHEDULERS_EFFICIENT = comfy.samplers.KSampler.SCHEDULERS + ['AYS SD1', 'AYS SDXL', 'AYS SVD']
SCHEDULERS_IMPACT = comfy.samplers.KSampler.SCHEDULERS + ['AYS SDXL', 'AYS SD1', 'AYS SVD', 'GITS[coeff=1.2]']
SCHEDULERS_RESTART = ('normal', 'karras', 'exponential', 'sgm_uniform', 'simple', 'ddim_uniform', 'simple_test')

SAMPLERS_COMFY = comfy.samplers.KSampler.SAMPLERS
SAMPLERS_RESTART = ['euler', 'euler_cfg_pp', 'euler_ancestral', 'euler_ancestral_cfg_pp', 'heun', 'heunpp2', 'dpm_2', \
                    'dpm_2_ancestral', 'lms', 'dpmpp_2s_ancestral', 'dpmpp_2m', 'ddpm', 'lcm', 'ipndm', 'ipndm_v', 'deis', 'ddim']
