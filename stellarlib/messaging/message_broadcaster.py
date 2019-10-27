from message_center import MessageCenter


class MessageBroadcaster(object):

    def __init__(self):
        pass

    def get_message_center(self):
        return MessageCenter.get_instance()
