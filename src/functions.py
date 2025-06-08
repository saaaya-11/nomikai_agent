from typing import List, Literal

from agents import function_tool

import components.hotpepper as func_hotpepper

@function_tool
def get_large_service_area_code_hotpepper():
    """
    Get large service area code list
    Returns:
        str(List[Dict]) : large service area code list
    """
    print(f"[DEBUG] get_large_service_area_code_hotpepper")
    return str(func_hotpepper.get_learge_service_area_code_hotpepper())

@function_tool
def get_service_area_code_hotpepper():
    """
    Get service area code list
    Returns:
        str(List[Dict]) : large service area code list
    """
    print(f"[DEBUG] get_service_area_code_hotpepper")
    return str(func_hotpepper.get_service_area_code_hotpepper())

@function_tool
def get_large_area_code_hotpepper(keyword:str):
    """
    Get large area code list
    Args:
        keyword(str) : keyword to search (e.g., 東京，広島，大阪)
    Returns:
        str(List[Dict]) : large service area code list
    """
    print(f"[DEBUG] get_large_area_code_hotpepper {keyword=}")
    return str(func_hotpepper.get_large_area_code_hotpepper(keyword=keyword))

@function_tool
def get_middle_area_code_hotpepper(large_area:List[str]|None = None, keyword:str|None=None):
    """
    Get middle area code list
    Args:
        Give at least one arg.
        large_area(List[str]) : Large area code to search. Upto 5 codes.
        keyword(str) : keyword to search (e.g., 品川，呉，大阪市)
    Returns:
        str(List[Dict]) : large service area code list
    """
    print(f"[DEBUG] get_middle_area_code_hotpepper {large_area=},{keyword=}")
    return str(func_hotpepper.get_middle_area_code_hotpepper(large_area=large_area, keyword=keyword))

@function_tool
def get_small_area_code_hotpepper(middle_area:List[str]|None = None, keyword:str|None=None):
    """
    Get small area code list
    Args:
        Give at least one arg.
        middle_area(List[str]) : Middle area code to search. Upto 5 codes.
        keyword(str) : keyword to search (e.g., 品川，呉，大阪市)
    Returns:
        str(List[Dict]) : small area code list
    """
    print(f"[DEBUG] get_small_area_code_hotpepper {keyword=}")
    return str(func_hotpepper.get_small_area_code_hotpepper(middle_area=middle_area, keyword=keyword))

@function_tool
def get_genre_code(
    keyword:str|None=None
):
    """
    Get genre code
    Args:
        Optional: keyword(str) : keyword to search (e.g., 和食，イタリアン)
    Returns:
        str(List[Dict]) : genre code list
    """
    print(f"[DEBUG] get_genre_code{keyword=}")
    return str(func_hotpepper.get_genre_code(keyword=keyword))

