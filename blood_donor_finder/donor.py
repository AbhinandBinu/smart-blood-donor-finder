import uuid

class Donor:
    def __init__(
        self,
        name,
        blood_group,
        location,
        phone,
        certificate,
        status="pending",
        id=None
    ):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.blood_group = blood_group.strip().upper()
        self.location = location.lower()
        self.phone = phone
        self.certificate = certificate
        self.status = status

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Donor(**data)
