class Utils:
    @staticmethod
    def fill_db():
        return {
            'short_name': '1kCap',
            'full_name': '100 Capacity',
            'latitude': 5.0492068,
            'longitude': 7.9363032
        }
        
    @staticmethod
    def params_near():
        return {
            'name': '1kCap',
            'latitude': 5.0492068,
            'longitude': 7.9363032
        }
        
    @staticmethod
    def params_far():
        return {
            'name': '1kCap',
            'latitude': 5.0051067,
            'longitude': 7.9580944
        }

    @staticmethod
    def custom_assert(response, Status_code=None, distance=None, proximity=None, proximity_qst=None):
        if Status_code is not None:
            assert response.status_code == Status_code
        if distance is not None:
            assert distance in response.data
        if proximity is not None:
            assert response.data.get(proximity_qst) == proximity
            assert proximity_qst in response.data