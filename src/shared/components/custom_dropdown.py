from flet import Dropdown, DropdownOption, Text

from core.service.app.base_entity_service import BaseEntityService
from shared.colors import Colors


class CustomDropdown(Dropdown):
    def __init__(
        self,
        label: str,
        service: BaseEntityService,
        option_selector: str,
        option_key_selector: str = "id",
        color=Colors.TEXT_DARK,
        bgcolor=Colors.BACKGROUND,
        value: str | None = None,
        expand: bool | None = None,
        expand_loose: bool | None = None,
        width: int | float | None = None,
    ):
        self._service = service
        self._option_key_selector = option_key_selector
        self.option_selector = option_selector

        super().__init__(
            label=label,
            value=value,
            color=color,
            bgcolor=bgcolor,
            expand=expand,
            expand_loose=expand_loose,
            width=width,
        )

    def did_mount(self):
        self.page.run_task(self.__load_options)

    async def __load_options(self, *args, **kwargs):
        request = await self._service.all()

        _options = []

        for option in request.data:
            dict_model = option.to_dict()

            _options.append(
                DropdownOption(
                    key=str(dict_model.get(self._option_key_selector)),
                    text=dict_model.get(self.option_selector),
                    content=Text(
                        dict_model.get(self.option_selector), color=Colors.TEXT_DARK
                    ),
                    data=option,
                )
            )

        self.options = _options
        self.update()

    @property
    def payload(self):
        selected_option = next(
            (opt for opt in self.options if opt.key == self.value), None
        )
        return selected_option.data if selected_option else None

    def set_value(self, value: str):
        self.value = str(value.get(self._option_key_selector))

    def clean_field(self):
        self.value = None
        self.text = None
