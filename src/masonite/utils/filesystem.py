import os
import platform
import pathlib


def make_directory(directory: str) -> bool:
    """Create all directories to the given file directory if they do not exist"""
    if not os.path.isfile(directory):
        if not os.path.exists(os.path.dirname(directory)):
            # Create the path to the model if it does not exist
            os.makedirs(os.path.dirname(directory))

        return True

    return False


def make_full_directory(directory: str) -> bool:
    """Create all directories to the given path directory if they do not exist"""
    if not os.path.isfile(directory):
        if not os.path.exists(directory):
            # Create the path to the model if it does not exist
            os.makedirs(directory)

        return True

    return False


def creation_date(path_to_file: str) -> "float|int":
    """Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    """
    if platform.system() == "Windows":
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime


def modified_date(path_to_file: str) -> "float|int":
    if platform.system() == "Windows":
        return os.path.getmtime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_mtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return 0


def render_stub_file(stub_file: str, name: str) -> str:
    """Read stub file, replace placeholders and return content."""
    with open(stub_file, "r") as f:
        content = f.read()
        content = content.replace("__class__", name)
    return content


def get_module_dir(module_file):
    return os.path.dirname(os.path.realpath(module_file))


def get_extension(filepath: str, without_dot: bool = False) -> str:
    """Get file extension from a filepath. If without_dot=True the . prefix will be removed from
    the extension."""
    extension = "".join(pathlib.Path(filepath).suffixes)
    if without_dot:
        return extension[1:]
    return extension
