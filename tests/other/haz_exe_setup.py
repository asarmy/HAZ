"""
For setting up and validating a HAZ executable. This module provides:
- A class (`HazExeSetup`) for managing relative filepaths, including automatic discovery of a
  HAZ*.exe executable in a predefined build directory, and a method for executing HAZ with
  command-line input.
- A pytest fixture (`validate_executable`) ensures the HAZ executable exists and is validated
  before running any test cases via a session-scoped fixture for pre-test validation.
"""


import os
import pytest
import glob
import subprocess


class HazExeSetup:
    """Base class to set up and validate the HAZ executable."""

    @classmethod
    def setup_class(cls):
        """Set up shared resources for all test classes."""
        cls.this_dir = os.path.dirname(os.path.abspath(__file__))
        cls.project_dir = os.path.dirname(os.path.dirname(cls.this_dir))
        cls.build_dir = os.path.join(cls.project_dir, "build")
        cls.haz_exe = cls.find_haz_exe()

    @classmethod
    def find_haz_exe(cls):
        """Find exactly one HAZ*.exe in the class's build directory."""
        exe_candidates = [
            f
            for f in glob.glob(os.path.join(cls.build_dir, "*"))
            if f.lower().endswith(".exe") and "haz" in os.path.basename(f).lower()
        ]
        if not exe_candidates:
            raise FileNotFoundError(
                f"No HAZ executable found in the build directory: {cls.build_dir}"
            )
        elif len(exe_candidates) > 1:
            raise FileNotFoundError(
                f"Expected exactly one HAZ*.exe, but found multiple: {exe_candidates}"
            )
        return exe_candidates[0]

    @classmethod
    def run_exe_with_input(cls, input_str):
        """Run the HAZ executable with the given input."""
        result = subprocess.run(
            [cls.haz_exe],
            text=True,
            input=input_str,
            capture_output=True,
            cwd=cls.this_dir,
        )
        assert result.returncode == 0, (
            f"HAZ.exe returned nonzero exit code.\n"
            f"--- USER INPUT ---\n{input_str}\n"
            f"--- STDOUT ---\n{result.stdout}\n"
            f"--- STDERR ---\n{result.stderr}"
        )
        return result


# Shared fixture for validation
# Runs automatically at start of pytest session with `autouse=True`
@pytest.fixture(scope="session", autouse=True)
def validate_executable():
    """Ensure the HAZ executable exists once per test session."""
    HazExeSetup.setup_class()
    if not os.path.exists(HazExeSetup.haz_exe):
        raise FileNotFoundError(f"Executable not found: {HazExeSetup.haz_exe}")
