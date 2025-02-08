import os

class FileSaver:

    def __init__(self):
        self.output_folder = 'output'
        os.makedirs(self.output_folder, exist_ok=True)

    def save_to_file(self,  content, file_name):
        file_name = file_name.replace(' ', '_').lower()
        file_path = os.path.join(self.output_folder, file_name)
        print(f'Saving to file: {file_path}')
        with open(file_path, 'w') as file:
            for line in content:
                self.write_to_file(line + '\n', file)
    
    def write_to_file(self, content, file):
        file.write(content)
