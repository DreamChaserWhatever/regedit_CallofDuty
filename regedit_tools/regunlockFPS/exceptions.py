"""
exceptions.py
自定义异常模块
包含注册表操作相关异常
"""


class RegistryOperationError(Exception):
    """注册表操作异常基类"""

    def __init__(self, message, key_path=None, value_name=None):
        self.message = message
        self.key_path = key_path
        self.value_name = value_name
        super().__init__(f"{message} | 路径: {key_path} | 值: {value_name}")


class RegistryReadError(RegistryOperationError):
    """注册表读取失败异常"""
    pass


class RegistryWriteError(RegistryOperationError):
    """注册表写入失败异常"""
    pass


class RegistryPermissionError(RegistryOperationError):
    """注册表权限不足异常"""
    pass
