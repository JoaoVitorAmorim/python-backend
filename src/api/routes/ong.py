from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_ongs() -> None:
	return{"message":"GET ALL ONGS ROUTE"}