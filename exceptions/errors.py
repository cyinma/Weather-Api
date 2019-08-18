from flask import jsonify


def entity_not_found(entity: str):
    response = jsonify({'message': f"{entity} not found"})
    response.status_code = 400
    return response
