def expand_list(items, prefix=''):
    expanded_list = []
    for item in items:
        if isinstance(item, dict):
            item_key = list(item.keys())[0]
            item_value = item[item_key]
            expanded_list.extend(expand_list(item_value, prefix=item_key+'-'))
        else:
            expanded_list.append(prefix + item)
    return expanded_list

original_list = [
    {
        'client': [
            {
                'site': [
                    'access_control',
                    'alarm_panels',
                    'media_players',
                    {
                        'network': [
                            'firewalls',
                            'media_converters',
                            'modems',
                            'switches',
                            'routers',
                            'nvrs',
                            'wireless_access_points',
                            'wireless_networks'
                        ]
                    },
                    {
                        'physical': [
                            'door_codes',
                            'gates',
                            'lockers'
                        ]
                    },
                    {
                        'printers': [
                            '3d',
                            'documents',
                            'id',
                            'labels'
                        ]
                    },
                    'servers',
                    'tablets',
                    {
                        'video': [
                            'cameras',
                            'converters',
                            'distributers',
                            'extenders',
                            'recorders'
                        ]
                    },
                    'workstations'
                ]
            }
        ]
    }
]

expanded_list = expand_list(original_list)
for item in expanded_list:
    print(item)


    # Write to file
with open('topology_list.txt', 'w') as file:
    for item in expanded_list:
        file.write(item + '\n')
