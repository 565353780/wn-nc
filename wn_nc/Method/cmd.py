import os

def runCMD(command: str) -> bool:
    ret_code = os.system(command)
    return True
