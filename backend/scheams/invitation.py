from tortoise.contrib.pydantic import pydantic_model_creator

from ..models.invitation import create_invitation

invitation_Pydantic = pydantic_model_creator(create_invitation,name="invitation")

invitationIn_Pydantic = pydantic_model_creator(create_invitation,name="invitationIn")