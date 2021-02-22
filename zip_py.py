import os
import zipfile


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(
                os.path.join(root, file),
                os.path.relpath(os.path.join(root, file), os.path.join(path, "..")),
            )


zipf = zipfile.ZipFile("Python.zip", "w", zipfile.ZIP_DEFLATED)


from pathlib import Path

p = Path("data")

for lib in p.iterdir():
    if not lib.is_dir():
        continue
    libname, version = lib.name.split("_")
    print(libname)

    with zipfile.ZipFile(f"{libname}-{version}.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
        zipdir(lib, zipf)
