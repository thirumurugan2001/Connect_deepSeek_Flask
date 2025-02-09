from deepSeek import *

# This deepSeekController function is use to Validate the payload data["prompt"] is not empty and string format.
def deepSeekController(data):
    try:
        if "Question" in data:
            if data["Question"] != "":
                return DeepSeektext(data)
            else:
                return {
                    "message":"Invaild data !",
                    "statusCode":400
                }
        else:
            return {
                "message":"All fields (Question) are required.",
                "statusCode":400
            }
    except Exception as e:
        return {
                "Error":str(e),
                "statusCode":400
            }