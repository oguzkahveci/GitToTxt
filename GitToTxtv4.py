# Gerekli kütüphaneleri yükle
import os
import subprocess

# Repository URL'si ve klonlanacak yerel dizin
repo_url = 'https://bitbucket.org/catlikecoding-projects/custom-srp-project.git'
clone_dir = '/content/custom_srp_project'  # Klonlanacak dizin

# Repository'yi klonlama komutu
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

# .cs ve .hlsl dosyalarını ara ve birleştir
combined_code = ''
for root, dirs, files in os.walk(clone_dir):
    for file in files:
        if file.endswith('.cs') or file.endswith('.hlsl') or file.endswith('.shader'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as file:
                combined_code += file.read() + '\n\n'

# Birleştirilmiş kodları bir txt dosyasına yaz
# Dosya adını, clone_dir değişkenindeki dizin ismi ile aynı yap
output_file_name = os.path.basename(os.path.normpath(clone_dir)) + '.txt'
output_file_path = os.path.join('/content', output_file_name)
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(combined_code)

print(f'Birleştirilmiş kodlar {output_file_path} dosyasına yazıldı.')
