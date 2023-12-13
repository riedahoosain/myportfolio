import zipfile

def extract_archive(archivefilepath, destinationfolder):
    with zipfile.ZipFile(archivefilepath, 'r') as archivefile:
        archivefile.extractall(destinationfolder)


if __name__ == "__main__":
    print("This is the zip_creator function")