from enum import Enum

from flet import Container, InputFilter, Ref, TextField

from shared.colors import Colors

INT_ONLY_FILTER = InputFilter(regex_string=r"^\d*$")
FLOAT_FILTER = InputFilter(regex_string=r"^(\d*)[\,\.]?(\d*)$")


class NumericInputType(Enum):
    INT = "int"
    FLOAT = "float"


class NumericInput(Container):
    def __init__(
        self,
        label: str | None = None,
        type: NumericInputType = NumericInputType.FLOAT,
        value: int | float | None = None,
        height: float | int | None = None,
        width: float | int | None = None,
        expand: bool | None = None,
        expand_loose: bool | None = None,
        ref: Ref | None = None,
        as_str: bool = False,  # return string or int/float
    ) -> None:
        self._type = type
        self._as_str: bool = as_str
        self._input_ref = Ref[TextField]()

        super().__init__(
            TextField(
                value=value,
                label=label,
                height=height,
                width=width,
                expand=expand,
                expand_loose=expand_loose,
                color=Colors.TEXT_DARK,
                input_filter=INT_ONLY_FILTER
                if self._type == NumericInputType.INT
                else FLOAT_FILTER,
                ref=self._input_ref,
            ),
            ref=ref,
        )

    @property
    def value(self) -> int | float | None:
        if self._input_ref.current.value is None:
            return None

        if self._as_str:
            return str(self._input_ref.current.value)

        try:
            return (
                int(self._input_ref.current.value)
                if self._type == NumericInputType.INT
                else float(self._input_ref.current.value.replace(",", "."))
            )
        except ValueError:
            return None

    @value.setter
    def value(self, value: int | float | None) -> None:
        self._input_ref.current.value = str(value) if value is not None else None
        try:
            self._input_ref.current.update()
        except Exception:
            pass

    def clean_field(self):
        self.value = None
        self.update()
