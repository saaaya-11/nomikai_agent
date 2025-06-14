# hotpepper.py
# Ref: https://webservice.recruit.co.jp/doc/hotpepper/reference.html
from typing import List, Literal
from settings import RECRUIT_API_KEY
from components.call_api import api_get_response

def search_restaurants(
    max_num:int = 10,
    name:str|None = None,
    tel:str|None = None,
    address:str|None = None,
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
    if all((name,tel,large_service_area,service_area,middle_area,small_area,keyword)) is None:
        raise Exception(f"Warning: Any of [name,tel,large_service_area,service_area,middle_area,small_area,keyword] is required")
    if max_num < 1:
        raise Exception(f"`max` should be equals to or larger than 1")
    
    cursor = 1
    final_results = []

    while cursor < max_num:

        params = {
            "key": RECRUIT_API_KEY,
            "order": order,
            "format": "json",
            "count": min(max_num, 100),
            "max":10,
        }
        if name:
            params["name"] = name
        if tel:
            params["tel"] = tel
        if address:
            params["address"] = address
        if large_service_area:
            params["large_service_area"] = large_service_area
        if service_area:
            params["service_area"] = service_area
        if large_area:
            params["large_area"] = large_area
        if middle_area:
            params["middle_area"] = middle_area
        if small_area:
            params["small_area"] = small_area
        if keyword:
            params["keyword"] = ' '.join(keyword)
        if genre:
            params["genre"] = genre
        if party_capacity:
            params["party_capacity"] = party_capacity
        if wifi:
            params["wifi"] = 1
        if cource:
            params["cource"] = 1
        if free_drink:
            params["free_drink"] = 1
        if free_food:
            params["free_food"] = 1
        if private_room:
            params["private_room"] = 1
        if horigotatsu:
            params["horigotatsu"] = 1
        if tatami:
            params["tatami"] = 1
        if cocktail:
            params["cocktail"] = 1
        if shochu:
            params["shochu"] = 1
        if sake:
            params["sake"] = 1
        if wine:
            params["wine"] = 1
        if card:
            params["card"] = 1
        if non_smaking:
            params["non_smaking"] = 1
        if charter:
            params["charter"] = 1
        if parking:
            params["parking"] = 1
        if barrier_free:
            params["barrier_free"] = 1
        if sommelier:
            params["sommelier"] = 1
        if night_view:
            params["night_view"] = 1
        if open_air:
            params["open_air"] = 1
        if show:
            params["show"] = 1
        if equipment:
            params["equipment"] = 1
        if karaoke:
            params["karaoke"] = 1
        if band:
            params["band"] = 1
        if tv:
            params["tv"] = 1
        if lunch:
            params["lunch"] = 1
        if midnight:
            params["midnight"] = 1
        if midnight_meal:
            params["midnight_meal"] = 1
        if english:
            params["english"] = 1
        if pet:
            params["pet"] = 1
        if child:
            params["child"] = 1 
        print(f"{params=}")
        endpoint = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
        response = api_get_response(endpoint, params=params)
        shops = response["results"]["shop"]
        final_results.extend(shops)
        cursor += len(shops)
        print(f"{cursor=}")
        if cursor > int(response["results"]["results_available"]):
            # これ以上は検索できない
            break

    return final_results

def get_learge_service_area_code_hotpepper():
    endpoint = "http://webservice.recruit.co.jp/hotpepper/large_service_area/v1/"
    params = {
        "key":RECRUIT_API_KEY,
        "format":"json"
    }
    print(f"{params=}")
    response = api_get_response(endpoint, params=params)
    return response["result"]["large_service_area"]

def get_service_area_code_hotpepper():
    endpoint = "http://webservice.recruit.co.jp/hotpepper/service_area/v1/"
    params = {
        "key":RECRUIT_API_KEY,
        "format":"json"
    }
    print(f"{params=}")
    response = api_get_response(endpoint, params=params)
    return response["result"]["service_area"]

def get_large_area_code_hotpepper(
        large_area_ids:List[str]|None=None,
        keyword:str|None = None
        ):
    """
    Arg:
        large_area_ids : upto 3 ids
        keyword: 大エリア名で検索(部分一致)します。UTF8(URLエンコード)で指定
    """
    endpoint = "http://webservice.recruit.co.jp/hotpepper/large_area/v1/",
    params = {
        "key":RECRUIT_API_KEY,
        "format":"json"
    }
    
    if large_area_ids is not None:
        params["large_area"] = ','.join(large_area_ids)
    if keyword is not None:
        params["keyword"] = keyword
    print(f"{params=}")
    response = api_get_response(endpoint=endpoint, params=params)
    return response["result"]["large_area"]

def get_middle_area_code_hotpepper(
    middle_area : List[str]|None = None,
    large_area : List[str]|None = None,
    keyword: str = "",
):
    endpoint = "http://webservice.recruit.co.jp/hotpepper/middle_area/v1/"
    params = {
        "key" : RECRUIT_API_KEY,
        "format" : "json",
    }
    if middle_area is not None:
        params["middle_area"] = ','.join(middle_area)
    if large_area is not None:
        params["large_area"] = ','.join(large_area)
    if keyword is not None:
        params["keyword"] = keyword
    print(f"{params=}")
    response = api_get_response(endpoint=endpoint, params=params)
    return response["result"]["middle_area"]
    

def get_small_area_code_hotpepper(
    small_area : List[str]|None = None,
    middle_area : List[str]|None = None,
    keyword: str = "",
):
    endpoint = "http://webservice.recruit.co.jp/hotpepper/small_area/v1/"
    params = {
        "key" : RECRUIT_API_KEY,
        "format" : "json",
    }
    if small_area is not None:
        params["small_area"] = ','.join(small_area)
    if middle_area is not None:
        params["middle_area"] = ','.join(middle_area)
    if keyword is not None:
        params["keyword"] = keyword
    print(f"{params=}")
    response = api_get_response(endpoint=endpoint, params=params)
    return response["result"]["middle_area"]

def get_genre_code(keyword:str|None=None):
    endpoint = "http://webservice.recruit.co.jp/hotpepper/genre/v1/"
    params = {
        "key" : RECRUIT_API_KEY,
        "format" : "json",
    }
    if keyword is not None:
        params["keyword"] = keyword
    print(f"{params=}")
    response = api_get_response(endpoint=endpoint, params=params)
    return response["result"]["genre"]