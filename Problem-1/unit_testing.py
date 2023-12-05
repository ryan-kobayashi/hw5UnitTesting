from unit_testing_sample_code import string_capitalizer, capitalize_list, integer_manipulator, manipulate_list


def test_string(num, eoutput, output):
    if (eoutput == output):
        print("Test " + str(num) + " passed! " +
              "'" + str(eoutput) + "'" + " matches '" + str(output) + "'")
    else:
        print("Test " + str(num) + " failed. Expected: '" +
              str(eoutput) + "'. Got: '" + str(output) + "'.")


def test_strlist(num, eoutput, output):
    if len(output) != len(eoutput):
        print("Expected output and actual output have different lengths")
    else:
        print("Test " + str(num) + ":")
        for i in range(len(output)):
            if output[i] == eoutput[i]:
                print("Part " + str(i) + " in test " + str(num) + " passed! " +
                      "'" + str(eoutput[i]) + "'" + " matches '" + str(output[i]) + "'")
            else:
                print("Part " + str(i) + " int test " + str(num) + " failed. Expected: '" +
                      str(eoutput[i]) + "'. Got: '" + str(output[i]) + "'.")


def test_int(num, eoutput, output):
    if (eoutput == output):
        print("Test " + str(num) + " passed! " +
              "'" + str(eoutput) + "'" + " matches '" + str(output) + "'")
    else:
        print("Test " + str(num) + " failed. Expected: '" +
              str(eoutput) + "'. Got: '" + str(output) + "'.")


def test_intlist(num, eoutput, output):
    if len(output) != len(eoutput):
        print("Expected output and actual output have different lengths")
    else:
        print("Test " + str(num) + ":")
        for i in range(len(output)):
            if output[i] == eoutput[i]:
                print("Part " + str(i) + " in test " + str(num) + " passed! " +
                      "'" + str(eoutput[i]) + "'" + " matches '" + str(output[i]) + "'")
            else:
                print("Part " + str(i) + " int test " + str(num) + " failed. Expected: '" +
                      str(eoutput[i]) + "'. Got: '" + str(output[i]) + "'.")


print("\nString Capitalizer Tests:")
# test_string is the function for testing the string capitalizer and takes # three arguments: test number (“0”), expected output value (“TwO”), and
# the call to the string_capitalizer function with the argument “two”. test_string("0", "TwO", string_capitalizer("two"))
test_string("1", "C", string_capitalizer("c"))
test_string("2", "FouR", string_capitalizer(4))
test_string("3", "", string_capitalizer(""))
print("\nList Capitalizer Tests:")
test_strlist("0", ["TwO", "C", "FouR", ""],
             capitalize_list(["two", "c", 4, ""]))
print("\nInteger Manipulator Tests:")
test_int("0", 66, integer_manipulator(10))
test_int("1", 2, integer_manipulator(2))
test_int("2", 6, integer_manipulator(3))
test_int("3", 0, integer_manipulator(0))
test_int("4", 1, integer_manipulator("three"))
print("\nManipulate List Tests:")
test_intlist("0", [66, 2, 6, 0, 1], manipulate_list([10, 2, 3, 0, "three"]))
