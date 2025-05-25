import ctypes
import os
import re
import winreg
from ctypes import wintypes

# 定义Windows API所需的数据结构和函数
advapi32 = ctypes.WinDLL("advapi32.dll")

RegOpenKeyEx = advapi32.RegOpenKeyExW
RegOpenKeyEx.argtypes = [
    wintypes.HKEY,
    wintypes.LPCWSTR,
    wintypes.DWORD,
    wintypes.DWORD,  # 使用 DWORD 替代 REGSAM
    ctypes.POINTER(wintypes.HKEY),
]
RegOpenKeyEx.restype = wintypes.LONG

RegQueryValueEx = advapi32.RegQueryValueExW
RegQueryValueEx.argtypes = [
    wintypes.HKEY,
    wintypes.LPCWSTR,
    wintypes.LPDWORD,
    ctypes.POINTER(wintypes.DWORD),
    ctypes.POINTER(ctypes.c_ubyte),
    ctypes.POINTER(wintypes.DWORD),
]
RegQueryValueEx.restype = wintypes.LONG

RegCloseKey = advapi32.RegCloseKey
RegCloseKey.argtypes = [wintypes.HKEY]
RegCloseKey.restype = wintypes.LONG

# 常量定义
ERROR_SUCCESS = 0
KEY_READ = winreg.KEY_READ
REG_BINARY = winreg.REG_BINARY

root_key = winreg.HKEY_CURRENT_USER
sub_key = r"SOFTWARE\Tencent\Call-of-Duty"
pattern = re.compile(
    r"^CODM_\d+_"  # 动态前缀
    r"iMSDK_CN_"  # 固定模块标识
    r"(PVE|PVP|TD|Br|PVEFiring|PVPFiring|TDFiring|BrFiring)"  # 扩展模式部分
    r"(_(?:RotateSensitive|AimRotate|ReddotHolo|Sniper|Free|ACOG|[\dX]+|SkyVehicle|GroundVehicle|Vertical|Ult).*?)?"  # 动态描述部分
    r"_h\d+$",  # 固定后缀哈希值
    re.IGNORECASE,
)


def read_raw_binary_value(hkey, sub_key, value_name):
    """
    直接读取注册表键值的原始二进制数据（忽略类型）
    """
    h_key = wintypes.HKEY()
    if RegOpenKeyEx(hkey, sub_key, 0, KEY_READ, ctypes.byref(h_key)) != ERROR_SUCCESS:
        return None

    data_type = wintypes.DWORD()
    data_size = wintypes.DWORD()

    # 第一次调用获取数据大小
    if (
            RegQueryValueEx(
                h_key,
                value_name,
                None,
                ctypes.byref(data_type),
                None,
                ctypes.byref(data_size),
            )
            != ERROR_SUCCESS
    ):
        RegCloseKey(h_key)
        return None

    # 分配缓冲区并读取数据（使用无符号字节数组）
    data_buffer = (ctypes.c_ubyte * data_size.value)()
    if (
            RegQueryValueEx(
                h_key, value_name, None, None, data_buffer, ctypes.byref(data_size)
            )
            != ERROR_SUCCESS
    ):
        RegCloseKey(h_key)
        return None

    RegCloseKey(h_key)
    return bytes(data_buffer)


def read_codm_registry_keys():
    try:
        # 打开注册表键
        with winreg.OpenKey(
                root_key, sub_key, 0, winreg.KEY_READ | winreg.KEY_WRITE
        ) as key:
            print(f"[*]成功打开注册表路径: HKEY_CURRENT_USER\\{sub_key}")
            i = 0
            while True:
                try:
                    # 枚举所有键值
                    name, value, value_type = winreg.EnumValue(key, i)
                    if pattern.match(name) and value_type == winreg.REG_DWORD:
                        # 使用底层API读取原始十六进制数据
                        raw_data = read_raw_binary_value(root_key, sub_key, name)
                        if raw_data:
                            print(f"\n[操作] 正在处理键: {name}")
                            print(
                                f"[原始十六进制值]: {' '.join(f'{b:02X}' for b in raw_data)}"
                            )

                            # 修改第一个字节为0x01
                            modified_data = bytes([0x01]) + raw_data[1:]
                            print(
                                f"[修改后十六进制值]: {' '.join(f'{b:02X}' for b in modified_data)}"
                            )

                            # 写入新值（需管理员权限）
                            with winreg.OpenKey(
                                    root_key, sub_key, 0, winreg.KEY_SET_VALUE
                            ) as write_key:
                                winreg.SetValueEx(
                                    write_key, name, 0, REG_BINARY, modified_data
                                )
                                print("[修改成功]")

                    i += 1
                except OSError:
                    print("[修改已修改完毕]")  # 无更多键值时退出
                    break

    except FileNotFoundError:
        print(f"[错误]: 注册表路径不存在 HKEY_CURRENT_USER\\{sub_key}")
    except Exception as e:
        print(f"[未知错误]: {str(e)}")


if __name__ == "__main__":
    # ——————————————————————————————————————————
    print("仅供学习交流,开源免费工具")
    print("\nbilibili: DC随便 UID:3493117248407780")
    print("\nbilibili: https://space.bilibili.com/3493117248407780")
    print("github:")

    # ——————————————————————————————————————————
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("[错误] 请以管理员身份运行！")
        os.system("pause")  # 按任意键继续
    else:
        read_codm_registry_keys()
        os.system("pause")  # 按任意键继续
