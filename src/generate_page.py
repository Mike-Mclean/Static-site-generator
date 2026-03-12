from split_blocks import *
import os

def generate_page(from_path, template_path, dest_path):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        md = file.read()

    with open(template_path, "r") as tp:
        template = tp.read()

    html = markdown_to_HTML_node(md).to_html()
    title = extract_title(md)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as new_html:
        new_html.write(template)

if __name__ == "__main__":
    from_path = "/home/mikemclean/github.com/Mike-Mclean/Static-site-generator/content/index.md"
    template_path = "/home/mikemclean/github.com/Mike-Mclean/Static-site-generator/template.html"
    dest_path = "/home/mikemclean/github.com/Mike-Mclean/Static-site-generator/public/index.html"
    generate_page(from_path, template_path, dest_path)