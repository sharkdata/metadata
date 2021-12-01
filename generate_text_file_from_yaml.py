
import pathlib
import yaml

with open("text_file_from_all.txt", "w", encoding="utf8") as out_file:
    for file_path in sorted(pathlib.Path("dcat_ap_se").glob("*.yaml")):
        if str(file_path) == "dcat_ap_se/0_template.yaml":
            continue
        with open(file_path, encoding="utf8") as file:
            try:
                # Parse yaml.
                metadata = yaml.load(file, Loader=yaml.FullLoader)
                # Print content.
                out_file.write("\n====================================================\n")
                out_file.write("From YAML-file: " + str(file_path))
                out_file.write("\n====================================================\n")
                out_file.write("\nTITLE(en):\n")
                out_file.write(str(metadata["dataset"]["title"]["en"]))
                out_file.write("\nDESCRIPTION(en):\n")
                out_file.write(str(metadata["dataset"]["description"]["en"]))
                out_file.write("\nTITLE(sv):\n")
                out_file.write(str(metadata["dataset"]["title"]["sv"]))
                out_file.write("\nDESCRIPTION(sv):\n")
                out_file.write(str(metadata["dataset"]["description"]["sv"]))
                out_file.write("\n")
            except Exception as e:
                print("ERROR: ", e)