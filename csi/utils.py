import importlib
from pathlib import Path

def load_module(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        import csi.utils
        import importlib
        path = Path(f"csi/plugins/{plugin_name}.py")
        name = "csi.plugins.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("csi has (re)Imported " + plugin_name)
    else:
        import csi.utils
        import importlib
        path = Path(f"csi/plugins/{plugin_name}.py")
        name = "csi.plugins.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.csi = csi