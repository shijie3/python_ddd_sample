# coding=utf-8
from domain.base.provider import Provider


class ResVimProvider(object):

    def create(self, res_model_json, location_info):
        pass


Provider.register(ResVimProvider)

if __name__ == '__main__':
    provider = ResVimProvider()
    print('Subclass:', issubclass(ResVimProvider, Provider))
    print('Instance:', isinstance(provider, Provider))
    provider.create(None, None)
