from core import commands


def handle_message(msg):
    command_found = [
        command for command in commands.value if command['key'] == msg][0]
    command_found['callback'](msg)


handle_message('another')
