class AssetManager:
    _assets_dict: dict = dict()

    @staticmethod
    def get_asset(asset_id):
        if asset_id in AssetManager._assets_dict.keys():
            return AssetManager._assets_dict[asset_id]

    @staticmethod
    def set_asset(asset_id, game_asset):
        if asset_id not in AssetManager._assets_dict.keys():
            AssetManager._assets_dict[asset_id] = game_asset

    @staticmethod
    def del_asset(asset_id):
        if asset_id in AssetManager._assets_dict.keys():
            game_asset = AssetManager._assets_dict[asset_id]
            del AssetManager._assets_dict[asset_id]
            del game_asset
