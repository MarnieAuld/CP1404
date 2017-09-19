
class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """Initialise ProgrammingLanguage from given field types"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".\
            format(self.name, self.typing, self.reflection, self.year)
