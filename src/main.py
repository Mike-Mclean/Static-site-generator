from generate_page import *
from copystatic import dir_copy
import sys

static_path = "./static"
public_path = "./docs"
content_path = "./content"
template_path = "./template.html"

def main():

    if sys.argv[1] is None:
        basepath = "/"
    else:
        basepath = sys.argv[1]

    dir_copy(static_path, public_path)
    generate_pages_recursive(content_path, template_path, public_path, basepath)

if __name__ == "__main__":
    main()
