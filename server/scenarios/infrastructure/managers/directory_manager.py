from django.db import models


class DirectoryManager(models.Manager):

    def get_root_directories(self):
        return self.filter(parent__isnull=True)

    def get_parents(self, directory):
        parents = []
        while directory.parent:
            parents.append(directory.parent)
            directory = directory.parent
        return parents
