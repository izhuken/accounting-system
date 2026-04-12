from presentation.admin.materials.components import MaterialTabs
from shared.components.common_page import CommonPage
from shared.lib.router import Router


class MaterialListPage(CommonPage):
    def __init__(self, router: Router):
        super().__init__("Материалы", router, [MaterialTabs(router)])
