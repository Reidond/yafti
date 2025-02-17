import json


def parse_packages(packages: dict | list) -> dict:
    output = {}

    if isinstance(packages, dict):
        for group, value in packages.items():
            output[f"group:{group}"] = True
            output.update(parse_packages(value["packages"]))
        return output

    for pkgcfg in packages:
        for package in pkgcfg.values():
            if isinstance(package, dict):
                package = json.dumps(package)
            output[f"pkg:{package}"] = True
    return output
