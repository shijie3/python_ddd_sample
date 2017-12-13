# coding=utf-8

from domain.base.provider import Provider


class VnfConfigProvider(object):

    def send(self, res_model_json):
        pass


Provider.register(VnfConfigProvider)

if __name__ == '__main__':
    provider = VnfConfigProvider()
    print('Subclass:', issubclass(VnfConfigProvider, Provider))
    print('Instance:', isinstance(provider, Provider))
    provider.send(None)
