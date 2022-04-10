import os
import zipfile
from pathlib import Path
import json


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(
                os.path.join(root, file),
                os.path.relpath(os.path.join(root, file), os.path.join(path, "..")),
            )


zipf = zipfile.ZipFile("Python.zip", "w", zipfile.ZIP_DEFLATED)



p = Path("data")

index = {"packages": {}}

for lib in p.iterdir():
    if not lib.is_dir():
        continue
    libname, version = lib.name.split("_")
    print(libname)

    filename = f"{libname}-{version}.zip"
    index["packages"].setdefault(libname, {})[version] = filename
    with zipfile.ZipFile(f"{libname}-{version}.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
        zipdir(lib, zipf)

Path("index.json").write_text(json.dumps(index, indent=2))
