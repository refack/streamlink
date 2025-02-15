# This module will get replaced by versioningit when building a source distribution
# and instead of trying to get the version string from git, a static version string will be set



def _get_version() -> str:
    """
    Get the current version from git in "editable" installs
    """
    # ruff: disable[import-outside-top-level, unsorted-imports]
    from pathlib import Path
    from versioningit import get_version
    # ruff: enable[import-outside-top-level, unsorted-imports]
    try:
        ret = get_version(project_dir=Path(__file__).parents[2])
    except:
        ret = "0.0.0"
    return ret


__version__ = _get_version()
