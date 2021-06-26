import uuid

from automated_grading_system.assignment import Assignment
from automated_grading_system.assignment_grader import AssignmentGrader


class Grader:
    """Class for managing which assignments are available and which one each student is currently working on"""

    def __init__(self):
        self.student_graders = {}
        self.assignment_classes = {}

    def register(self, assignment_class):
        if not issubclass(assignment_class, Assignment):
            raise RuntimeError("Your class does not have the right methods")

        id = uuid.uuid4()
        self.assignment_classes[id] = assignment_class
        return id

    def start_assignment(self, student, id):
        self.student_graders[student] = AssignmentGrader(student, self.assignment_classes[id])

    def get_lesson(self, student):
        assignment = self.student_graders[student]
        return assignment.lesson()

    def check_assignment(self, student, code):
        assignment = self.student_graders[student]
        return assignment.check(code)

    def assignment_summary(self, student):
        grader = self.student_graders[student]
        return f"""
        {student}'s attempts at {grader.assignment.__class__.__name__}: 
        
        attempts..: {grader.attempts}
        correct...: {grader.correct_attempts}
        passed....: {grader.correct_attempts > 0}
        """
