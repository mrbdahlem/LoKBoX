import webrepl

import gc
import micropython

webrepl.start(password="LoKBoX")

print()
print("-----------------")
gc.collect()
micropython.mem_info()
print("-----------------")
print()