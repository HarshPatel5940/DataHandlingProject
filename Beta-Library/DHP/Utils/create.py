from DHP.paths import user_file_path

def write_user(id11, name, password):
    with open(user_file_path, "a", newline="") as f:
        cprint("Data Is OK", 'green')
        file = csv.writer(f)
        user_row = [id11, name, password]
        file.writerow(user_row)
