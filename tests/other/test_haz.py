import os
import pytest

from haz_exe_setup import HazExeSetup
from utils import read_file_lines, verify_output_against_expected


@pytest.mark.parametrize(
    "inp",
    [
        inp.strip()
        for inp in open(os.path.join(os.path.dirname(__file__), "scenario_run_files.txt"))
        if inp.strip()
    ],
)
@pytest.mark.dependency(name="run_dsha")
def test_run_dsha(inp):
    """Run DSHA (spectral models, option 2)."""
    HazExeSetup.setup_class()
    absolute_path = os.path.join(HazExeSetup.this_dir, inp)
    input_str = f"0\n2\n{absolute_path}\n"
    HazExeSetup.run_exe_with_input(input_str)


@pytest.mark.parametrize(
    "inp",
    [
        inp.strip()
        for inp in open(os.path.join(os.path.dirname(__file__), "scenario_run_files.txt"))
        if inp.strip()
    ],
)
@pytest.mark.dependency(depends=["run_dsha"])
def test_verify_dsha(inp):
    """Verify DSHA calculations."""
    this_dir = os.path.dirname(os.path.abspath(__file__))

    # Read input file to get output filename/filepath
    absolute_path = os.path.join(this_dir, inp)
    with open(absolute_path, "r") as fin:
        input_file_lines = fin.read().splitlines()
    output_filename = input_file_lines[1].strip()
    output_filepath = os.path.join(this_dir, output_filename)

    # Determine output filename/filepath
    # NOTE: It is set to be the same as specified in the .inp except with a .txt extension
    root, _ = os.path.splitext(output_filename)
    expected_filename = f"{root}.txt"
    expected_filepath = os.path.join(this_dir, "expected", expected_filename)

    # Verify files match
    verify_output_against_expected(output_filepath, expected_filepath)
