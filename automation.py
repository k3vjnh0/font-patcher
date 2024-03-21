import os

path = os.getcwd()

lst_fonts = os.listdir(f"{path}/fonts")

try:
    lst_fonts.remove(".DS_Store")
except Exception as e:
    print(e)
    pass

while True:
    os.system("clear")
    options = {}

    for index, font_name in enumerate(lst_fonts):
        print(f"({index + 1}) {font_name}")
        options[str(index + 1)] = font_name

    usr_input = input("Select font to patch: ")

    if usr_input in options:
        font_family = options[usr_input]
        path_to_font = f"{path}/fonts/{font_family}"
        output_dir = f"{path}/nerd-fonts/{font_family}"

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_dir = output_dir.replace(" ", "\ ")

        fonts = os.listdir(path_to_font)
        for font in fonts:
            if font.endswith(".ttf") or font.endswith(".otf"):
                input_dir = f"{path_to_font}/{font}".replace(" ", "\ ")
                os.system(
                    f"fontforge -script font-patcher {input_dir} -c -out {output_dir}"
                )
        break
    else:
        continue
