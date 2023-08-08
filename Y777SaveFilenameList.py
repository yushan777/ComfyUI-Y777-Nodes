# ComfyUI Node that Provides a list of file path/name prefix for files to save time typing them in
# dirs are separated by forward slash, last element = prefix

class Y777SaveFilenameList:
    def __init__(self):
        pass

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
    RETURN_NAMES = ("fname",)
    FUNCTION = "Get_AspectRatio"
    CATEGORY = "image"

    def Get_AspectRatio(self, fname, fileName):
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
    "Y777SaveFilenameList": Y777SaveFilenameList
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Y777SaveFilenameList": "Y777 Save File Name List"
}
