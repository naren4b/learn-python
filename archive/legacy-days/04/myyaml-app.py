import yaml

with open("res/config.yaml", "r") as file:
    config = yaml.safe_load(file)

# print("Configuration Data:", config)
# print("Type of config:", type(config))

sources = config.get("spec").get("sources")
# print("Spec Data:", sources)

for source in sources:
    print("Source:", source)


# Why *keys is Better than ["spec", "sources"]
# With *keys (cleaner):
# With list (more verbose):
# Key Concepts

# Concept	Example	Purpose
# *keys	*keys → ("a", "b", "c")	Accept unlimited positional args
# *args unpacking	*["a", "b"] → passed as a, b	Unpack list into args
# Keyword-only arg	default=None after *keys	Force named parameter
# isinstance() check	isinstance(d, dict)	Verify type before operations
# This is a production-grade pattern used in frameworks like Django and libraries for safe nested dictionary access!
