class DriverNotFound(Exception):
    """Raised when Selenium driver cannot be found in system"""
    pass

class RequestBlocked(Exception):
    """Rasied when Animeheaven blocked the request for abuse"""
    pass
