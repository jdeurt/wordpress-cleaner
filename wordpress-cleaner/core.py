from helpers import crawl as crawl_helper
import os
import re

def clean_files(root_dir, target_pattern, ext):
    print("Working in directory: " + os.path.realpath(os.path.normpath(root_dir)))

    crawler = crawl_helper.DirectoryCrawler(root_dir)

    files = crawler.crawl(ext)
    files_clean_count = 0

    print("Found " + str(len(files)) + " files.")

    print("Progress: " + str(files_clean_count) + "/" + str(len(files)))

    for file in files:
        modified_lines = []

        with open(file, "r") as f:
            for line in f:
                line = re.sub(target_pattern, "", line)

                modified_lines.append(line)

        with open(file, "w") as f:
            for line in modified_lines:
                f.write(line)

        files_clean_count += 1
        print("Progress: " + str(files_clean_count) + "/" + str(len(files)))
