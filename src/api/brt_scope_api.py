from fastapi import Request
from pydantic import BaseModel


from src.business.brt_scope import BRTProject


class Api_Request(BaseModel):
    countryname: str
    cityname: str
    start_year: str


def brt_scope_api(request_context: Request, event: Api_Request):
    brt_project = BRTProject(countryname=event.countryname, cityname=event.cityname, start_year=event.start_year)
    return {
        "worldregion": brt_project.worldregion,
        "city_name": brt_project.city_name,
        "start_year": brt_project.start_year,
        "pop_growth_rate": brt_project.pop_growth_rate,
        "working_days": brt_project.working_days,
        "city_modesplit": brt_project.city_modesplit,
        "pop_density": brt_project.pop_density,
        "occupancy": brt_project.occupancy
    }
