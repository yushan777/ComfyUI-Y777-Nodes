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

class Y777SaveFilenameList:

    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                    "fname": ("STRING", {"default": ""}),
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

    def Get_SaveFilename(self, fname, fileName):
        if fileName == "step=1000/base":
            fname = "step=1000/base"
        elif fileName == "step=2000/base":
            fname = "step=2000/base"
        elif fileName == "step=3000/base":
            fname = "step=3000/base"
        elif fileName == "step=4000/base":
            fname = "step=4000/base"
        elif fileName == "step=5000/base":
            fname = "step=5000/base"
        elif fileName == "step=6000/base":
            fname = "step=6000/base"
        elif fileName == "step=7000/base":
            fname = "step=7000/base"
        elif fileName == "step=8000/base":
            fname = "step=8000/base"
        elif fileName == "step=9000/base":
            fname = "step=9000/base"
        elif fileName == "step=10000/base":
            fname = "step=10000/base"
        return(fname,)

NODE_CLASS_MAPPINGS = {
    "Y777SDXLAspectRatio": Y777SDXLAspectRatio,
    "Y777SaveFilenameList": Y777SaveFilenameList
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Y777SDXLAspectRatio": "Y777 SDXL Aspect Ratio",
    "Y777SaveFilenameList": "Y777 Save File Name List"
}
