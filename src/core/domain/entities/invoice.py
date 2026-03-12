from datetime import datetime

from core.domain.value_objects.invoice import InvoiceId, InvoicePerson, InvoiceType
from core.domain.value_objects.shared import ContentType


class Invoice:
    def __init__(
        self,
        id: InvoiceId,
        type: InvoiceType,
        content_type: ContentType,
        sender_person: InvoicePerson,
        recipient_person: InvoicePerson,
        created_ad: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ) -> None:
        self._id = id
        self._type = type
        self._content_type = content_type
        self._sender_person = sender_person
        self._recipient_person = recipient_person
        self._created_ad = created_ad
        self._updated_at = updated_at

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Invoice):
            return self.id == obj.id

        return False

    @property
    def id(self) -> InvoiceId:
        return self._id

    @property
    def type(self) -> InvoiceType:
        return self._type

    @property
    def content_type(self) -> ContentType:
        return self._content_type

    @property
    def sender_person(self) -> InvoicePerson:
        return self._sender_person

    @property
    def recipient_person(self) -> InvoicePerson:
        return self._recipient_person

    @property
    def created_at(self) -> datetime:
        return self._created_ad

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update_type(self, type: InvoiceType) -> None:
        self._type = type
        self._updated_at = datetime.now()

    def update_content_type(self, content_type: ContentType) -> None:
        self._content_type = content_type
        self._updated_at = datetime.now()

    def update_sender_person(self, sender_person: InvoicePerson) -> None:
        self._sender_person = sender_person
        self._updated_at = datetime.now()

    def update_recipient_person(self, recipient_person: InvoicePerson) -> None:
        self._recipient_person = recipient_person
        self._updated_at = datetime.now()

    @staticmethod
    def create(
        self,
        id: InvoiceId,
        type: InvoiceType,
        content_type: ContentType,
        sender_person: InvoicePerson,
        recipient_person: InvoicePerson,
    ) -> Invoice:
        return Invoice(
            id=id,
            type=type,
            content_type=content_type,
            sender_person=sender_person,
            recipient_person=recipient_person,
        )
