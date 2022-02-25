import obtain_path
import os, sys
import zip_file
if __name__ == '__main__':
    file_path = obtain_path.obtain_web_file_path()
    try:
        os.system(f"cd {file_path} && npm run build-analysis-large")
        print('>>> build finesh! <<<')
        zip_path = obtain_path.obtain_zip_path()
        zip_file_path = os.path.join(file_path, 'dist')

        files = [zip_file_path]
        zip_file_name = os.path.join(zip_path, 'web_build_package.zip')
        zip_file.zip_files(files, zip_file_name)
    except Exception as e:
        print(e)
        print('>>> build error! <<<')
        sys.exit(1)
