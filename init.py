# accept user input as argument for the number of UUIDs to generate and copy to clipboard
import pyperclip
import uuid
import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate UUIDs')
    parser.add_argument('num', type=int, nargs='?', help='Number of UUIDs to generate')
    args = parser.parse_args()

    def generate_uuid():
        return str(uuid.uuid4())

    if args.num == None or args.num == 1:
        uuid_str = generate_uuid()
        pyperclip.copy(uuid_str)
        print("📎✅ UUID copied to clipboard: " + uuid_str)

    else:
        list_uuids = []

        for i in range(args.num):
            uuid_str = generate_uuid()
            list_uuids.append(uuid_str)

        pyperclip.copy('\n'.join(list_uuids))
        print("📎✅ Done generating " + str(args.num) + " UUIDs")


if __name__ == '__main__':
    main()
