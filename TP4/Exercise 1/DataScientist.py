from Employee import Employee


class DataScientist(Employee):
    def __init__(self, name, emp_id, exp, specialisation, programming_languages: list):
        super().__init__(name, emp_id, exp)
        self._specialisation = specialisation
        self._programming_languages = programming_languages

    @property
    def specialisation(self):
        return self._specialisation

    @specialisation.setter
    def specialisation(self, specialisation):
        self._specialisation = specialisation

    @property
    def programming_languages(self):
        return self._programming_languages

    @programming_languages.setter
    def programming_languages(self, programming_languages):
        self._programming_languages = programming_languages

    def add_language(self, language):
        self._programming_languages.append(language)

    def display_info(self):
        super().display_info(endLine=", ")
        print(
            f"Specialisation: {self._specialisation}, Programming Languages: {', '.join(self._programming_languages)}")
