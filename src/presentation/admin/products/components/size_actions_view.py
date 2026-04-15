from core.domain.repositories.exc import RemoveException
from core.service.app import SizeService
from core.service.command import SizeRemoveCommand
from shared.components.common_actions_view import CommonActionsColumn
from shared.lib import SnackBarType, snack

from .size_update_modal import SizeUpdateModal


class SizeActionsView(CommonActionsColumn):
    service = SizeService
    modal = SizeUpdateModal
    topic_name = "size_list_page__refetch"
    remove_command = SizeRemoveCommand

    async def delete_item(self, *args, **kwargs):
        command = self.remove_command()
        try:
            await command.execute(self.payload.get("code"))
        except RemoveException as e:
            return snack(self.page, e.message, SnackBarType.ERROR)

        snack(self.page, "Запись успешно удалена!")
        self.page.pubsub.send_all_on_topic(self.topic_name, "refresh")
