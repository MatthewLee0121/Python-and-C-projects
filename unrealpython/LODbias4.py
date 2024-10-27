import unreal

def set_lod_bias(asset_path, lod_bias):
    assets = unreal.EditorAssetLibrary.list_assets(asset_path, recursive=True)
    for asset in assets:
        asset_obj = unreal.load_asset(asset)
        if isinstance(asset_obj, unreal.Texture):
            asset_obj.set_editor_property("lod_bias", lod_bias)
            unreal.EditorAssetLibrary.save_asset(asset)

if __name__ == "__main__":
    asset_path = "/Game/HwaseongHaenggung/Textures"
    lod_bias = 8
    set_lod_bias(asset_path, lod_bias)

