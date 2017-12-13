# coding=utf-8
"""the implement of cargo"""
from domain.base.entity import Entity
from domain.value_object.location_info_value_object import LocationInfo


class VnfInstanceEntity(object):
    """the vnf instance class
    """
    
    def __init__(self, vnf_instance_id, package_id):
        self._vnf_instance_id = vnf_instance_id
        self._package_id = package_id
        self._location_info = None
        self._res_model = None
        self._vim_resource = None

    def set_location_info(self, vim_id, tenant):
        self._location_info = LocationInfo(vim_id, tenant)

    def set_res_model(self, res_model):
        self._res_model = res_model

    def set_vim_resource(self, vim_resource):
        self._vim_resource = vim_resource

    @property
    def vnf_instance_id(self):
        return self._vnf_instance_id

    @property
    def package_id(self):
        return self._package_id

    @property
    def location_info(self):
        """resource location information"""
        return self._location_info

    @property
    def res_model(self):
        """resource model"""
        return self._res_model

    @property
    def vim_resource(self):
        """resource model"""
        return self._vim_resource

    def check_instance_exist(self, instance_id):
        print "check instance exist"


Entity.register(VnfInstanceEntity)

if __name__ == '__main__':
    print('Subclass:', issubclass(VnfInstanceEntity, Entity))
    print('Instance:', isinstance(VnfInstanceEntity(1, "1"), Entity))


