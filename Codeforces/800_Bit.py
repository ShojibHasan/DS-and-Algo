import re
def bitland(single_integer):
    final_value_positive = 0
    final_value_negative = 0
    for i in range(single_integer):
        statement = input()
        if re.search("[++]",statement):
            final_value_positive=final_value_positive+1
        elif re.search("[--]",statement):
            final_value_negative =final_value_negative+1
    final_output = final_value_positive-final_value_negative
    print(final_output)


single_integer = int(input())
bitland(single_integer)