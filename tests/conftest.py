import pytest

from models import (
    Classroom,
    Learner,
    Skill,
    Trainer,
    User,
    Validation,
    ValidationStatus,
)


@pytest.fixture
def user() -> User:
    return User(name="Alice", id=1)


@pytest.fixture
def learner() -> Learner:
    return Learner(name="Bob", id=2)


@pytest.fixture
def learner_with_skill() -> Learner:
    l = Learner(name="Bob", id=2)
    l.add_skill(1)
    return l


@pytest.fixture
def trainer() -> Trainer:
    return Trainer(name="John", id=99)


@pytest.fixture
def classroom() -> Classroom:
    return Classroom(name="P1")


@pytest.fixture
def classroom_with_users(learner: Learner, trainer: Trainer) -> Classroom:
    c = Classroom(name="P1")
    c.add_user(learner)
    c.add_user(trainer)
    return c


@pytest.fixture
def skill() -> Skill:
    return Skill(id=1, name="Python")


@pytest.fixture
def validation() -> Validation:
    return Validation(
        id=1,
        learner_id=10,
        skill_id=1,
        status=ValidationStatus.PENDING,
    )