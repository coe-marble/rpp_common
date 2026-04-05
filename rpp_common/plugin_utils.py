from rpp_common import RPP_Plugin

def get_plugin_base_fully_specified_class_name():
    return "<class '" + f"{RPP_Plugin.__module__}.{RPP_Plugin.__name__}" + "'>"
