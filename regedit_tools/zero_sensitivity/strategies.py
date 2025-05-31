"""
处理策略实现
包含具体的注册表修改策略
"""

import winreg
from .registry_utils import read_raw_binary_value, REG_BINARY
from .exceptions import RegistryOperationError


class BaseRegistryStrategy:
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


class ZeroSensitivityStrategy(BaseRegistryStrategy):
    """灵敏度修改策略"""

    def execute(self, root_key, sub_key, value_name):
        # 使用底层API读取原始十六进制数据
        raw_data = read_raw_binary_value(root_key, sub_key, value_name)
        if not raw_data:
            raise RegistryOperationError(f"[错误]无法读取注册表值: {sub_key}\\{value_name}")
        print(f"\n[操作] 正在处理键: {value_name}")
        print(
            f"[原始十六进制值]: {' '.join(f'{b:02X}' for b in raw_data)}"
        )

        # 修改第一个字节为0x01
        modified_data = bytes([0x01]) + raw_data[1:]
        print(
            f"[修改后十六进制值]: {' '.join(f'{b:02X}' for b in modified_data)}"
        )

        # 写入新值（需管理员权限）
        try:
            with winreg.OpenKey(
                    root_key, sub_key, 0, winreg.KEY_SET_VALUE
            ) as write_key:
                winreg.SetValueEx(
                    write_key, value_name, 0, REG_BINARY, modified_data)
                print("[修改成功]")
        except WindowsError as e:
            raise RegistryOperationError(f"[错误]注册表写入失败: {str(e)}")

