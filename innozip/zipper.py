import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:

        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

def extract_archive(archivefilepath, destinationfolder):
    with zipfile.ZipFile(archivefilepath, 'r') as archivefile:
        archivefile.extractall(destinationfolder)


if __name__ == "__main__":
    print("This is the zip creat and extract function")