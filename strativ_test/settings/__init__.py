env_name = "local"

if env_name == "prod":
    from .prod import *
elif env_name == "stage":
    from .stage import *
else:
    from .local import *