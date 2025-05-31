"""
处理策略实现
包含具体的注册表修改策略
"""
import re
import winreg
from .exceptions import RegistryOperationError


class BaseRegUnlockFPS:
    """注册表修改策略基类"""

    def execute(self, root_key, sub_key, value_name):
        """
        执行注册表修改操作

        参数:
            root_key: 根键
            sub_key: 子键路径
            value_name: 值名称

        异常:
            RegistryOperationError: 操作失败时抛出
        """
        raise NotImplementedError("子类必须实现此方法")


class RegUnlockFPSStrategy(BaseRegUnlockFPS):
    """帧率修改策略"""

    def execute(self, root_key, sub_key, value_name):
        with winreg.OpenKey(root_key, sub_key, 0, winreg.KEY_READ) as key:
            current_value, value_type = winreg.QueryValueEx(key, value_name)
            if re.search(r'EnableFramerateCustomize', value_name):
                if current_value != 1:
                    modified_data = 1
                else:
                    return
            elif re.search(r'FramerateCustomizeValue', value_name):
                if current_value != 0:
                    modified_data = 0
                else:
                    return
            print(f"\n[操作] 正在处理键: {value_name}")
            print(
                f"[原始十进制值]: {' '.join(f'{current_value}')}"
            )
            print(
                f"[修改后十进制值]: {' '.join(f'{modified_data}')}"
            )
            # 写入新值（需管理员权限）
            try:
                with winreg.OpenKey(
                        root_key, sub_key, 0, winreg.KEY_SET_VALUE
                ) as write_key:
                    winreg.SetValueEx(
                        write_key, value_name, 0, winreg.REG_DWORD, modified_data)
                    print("[修改成功]")
            except WindowsError as e:
                raise RegistryOperationError(f"[错误]注册表写入失败: {str(e)}")
