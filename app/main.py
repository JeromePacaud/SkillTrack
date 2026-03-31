from models import Classroom, Learner, User

if __name__ == '__main__':
    user = User(name='Alice', id=1)
    learner_1 = Learner(name='Bob', id=2)
    learner_2 = Learner(name='Charlie', id=3)
    learner_3 = Learner(name='David', id=4)
    learner_4 = Learner(name='Eve', id=5)

    # User tests
    print(user.name)
    print(user.id)
    print(user.can_validate(skill_id=1))

    # Learner tests
    print(learner_1.name)
    print(learner_1.id)
    print(learner_1.can_validate(skill_id=1))
    learner_1.add_skill(skill_id=1)
    print(learner_1.can_validate(skill_id=1))
    print(learner_1)
    print(learner_2)
    print(learner_3)
    print(learner_4)

    # Classroom tests
    classroom_1 = Classroom('P1')
    classroom_2 = Classroom('P2')
    classroom_3 = Classroom('P32')
    classroom_4 = Classroom('P28')
    print(classroom_1.name)
    classroom_1.add_user(learner_1)
    classroom_1.add_user(learner_2)

    print(classroom_2.name)
    classroom_2.add_user(learner_3)
    classroom_2.add_user(learner_4)

    p3 = classroom_1 + classroom_2
    print(p3)
    print(p3.get_users())

    p4 = classroom_3 + classroom_4
    print(p4)


