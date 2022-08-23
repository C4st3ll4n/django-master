from rest_framework.exceptions import APIException


class CantRateYourArticle(APIException):
    status_code = 403
    default_detail = "You can't rate your own article"


class AlreadyRated(APIException):
    status_code = 400
    default_detail = "You already rated this article"
