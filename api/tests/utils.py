import json

class Utils:
    @staticmethod
    def fill_db():
        return {
            'short_name': 'ELF',
            'full_name': '100 Capacity',
            'latitude': 5.0492068,
            'longitude': 7.9363032
        }
        
    @staticmethod
    def params_near():
        return {
            'name': 'ELF',
            'latitude': 5.0492068,
            'longitude': 7.9363032
        }
        
    @staticmethod
    def params_far():
        return {
            'name': 'ELF',
            'latitude': 5.0051067,
            'longitude': 7.9580944
        }

    @staticmethod
    def custom_assert(response, distance=None, proximity=None, proximity_qst=None):
        if distance is not None:
            assert distance in response.data
        if proximity is not None:
            assert proximity_qst in response.data