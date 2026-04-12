from datetime import datetime

from core.domain.entities.entity import Entity
from core.domain.value_objects.metric import MetricCode, MetricName


class Metric(Entity):
    def __init__(
        self,
        code: int,
        name: str,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ) -> None:
        self._code = MetricCode(code)
        self._name = MetricName(name)
        self._created_at = created_at
        self._updated_at = updated_at

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Metric):
            return False

        return self.id == obj.id

    @property
    def code(self) -> MetricCode:
        return self._code

    @property
    def name(self) -> MetricName:
        return self._name

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update_name(self, name: str) -> None:
        self._name = MetricName(name)
        self._updated_at = datetime.now()

    def to_dict(self) -> dict:
        return {
            "code": self.code.value,
            "name": self.name.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(code: int, name: str) -> Metric:
        return Metric(code=code, name=name)
