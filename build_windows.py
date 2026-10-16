from pathlib import Path
import importlib.util
import subprocess
import sys
import shutil

root = Path(__file__).resolve().parent
subprocess.run(['uv', 'sync', '--frozen', '--no-dev'], cwd=root, check=True)
python = root / '.venv/Scripts/python.exe'
args = [str(python), '-m', 'PyInstaller', '--noconfirm', '--clean', '--onedir', '--windowed', '--name', 'sp', '--contents-directory', '_internal', '--collect-all', 'videotrans']
packages = ['torch', 'torchaudio', 'ctranslate2', 'faster_whisper', 'whisper', 'transformers', 'transformers4576', 'diffusers', 'tokenizers', 'tiktoken', 'onnxruntime', 'sherpa_onnx', 'ten_vad', 'litellm', 'librosa', 'soundfile', 'scipy', 'sklearn', 'piper', 'gtts', 'edge_tts', 'modelscope', 'funasr', 'pyannote.audio', 'gradio_client', 'certifi', 'sentencepiece', 'av', 'soynlp', 'nagisa']
for package in packages:
    args.extend(['--collect-all', package])
args.append('sp.py')
subprocess.run(args, cwd=root, check=True)
dist = root / 'dist/sp'
# Application paths and the splash screen resolve resources beside sp.exe.
shutil.copytree(root / 'videotrans', dist / 'videotrans', ignore=shutil.ignore_patterns('__pycache__', '*.pyc'), dirs_exist_ok=True)
shutil.copytree(root / 'ffmpeg', dist / 'ffmpeg', dirs_exist_ok=True)
shutil.copy2(root / 'LICENSE', dist / 'LICENSE')
(dist / 'START_HERE.txt').write_text('Extract the entire ZIP to a folder, then open sp.exe. Do not move sp.exe out of this folder. Python is bundled. AI models are downloaded when needed. GPU features require a compatible NVIDIA driver.\n', encoding='utf-8')
(dist / 'smoke.py').write_text("import sys\nfrom PySide6.QtWidgets import QApplication\nimport torch, ctranslate2, faster_whisper, gtts, edge_tts\nfrom videotrans.configure import config\napp = QApplication([])\nprint('Portable import check passed')\n", encoding='utf-8')
subprocess.run([str(dist / 'sp.exe'), str(dist / 'smoke.py')], cwd=dist, check=True, timeout=240)
(dist / 'smoke.py').unlink()
print('Windows portable build and import check completed.')
