# coding=utf-8
from domain.provider.res_vim_provider import ResVimProvider


class ResVimProviderImpl(ResVimProvider):

    def create(self, res_model_json, location_info):
        print('resource create')


if __name__ == '__main__':
    from domain.base import Provider
    provider = ResVimProviderImpl()
    print('Subclass:', issubclass(ResVimProviderImpl, Provider))
    print('Instance:', isinstance(provider, Provider))
    provider.create(None, None)
