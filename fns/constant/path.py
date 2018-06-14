class Paths:
    class Resources:
        _dir = "resources/"

        class NewsAPI:
            _dir = "keychain/"

            _api_key_file_name = "newsapi.json"

            @staticmethod
            def get_api_key_file_path():
                return Paths.Resources._dir + Paths.Resources.NewsAPI._dir + Paths.Resources.NewsAPI._api_key_file_name

        _category_map_file_name = "default-category-map.json"

        @staticmethod
        def get_default_category_maps():
            return Paths.Resources._dir + Paths.Resources._category_map_file_name
