# coding=utf-8
from domain.repository.job_repository import JobRepository


class JobRepositoryImpl(JobRepository):
    def __init__(self):
        self._repo = {}

    def add(self):
        print "add job"

    def save(self):
        print "save job"

    def update(self):
        print "update job"

    def delete(self):
        print "delete job"

    def find_by_id(self):
        print "find job"

    def _has_key(self):
        print "check job"


if __name__ == '__main__':
    from domain.base.repository import Repository
    print('Subclass:', issubclass(JobRepositoryImpl, Repository))
    print('Instance:', isinstance(JobRepositoryImpl(), Repository))
