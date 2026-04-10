from core.service.app import InitDBService

from .icommand import ICommand


class InitCommand(ICommand):
    async def execute(self):
        init_service = InitDBService()
        await init_service.init_db()
