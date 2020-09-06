import os

class DirectoryCrawler:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    # https://stackoverflow.com/questions/18394147/recursive-sub-folder-search-and-return-files-in-a-list-python/#answer-59803793
    def _scandir(self, dir, ext):
        subfolders, files = [], []

        for f in os.scandir(dir):
            if f.is_dir():
                subfolders.append(f.path)
            if f.is_file():
                if os.path.splitext(f.name)[1].lower() in ext:
                    files.append(f.path)

        for dir in list(subfolders):
            sf, f = self._scandir(dir, ext)
            subfolders.extend(sf)
            files.extend(f)
        return subfolders, files

    def crawl(self, ext):
        subfolders, files = self._scandir(self.root_dir, ext)
        
        norm_files = [os.path.realpath(os.path.normpath(file)) for file in files]\

        return norm_files
