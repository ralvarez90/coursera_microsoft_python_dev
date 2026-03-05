"""
MEDIA SENDER
"""
import glob
import os

NUMBER_OF_THREADS = 8

file_extensions = [
    'mp4', 'mkv', 'avi', 'mov', 'flv', 'mpg', 'mpeg', 'jpg', 'jpeg', 'png',
]


def get_user_cwd() -> str:
    home = os.environ.get('USERPROFILE') or os.environ.get('HOME')
    return home


def get_path_files(cwd: str) -> list[str]:
    path_to_search = os.path.join(get_user_cwd(), '**', f'*.{str(file_extensions).replace("'", "")}')
    return glob.glob(path_to_search, recursive=True)


def send_media(ip: str, files: list[str]):
    pass


if __name__ == '__main__':
    userpath = get_user_cwd()
    files = get_path_files(userpath)
    for f in files:
        print(f'- {f}')

    input('\nPress ENTER to continue...')
