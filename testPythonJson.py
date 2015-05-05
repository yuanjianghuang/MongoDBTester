
import json
import treelib
def main():
    with open("E:\PythonProject\\ronmofang\\tree.txt", 'r') as handle:
        parsed = json.load(handle)

    print json.dumps(parsed, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()