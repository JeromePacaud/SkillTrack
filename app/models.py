from dataclasses import dataclass
import json


class User:
    def __init__(self, name: str, id: int) -> None:
        self.name: str = name
        self.id: int = id

    def can_validate(self, skill_id: int) -> bool:
        return False

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
        }

    def __str__(self) -> str:
        return f'Utilisateur : {self.id} | {self.name}'

    def __repr__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)


class Learner(User):
    def __init__(self, name: str, id: int) -> None:
        super().__init__(name, id)
        self._validated_skills: list[int] = []

    def can_validate(self, skill_id: int) -> bool:
        return skill_id in self._validated_skills

    def add_skill(self, skill_id: int) -> None:
        if skill_id in self._validated_skills:
            raise ValueError(f'La compétences {skill_id} est déja validée !')
        self._validated_skills.append(skill_id)

    def to_dict(self) -> dict:
        data = super().to_dict()
        data['validated_skills'] = self._validated_skills
        return data

    def __str__(self) -> str:
        return f'Apprenant : {self.id} | {self.name}'


class Trainer(User):
    def can_validate(self, skill_id: int) -> bool:
        return True

    def __str__(self) -> str:
        return f'Formateur : {self.id} | {self.name}'


class Classroom:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self._users: list[User] = []

    def get_users(self) -> list[User]:
        return self._users

    def add_user(self, user: User) -> None:
        self._users.append(user)

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'users': [user.to_dict() for user in self._users],
        }

    def __add__(self, other: Classroom) -> Classroom:
        merged_classroom = Classroom(
            f'{self.name} + {other.name} => P{int(self.name[1:]) + int(other.name[1:])}'
        )

        for user in self._users:
            merged_classroom.add_user(user)
        for user in other._users:
            merged_classroom.add_user(user)

        return merged_classroom

    def __str__(self) -> str:
        return f'Promotion : {self.name} | {len(self._users)} users'

    def __repr__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
