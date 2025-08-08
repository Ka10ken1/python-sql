from abc import ABC, abstractmethod
from typing import List, Optional
from psycopg2.extras import RealDictRow


class IDatabase(ABC):
    @abstractmethod
    def connect(self) -> Optional["connection"]:
        pass

    @abstractmethod
    def execute(self, query: str, params=None):
        pass

    @abstractmethod
    def fetchall(self, query: str, params=None) -> Optional[List[RealDictRow]]:
        pass


class IQuery(ABC):
    @abstractmethod
    def run(self):
        pass
