# coding=utf-8
"""the implement of entity"""
from domain.entity.vnf_instance_entity import VnfInstanceEntity


class NfInstantiateService(object):
    """cargo service class
    """
        
    def __init__(self, inst_repo, job_repo, catalog_provider, lcm_provider, res_calc_provider, res_grant_provider, res_vim_provider, vnf_config_provider):
        self._inst_repo = inst_repo
        self._job_repo = job_repo
        self._catalog_provider = catalog_provider
        self._lcm_provider = lcm_provider
        self._res_calc_provider = res_calc_provider
        self._res_grant_provider = res_grant_provider
        self._res_vim_provider = res_vim_provider
        self._vnf_config_provider = vnf_config_provider

    def instantiate(self, vnf_instance_id, package_id, inputs):
        """vnf instantiation"""
        nf_instance = VnfInstanceEntity(vnf_instance_id, package_id)
        inst_obj = self._inst_repo.find_by_id(nf_instance.vnf_instance_id)
        nf_instance.check_instance_exist(inst_obj)
        self._job_repo.add()
        self._inst_repo.update()
        self._catalog_provider.check_status(package_id)
        res_model = self._res_calc_provider.calc(package_id, inputs)
        nf_instance.set_res_model(res_model)
        vim_id, tenant = self._res_grant_provider.grant(nf_instance.res_model)
        nf_instance.set_location_info(vim_id, tenant)
        vim_resource = self._res_vim_provider.create(nf_instance.res_model, nf_instance.location_info)
        nf_instance.set_vim_resource(vim_resource)
        self._vnf_config_provider.send(nf_instance.res_model)
        self._lcm_provider.notify(nf_instance.vnf_instance_id, nf_instance.vim_resource)
        self._inst_repo.update()
        self._job_repo.update()
