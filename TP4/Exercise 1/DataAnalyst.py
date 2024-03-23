from Employee import Employee

class DataAnalyst(Employee):

    def __init__(self, name, emp_id, exp, tools: list, project_completed):
        super().__init__(name, emp_id, exp)
        self._tools = tools
        self._project_completed = project_completed

    @property
    def tools(self):
        return self._tools

    @tools.setter
    def tools(self, tools):
        self._tools = tools

    @property
    def project_completed(self):
        return self._project_completed

    @project_completed.setter
    def project_completed(self, project_completed):
        self._project_completed = project_completed

    def add_tools(self, tool):
        self._tools.append(tool)

    def display_info(self):
        super().display_info(endLine=", ")
        print(f"Tools: {', '.join(self._tools)}, Projects Completed: {self._project_completed}")
