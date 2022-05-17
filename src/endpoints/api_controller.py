import logging
from typing import Final

import flask_injector
import injector
from bp.max_area_getter import MaxAreaGetter
from bp.max_area_getter import Parameters
from di import provider
from flask import jsonify
from flask import request
from flask_api import exceptions
from flask_api import FlaskAPI
from flask_api import status
from flask_expects_json import expects_json

CODE: Final = "code"
MESSAGE: Final = "message"
HEIGHTS: Final = "heights"
AREA: Final = "area"

INJECTOR_DEFAULT_MODULES = dict(max_area_getter=provider.MaxAreaGetterModule())


def _configure_dependency_injection(flask_app, injector_modules, custom_injector):
    modules = dict(INJECTOR_DEFAULT_MODULES)
    if injector_modules:
        modules.update(injector_modules)

    flask_injector.FlaskInjector(
        app=flask_app,
        injector=custom_injector,
        modules=modules.values(),
    )


def create_app(
    *,
    custom_injector: injector.Injector = None,
    injector_modules=None,
):
    app = FlaskAPI(__name__)

    schema = {HEIGHTS: ["int"], "required": [HEIGHTS]}

    @app.route("/tekton/max_area_getter/1.0.0", methods=["POST"])
    @expects_json(schema)
    def calculate_max_area(max_area_getter: MaxAreaGetter):
        try:
            req_data = request.get_json()
            heights = req_data[HEIGHTS]
            parameters = Parameters(heights)
            output = max_area_getter.run(parameters)
            return {AREA: output}, status.HTTP_200_OK
        except Exception as e:
            logging.error("Fatal error in max_area_getter", exc_info=True)
            return {CODE: 500, MESSAGE: str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR

    _configure_dependency_injection(app, injector_modules, custom_injector)

    return app
