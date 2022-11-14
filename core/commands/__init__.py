from core.commands.testing import testing_key, testing_callback
from core.commands.another_command import testing_key as another_key, testing_callback as another_callback

value = [
    {
        "key": testing_key,
        "callback": testing_callback
    },
    {
        "key": another_key,
        "callback": another_callback
    }
]
