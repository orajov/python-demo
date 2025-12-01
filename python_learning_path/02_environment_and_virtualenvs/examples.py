"""Show how paths change inside a virtual environment."""

import sys
import sysconfig

print("Executable:", sys.executable)
print("Site-packages:", sysconfig.get_paths()["purelib"])
