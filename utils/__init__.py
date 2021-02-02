import os

# get a list of valid python files to import as modules
# uses location of __file__ to identify the folder
list_of_files = [ f for f in os.listdir(os.path.dirname(__file__))\
                             if not f.startswith('_')\
                             and not f.startswith('.')\
                             and f.endswith('.py')\
                             and os.path.isfile ]

module_list = []
# drop the .py extension from the file list and populate the module_list
for name in list_of_files:
    module_list.append(os.path.splitext(name)[0])

# Use the generated module_list for wildcard imports
__all__ = module_list
