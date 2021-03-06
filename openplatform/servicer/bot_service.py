#encoding=utf-8
from bixin.bot_utils import select_event_item
from bixin.bot import Bot

class BotService(Bot):

    def __init__(self, name, bot_access_token, bot_aes_key):
        super(BotService, self).__init__(name, bot_access_token, bot_aes_key)

    def process_welcome_msg(self):
        text = "welcome to {} bot, enjoy yourself".format(self.name)
        return self.send_text_msg(text)

    def process_event_msg(self):
        target_id = self.evt.data['sender']['id']
        content = self.evt.data['content']

        event_type = content['event']

        if event_type == 'help':
            text = "The telephone is xxxxx, please contract with"
            return self.send_text_msg(text)
        elif event_type == 'select_menu' or event_type.startswith('select'):
            return self.send_select_menu()
        elif event_type == 'action_demo':
            return self.send_text_msg('action demo')
        else:
            return self.send_text_msg('Unknown event')

    def process_text_msg(self):
        content = self.evt.data['content']['text']
        if content == 'help':
            text = "The telephone is xxxxx, please contract with"
        elif content == 'select':
            return self.send_select_menu()
        else:
            text = "your can deal your business by different words"
        return self.send_text_msg(text)

    def process_img_msg(self):
        image_url = self.evt.data['content']['image_url']
        return self.send_text_msg('deal ok!')

    def send_select_menu(self):
        target_id = self.evt.data['sender']['id']

        data = {
            'target_id': target_id,
            'text': 'dialog select event demo',
            'select':[select_event_item('select1', 'select1_event_type'),
                      select_event_item('select2', 'select2_event_type')]
            }
        return self.send_select_msg(data)
