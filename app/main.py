from models import Classroom, Learner, Skill, Trainer, Validation, ValidationStatus

# --- Trainer --- #
trainer_1: Trainer = Trainer(name='John', id=1)
trainer_2: Trainer = Trainer(name='Bob', id=2)
trainer_3: Trainer = Trainer(name='Alice', id=3)

# --- Learner --- #
learner_1: Learner = Learner(name='Jerome', id=1)
learner_2: Learner = Learner(name='Theo', id=2)
learner_3: Learner = Learner(name='Fanny', id=3)

# --- Skills --- #
skill_1: Skill = Skill(id=1, name='Python')
skill_2: Skill = Skill(id=2, name='Java')

# --- Validations --- #
validation_1: Validation = Validation(
	id=1,
	learner_id=1,
	skill_id=1,
	status=ValidationStatus.VALIDATED,
	pre_validated_by=learner_1.id,
	validated_by=trainer_1.id,
)

validation_2: Validation = Validation(
	id=2,
	learner_id=2,
	skill_id=1,
	status=ValidationStatus.SELF_VALIDATED,
	pre_validated_by=learner_2.id,
)

validation_3 = Validation(
	id=1,
	learner_id=3,
	skill_id=1,
	status=ValidationStatus.PENDING,
)

# --- Classrooms --- #
class_1: Classroom = Classroom(name='P1')
class_2: Classroom = Classroom(name='P2')

class_1.add_user(user=trainer_1)
class_1.add_user(user=learner_1)
class_1.add_user(user=learner_2)

class_2.add_user(user=trainer_2)
class_2.add_user(user=learner_3)

class_3: Classroom = class_1 + class_2

# --- Display --- #

learner_1.add_skill(skill_id=1)
learner_1.add_skill(skill_id=2)
learner_2.add_skill(skill_id=2)
learner_3.add_skill(skill_id=2)

print(' Classes '.center(50, '#'), end='\n\n')

print(f' Classe : {class_1.name} '.center(50, '#'), end='\n\n')
print(class_1)
print(class_1.get_users(), end='\n\n')

print(f' Classe : {class_2.name} '.center(50, '#'), end='\n\n')
print(class_2)
print(class_2.get_users(), end='\n\n')

print(f' Classe : {class_3.name} '.center(50, '#'), end='\n\n')
print(class_3)
print(class_3.get_users(), end='\n\n')

print(' Compétences '.center(50, '#'), end='\n\n')
print(skill_1, end='\n\n')
print(skill_2, end='\n\n')
print(skill_1 == skill_2)
print(skill_1 == Skill(id=1, name='Python'), end='\n\n')

print(' Validations '.center(50, '#'), end='\n\n')
print(validation_1, end='\n\n')
print(validation_2, end='\n\n')
