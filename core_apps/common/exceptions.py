from rest_framework.views import exception_handler


def handler_generic_error(exc, context, response):
    status_code = response.status_code
    response.data = {"status_code": status_code, "errors": response.data}
    return response


def _handler_not_found_error(exc, context, response):
    view = context.get("view", None)
    if view and hasattr(view, "queryset") and view.queryset is not None:
        status_code = response.status_code
        error_key = view.queryset.model._meta.verbose_name
        response.data = {"status_code": status_code, "errors": {error_key:response.data['detail']}}
    else:
        response = handler_generic_error(exc, context, response)


def common_exception_handler(exc, context):
    response = exception_handler(exc, context)

    handlers = {
        "NotFound": _handler_not_found_error,
        "ValidationError": handler_generic_error,
    }

    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    return response
