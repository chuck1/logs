import pbs.classes.Executable

e = pbs.classes.Executable.Executable("test_util_0", self)

e.require("util")

e.make()

