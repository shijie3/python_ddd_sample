# coding=utf-8
from domain.provider.lcm_provider import LCMProvider


class LCMProviderImpl(LCMProvider):

    def notify(self, nf_instance_id, vim_resource):
        print('lcm change notify')


if __name__ == '__main__':
    from domain.base import Provider
    provider = LCMProviderImpl()
    print('Subclass:', issubclass(LCMProviderImpl, Provider))
    print('Instance:', isinstance(provider, Provider))
    provider.notify(None)
