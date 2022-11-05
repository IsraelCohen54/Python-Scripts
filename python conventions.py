def some_public_func(arg_input):
    print("don't do much, print class attribute number", arg_input)
    return None


class ClassNameConvention:
    """
    Some explanation about the class
    """

    _ClassNameConvention__attribute_one = 1  # Shared attribute. Inline comment example, only if really needed!!!

    # Constructor
    def __init__(self, attribute_one: int,
                 private_attribute) -> None:  # e.g. def __init__(self, attribute_one: int = 1)

        self._ClassNameConvention__attribute_one = attribute_one  # = Instance variables
        self._private_attribute = private_attribute

    def _internal_func(cls):
        """
        Print class attribute
        """
        print("dont do much, print class attribute number", cls._ClassNameConvention__attribute_one)
        return None

    def get_data(cls):
        """Return read only private member
        """
        return cls._private_attribute

    def set_data(cls, value):
        """Setter for private member
        """
        cls._private_attribute = value
        return None


# Inheritance example:
class AddedExample(ClassNameConvention):
    def __init__(self, added_var):
        # call parent class constructor
        super().__init__(attribute_one=2, private_attribute=2)
        self._added_var = added_var

    def _show_instances(cls):
        """
         If any return statement returns an expression, any return statements where no value is returned should
         explicitly state this as return None, and an explicit return statement should be present at the end of the
         function (if reachable):
        """
        print("cls.get_data(), inherited:", cls.get_data(),
              "cls.added_var:", cls._added_var)
        return None

    def f(cls, x):
        try:
            return x * cls._ClassNameConvention__attribute_one
        except type:  # should be specific type
            return "bad multiplication" + x + " " + cls._ClassNameConvention__attribute_one
        else:
            x + " " + cls._ClassNameConvention__attribute_one


if __name__ == '__main__':
    string_ = "int_"  # the trailing _ used to differentiate from string, int etcetera
    # cls;
    cls_name_convention = ClassNameConvention(1, 2)
    cls_name_convention.set_data(1)
    print(cls_name_convention.get_data())

    added_ex = AddedExample(1)
    added_ex._show_instances()

    """
    Some more examples:
    """
    some_str = "barricade brrr boom 123..."
    # Correct:
    if some_str.startswith("bar"):
        print("startswith() and endswith() are cleaner and less error prone")
    # Wrong:
    # if foo[:3] == 'bar':

    # Correct:
    if isinstance(some_str, str):
        print("Object type comparisons should always use isinstance() instead of comparing types directly")
    # Wrong:
    # if type(some_str) is type(str):
    #    print("str indeed")

    # Correct:
    if not some_str:
        if some_str:
            print("For sequences, (strings, lists, tuples), use the fact that empty sequences are false. String check")
    # Wrong:
    # if len(seq):
    # if not len(""):

    # Wrong - Don’t write string literals that rely on significant trailing whitespace.
    # my_string_literal = "trailing whitespace!!!                   "

    greeting = 1
    # Correct:
    if greeting:
        print("Don’t compare boolean values to True or False using ==")
    # Wrong:
    # if greeting == True:
    # if greeting is True:

    """
    def send_email(address,  # type: Union[str, List[str]]
                   sender,  # type: str
                   cc,  # type: Optional[List[str]]
                   bcc,  # type: Optional[List[str]]
                   subject='',
                   body=None  # type: List[str]
                   ):
        # type: (...) -> bool
        # # => Send an email message.  Return True if successful.
        < code >
    """

    """
    # Correct:

    code: int
    
    class Point:
        coords: Tuple[int, int]
        label: str = '<unknown>'

    # Wrong:
    code:int  # No space after colon
    code : int  # Space before colon
    
    class Test:
        result: int=0  # No spaces around equality sign
    """
