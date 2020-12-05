from app.api import bp
from flask import jsonify

@bp.route('/api/v1/', methods=['GET'])
def Api_Info():
    api_info = {
        'version': 'v1'
    }
    return jsonify(api_info)
