from chat_app.dtos import RegistrationRequest
from chat_app.models import TempUser

registration_requests: list[RegistrationRequest] = []


def find_registration_request_by_email(email: str) -> RegistrationRequest:
    # temp_users = TempUser.ob
    print(f"I'm here {registration_requests}")
    for request in registration_requests:
        if str(request.getUser().email).lower() is email.lower():
            return request
    return None


def save_registration_request(registration_request: RegistrationRequest):
    registration_requests.append(registration_request)
    print(registration_requests)


def delete_temp_user(temp_user: RegistrationRequest) -> None:
    registration_requests.remove(temp_user)
