# Use this file instead of main.py, to debug in VSCODE without adding start parameters
import sys
from src.main import main
sys.argv.append('run')
main()
