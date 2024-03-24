import _grabbers.DeptGrabber as DeptGrabber
import _grabbers.ProgramGrabber as ProgramGrabber

class Coordinator:

    list_dept = []
    list_colleges = []
    debt_grabber = None
    program_grabber = None

    def __init__(self):
        self.dept_grabber = DeptGrabber()
        self.program_grabber = ProgramGrabber()
    
