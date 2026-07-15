import os
import shutil
import sys

from block_extractors import extract_title
from markdown_to_html import markdown_to_html


def copy_structure(src, dst) -> None:
    objects_to_copy = os.listdir(src)
    for obj in objects_to_copy:
        is_dir = os.path.isdir(src + obj)
        split = obj.split("/")
        if is_dir:
            dir_name = dst + split[-1] + "/"
            os.mkdir(dir_name)
            copy_structure(src + obj + "/", dir_name)
        else:
            shutil.copy(src + obj, dst + split[-1])


def generate_page(from_path, template_path, dest_path, basepath) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        from_val = f.read()
    with open(template_path) as f:
        template_val = f.read()
    html_content = markdown_to_html(from_val)
    page_title = extract_title(from_val)
    template_val = (
        template_val.replace("{{ Title }}", page_title)
        .replace("{{ Content }}", html_content.to_html())
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )
    with open(dest_path, "w") as f:
        f.write(template_val)


def generate_pages_recursive(
    dir_path_content, template_path, dest_dir_path, basepath
) -> None:
    objects_to_copy = os.listdir(dir_path_content)
    for obj in objects_to_copy:
        is_dir = os.path.isdir(dir_path_content + obj)
        split = obj.split("/")
        if is_dir:
            dir_name = dest_dir_path + split[-1] + "/"
            os.mkdir(dir_name)
            generate_pages_recursive(
                dir_path_content + obj + "/",
                template_path,
                dest_dir_path + obj + "/",
                basepath,
            )
        else:
            generate_page(
                dir_path_content + obj,
                template_path,
                dest_dir_path + obj[:-2] + "html",
                basepath,
            )


def main():
    basepath = sys.argv[1]
    if basepath is None or basepath == "":
        basepath = "/"

    public_dir_path = "docs/"
    static_dir_path = "static/"
    if not os.path.exists(public_dir_path):
        os.mkdir(public_dir_path)
    elif len(os.listdir(public_dir_path)) > 0:
        shutil.rmtree(public_dir_path)
        os.mkdir(public_dir_path)
    copy_structure(static_dir_path, public_dir_path)
    generate_pages_recursive("content/", "template.html", public_dir_path, basepath)


if __name__ == "__main__":
    main()
