def _requirements():
    import os
    REQUIREMENTS_FILENAME = 'requirements.txt'
    directory = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(directory, REQUIREMENTS_FILENAME), "r") as f:
        return f.readlines()

def _callable(argument):
    # Module imports
    from external.dummy_module import dummy_function
    return dummy_function(argument)

requirements = _requirements()
callable = _callable