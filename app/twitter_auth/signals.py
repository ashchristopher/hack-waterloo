from django import dispatch

# sent when creating a new user.
twitter_user_created = dispatch.Signal(providing_args=["user", "screen_name", "user_id"])

# sent when a user is authenticated.
twitter_user_authenticated = dispatch.Signal(providing_args=["user", ])