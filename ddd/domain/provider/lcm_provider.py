# coding=utf-8
from domain.base.provider import Provider


class LCMProvider(object):

    def notify(self, nf_instance_id, vim_resource):
        pass

Provider.register(LCMProvider)

if __name__ == '__main__':
    provider = LCMProvider()
    print('Subclass:', issubclass(LCMProvider, Provider))
    print('Instance:', isinstance(provider, Provider))
    provider.notify(None)
