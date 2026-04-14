from core.domain.repositories.exc import RemoveException
from core.service.app import MetricService
from core.service.command import MetricRemoveCommand
from shared.components.common_actions_view import CommonActionsColumn
from shared.lib import SnackBarType, snack

from .metric_update_modal import MetricUpdateModal


class MetricActionsView(CommonActionsColumn):
    service = MetricService
    modal = MetricUpdateModal
    topic_name = "metric_list_page__refetch"
    remove_command = MetricRemoveCommand

    async def delete_item(self, *args, **kwargs):
        command = self.remove_command()
        try:
            await command.execute(self.payload.get("code"))
        except RemoveException as e:
            return snack(self.page, e.message, SnackBarType.ERROR)

        snack(self.page, "Запись успешно удалена!")
        self.page.pubsub.send_all_on_topic(self.topic_name, "refresh")
