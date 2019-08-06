## torflaio_validators
```
背景：在使用python web框架，如tornado, flask, aiohttp等框架时, 对于接口传入参数, 不同的人有不同的验证方式, 搞得项目很杂乱. 
以前用Django框架,django-rest-framework中serializers类的参数验证时,很正规，使用体验也非常好.
故参考django-rest-framework的serializers参数验证的风格开发的.用于统一tornado, flask, aiohttp等框架的参数验证方式.
```

### 版本说明：
```
v1.0.1: 优化项目结构。
v1.0.0: 初始版本发布。
```

### 安装：
  pip install torflaio_validators

### 使用样例:
```
from torflaio_validators.base.base_validator import BaseValidator
from torflaio_validators.base.fields import IntegerField, CharField, BoolField, DictField

1.先定义要验证的参数, 每个Field均包含 field_name field_value, required, default, max_length, min_length等参数,
可以根据所验证的字段是否必填,默认值等进行选择.
class PersonInfoValidator(BaseValidator):
    name = CharField()
    age = IntegerField()
    address = CharField()
    province = CharField()
    city = CharField()
    county = CharField()
    is_valid = BoolField(required=False, default=True)
    extra = DictField()
    
2.在view中引入该validator类
validator = PersonInfoValidator(data)  # data为初始验证参数
validator.validation()
validated_data = validator.validated_data   # 此处获取的validated_data就是经过验证的数据了.

3.如果不仅想要验证字段的基本信息(是否必填, 默认值，最大长度,最小长度等)，还想验证业务相关的,
可以重新定义validator的valiated_data属性(property属性). 使用如下：

from torflaio_validators.base.exceptions import ParamsValidationError

class PersonInfoValidator(BaseValidator):
    name = CharField()
    age = IntegerField()
    address = CharField()
    province = CharField()
    city = CharField()
    county = CharField()
    is_valid = BoolField(required=False, default=True)
    extra = DictField()
    
    @propery
    def validated_data(self):
        validated_data = super().validated_data    # 此步骤必须, 获取上一步验证后的数据
        age = validated_data.get('age')
        if age < 18:
            raise ParamsValidationError(err_code=400, err_msg="年龄不能小于18岁")    
            # 此处的ParamsValidationError为该验证框架默认Error类, 也可以根据喜好自定义抛出的错误
        return validated_data
```

#### 联系作者：
```
email: 896275756@qq.com
由于水平有限，难免有未知bug和考虑不周之处，如您有好的意见或建议，请发邮件给我，一起探讨和完善. 您的意见或建议将会体现在下一次的版本更新里。
```
