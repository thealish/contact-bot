from typing import List

from utils.db_api.database import User, Projects

async def add_new_user(**kwargs):
    user = await User(**kwargs).create()
    return user
async def get_user(user_id):
    user = await User.query.where(user_id == user_id).gino.first()
    return user
async def add_project(**kwargs):
    project = await Projects(**kwargs).create()
    return project
async def get_projects() -> List[Projects]:
    projects = await Projects.query.gino.all()
    return projects

