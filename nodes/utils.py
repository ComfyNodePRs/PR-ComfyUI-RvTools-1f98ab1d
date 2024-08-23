import re

from ..core import STRING, TEXTS, KEYS, CATEGORY, any, logger
from ._names import CLASSES

#---------------------------------------------------------------------------------------------------------------------#
# based on Logic-Utils
class RReplaceString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "String": ("STRING", {"default": ""}),
                "Regex": ("STRING", {"default": ""}),
                "ReplaceWith": ("STRING", {"default": ""}),
            }
    }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.OPERATION.value
    RETURN_TYPES = ("STRING",)

    FUNCTION = "execute"
    
    def execute(self, String, Regex, ReplaceWith):
        # using regex
        return (re.sub(Regex, ReplaceWith, String),)

    @classmethod
    def VALIDATE_INPUTS(self, String):
        return True

#---------------------------------------------------------------------------------------------------------------------#
## based on WAS-Node
class RMergeStrings:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input1": (any, {"default": ""}),
                "input2": (any, {"default": ""}),
                "Delimiter": ("STRING", {"default": ", "}),
            }
    }
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.OPERATION.value
    RETURN_TYPES = ("STRING", any,)
    FUNCTION = "execute"
    
    def execute(self, Delimiter, **kwargs):
        text_inputs = []

        # Handle special case where delimiter is "\n" (literal newline).
        if Delimiter in ("\n", "\\n"):
            Delimiter = "\n"

        # Iterate over the received inputs in sorted order.
        for k in sorted(kwargs.keys()):
            v = kwargs[k]

            # Only process string input ports.
            if isinstance(v, str):
               if v != "":
                  text_inputs.append(v)

        merged_text = Delimiter.join(text_inputs)

        return (merged_text,)

        #merged = str(input1) + str(Delimiter) + str(input2)
        #return (merged, merged)

    @classmethod
    def VALIDATE_INPUTS(self, Delimiter):
        return True

#---------------------------------------------------------------------------------------------------------------------#
# based on CrysTools
class RMergeStringsLarge:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "string_1": ("STRING", {"forceInput": True}),
                "string_2": ("STRING", {"forceInput": True}),
                "string_3": ("STRING", {"forceInput": True}),
                "string_4": ("STRING", {"forceInput": True}),
                "string_5": ("STRING", {"forceInput": True}),
                "string_6": ("STRING", {"forceInput": True}),
                "string_7": ("STRING", {"forceInput": True}),
                "string_8": ("STRING", {"forceInput": True}),
                "string_9": ("STRING", {"forceInput": True}),
                "string_10": ("STRING", {"forceInput": True}),
                "Delimiter": ("STRING", {"default": ", "}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.OPERATION.value
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)

    FUNCTION = "execute"

    def execute(self,
                string_1=None,
                string_2=None,
                string_3=None,
                string_4=None,
                string_5=None,
                string_6=None,
                string_7=None,
                string_8=None,
                string_9=None,
                string_10=None,
                Delimiter=""):

        list_str = []

        if string_1 is not None and string_1 != "":
            list_str.append(string_1)
        if string_2 is not None and string_2 != "":
            list_str.append(string_2)
        if string_3 is not None and string_3 != "":
            list_str.append(string_3)
        if string_4 is not None and string_4 != "":
            list_str.append(string_4)
        if string_5 is not None and string_5 != "":
            list_str.append(string_5)
        if string_6 is not None and string_6 != "":
            list_str.append(string_6)
        if string_7 is not None and string_7 != "":
            list_str.append(string_7)
        if string_8 is not None and string_8 != "":
            list_str.append(string_8)
        if string_9 is not None and string_9 != "":
            list_str.append(string_9)
        if string_10 is not None and string_10 != "":
            list_str.append(string_10)

        return Delimiter.join(list_str),
