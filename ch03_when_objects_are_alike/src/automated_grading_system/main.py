from automated_grading_system.grader import Grader
from automated_grading_system.lessons import IntroToPython
from automated_grading_system.lessons import Statistics


def main() -> None:
    grader = Grader()

    itp_id = grader.register(IntroToPython)
    grader.start_assignment("Eve", itp_id)

    print("Eve's lesson.....: ", grader.get_lesson("Eve"))
    print("Eve's check......: ", grader.check_assignment("Eve", "a = 1 ; b = 'hello'"))
    print("Eve's other check: ", grader.check_assignment("Eve", "a = 1\nb = 'hello'"))
    print(grader.assignment_summary("Eve"))

    stat_id = grader.register(Statistics)
    grader.start_assignment("Eve", stat_id)

    print("Eve's lesson.....: ", grader.get_lesson("Eve"))
    print("Eve's check......: ", grader.check_assignment("Eve", "avg=5.25"))
    print("Eve's other check: ", grader.check_assignment("Eve", "avg = statistics.mean([1, 5, 18, -3])"))
    print(grader.assignment_summary("Eve"))


if __name__ == '__main__':
    main()
