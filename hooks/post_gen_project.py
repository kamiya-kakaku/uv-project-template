import re
from pathlib import Path
import sys

def replace_python_version():
    """
    Replace the full Python version (e.g., "3.12.3") in pyproject.toml with the major.minor version format (e.g., ">=3.12").

    This function reads the pyproject.toml file, extracts the Python version specified in the cookiecutter context,
    parses it to get the major.minor version, and then updates the pyproject.toml file with this parsed version.

    Raises:
        SystemExit: If the python_version format is invalid.
    """
    project_path = Path.cwd()
    pyproject_file = project_path / "pyproject.toml"

    # Read the content of pyproject.toml
    with open(pyproject_file, "r") as file:
        content = file.read()

    # Extract the python_version from cookiecutter context
    python_version = "{{ cookiecutter.python_version }}"

    # Parse the major.minor version
    match = re.match(r"(\d+\.\d+)\.\d+", python_version)
    if match:
        major_minor_version = match.group(1)
    else:
        print(f"Error: Invalid python_version format: {python_version}")
        sys.exit(1)

    # Replace the placeholder with the required format
    new_content = content.replace(python_version, f"{major_minor_version}")

    # Write the new content back to pyproject.toml
    with open(pyproject_file, "w") as file:
        file.write(new_content)

if __name__ == "__main__":
    """
    Entry point for the script.

    This script is intended to be run immediately after the Cookiecutter template has been generated.
    It updates the pyproject.toml file to ensure the Python version is specified in the require format.
    """
    replace_python_version()