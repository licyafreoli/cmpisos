#!/usr/bin/env python3
import shutil
import os
from pathlib import Path

src_dir = Path('/vercel/share/v0-project/public/images/products')
dst_dir = Path('/vercel/share/v0-project/images/products')

# Criar pasta destino se não existir
dst_dir.mkdir(parents=True, exist_ok=True)

# Copiar todos os arquivos
if src_dir.exists():
    for file in src_dir.iterdir():
        if file.is_file():
            dst_file = dst_dir / file.name
            shutil.copy2(file, dst_file)
            print(f"Copiado: {file.name}")
    print(f"Total de arquivos copiados: {len(list(dst_dir.glob('*')))}")
else:
    print(f"Pasta origem não existe: {src_dir}")
