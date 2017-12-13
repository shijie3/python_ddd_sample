# coding=utf-8


class VnfInstantiateMsg(object):
    def __init__(self, vnf_instance_id, package_id, inputs, **kwargs):
        self._vnf_instance_id = vnf_instance_id
        self._package_id = package_id
        self._inputs = inputs
        self._kwargs = kwargs

    @property
    def vnf_instance_id(self):
        """the property of vnf instance id"""
        return self._vnf_instance_id

    @property
    def package_id(self):
        """the property of package id"""
        return self._package_id

    @property
    def inputs(self):
        """the property of inputs"""
        return self._inputs

    @property
    def kwargs(self):
        """the property of kwargs"""
        return self._kwargs
