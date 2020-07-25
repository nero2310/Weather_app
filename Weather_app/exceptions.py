class UnsafeAddress(Exception):
    """
    Exception occurred if user use http address instead of https.
    I highly disrecommend send data in http protocol because
    it's send data in not encrypted form,https is much safer
    """

    def __init__(self, message):
        super(Exception, self).__init__(message)


class CityNotFoundOrApiNotResponse(Exception):
    """
    Exception occured if APiNotResponse, or city doesn't exist
    """

    def __init__(self, message):
        super(Exception, self).__init__(message)
