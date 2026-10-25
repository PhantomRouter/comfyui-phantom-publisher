"""Phantom Publisher: toolbar-based immutable workflow publishing for ComfyUI."""

import logging

from .publisher import register_routes

WEB_DIRECTORY = "./web"
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

register_routes()

logging.getLogger("phantom.publisher").warning(
    "Phantom Publisher is retired: Phantom Router no longer accepts workflows "
    "from ComfyUI. Remove this node in ComfyUI Manager."
)

__all__ = ["WEB_DIRECTORY", "NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
