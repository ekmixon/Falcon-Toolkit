"""Falcon Toolkit: Console Utils.

This file contains tools to help with displaying data on the console in a user-friendly,
colourful and/or helpful way.
"""

import platform


ESC = '\033'
OSC = f'{ESC}]'
ST = ESC + '\\'


def build_hyperlink(target: str, text: str, link_id: str = None):
    """Build a clickable hyperlink that is compatible with modern shells."""
    id_str = f"id={link_id}" if link_id else ""
    return f'{OSC}8;{id_str};{target}{ST}{text}{OSC}8;;{ST}'


def build_file_hyperlink(file_path: str, text: str, link_id: str = None):
    """Extend the build_hyperlink function to support file paths, cross-platform."""
    hostname = "localhost" if platform.system() == "Windows" else platform.node()
    file_path = file_path.removeprefix('/')
    uri_file_path = f"file://{hostname}/{file_path}"
    return build_hyperlink(uri_file_path, text, link_id)
