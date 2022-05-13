from flask import jsonify

class JSONResponseBuilder:
    def __init__(self, response, status_code):
        self.response = response
        self.code = status_code
    
    def build(self):
        if self.code in [200, 201]:
            return jsonify({
                "response": self.response,
                "code": self.code,
            })
        return jsonify({
            "error": self.response,
            "code": self.code,
        })