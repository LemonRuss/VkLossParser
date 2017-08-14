import vk
import json
import parse_group
import wall_item
import sys
import dateutil.parser
from datetime import datetime

dateString = sys.stdin.readline().rstrip('\n')

groups = [parse_group.Group('easy_fit_ua','11164593'),
          parse_group.Group('poteryam_net','28977576'),
          parse_group.Group('findlost','60406482'),
          parse_group.Group('find.lose.moscow.myguardian','130162239'),
          parse_group.Group('buro_nahodok_public','50973473'),
          parse_group.Group('buro_nahodok_mo','39183262'),
          parse_group.Group('moskvanahodok','55789311'),
          parse_group.Group('poiskmsk','31262556'),
            ] 

date = dateutil.parser.parse(dateString).timestamp()
for group in groups:
    group.parse(date)
    with open("data/" + group.domain + '.json', encoding='utf-8', mode='w+') as f:
        json.dump([item.__dict__ for item in group.wall_items], f, indent=1, ensure_ascii=False)