@function_tool
def search_restaurant_hotpepper(
    max_num:int = 10,
    large_service_area:str|None = None,
    service_area:List[str]|None = None,
    large_area:List[str]|None = None,
    middle_area:List[str]|None = None,
    small_area:List[str]|None = None,
    keyword:List[str]|None = None,
    genre:str|None = None,
    party_capacity:int|None = None,
    wifi:bool = False,
    cource:bool = False,
    free_drink:bool = False,
    free_food:bool = False,
    private_room:bool = False,
    horigotatsu:bool = False,
    tatami:bool = False,
    cocktail:bool = False,
    shochu:bool = False,
    sake:bool = False,
    wine:bool = False,
    card:bool = False,
    non_smaking:bool = False,
    charter:bool = False,
    parking:bool = False,
    barrier_free:bool = False,
    sommelier:bool = False,
    night_view:bool = False,
    open_air:bool = False,
    show:bool = False,
    equipment:bool = False,
    karaoke:bool = False,
    band:bool = False,
    tv:bool = False,
    lunch:bool = False,
    midnight:bool = False, #23時以降
    midnight_meal:bool = False,
    english:bool = False,
    pet:bool = False,
    child:bool = False,
    order: Literal["name", "genre", "small_area", "recommendation"] = "recommendation"
):
    """Search restaurants
    Any of [large_service_area,service_area,middle_area,small_area,keyword] is required in Args
    Areas and genre has specific code to search. So please use other tools to get codes
    Args:
        max_num(int) : Max. num. of results
        large_service_area(str|None) = None, # Required Large service area code (Use `get_large_service_area_code_hotpepper` tool to get code)
        service_area:List[str]|None = None, # Required service area code (Use `get_service_area_code_hotpepper` tool to get code)
        large_area:List[str]|None = None, # Required large area code (Use `get_large_area_code_hotpepper` tool to get code)
        middle_area:List[str]|None = None, # Required middle area code (Use `get_middle_area_code_hotpepper` tool to get code)
        small_area:List[str]|None = None, # Required small area code (Use `get_small_area_code_hotpepper` tool to get code)
        keyword:List[str]|None = None, # Any keyword in list
        genre:str|None = None, # Required genre code (Use `get_genre_code` tool to get code)
        party_capacity:int|None = None, # number of the guests
        wifi:bool = False, # wifiがあるか?
        cource:bool = False, # コース料理?
        free_drink:bool = False, # 飲み放題?
        free_food:bool = False, # 食べ放題?
        private_room:bool = False, # 個室?
        horigotatsu:bool = False, # 掘りごたつ?
        tatami:bool = False, # 畳・座敷?
        cocktail:bool = False, # カクテル豊富?
        shochu:bool = False, # 焼酎豊富?
        sake:bool = False, # 日本酒豊富?
        wine:bool = False, # ワイン豊富?
        card:bool = False, # クレジットカード使える?
        non_smaking:bool = False, # 禁煙?
        charter:bool = False, # 貸切できる?
        parking:bool = False, # 駐車場ある?
        barrier_free:bool = False, # バリアフリー?
        sommelier:bool = False, # ソムリエがいる?
        night_view:bool = False, # 夜景がいい?
        open_air:bool = False, # オープンエア?
        show:bool = False, # ショー・見せものがある?
        equipment:bool = False, # エンターテイメント機器がある?
        karaoke:bool = False, # カラオケがある?
        band:bool = False, # 演奏可能?
        tv:bool = False, # TVある?
        lunch:bool = False, # ランチある?
        midnight:bool = False, # 23時以降も開いてる?
        midnight_meal:bool = False, # 23時以降の食事がある?
        english:bool = False, # 英語メニューがある?
        pet:bool = False, # ペット同伴可能?
        child:bool = False, # 子供同伴可能?
        order: Literal["name", "genre", "small_area", "recommendation"] = "recommendation" # 検索結果ならびかえ
    Returns:
        str(List[Dict]) : Restaurant list
    """
    print("[DEBUG] search_restaurant_tool")
    restaurants = func_hotpepper.search_restaurants(
        max_num=max_num,
        large_service_area=large_service_area,
        service_area=service_area,
        large_area=large_area,
        middle_area=middle_area,
        small_area=small_area,
        keyword=keyword,
        genre=genre,
        party_capacity=party_capacity,
        wifi=wifi,
        cource=cource,
        free_drink=free_drink,
        free_food=free_food,
        private_room=private_room,
        horigotatsu=horigotatsu,
        tatami=tatami,
        cocktail=cocktail,
        shochu=shochu,
        sake=sake,
        wine=wine,
        card=card,
        non_smaking=non_smaking,
        charter=charter,
        parking=parking,
        barrier_free=barrier_free,
        sommelier=sommelier,
        night_view=night_view,
        open_air=open_air,
        show=show,
        equipment=equipment,
        karaoke=karaoke,
        band=band,
        tv=tv,
        lunch=lunch,
        midnight=midnight,
        midnight_meal=midnight_meal,
        english=english,
        pet=pet,
        child=child,
        order=order
    )
    return str(restaurants)

