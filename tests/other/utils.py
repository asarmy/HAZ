"""Utility functions for tests."""

import os


def read_file_lines(filepath):
    """Read and return all lines from a file with trailing newlines stripped."""
    with open(filepath, "r") as f:
        return [" ".join(line.split()) for line in f if line.strip()]


def verify_output_against_expected(computed_filepath, reference_filepath):
    """
    Compare the contents of the output file against the expected file.
    Assert that both exist and their contents match.
    """
    # Assert files exist
    assert os.path.isfile(computed_filepath), f"Computed file not found: {computed_filepath}"
    assert os.path.isfile(reference_filepath), f"Referece file not found: {reference_filepath}"

    # Read and compare contents
    got_lines = read_file_lines(computed_filepath)
    exp_lines = read_file_lines(reference_filepath)

    assert got_lines == exp_lines, (
        f"Output mismatch for '{computed_filepath}'\n"
        f"--- Got lines ---\n{got_lines}\n\n"
        f"--- Expected lines ---\n{exp_lines}\n"
    )
