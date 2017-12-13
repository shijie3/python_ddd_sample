# coding=utf-8

class VnfInstantiateApi(object):
    
    def __init__(self, vnf_instantiate_service):
        self._vnf_instantiate_service = vnf_instantiate_service

    def instantiate(self, msg):
        self._vnf_instantiate_service.instantiate(msg.vnf_instance_id, msg.package_id, msg.inputs)
