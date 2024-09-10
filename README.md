## uv-project-template
The uv-project-template provides a new Python project template using [uv](https://github.com/astral-sh/uv), which is based on [cookiecutter-data-science](https://github.com/drivendataorg/cookiecutter-data-science).

### How to Create a Project
※ Strongly recommend to see the official page: [uv](https://github.com/astral-sh/uv) and [cookiecutter](https://github.com/cookiecutter/cookiecutter/tree/da0df9d3a09205749307c403f06a1b4ca3af4cb8).

1. Install cookiecutter.
```bash
pipx install cookiecutter
```
2. Install uv.
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
3. Use cookiecutter to reference the template repository.
```bash
cookiecutter https://github.com/kamiya-kakaku/uv-project-template.git
```
4. When prompted, provide an appropriate and clear project name (use hyphens to separate). The first and second prompts will be formatted according to your project name, so pressing Enter is fine for these.
```bash
project_name [My Python Project]: ai-xxxxxx
project_slug [ai-xxxxxx]:
package_name [ai_xxxxxx]:
```
5. Finally, set the Python version to be used in your project. The version specified here will be set when running `uv venv`.
```bash
python_version [3.12.5]:
```
6. After completion, check if a project directory has been created underneath.
7. After creating the Python project with cookiecutter, run the following command to activate venv. Ensure that the Python version matches the one specified during cookiecutter creation.
```bash
uv venv
source .venv/bin/activate
uv sync
```
8. For example, if you want to change the Python version to 3.12.0, run the following command:
```bash
uv python pin 3.12.0
uv sync
```