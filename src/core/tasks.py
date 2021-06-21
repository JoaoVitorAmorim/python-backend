from typing import Callable
from fastapi import FastAPI
from src.db.tasks import connect_to_db, close_db_connetion

def create_start_app_handler(app:FastAPI)->Callable:
	async def start_app()->None:
		await connect_to_db(app)
	return start_app
def create_stop_app_handler(app:FastAPI) -> Callable:
	async def stop_app() -> None:
		await close_db_connetion(app)
	return stop_app