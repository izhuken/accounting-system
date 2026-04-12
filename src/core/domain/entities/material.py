from datetime import datetime

from core.domain.entities.entity import Entity
from core.domain.entities.metric import Metric
from core.domain.value_objects.material import MaterialId, MaterialName


class Material(Entity):
    def __init__(
        self,
        id: MaterialId,
        name: str,
        metric: Metric | None = None,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ) -> None:
        self._id = id
        self._name = MaterialName(name)
        self._metric = metric
        self._created_at = created_at
        self._updated_at = updated_at

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Material):
            return False

        return self.id == obj.id

    @property
    def id(self) -> MaterialId:
        return self._id

    @property
    def name(self) -> MaterialName:
        return self._name

    @property
    def metric(self) -> Metric:
        return self._metric

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update_name(self, name: str) -> None:
        self._name = MaterialName(name)
        self._updated_at = datetime.now()

    def update_metric(self, metric: Metric) -> None:
        self._metric = metric
        self._updated_at = datetime.now()

    def to_dict(self) -> dict:
        return {
            "id": self.id.value,
            "name": self.name.value,
            "metric": self.metric.to_dict() if self.metric else None,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    # FIXME: фиксанить, metric не может быть None
    def create(name: str, metric: Metric | None = None) -> Material:
        return Material(
            id=MaterialId.generate(),
            name=name,
            metric=metric,
        )
