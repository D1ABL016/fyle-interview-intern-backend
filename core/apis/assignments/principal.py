from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from .schema import AssignmentSchema, TeacherSchema , AssignmentGradeSchema

principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)

@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def get_all_assignments(p):
    """Returns list of all assignments"""
    principal_assignments = Assignment.get_all_submiited_and_graded_assignment()
    principal_assignments_dump = AssignmentSchema().dump(principal_assignments, many=True)
    return APIResponse.respond(data=principal_assignments_dump)
    

@principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def get_all_techers(p):
    """Returns list of all taechers"""
    all_teachers = Assignment.get_all_teachers()
    all_teachers_dump = TeacherSchema().dump(all_teachers, many=True)
    return APIResponse.respond(data=all_teachers_dump)



@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_or_regrade_assignment(p,incoming_payload):
    """grades or re-grades any submitted or graded assignment"""
    # print('id => ',incoming_payload.id)
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)
    graded_assignment = Assignment.grade_by_principal(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    db.session.commit()
    return APIResponse.respond(data=graded_assignment_dump)
    

