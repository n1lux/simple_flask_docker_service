from flask import Flask, jsonify
import platform


app = Flask(__name__)

@app.route('/')
def index():
    return "Machine Information api!!!"

@app.route('/api/v0/machine')
def machine_info():
    p = platform.uname()
    info = {'machine': p.machine,
            'node': p.node,
            'processor': p.processor,
            'release': p.release,
            'system': p.system,
            'version': p.version
            }

    return jsonify(info)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
