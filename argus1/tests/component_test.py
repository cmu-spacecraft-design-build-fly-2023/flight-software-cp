"""
component_tests.py

This file contains the base class for all component tests.

Author: Harry Rosmann
Date: 2/14/2024
"""

class ComponentTest:
    """
    Base class for all component tests
    """
    def __initialize(self) -> None:
        """initialize: Initialize the component for testing
        """
        raise NotImplementedError("Subclasses must implement initialize method")


    def run_diagnostic_test(self) -> None:
        """run_diagnostic_test: Run all tests for the component
        """
        raise NotImplementedError("Subclasses must implement run_diagnostic_test method")