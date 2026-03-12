from datetime import datetime

from core.domain.entities.metric_code import Metric
from core.domain.value_objects import MaterialId, MaterialName


class Material:
    def __init__(
        self,
        id: MaterialId,
        name: MaterialName,
        metric: Metric = None,
        created_ad: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ) -> None:
        self._id = id
        self._name = name
        self._metric = metric
        self._created_ad = created_ad
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
        return self._created_ad

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update_name(self, name: MaterialName) -> None:
        self._name = name
        self._updated_at = datetime.now()

    def update_metric(self, metric: Metric) -> None:
        self._metric = metric
        self._updated_at = datetime.now()

    @staticmethod
    def create(name: MaterialName, metric: Metric) -> Material:
        return Material(
            id=MaterialId.generate(),
            name=name,
            metric=metric,
        )
