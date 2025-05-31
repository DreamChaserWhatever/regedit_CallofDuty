"""
ZeroSensitivity主模块
提供简化的API接口
"""

from .strategies import ZeroSensitivityStrategy
from .exceptions import RegistryOperationError


def apply_zero_sensitivity(root_key, sub_key, value_name):
    """
    应用灵敏度修改的快捷函数

    参数:
        root_key: 根键 (如winreg.HKEY_LOCAL_MACHINE)
        sub_key: 子键路径
        value_name: 值名称

    返回:
        dict: 包含操作结果和修改前后数据的字典

    异常:
        RegistryOperationError: 操作失败时抛出
    """
    strategy = ZeroSensitivityStrategy()
    return strategy.execute(root_key, sub_key, value_name)


# 公共API
__all__ = [
    'apply_zero_sensitivity',
    'RegistryOperationError'
]
