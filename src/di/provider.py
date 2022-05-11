import flask
import flask_injector
import injector
from bp.max_area_getter import MaxAreaGetter

class MaxAreaGetterModule(injector.Module):
    def configure(self, binder):
        binder.bind(MaxAreaGetter,
                    to=self.create,
                    scope=flask_injector.request)

    @injector.inject
    def create(self, config: flask.Config) -> MaxAreaGetter:
        return MaxAreaGetter()
