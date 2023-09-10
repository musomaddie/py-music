from pymusic import globalvars


def update_prefix(
        to_remove: str, to_replace: str, unless_contains="AAAAAAAAAAAAAAA"):
    """
    Update the prefix string used for the logger by replacing to_remove with to_replace.

    :param to_remove:
    :param to_replace:
    :return:
    """

    if unless_contains in globalvars.prefix:
        return

    globalvars.prefix = globalvars.prefix.replace(to_remove, to_replace)


def remove_section(to_remove: str):
    globalvars.prefix = globalvars.prefix.replace(to_remove, "")
