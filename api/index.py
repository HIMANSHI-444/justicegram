import os
import sys
from pathlib import Path

# Add project root directory to sys.path so 'app' and all project modules can be imported seamlessly
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app import create_app

env = 'production' if os.environ.get('VERCEL') else os.environ.get('FLASK_ENV', 'development')
app = create_app(env)

if __name__ == '__main__':
    app.run(debug=True)
