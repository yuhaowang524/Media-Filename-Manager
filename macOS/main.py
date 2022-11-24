import os
import sys


# This is a Python script designed to change file names according to
# following naming rule <folder_address> <media_type> <name> <season_number/year> <mode>
# folder_address: the absolute path of media folder noted that media content must be within the folder
# media_type: only 'm' or 't' are allowed 'm' means movie and 't' means tv shows
# name: new name of media
# season_number/year: if 't' is entered than season_number is followed else if year the movie is produced
# mode: 0 means a dry run 1 means actual rename it is highly recommended that a dry run will be performed
# before the actual rename happens


def filename_changer(argv):
    file_list = []
    try:
        file_address = argv[0]
        folder_dir = os.listdir(file_address)
    except (FileNotFoundError, IOError):
        print("Error: invalid <folder_address> absolute path is required\nplease enter <folder_address> <type> <name> "
              "<season_number / year> <mode>")

    for file in folder_dir:
        file_list.append(file)
    file_list.sort()

    if argv[1] == 't':
        if argv[4] == '0' or argv[4] == '1':
            if argv[4] == '0':
                print("This is the result of a dry run, please check before actual name changing")

            for num, file in enumerate(file_list, 1):
                file_ext = os.path.splitext(file)[-1].lower()
                if file_ext == '.mp4' or file_ext == '.mkv':
                    old_path = file_address + "/" + file
                    new_name = argv[2] + '_S' + argv[3] + 'E' + str(num) + file_ext
                    new_path = file_address + "/" + new_name
                    if argv[4] == '1':
                        os.rename(old_path, new_path)
                    print(file + " now changes to " + new_name)

        else:
            print("Error: invalid <mode> only allows '0' or '1' \nplease enter <folder_address> <type> <name> "
                  "<season_number / year> <mode>")
            sys.exit(0)

    elif argv[1] == 'm':
        if argv[4] == '0' or argv[4] == '1':
            if argv[4] == '0':
                print("This is the result of a dry run, please check before actual name changing")

            for file in file_list:
                file_ext = os.path.splitext(file)[-1].lower()
                if file_ext == '.mp4' or file_ext == '.mkv':
                    old_path = file_address + "/" + file
                    new_name = argv[2] + '_' + argv[3] + file_ext
                    new_path = file_address + "/" + new_name
                    if argv[4] == '1':
                        os.rename(old_path, new_path)
                    print(file + " now changes to " + new_name)

        else:
            print("Error: invalid <mode> only allows '0' or '1' \nplease enter <folder_address> <type> <name> "
                  "<season_number / year> <mode>")
            sys.exit(0)

    else:
        print("Error: invalid <media_type> only allows 't' or 'm'\nplease enter <folder_address> <type> <name> "
              "<season_number / year> <mode>")
        sys.exit(0)


if __name__ == '__main__':
    filename_changer(sys.argv[1:])
