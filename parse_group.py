import vk
import wall_item

class Group(object):
    
    def __init__(self, domain, group_id):
        session = vk.Session(access_token='b2bf0ef2b2bf0ef2b2bf0ef201b2e3c638bb2bfb2bf0ef2ebf88397fb0a6856202f1676')
        self.vk_api = vk.API(session)
        self.domain = domain
        self.group_id = group_id
        self.url = 'https://vk.com/' + domain
        self.wall_items = []

    def parse(self, till_date):
        count = 100
        total = 50000
        offset = 0
        for offset in range(1, total, count):
            json_items = self.vk_api.wall.get(domain=self.domain,extended1=1, offset=offset, count=count)
            for json_item in json_items[1:]:
                parsed_item = wall_item.Item(json_item, self.url, self.group_id)
                if parsed_item.date < till_date:
                    return
                self.wall_items.append(parsed_item)