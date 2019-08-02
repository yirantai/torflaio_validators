# -*- coding:utf-8 -*-

"""
定义一些错误类型，在出现的时候抛出异常
"""


class BaseExceptionError(Exception):
    """ 通用类型错误
    """

    def __init__(self, err_msg='', err_code=400):
        super().__init__(err_code, err_msg)
        self.err_code = err_code
        self.err_msg = err_msg


class UnAuthorizationError(BaseExceptionError):
    """
    未登录错误
    """
    def __init__(self,
                 err_msg='invalid authorization params',
                 err_code=401):
        super().__init__(err_msg, err_code)


class ParamsError(BaseExceptionError):
    """ http请求参数错误
    """

    def __init__(self, err_msg='请求参数错误', err_code=400):
        super(ParamsError, self).__init__(err_msg, err_code)


class SystemError(BaseExceptionError):
    """ 系统内部错误
    """

    def __init__(self, err_msg='系统内部错误', err_code=500):
        super().__init__(err_msg, err_code)


class ParamsValidationError(BaseExceptionError):
    """ 参数验证错误
    """

    def __init__(self, err_msg='参数验证错误', err_code=400):
        super().__init__(err_msg, err_code)


class PermissionValidationError(BaseExceptionError):
    """
    权限验证错误
    """
    def __init__(self, err_msg='权限验证错误', err_code=400):
        super().__init__(err_msg, err_code)
