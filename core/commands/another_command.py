def another_callback(msg):
    return str(msg.author.nick or msg.author.name) + ' é corno'

testing_key = '!corno'
testing_callback = another_callback
