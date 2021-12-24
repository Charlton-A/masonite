import jwt
import pendulum
from masonite.facades import Auth


class Api:
    def __init__(self, application, driver_config=None):
        self.application = application

    def set_configuration(self, config):
        self.config = config
        return self

    def generate_token(self):
        secret = self.config.get("jwt").get("secret")
        algorithm = self.config.get("jwt").get("algorithm")
        expire_minutes = self.config.get("jwt").get("expires")
        version = self.config.get("jwt").get("version")
        if expire_minutes:
            expire_minutes = (
                pendulum.now(tz="GMT").add(minutes=expire_minutes).to_datetime_string()
            )
        token = jwt.encode({"expires": expire_minutes, "version": version}, secret, algorithm=algorithm)

        return token

    def get_token(self):
        request = self.application.make('request')
        token = request.input('token')

        if token:
            return token
        
        header = request.header('Authorization')

        if header:
            return header.replace('Bearer ', '')

    def validate_token(self, token):
        secret = self.config.get("jwt").get("secret")
        algorithm = self.config.get("jwt").get("algorithm")
        expire_minutes = self.config.get("jwt").get("expires")
        authenticates = self.config.get("jwt").get("authenticates")
        version = self.config.get("jwt").get("version")
        if expire_minutes:
            expire_minutes = (
                pendulum.now(tz="GMT").add(minutes=expire_minutes).to_datetime_string()
            )

        unencrypted_token = jwt.decode(token, secret, algorithms=[algorithm])
        expires = unencrypted_token.get("expires")
        if not expires:
            return True

        expired = pendulum.parse(expires, tz="GMT").is_past()

        if expired:
            return False

        if version:
            if unencrypted_token["version"] != version:
                return False

        if authenticates:
            return self.attempt_by_token(token)
        
        return True

    def regenerate_token(self, token):
        # if the token can be decoded, regenerate new token
        secret = self.config.get("jwt").get("secret")
        algorithm = self.config.get("jwt").get("algorithm")
        try:
            jwt.decode(token, secret, algorithms=[algorithm])
            return self.generate_token()
        except jwt.DecodeError:
            pass

        return False
    
    def attempt_by_token(self, token):
        model = self.config.get("jwt").get("model")()
        return model.attempt_by_token(token)