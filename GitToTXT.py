import os
import subprocess

repo_url = 'https://bitbucket.org/catlikecodingunitytutorials/custom-srp-11-post-processing.git'
clone_dir = '/content/custom_srp_11_post_processing'  # Klonlanacak dizin

if not os.path.isdir(clone_dir):
    os.makedirs(clone_dir, exist_ok=True)
    cmd = f'git clone {repo_url} "{clone_dir}"'
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print('Repository başarıyla klonlandı.')
    else:
        print(f'Hata: {stderr.decode("utf-8")}')
else:
    print(f'{clone_dir} zaten mevcut.')

combined_code = ''
for root, dirs, files in os.walk(clone_dir):
    for file in files:
        if file.endswith('.cs') or file.endswith('.hlsl'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as file:
                combined_code += file.read() + '\n\n'

# Birleştirilmiş kodları bir txt dosyasına yaz
output_file_path = '/content/combined_code.txt'
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(combined_code)

print(f'Birleştirilmiş kodlar {output_file_path} dosyasına yazıldı.')
