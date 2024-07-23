# Function with return value
def strip_and_lowercase(original):
    modified = original.strip().lower()
    return modified

uggly_string = "   MixED cASe  "
pretty = strip_and_lowercase(uggly_string)
print("pretty result: {}".format(pretty))