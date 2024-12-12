from server import Path
from .views import (
    bomb_on, bomb_off, bomb_state, 
    index, javascript, style, 
    sensors_data, get_humedad, get_temperatura
)

routes = [
    Path('/', index),
    Path('/style.css', style),
    Path('/main.js', javascript),
    Path('/bomb/on', bomb_on),
    Path('/bomb/off', bomb_off),
    Path('/bomb/state', bomb_state),
    Path('/sensors/data', sensors_data),  # Nueva ruta para datos de sensores
    Path('/humedad', get_humedad),        # Ruta para obtener humedad
    Path('/temperatura', get_temperatura) # Ruta para obtener temperatura
]
