

from viewflow.base import this, Flow

from Wish.views import create, validate, delegate, implement, approve, issue

from viewflow import flow
from viewflow.base import this, Flow
from .models import Task

"""
class Workflow(Flow):

    '''
    States
    0:    START
    1:    WAITING_FOR_VALIDATION
    2:    WAITING_FOR_IMPLEMENTATION
    3:    WAITING_FOR_APPROVAL
    4:    REFUSED
    5:    COMPLETED
    '''

    #process_class = Task

    # Create task
    # 0->1
    create = flow.Start(create).Next(this.validate)

    # Validate task
    # 1->2, kick off   (state==2)
    # 1->4: refused    (state==4)
    validate = flow.View(validate).Next(this.check_validate)
    check_validate = flow.If(this.state==2) \
                             .Then(this.implement) \
                         .Else(this.refuse)

    # Implement task
    # 2->3
    implement = flow.View(implement).Next(this.approve)

    # Approve task
    # 3->2, back to implementation (state==2)
    # 3->5: completed              (state==5)
    approve = flow.View(approve).Next(this.check_approve)
    check_approve = flow.If(this.state==2) \
                             .Then(this.implement) \
                         .Else(this.complete)

    # Refuse task
    # ->4
    refuse = flow.End()

    # Complete task
    # ->5
    completed = flow.End()
"""