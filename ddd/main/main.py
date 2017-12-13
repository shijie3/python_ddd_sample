from application.service.vnf_instantiate_api import VnfInstantiateApi
from application.service.vnf_instantiate_msg import VnfInstantiateMsg
from domain.provider.catalog_provider import CatalogProvider
from domain.provider.lcm_provider import LCMProvider
from domain.provider.res_calc_provider import ResCalcProvider
from domain.provider.res_grant_provider import ResGrantProvider
from domain.provider.res_vim_provider import ResVimProvider
from domain.provider.vnf_config_provider import VnfConfigProvider
from domain.repository.job_repository import JobRepository
from domain.repository.vnf_instance_repository import VnfInstanceRepository
from domain.service.nf_instantiate_service import NfInstantiateService
from infrastructure.provider.catalog_provider_impl import CatalogProviderImpl
from infrastructure.provider.lcm_provider_impl import LCMProviderImpl
from infrastructure.provider.res_calc_provider_impl import ResCalcProviderImpl
from infrastructure.provider.res_grant_provider_impl import ResGrantProviderImpl
from infrastructure.provider.res_vim_provider_impl import ResVimProviderImpl
from infrastructure.provider.vnf_config_provider_impl import VnfConfigProviderImpl
from infrastructure.repository.job_repository_impl import JobRepositoryImpl
from infrastructure.repository.vnf_instance_repository_impl import VnfInstanceRepositoryImpl

if __name__ == '__main__':
    inst_repo = VnfInstanceRepositoryImpl()
    job_repo = JobRepositoryImpl()
    catalog_provider = CatalogProviderImpl()
    lcm_provider = LCMProviderImpl()
    res_calc_provider = ResCalcProviderImpl()
    res_grant_provider = ResGrantProviderImpl()
    res_vim_provider = ResVimProviderImpl()
    vnf_config_provider = VnfConfigProviderImpl()
    service = NfInstantiateService(inst_repo, job_repo, catalog_provider, lcm_provider, res_calc_provider, res_grant_provider, res_vim_provider, vnf_config_provider)
    api = VnfInstantiateApi(service)
    msg = VnfInstantiateMsg(vnf_instance_id=1, package_id="2", inputs={"a": "b"})
    api.instantiate(msg)