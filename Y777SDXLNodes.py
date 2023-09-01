# ComfyUI Node that Provides a list of recommended SDXL Aspect Ratios
import os 

comfy_dir = os.getcwd()
print("-----> "+ comfy_dir)

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

# ========================================================================
# produces a drop-down list of pre-defined filenames for saving images
# names are saved in filenames.txt
# if entry selected is Custom, then it will use the name set in custom field.
class Y777SaveFilenameList:
     
    @classmethod
    def INPUT_TYPES(s):

        # name_list = ["250", "500", "750", "1000", "1250", "1500", "1750", "2000", "2250", "2500", "2750", "3000", "3250", "3500", "3750", "4000", "4250", "4500", "4750", "5000", "5250", "5500", "5750", "6000"]
        
        print("cwd=" + comfy_dir)        
        file_path = f"{comfy_dir}/custom_nodes/ComfyUI-Y777-Nodes/filenames.txt"
        with open(file_path, "r") as file:
            name_list = [line.strip() for line in file]

        return {
                "required": {
                    "folder": ("STRING", {"default": "foldername/blah"}),
                    "custom_name": ("STRING", {"default": "customName"}),
                    "fileName": (name_list,)
            }
        }


    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("return_name", )
    FUNCTION = "Get_SaveFilename"
    CATEGORY = "Y777"

    def Get_SaveFilename(self, custom_name, fileName, folder):

        if len(folder) > 0:
            folder = f'{folder}/' 

        file_path = f"{comfy_dir}/custom_nodes/ComfyUI-Y777-Nodes/filenames.txt"
        with open(file_path, "r") as file:
            name_list = [line.strip() for line in file]
            
        for fname in name_list:
            if fname == fileName:
                if fname.lower() == "custom":
                    return_name = f"{folder}{custom_name}"
                else:
                    return_name = f"{folder}{t}"
                
        return(return_name,)

# ========================================================

NODE_CLASS_MAPPINGS = {
    "Y777SDXLAspectRatio": Y777SDXLAspectRatio,
    "Y777SDXLAspectRatio_Short": Y777SDXLAspectRatio_Short,
    "Y777SaveFilenameList": Y777SaveFilenameList
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Y777SDXLAspectRatio": "Y777 SDXL Aspect Ratio",
    "Y777SDXLAspectRatio_Short": "Y777 SDXL Aspect Ratio (Short)",
    "Y777SaveFilenameList": "Y777 Save File Name List"
}