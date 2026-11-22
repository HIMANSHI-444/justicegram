import os
import sys

# Ensure root directory is in python search path
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root not in sys.path:
    sys.path.insert(0, root)

try:
    from app import create_app
    app = create_app('production')
except Exception as e:
    # Safe fallback handler in case of cold-start exception
    from flask import Flask
    app = Flask(__name__)
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        import traceback
        return f"<h3>JusticeGram Startup Error</h3><pre>{traceback.format_exc()}</pre>", 500
