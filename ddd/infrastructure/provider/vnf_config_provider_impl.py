# coding=utf-8
from domain.provider.vnf_config_provider import VnfConfigProvider


class VnfConfigProviderImpl(VnfConfigProvider):

    def send(self, res_model_json):
        print('vnf config send')


if __name__ == '__main__':
    from domain.base import Provider
    provider = VnfConfigProviderImpl()
    print('Subclass:', issubclass(VnfConfigProviderImpl, Provider))
    print('Instance:', isinstance(provider, Provider))
    provider.send(None)
