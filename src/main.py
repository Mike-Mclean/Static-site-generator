import os
from generate_page import *
from copystatic import dir_copy

static_path = "./static"
public_path = "./public"
content_path = "./content"
template_path = "./template.html"

def main():
    dir_copy(static_path, public_path)

    from_path = os.path.join(content_path, "index.md")
    dest_path = os.path.join(public_path, "index.html")
    generate_page(from_path, template_path, dest_path)


if __name__ == "__main__":
    main()
