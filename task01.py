import os
import shutil
import argparse

def copy_files(src_dir, dest_dir):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            file_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1][1:]  # Отримаємо розширення файлу без крапки

            # Створимо підкаталог на основі розширення файлу
            sub_dir = os.path.join(dest_dir, extension)
            os.makedirs(sub_dir, exist_ok=True)

            # Копіюємо файл у відповідний підкаталог
            try:
                shutil.copy(file_path, os.path.join(sub_dir, file))
                print(f"Скопійовано: {file_path} до {sub_dir}")
            except Exception as e:
                print(f"Помилка копіювання {file_path}: {str(e)}")

        for dir in dirs:
            copy_files(os.path.join(root, dir), dest_dir)

def main():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та впорядковання файлів на основі їх розширень.")
    parser.add_argument("src_dir", help="Шлях до вихідного каталогу")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Шлях до каталогу призначення (default: dist)")
    args = parser.parse_args()

    src_dir = args.src_dir
    dest_dir = args.dest_dir

    try:
        copy_files(src_dir, dest_dir)
        print("Копіювання та впорядкування файлів успішно завершено.")
    except Exception as e:
        print(f"Помилка: {str(e)}")

if __name__ == "__main__":
    main()
