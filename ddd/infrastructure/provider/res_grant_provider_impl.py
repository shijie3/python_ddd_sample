# coding=utf-8
from domain.base.provider import Provider
from domain.provider.res_grant_provider import ResGrantProvider


class ResGrantProviderImpl(ResGrantProvider):

    def grant(self, res_model_json):
        print('resource grant')
        return "1", "tenant"


if __name__ == '__main__':
    provider = ResGrantProviderImpl()
    print('Subclass:', issubclass(ResGrantProviderImpl, Provider))
    print('Instance:', isinstance(provider, Provider))
    provider.grant(None)
