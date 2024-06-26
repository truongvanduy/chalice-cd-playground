from chalice import Chalice
from chalice import BadRequestError

app = Chalice(app_name='hello-world')
app.debug = True

CITIES_TO_STATE = {
    'seattle': 'WA',
    'portland': 'OR',
    'sanfrancisco': 'CA',
}


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/cities/{city}')
def state_of_city(city):
    try:
        return {
            'state': CITIES_TO_STATE[city]
        }
    except KeyError:
        raise BadRequestError('Unknown city: %s, valid choices are: %s' % (
            city, ', '.join(CITIES_TO_STATE.keys())))


@app.route('/test', methods=['GET'])
def test_deployment():
    return {'status': 'success'}


@app.route('/resource/{value}', methods=['PUT'])
def put_test(value):
    return {'value': value}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