#---------------------------------------------------------------------------------------------------------------------#
# based on CrysTools
class RBusAny8CH_IN:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                CLASSES.RBUS_ANY_TYPE.value: (CLASSES.RBUS_ANY_TYPE.value,),
                "any_1": (any,),
                "any_2": (any,),
                "any_3": (any,),
                "any_4": (any,),
                "any_5": (any,),
                "any_6": (any,),
                "any_7": (any,),
                "any_8": (any,),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = (CLASSES.RBUS_ANY_TYPE.value,)

    FUNCTION = "execute"

    def execute(self, pipe=None, any_1=None, any_2=None, any_3=None, any_4=None, any_5=None, any_6=None, any_7=None, any_8=None):
        any_1_original = None
        any_2_original = None
        any_3_original = None
        any_4_original = None
        any_5_original = None
        any_6_original = None
        any_7_original = None
        any_8_original = None

        if pipe != None:
            any_1_original, any_2_original, any_3_original, any_4_original, any_5_original, any_6_original, any_7_original, any_8_original = pipe

        RBusAnyMod = []

        RBusAnyMod.append(any_1 if any_1 is not None else any_1_original)
        RBusAnyMod.append(any_2 if any_2 is not None else any_2_original)
        RBusAnyMod.append(any_3 if any_3 is not None else any_3_original)
        RBusAnyMod.append(any_4 if any_4 is not None else any_4_original)
        RBusAnyMod.append(any_5 if any_5 is not None else any_5_original)
        RBusAnyMod.append(any_6 if any_6 is not None else any_6_original)
        RBusAnyMod.append(any_7 if any_7 is not None else any_7_original)
        RBusAnyMod.append(any_8 if any_8 is not None else any_8_original)

        return (RBusAnyMod,)
#---------------------------------------------------------------------------------------------------------------------#
# based on CrysTools
class RBusAny8CH_OUT:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                CLASSES.RBUS_ANY_TYPE.value: (CLASSES.RBUS_ANY_TYPE.value,),
            },
            "optional": {
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = (CLASSES.RBUS_ANY_TYPE.value, any, any, any, any, any, any, any, any,)
    RETURN_NAMES = (CLASSES.RBUS_ANY_TYPE.value, "any_1", "any_2", "any_3", "any_4", "any_5", "any_6", "any_7", "any_8",)

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        any_1, any_2, any_3, any_4, any_5, any_6, any_7, any_8 = pipe
        return pipe, any_1, any_2, any_3, any_4, any_5, any_6, any_7, any_8
#---------------------------------------------------------------------------------------------------------------------#
# based on CrysTools    
class RBusAny12CH_IN:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                CLASSES.RBUS_ANY_TYPE.value: (CLASSES.RBUS_ANY_TYPE.value,),
                "any_1": (any,),
                "any_2": (any,),
                "any_3": (any,),
                "any_4": (any,),
                "any_5": (any,),
                "any_6": (any,),
                "any_7": (any,),
                "any_8": (any,),
                "any_9": (any,),
                "any_10": (any,),
                "any_11": (any,),
                "any_12": (any,),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = (CLASSES.RBUS_ANY_TYPE.value,)

    FUNCTION = "execute"

    def execute(self, pipe=None, any_1=None, any_2=None, any_3=None, any_4=None, any_5=None, any_6=None, any_7=None, any_8=None, any_9=None, any_10=None, any_11=None, any_12=None):
        any_1_original = None
        any_2_original = None
        any_3_original = None
        any_4_original = None
        any_5_original = None
        any_6_original = None
        any_7_original = None
        any_8_original = None
        any_9_original = None
        any_10_original = None
        any_11_original = None
        any_12_original = None

        if pipe != None:
            any_1_original, any_2_original, any_3_original, any_4_original, any_5_original, any_6_original, any_7_original, any_8_original, any_9_original, any_10_original, any_11_original, any_12_original = pipe

        RBusAnyMod = []

        RBusAnyMod.append(any_1 if any_1 is not None else any_1_original)
        RBusAnyMod.append(any_2 if any_2 is not None else any_2_original)
        RBusAnyMod.append(any_3 if any_3 is not None else any_3_original)
        RBusAnyMod.append(any_4 if any_4 is not None else any_4_original)
        RBusAnyMod.append(any_5 if any_5 is not None else any_5_original)
        RBusAnyMod.append(any_6 if any_6 is not None else any_6_original)
        RBusAnyMod.append(any_7 if any_7 is not None else any_7_original)
        RBusAnyMod.append(any_8 if any_8 is not None else any_8_original)
        RBusAnyMod.append(any_9 if any_9 is not None else any_9_original)
        RBusAnyMod.append(any_10 if any_10 is not None else any_10_original)
        RBusAnyMod.append(any_11 if any_11 is not None else any_11_original)
        RBusAnyMod.append(any_12 if any_12 is not None else any_12_original)


        return (RBusAnyMod,)
#---------------------------------------------------------------------------------------------------------------------#
# based on CrysTools 
class RBusAny12CH_OUT:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                CLASSES.RBUS_ANY_TYPE.value: (CLASSES.RBUS_ANY_TYPE.value,),
            },
            "optional": {
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = (CLASSES.RBUS_ANY_TYPE.value, any, any, any, any, any, any, any, any, any, any, any, any,)
    RETURN_NAMES = (CLASSES.RBUS_ANY_TYPE.value, "any_1", "any_2", "any_3", "any_4", "any_5", "any_6", "any_7", "any_8", "any_9", "any_10", "any_11", "any_12",)

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        any_1, any_2, any_3, any_4, any_5, any_6, any_7, any_8, any_9, any_10, any_11, any_12 = pipe
        return pipe, any_1, any_2, any_3, any_4, any_5, any_6, any_7, any_8, any_9, any_10, any_11, any_12
#---------------------------------------------------------------------------------------------------------------------------------------------------#
# based on Mikey Nodes
class RIntegerToString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"int_": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "forceInput": True}),
                }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ("STRING", )

    FUNCTION = 'execute'

    def execute(self, int_):
        return (f'{int_}',)

    @classmethod
    def VALIDATE_INPUTS(self, int_):
        return True

