import ctypes
import os
import re
import winreg
from regedit_tools.zero_sensitivity import apply_zero_sensitivity, RegistryOperationError
from regedit_tools.regunlockFPS import apply_regunlockfps, RegistryOperationError

root_key = winreg.HKEY_CURRENT_USER
sub_key = r"SOFTWARE\Tencent\Call-of-Duty"
pattern = [re.compile(
    r"^CODM_\d+_"  # 动态前缀
    r"iMSDK_CN_"  # 固定模块标识
    r"(PVE|PVP|TD|Br|PVEFiring|PVPFiring|TDFiring|BrFiring)"  # 扩展模式部分
    r"(_(?:RotateSensitive|AimRotate|ReddotHolo|Sniper|Free|ACOG|[\dX]+|SkyVehicle|GroundVehicle|Vertical|Ult).*?)?"  # 动态描述部分
    r"_h\d+$",  # 固定后缀哈希值
    re.IGNORECASE
),
    re.compile(
    r"^CODM_\d+_"  # 动态前缀
    r"iMSDK_CN_"  # 固定模块标识
    r"(EnableFramerateCustomize|FramerateCustomizeValue)"  # 关键部分
    r"_h\d+$",  # 固定后缀哈希值
    re.IGNORECASE)
]


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
                    if pattern[0].match(name) and value_type == winreg.REG_DWORD:
                        try:
                            apply_zero_sensitivity(root_key, sub_key, name)

                        except RegistryOperationError as e:
                            print(f"[错误]注册表操作失败: {str(e)}")
                    elif pattern[1].match(name) and value_type == winreg.REG_DWORD:
                        try:
                            apply_regunlockfps(root_key, sub_key, name)

                        except RegistryOperationError as e:
                            print(f"[错误]注册表操作失败: {str(e)}")
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
    print("\ngithub: https://github.com/DreamChaserWhatever")

    # ——————————————————————————————————————————
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("[错误] 请以管理员身份运行！")
        os.system("pause")  # 按任意键继续
    else:
        read_codm_registry_keys()
        os.system("pause")  # 按任意键继续
