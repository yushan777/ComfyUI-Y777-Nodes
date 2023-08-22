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
class Y777SaveFilenameList3:
    # Fixed List of filenames, with custom folder and name

    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                    "folder": ("STRING", {"default": "LR"}),
                    "custom_name": ("STRING", {"default": ""}),
                    "fileName": ([
                    "Custom",
                    "step_100", 
                    "step_200", 
                    "step_300", 
                    "step_400", 
                    "step_500", 
                    "step_600", 
                    "step_700", 
                    "step_800", 
                    "step_900", 
                    "step_1000", 
                    "step_1100", 
                    "step_1200", 
                    "step_1300", 
                    "step_1400", 
                    "step_1500", 
                    "step_1600", 
                    "step_1700", 
                    "step_1800", 
                    "step_1900", 
                    "step_2000", 
                    "step_2100", 
                    "step_2200", 
                    "step_2300", 
                    "step_2400", 
                    "step_2500", 
                    "step_2600", 
                    "step_2700", 
                    "step_2800", 
                    "step_2900", 
                    "step_3000", 
                    "step_3100", 
                    "step_3200", 
                    "step_3300", 
                    "step_3400", 
                    "step_3500", 
                    "step_3600", 
                    "step_3700", 
                    "step_3800", 
                    "step_3900", 
                    "step_4080", 
                    "step_4100", 
                    "step_4200", 
                    "step_4300", 
                    "step_4400", 
                    "step_4500", 
                    "step_4600", 
                    "step_4700", 
                    "step_4800", 
                    "step_4900", 
                    "step_5000"],)
            }
        }


    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("return_name", )
    FUNCTION = "Get_SaveFilename"
    CATEGORY = "Y777"

    def Get_SaveFilename(self, custom_name, fileName, folder):

        if len(folder) > 0:
            folder = f'{folder}/'

        if fileName == "step_100":
            return_name = f"{folder}step_100"
        elif fileName == "step_200":
            return_name = f"{folder}step_200"
        elif fileName == "step_300":
            return_name = f"{folder}step_300"
        elif fileName == "step_400":
            return_name = f"{folder}step_400"
        elif fileName == "step_500":
            return_name = f"{folder}step_500"
        elif fileName == "step_600":
            return_name = f"{folder}step_600"
        elif fileName == "step_700":
            return_name = f"{folder}step_700"
        elif fileName == "step_800":
            return_name = f"{folder}step_800"
        elif fileName == "step_900":
            return_name = f"{folder}step_900"
        elif fileName == "step_1000":
            return_name = f"{folder}step_1000"
        elif fileName == "step_1100":
            return_name = f"{folder}step_1100"
        elif fileName == "step_1200":
            return_name = f"{folder}step_1200"
        elif fileName == "step_1300":
            return_name = f"{folder}step_1300"
        elif fileName == "step_1400":
            return_name = f"{folder}step_1400"
        elif fileName == "step_1500":
            return_name = f"{folder}step_1500"
        elif fileName == "step_1600":
            return_name = f"{folder}step_1600"
        elif fileName == "step_1700":
            return_name = f"{folder}step_1700"
        elif fileName == "step_1800":
            return_name = f"{folder}step_1800"
        elif fileName == "step_1900":
            return_name = f"{folder}step_1900"
        elif fileName == "step_2000":
            return_name = f"{folder}step_2000"
        elif fileName == "step_2100":
            return_name = f"{folder}step_2100"
        elif fileName == "step_2200":
            return_name = f"{folder}step_2200"
        elif fileName == "step_2300":
            return_name = f"{folder}step_2300"
        elif fileName == "step_2400":
            return_name = f"{folder}step_2400"
        elif fileName == "step_2500":
            return_name = f"{folder}step_2500"
        elif fileName == "step_2600":
            return_name = f"{folder}step_2600"
        elif fileName == "step_2700":
            return_name = f"{folder}step_2700"
        elif fileName == "step_2800":
            return_name = f"{folder}step_2800"
        elif fileName == "step_2900":
            return_name = f"{folder}step_2900"
        elif fileName == "step_3000":
            return_name = f"{folder}step_3000"
        elif fileName == "step_3100":
            return_name = f"{folder}step_3100"
        elif fileName == "step_3200":
            return_name = f"{folder}step_3200"
        elif fileName == "step_3300":
            return_name = f"{folder}step_3300"
        elif fileName == "step_3400":
            return_name = f"{folder}step_3400"
        elif fileName == "step_3500":
            return_name = f"{folder}step_3500"
        elif fileName == "step_3600":
            return_name = f"{folder}step_3600"
        elif fileName == "step_3700":
            return_name = f"{folder}step_3700"
        elif fileName == "step_3800":
            return_name = f"{folder}step_3800"
        elif fileName == "step_3900":
            return_name = f"{folder}step_3900"
        elif fileName == "step_4000":
            return_name = f"{folder}step_4000"
        elif fileName == "step_4100":
            return_name = f"{folder}step_4100"
        elif fileName == "step_4200":
            return_name = f"{folder}step_4200"
        elif fileName == "step_4300":
            return_name = f"{folder}step_4300"
        elif fileName == "step_4400":
            return_name = f"{folder}step_4400"
        elif fileName == "step_4500":
            return_name = f"{folder}step_4500"
        elif fileName == "step_4600":
            return_name = f"{folder}step_4600"
        elif fileName == "step_4700":
            return_name = f"{folder}step_4700"
        elif fileName == "step_4800":
            return_name = f"{folder}step_4800"
        elif fileName == "step_4900":
            return_name = f"{folder}step_4900"
        elif fileName == "step_5000":
            return_name = f"{folder}step_5000"
        elif fileName == "Custom":
            return_name = f"{folder}{custom_name}"
        return(return_name,)

