# coding=utf-8
"""the sample of value object"""
from domain.base.value_object import ValueObject


class LocationInfo(object):
    """delivery class
    """
    
    def __init__(self, vim_id, tenant):
        self._vim_id = vim_id
        self._tenant = tenant

    @property
    def vim_id(self):
        """the property of vim id"""
        return self._vim_id

    @property
    def tenant(self):
        """the property of tenant"""
        return self._tenant


ValueObject.register(LocationInfo)

if __name__ == '__main__':
    print('Subclass:', issubclass(LocationInfo, ValueObject))
    print('Instance:', isinstance(LocationInfo(1, 'admin'), ValueObject))
