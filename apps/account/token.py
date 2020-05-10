from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class UserTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        user_id = text_type(user.pk)
        ts = text_type(timestamp)
        is_active = text_type(user.is_active)
        return f"{user_id}{ts}{is_active}"


user_tokenizer = UserTokenGenerator()
