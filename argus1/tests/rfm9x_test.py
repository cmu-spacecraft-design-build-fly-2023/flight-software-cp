from board_config import BoardConfig
from components import pycubed_rfm9x
from .component_test import ComponentTest

class RFM9X_Test(ComponentTest):
    """
    Class: RFM9X_Test

    Contains the test functions for the RFM9X module.
    """
    def __init__(self):
        try:
            self._initialize()
        except Exception as e:
            print("Could not initialize RFM9X. Error: " + str(e))

    
    def _initialize(self) -> None:
        """initialize: Initialize the RFM9X module for testing
        """
        pass

        
    def run_diagnostic_test(self) -> None:
        """run_diagnostic_test: Run all tests for the RFM9X module
        """
        pass