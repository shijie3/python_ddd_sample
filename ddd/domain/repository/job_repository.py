# coding=utf-8

from domain.base.repository import Repository


class JobRepository(object):
    def __init__(self):
        pass

    def add(self):
        pass

    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def find_by_id(self):
        pass

    def _has_key(self):
        pass

Repository.register(JobRepository)

if __name__ == '__main__':

    print('Subclass:', issubclass(JobRepository, Repository))
    print('Instance:', isinstance(JobRepository(), Repository))
