import os
import win32api

def getFileVersion(file_name):
    ''' 获取文件版本信息 '''
    info = win32api.GetFileVersionInfo(file_name, os.sep)
    ms = info['FileVersionMS']
    ls = info['FileVersionLS']
    version = '%d.%d.%d.%d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))
    return version

# 使用示例
file_name = r"D:\code_study\my_code\2024.11.29_allToolSets\tpComAlgorithmMng.dll"
version = getFileVersion(file_name)
print(f"DLL Version: {version}")