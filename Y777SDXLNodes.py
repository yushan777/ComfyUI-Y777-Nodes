# ComfyUI Node that Provides a list of recommended SDXL Aspect Ratios

class Y777SDXLAspectRatio:

    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                    "width": ("INT", {"default": 1024, "min": 512, "max": 2048,}),
                    "height": ("INT", {"default": 1024, "min": 512, "max": 2048}),
                    "aspectRatio": ([
                    "Custom",
                    "1. 1024x1024 square (1:1)", 
                    "2. 896x1152 portrait (1:1.29)", 
                    "3. 832x1216 portrait (1:1.46)", 
                    "4. 768x1344 portrait (1:1.75)", 
                    "5. 640x1536 portrait (1:2.4)", 
                    "6. 1152x896 landscape (1.29:1)", 
                    "7. 1216x832 landscape (1.46:1)",                     
                    "8. 1344x768 landscape (1.75:1)", 
                    "9. 1536x640 landscape (2.4:1)"],)
            }
        }
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("Width", "Height")
    FUNCTION = "Get_AspectRatio"
    CATEGORY = "Y777"

    def Get_AspectRatio(self, width, height, aspectRatio):
        if aspectRatio == "1. 1024x1024 square (1:1)":
            width, height = 1024, 1024
        elif aspectRatio == "2. 896x1152 portrait (1:1.29)":
            width, height = 896, 1152
        elif aspectRatio == "3. 832x1216 portrait (1:1.46)":
            width, height = 832, 1216
        elif aspectRatio == "4. 768x1344 portrait (1:1.75)":
            width, height = 768, 1344
        elif aspectRatio == "5. 640x1536 portrait (1:2.4)":
            width, height = 640, 1536
        elif aspectRatio == "6. 1152x896 landscape (1.29:1)":
            width, height = 1152, 896
        elif aspectRatio == "7. 1216x832 landscape (1.46:1)":
            width, height = 1216, 832
        elif aspectRatio == "8. 1344x768 landscape (1.75:1)":
            width, height = 1344, 768
        elif aspectRatio == "9. 1536x640 landscape (2.4:1)":
            width, height = 1536, 640
        return(width, height)

class Y777SDXLAspectRatio_Short:
    # cut down version of the one above for testing, 
    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                    "width": ("INT", {"default": 1024, "min": 512, "max": 2048,}),
                    "height": ("INT", {"default": 1024, "min": 512, "max": 2048}),
                    "aspectRatio": ([
                    "1. 1024x1024 square (1:1)", 
                    "2. 896x1152 portrait (1:1.29)", 
                    "3. 832x1216 portrait (1:1.46)",  
                    "4. 1216x832 landscape (1.46:1)",                     
                    "5. 1344x768 landscape (1.75:1)"],)
            }
        }
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("Width", "Height")
    FUNCTION = "Get_AspectRatio"
    CATEGORY = "Y777"

    def Get_AspectRatio(self, width, height, aspectRatio):
        if aspectRatio == "1. 1024x1024 square (1:1)":
            width, height = 1024, 1024
        elif aspectRatio == "2. 896x1152 portrait (1:1.29)":
            width, height = 896, 1152
        elif aspectRatio == "3. 832x1216 portrait (1:1.46)":
            width, height = 832, 1216
        elif aspectRatio == "4. 1216x832 landscape (1.46:1)":
            width, height = 1216, 832
        elif aspectRatio == "5. 1344x768 landscape (1.75:1)":
            width, height = 1344, 768
        return(width, height)

# ===========================================================
class Y777SaveFilenameList:
    # Fixed List of filenames, with custom option
    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                    "custom_name": ("STRING", {"default": ""}),
                    "fileName": ([
                    "Custom",
                    "step=1000/base",
                    "step=2000/base", 
                    "step=3000/base", 
                    "step=4000/base", 
                    "step=5000/base", 
                    "step=6000/base", 
                    "step=7000/base",                     
                    "step=8000/base", 
                    "step=9000/base", 
                    "step=10000/base"],)
            }
        }
        
    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("fname", )
    FUNCTION = "Get_SaveFilename"
    CATEGORY = "Y777"

    def Get_SaveFilename(self, custom_name, fileName):
        if fileName == "step=1000/base":
            return_name = "step=1000/base"
        elif fileName == "step=2000/base":
            return_name = "step=2000/base"
        elif fileName == "step=3000/base":
            return_name = "step=3000/base"
        elif fileName == "step=4000/base":
            return_name = "step=4000/base"
        elif fileName == "step=5000/base":
            return_name = "step=5000/base"
        elif fileName == "step=6000/base":
            return_name = "step=6000/base"
        elif fileName == "step=7000/base":
            return_name = "step=7000/base"
        elif fileName == "step=8000/base":
            return_name = "step=8000/base"
        elif fileName == "step=9000/base":
            return_name = "step=9000/base"
        elif fileName == "step=10000/base":
            return_name = "step=10000/base"
        return(return_name,)

# ===========================================================
class Y777SaveFilenameList2:
    # Fixed List of filenames, with custom folder and name

    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                    "folder": ("STRING", {"default": "LR"}),
                    "custom_name": ("STRING", {"default": ""}),
                    "fileName": ([
                    "Custom",
                    "step_1000",
                    "step_2000", 
                    "step_3000", 
                    "step_4000", 
                    "step_5000", 
                    "step_6000", 
                    "step_7000",                     
                    "step_8000", 
                    "step_9000", 
                    "step_10000"],)
            }
        }


    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("return_name", )
    FUNCTION = "Get_SaveFilename"
    CATEGORY = "Y777"

    def Get_SaveFilename(self, custom_name, fileName, folder):

        if len(folder) > 0:
            folder = f'{folder}/'

        if fileName == "step_1000":
            return_name = f"{folder}step_1000"
        elif fileName == "step_2000":
            return_name = f"{folder}step_2000"
        elif fileName == "step_3000":
            return_name = f"{folder}step_3000"
        elif fileName == "step_4000":
            return_name = f"{folder}step_4000"
        elif fileName == "step_5000":
            return_name = f"{folder}step_5000"
        elif fileName == "step_6000":
            return_name = f"{folder}step_6000"
        elif fileName == "step_7000":
            return_name = f"{folder}step_7000"
        elif fileName == "step_8000":
            return_name = f"{folder}step_8000"
        elif fileName == "step_9000":
            return_name = f"{folder}step_9000"
        elif fileName == "step_10000":
            return_name = f"{folder}step_10000"
        elif fileName == "Custom":
            return_name = f"{folder}{custom_name}"
        return(return_name,)

# ===========================================================

NODE_CLASS_MAPPINGS = {
    "Y777SDXLAspectRatio": Y777SDXLAspectRatio,
    "Y777SDXLAspectRatio_Short": Y777SDXLAspectRatio_Short,
    "Y777SaveFilenameList": Y777SaveFilenameList,
    "Y777SaveFilenameList2": Y777SaveFilenameList2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Y777SDXLAspectRatio": "Y777 SDXL Aspect Ratio",
    "Y777SDXLAspectRatio_Short": "Y777 SDXL Aspect Ratio (Short)",
    "Y777SaveFilenameList": "Y777 Save File Name List",
    "Y777SaveFilenameList2": "Y777 Save File Name List 2"
}