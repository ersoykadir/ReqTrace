"""
Kadir Ersoy
Internship Project
Auth Router
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from server.user import user_crud, user_schema
from server.database.database import get_db
from server.authentication import auth_utils, auth_google_utils

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.get("/google")
def register_user():
    """Redirects user to google login page"""
    response = RedirectResponse(url=auth_google_utils.get_google_auth_url())
    # print(response)
    return response


# Get user data from identity provider using the code
# Save user data in database,
# Create a JWT token and return it to user,
# token expiration can be same as identity providers token expiration
@router.get("/google/callback")
def oauth2callback(state, code, database: Session = Depends(get_db)):
    """Get user data from identity provider using the code"""
    # Confirm state
    if state != auth_google_utils.STATE:
        raise HTTPException(status_code=401, detail="Invalid state")

    # Get user data from identity provider
    credentials = auth_google_utils.get_credentials(code)
    user_data, exp = auth_google_utils.get_user_data_from_id_token(credentials)

    # Create user
    user = user_crud.user.get_user_by_email(database, email=user_data["email"])
    if not user:
        user = user_crud.user.create_user(database, user_schema.UserBase(**user_data))

    # Create token
    token = auth_utils.create_access_token(data={"sub": user.email}, expire=exp)
    access_token = {"access_token": token, "token_type": "bearer"}
    
    # Redirect user to frontend with token
    response = RedirectResponse(url=f"http://localhost:1234?access_token={access_token['access_token']}")
    # print(response)
    return response
