# coding: utf-8
import datetime

from .exceptions import ParamsValidationError
from .time_tools import dt_str_to_datetime


class BaseField(object):

    field_type = None
    field_type_name = None

    def __init__(self, field_name=None, field_value=None, required=True, default=None, max_length=0, min_length=0):
        self.field_name = field_name
        self.field_value = field_value
        self.required = required
        self.default = default
        self.max_length = max_length
        self.min_length = min_length

    def integrity_validate(self):
        """Parameter integrity verification"""
        if self.required and self.field_value is None:
            raise ParamsValidationError('param integrity error, field %s is required' % self.field_name)

    def type_validate(self):
        """Parameter type validation"""
        if self.required and not isinstance(self.field_value, self.field_type):
            raise ParamsValidationError('param type error, field %s should be %s type' % (
                self.field_name, self.field_type_name))

    def length_validate(self):
        """参数长度验证"""
        if self.max_length and len(self.field_value) > self.max_length:
            raise ParamsValidationError('param length error, field %s length cannot exceed %s' % (
                self.field_name, self.max_length))

        if self.min_length:
            if len(self.field_value) < self.min_length:
                raise ParamsValidationError('param length error, field %s length cannot be less than%s' % (
                    self.field_name, self.min_length))

    def validate(self):
        self.integrity_validate()
        self.type_validate()
        self.length_validate()
        if not self.field_value and not self.required and self.default is not None:
            self.field_value = self.default

    @property
    def validated_data(self):
        return {self.field_name: self.field_type(self.field_value)}


class IntegerField(BaseField):

    field_type = int
    field_type_name = 'int'

    def length_validate(self):
        if self.field_value and self.max_length and self.field_value > self.max_length:
            raise ParamsValidationError('字段%s最大值不能超过%s' % (self.field_name, self.max_length))

        if self.field_value and self.min_length and self.field_value < self.min_length:
            raise ParamsValidationError('字段%s最大值不能小于%s' % (self.field_name, self.min_length))


class CharField(BaseField):

    field_type = str
    field_type_name = 'str'


class BoolField(BaseField):

    field_type = bool
    field_type_name = 'bool'


class FloatField(BaseField):

    field_type = float
    field_type_name = 'float'


class DateField(BaseField):

    field_type = datetime.date
    field_type_name = 'date'


class DateTimeField(BaseField):

    field_type = datetime.datetime
    field_type_name = 'datetime'

    def type_validate(self):
        try:
            if not isinstance(dt_str_to_datetime(self.field_value), self.field_type):
                raise ParamsValidationError('param type error, field %s should be %s type' % (
                    self.field_name, self.field_type_name
                ))
        except:
            raise ParamsValidationError('param type error, field %s should be %s type' % (
                self.field_name, self.field_type_name
            ))
        self.field_value = dt_str_to_datetime(self.field_value)


class ListField(BaseField):

    field_type = list
    field_type_name = 'list'


class DictField(BaseField):

    field_type = dict
    field_type_name = 'dict'

