import os
import json
import compatibility as cpb
from server.request import Request
from server.response import get_response, get_file_response, Response
from state import state


def _get_bomb_state(request: Request) -> Response:
    response = f"""{{"state": {"true" if state.bomb.get_state() else "false"}}}"""
    return get_response(request, message=response, content_type='application/json')


def get_humedad(request: Request) -> Response:
    humidity = state.get_humidity()
    return get_response(request, message=str(humidity), content_type='application/json')


def get_temperatura(request: Request) -> Response:
    temperature = state.get_temperature()
    return get_response(request, message=str(temperature), content_type='application/json')


def _get_sensors_state(request: Request) -> Response:
    humidity = state.get_humidity()
    temperature = state.get_temperature()

    response = {
        "humidity": humidity,
        "temperature": temperature
    }

    # Convertir los datos en JSON y devolver la respuesta
    return get_response(request, message=json.dumps(response), content_type='application/json')


def index(request: Request) -> Response:
    file_path = cpb.join_path(os.getcwd(), 'static', 'index.html')
    return get_file_response(
        request,
        file_path,
        'text/html'
    )


def style(request: Request) -> Response:
    file_path = cpb.join_path(os.getcwd(), 'static', 'style.css')
    return get_file_response(
        request,
        file_path,
        'text/css'
    )


def javascript(request: Request) -> Response:
    file_path = cpb.join_path(os.getcwd(), 'static', 'main.js')
    return get_file_response(
        request,
        file_path,
        'text/javascript'
    )


def bomb_on(request: Request) -> Response:
    state.bomb.on()
    return _get_bomb_state(request)


def bomb_off(request: Request) -> Response:
    state.bomb.off()
    return _get_bomb_state(request)


def bomb_state(request: Request) -> Response:
    return _get_bomb_state(request)


def sensors_data(request: Request) -> Response:
    return _get_sensors_state(request)
