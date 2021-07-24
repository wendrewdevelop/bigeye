import os
from datetime import datetime


def console_log(alert_type, description):
    """
        Gera uma mensagem de log no console
        do terminal.

        PARAMS:
            alert_type: tipo da mensagem (INF0, ERROR, WARNING, SUCCESS).
            description: descrição do log.
    """

    try:
        text = f"{alert_type}: {description}. - Time {str(datetime.now())}"
        print(text.encode('utf-8'))
    except Exception as error:
        print(f"ERROR: funcion {console_log.__name__} -> error -> {str(error)}")
