from app.api import bp
from flask import jsonify
from app.models import Source, Software
from flask import current_app as app


@bp.route('/api/v1/', methods=['GET'])
def Api_Info():
    api_info = {
        'version': 'v1'
    }
    return jsonify(api_info)


@bp.route('/api/v1/sources',methods=['GET'])
def Get_Sources():
    query_results = Source.query.all()
    results = [r.as_dict() for r in query_results]
    return jsonify(results)


@bp.route('/api/v1/softwares',methods=['GET'])
def Get_Softwares():
    query_results = Software.query.all()
    results = [r.as_dict() for r in query_results]
    return jsonify(results)