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


# --- User --- #
class TestUser:
    def test_create_user(self, user: User) -> None:
        assert user.name == "Alice"
        assert user.id == 1

    def test_can_validate_should_returns_false(self, user: User) -> None:
        assert user.can_validate(skill_id=1) is False

    def test_str_representation(self, user: User) -> None:
        assert "Alice" in str(user)
        assert "1" in str(user)


# --- Learner --- #
class TestLearner:
    def test_create_learner(self, learner: Learner) -> None:
        assert learner.name == "Bob"
        assert learner.id == 2

    def test_can_validate_without_skills_should_returns_false(self, learner: Learner) -> None:
        assert learner.can_validate(skill_id=1) is False

    def test_add_skill(self, learner: Learner) -> None:
        learner.add_skill(1)
        assert learner.can_validate(skill_id=1) is True

    def test_add_skill_duplicate_should_raises_value_error(self, learner: Learner) -> None:
        learner.add_skill(1)
        with pytest.raises(ValueError):
            learner.add_skill(1)

    def test_can_validate_unknown_skill_returns_false(self, learner_with_skill: Learner) -> None:
        assert learner_with_skill.can_validate(skill_id=99) is False

    def test_str_representation(self, learner: Learner) -> None:
        assert "Bob" in str(learner)


# --- Trainer --- #
class TestTrainer:
    def test_create_trainer(self, trainer: Trainer) -> None:
        assert trainer.name == "John"
        assert trainer.id == 99

    def test_can_validate_should_always_returns_true(self, trainer: Trainer) -> None:
        assert trainer.can_validate(skill_id=1) is True
        assert trainer.can_validate(skill_id=99) is True
        assert trainer.can_validate(skill_id=0) is True

    def test_str_representation(self, trainer: Trainer) -> None:
        assert "John" in str(trainer)


# --- Classroom --- #
class TestClassroom:
    def test_create_classroom(self, classroom: Classroom) -> None:
        assert classroom.name == "P1"
        assert classroom.get_users() == []

    def test_add_user(self, classroom: Classroom, learner: Learner) -> None:
        classroom.add_user(learner)
        assert len(classroom.get_users()) == 1

    def test_add_multiple_users(self, classroom_with_users: Classroom) -> None:
        assert len(classroom_with_users.get_users()) == 2

    def test_merge_classrooms(self, learner: Learner, trainer: Trainer) -> None:
        c1 = Classroom(name="P1")
        c1.add_user(learner)

        c2 = Classroom(name="P2")
        c2.add_user(trainer)

        c3 = c1 + c2
        assert len(c3.get_users()) == 2

    def test_merge_keeps_originals_intact(self, learner: Learner, trainer: Trainer) -> None:
        c1 = Classroom(name="P1")
        c1.add_user(learner)

        c2 = Classroom(name="P2")
        c2.add_user(trainer)

        _ = c1 + c2
        assert len(c1.get_users()) == 1
        assert len(c2.get_users()) == 1

    def test_str_representation(self, classroom: Classroom) -> None:
        assert "P1" in str(classroom)


# --- Skill --- #
class TestSkill:
    def test_create_skills(self, skill: Skill) -> None:
        assert skill.id == 1
        assert skill.name == "Python"

    def test_equality(self, skill: Skill) -> None:
        assert skill == Skill(id=1, name="Python")

    def test_inequality(self, skill: Skill) -> None:
        assert skill != Skill(id=2, name="FastAPI")


# --- Validation --- #
class TestValidation:
    def test_creation_pending(self, validation: Validation) -> None:
        assert validation.status == ValidationStatus.PENDING
        assert validation.pre_validated_by is None
        assert validation.validated_by is None

    def test_creation_pre_validated(self) -> None:
        v = Validation(
            id=2,
            learner_id=11,
            skill_id=1,
            status=ValidationStatus.SELF_VALIDATED,
            pre_validated_by=10,
        )
        assert v.status == ValidationStatus.SELF_VALIDATED
        assert v.pre_validated_by == 10

    def test_creation_validated(self) -> None:
        v = Validation(
            id=3,
            learner_id=12,
            skill_id=1,
            status=ValidationStatus.VALIDATED,
            validated_by=99,
        )
        assert v.status == ValidationStatus.VALIDATED
        assert v.validated_by == 99