#---------------------------------------------------------------------------------------------------------------------------------------------------#
# based on Mikey Nodes
class RFloatToString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"float_": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1000000.0, "forceInput": True}),
                }        
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ('STRING',)

    FUNCTION = 'execute'

    def execute(self, float_):
        return (f'{float_}',)

    @classmethod
    def VALIDATE_INPUTS(self, float_):
        return True

#---------------------------------------------------------------------------------------------------------------------
# based on Mikey Nodes
class RFloatToInteger:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"_float": ("FLOAT", {"default": 0.0, "forceInput": True}),
                }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ("INT",)

    FUNCTION = "execute"

    def execute(self, _float):
        return (int(_float),)

    @classmethod
    def VALIDATE_INPUTS(self, _float):
        return True

#---------------------------------------------------------------------------------------------------------------------#    
class RSizesPlusXYOffset:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Width": ("INT", {"default": 150}),
                "Height": ("INT", {"default": 20}),
            },
            "optional": {
                "Offset_Y": ("INT",{"default": 0}),
                "Offset_X": ("INT",{"default": 0}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.OPERATION.value
    RETURN_TYPES = ("INT","INT","INT","INT",)
    RETURN_NAMES = ("width","height","offset_y","offset_x",)

    FUNCTION = "execute"

    def execute(self, Width, Height, Offset_Y, Offset_X):
        return (Width,Height,Offset_Y,Offset_X,)
    
    @classmethod
    def VALIDATE_INPUTS(self, Width, Height):
        return True

#---------------------------------------------------------------------------------------------------------------------#
#based on LogicUtil
class RStringListToCombo:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"default": ""}),
                "separator": ("STRING", {"default": "$"}),
            },
            "optional": {
                "index": ("INT", {"default": 0}),
        }
    }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = (any,)
    FUNCTION = "execute"

    def execute(self, string, separator, index = 0):
        if isinstance(string, (float, int, bool)):
            return (string,)
        if separator == "" or separator == None or separator not in string:
            return (string,)
        # check length
        splitted = string.split(separator)
        if index >= len(splitted):
            return (splitted[-1],)
        return (splitted[index],)
#---------------------------------------------------------------------------------------------------------------------#
class RComboToString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "combo": (any, {"default": []}),
                "separator": ("STRING", {"default": "$"}),
        }
    }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"

    def execute(self, combo, separator):
        if isinstance(combo, (str, float, int, bool)):
            return (combo,)
        return (separator.join(combo),)

    @classmethod
    def VALIDATE_INPUTS(self, combo):
        return True

#---------------------------------------------------------------------------------------------------------------------#  
class RIfExecute:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "on_true": (any, {}),
                "on_false": (any, {}),
                "boolean": ("BOOLEAN", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.OPERATION.value
    RETURN_TYPES = (any,)

    FUNCTION = "execute"

    def execute(self, on_true, on_false, boolean=True):
        logger.debug("Any switch: " + str(boolean))

        if boolean:
            return (on_true,)
        else:
            return (on_false,)
 
    @classmethod
    def VALIDATE_INPUTS(self, boolean):
        return True

