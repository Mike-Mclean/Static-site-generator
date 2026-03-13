from split_blocks import *
import os

def generate_page(from_path, template_path, dest_path, basepath):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        md = file.read()

    with open(template_path, "r") as tp:
        template = tp.read()

    html = markdown_to_HTML_node(md).to_html()
    title = extract_title(md)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as new_html:
        new_html.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        if not os.path.isfile(item_path):
            new_dest_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(item_path, template_path, new_dest_path, basepath)
        else:
            new_dest_path = os.path.join(dest_dir_path, "index.html")
            generate_page(item_path, template_path, new_dest_path, basepath)
