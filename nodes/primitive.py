from ..core import BOOLEAN, CATEGORY, STRING, INT, FLOAT, STRING_ML


class RBoolean:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "boolean": BOOLEAN,
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PRIMITIVE.value
    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("boolean",)

    FUNCTION = "execute"

    def execute(self, boolean=True):
        return (boolean,)


class RText:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string": STRING,
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PRIMITIVE.value
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)

    FUNCTION = "execute"

    def execute(self, string=""):
        return (string,)


class RTextML:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string": STRING_ML,
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PRIMITIVE.value
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)

    FUNCTION = "execute"

    def execute(self, string=""):
        return (string,)


class RInteger:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "int": INT,
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PRIMITIVE.value
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("int",)

    FUNCTION = "execute"

    def execute(self, int=True):
        return (int,)


class RFloat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "float": FLOAT,
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PRIMITIVE.value
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("float",)

    FUNCTION = "execute"

    def execute(self, float=True):
        return (float,)
