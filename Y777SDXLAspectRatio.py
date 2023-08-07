# ComfyUI Node that Provides a list of recommended SDXL Aspect Ratios

class Y777SDXLAspectRatio:
    def __init__(self):
        pass

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
    CATEGORY = "image"

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

            
NODE_CLASS_MAPPINGS = {
    "Y777SDXLAspectRatio": Y777SDXLAspectRatio
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Y777SDXLAspectRatio": "Y777 SDXL Aspect Ratio"
}