from unit_testing_sample_code import string_capitalizer, capitalize_list, integer_manipulator, manipulate_list


class TestClass:

    def test_string1(self):
        assert string_capitalizer("c") == "C"

    def test_string2(self):
        assert string_capitalizer("") == ""

    def test_string3(self):
        assert string_capitalizer(4) == "FouR"

    def test_strlist1(self):
        assert capitalize_list(["two", "c", "4", ""]) == [
            "TwO", "C", "FouR", ""]

    def test_int1(self):
        assert integer_manipulator(10) == 66

    def test_int2(self):
        assert integer_manipulator(2) == 2

    def test_int3(self):
        assert integer_manipulator(3) == 6

    def test_int4(self):
        assert integer_manipulator(0) == 0

    def test_int5(self):
        assert integer_manipulator("three") == 1

    def test_int_list1(self):
        assert manipulate_list([10, 2, 3, 0, "three"]) == [66, 2, 6, 0, 1]


"""test_strlist("0", ["TwO", "C", "FouR", ""],
             capitalize_list(["two", "c", 4, ""]))
print("\nInteger Manipulator Tests:")
test_int("0", 66, integer_manipulator(10))
test_int("1", 2, integer_manipulator(2))
test_int("2", 6, integer_manipulator(3))
test_int("3", 0, integer_manipulator(0))
test_int("4", 1, integer_manipulator("three"))
print("\nManipulate List Tests:")
test_intlist("0", [66, 2, 6, 0, 1], manipulate_list([10, 2, 3, 0, "three"]))"""
