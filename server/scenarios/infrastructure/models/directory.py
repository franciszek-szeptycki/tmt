from scenarios.infrastructure.managers.directory_manager import DirectoryManager
from scenarios.infrastructure.models.abstract import LocatedUnitModel


class Directory(LocatedUnitModel):

    objects = DirectoryManager()
