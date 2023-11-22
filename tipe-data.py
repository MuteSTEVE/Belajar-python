data_str = "False"
data_int = 1

print("data =", data_str, "Type =", type(data_str))
print("data =", data_int, "Type =", type(data_int))

print("""
#####################
  Casting datatype
#####################
""")

cast_str = str(data_str)
cast_float = float(data_str)
cast_bool = bool(data_str)

print(f"data =, '{cast_str}', Type =, '{type(cast_str)}'")
print(f"data =, '{cast_float}', Type =, '{type(cast_float)}'")
print(f"data =, '{cast_bool}', Type =, '{type(cast_bool)}'")
