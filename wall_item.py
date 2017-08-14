
class Item(object):
    def __init__(self, item, root_url, group_id):
        self.text = item['text'].replace('\n’','. ')
        self.text = self.text.replace(',',' ')
        self.text = self.text.replace('/',' ')
        self.text = self.text.replace('<br>',' ')
        self.text = self.text.replace('ул.','ул')
        self.text = self.text.replace('ст.','ст')
        self.text = self.text.replace('пр.','пр')
        self.text = self.text.replace('просп.','просп')
        self.text = self.text.replace('пр-д.','пр-д')
        self.text = self.text.replace('ш.','ш')
        self.text = self.text.replace('им.','им')
        self.url = root_url + '?w=wall-' + str(group_id) + '_' + str(item['id'])
        self.date = item['date']