# ===========================================================


class Y777SaveFilenameList4:
    # Fixed List of filenames, with custom folder and name    
    @classmethod
    def INPUT_TYPES(s):

        # test_list = ["250", "500", "750", "1000", "1250", "1500", "1750", "2000", "2250", "2500", "2750", "3000", "3250", "3500", "3750", "4000", "4250", "4500", "4750", "5000", "5250", "5500", "5750", "6000"]
        
        print("cwd=" + comfy_dir)        
        file_path = f"{comfy_dir}/custom_nodes/ComfyUI-Y777-Nodes/filenames.txt"
        with open(file_path, "r") as file:
            test_list = [line.strip() for line in file]

        return {
                "required": {
                    "folder": ("STRING", {"default": "LR"}),
                    "custom_name": ("STRING", {"default": ""}),
                    "fileName": (test_list,)
            }
        }


    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("return_name", )
    FUNCTION = "Get_SaveFilename"
    CATEGORY = "Y777"

    def Get_SaveFilename(self, custom_name, fileName, folder):

        if len(folder) > 0:
            folder = f'{folder}/'

        # test_list = ["250", "500", "750", "1000", "1250", "1500", "1750", "2000", "2250", "2500", "2750", "3000", "3250", "3500", "3750", "4000", "4250", "4500", "4750", "5000", "5250", "5500", "5750", "6000"]

        file_path = f"{comfy_dir}/custom_nodes/ComfyUI-Y777-Nodes/filenames.txt"
        with open(file_path, "r") as file:
            test_list = [line.strip() for line in file]
            
        for t in test_list:
            if t == fileName:
                if t == "Custom":
                    return_name = f"{folder}{custom_name}"
                else:
                    return_name = f"{folder}{t}"
                
        return(return_name,)

# ========================================================

NODE_CLASS_MAPPINGS = {
    "Y777SDXLAspectRatio": Y777SDXLAspectRatio,
    "Y777SDXLAspectRatio_Short": Y777SDXLAspectRatio_Short,
    "Y777SaveFilenameList": Y777SaveFilenameList,
    "Y777SaveFilenameList2": Y777SaveFilenameList2,
    "Y777SaveFilenameList3": Y777SaveFilenameList3,
    "Y777SaveFilenameList4": Y777SaveFilenameList4
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Y777SDXLAspectRatio": "Y777 SDXL Aspect Ratio",
    "Y777SDXLAspectRatio_Short": "Y777 SDXL Aspect Ratio (Short)",
    "Y777SaveFilenameList": "Y777 Save File Name List",
    "Y777SaveFilenameList2": "Y777 Save File Name List 2",
    "Y777SaveFilenameList3": "Y777 Save File Name List 3",
    "Y777SaveFilenameList4": "Y777 Save File Name List 4"
}