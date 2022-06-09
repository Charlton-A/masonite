from mergedeep import merge


class BaseDriver:
    """Base Session driver"""

    def __init__(self, application: "Application"):
        self.application = application
        self.options = {}

    def set_options(self, options: dict):
        self.options = merge(self.options, options)
        return self
