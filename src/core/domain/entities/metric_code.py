from datetime import datetime

from core.domain.value_objects.metric import MetricCode, MetricName


class Metric:
    def __init__(
        self,
        code: MetricCode,
        name: MetricName,
        created_ad: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ) -> None:
        self._code = code
        self._name = name
        self._created_ad = created_ad
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
        return self._created_ad

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update_name(self, name: MetricName) -> None:
        self._name = name
        self._updated_at = datetime.now()

    @staticmethod
    def create(code: MetricCode, name: MetricName) -> Metric:
        return Metric(code=code, name=name)
