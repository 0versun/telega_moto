import yaml


def data_write(data_tag=None, value=None):
    with open('./data/settings/data_storage.yaml', 'r') as read_file:
        data = yaml.load(read_file)
    if value not in (None, '', [], 'null') and data_tag in (
            'destination', 'seazon_reason', 'destination_time',
            'seazon_start_day', 'seazon_start_mounth', 'seazon_start_yaer','wake_up_time'):
        data[data_tag] = value
        with open('./data/settings/data_storage.yaml', 'w') as write_data:
            yaml.dump(data, write_data, default_flow_style=False)
    else:
        print('Nothing to change', data)


def data_read(data_tag=None):
    with open('./data/settings/data_storage.yaml', 'r') as read_file:
        data = yaml.load(read_file)
    if data_tag not in (None, '', []):
        return data[data_tag]
    else:
        print('Something went wrong')


def data_compressor(data):
    with open('./data/settings/chat_id.dat', 'r') as read_file:
        actual_data = read_file.read().splitlines()
        if str(data) not in actual_data:
            with open('./data/settings/chat_id.dat', 'a') as write_data:
                write_data.write(str(data)+'\n')

def return_stored_chat_id():
    with open('./data/settings/chat_id.dat', 'r') as read_file:
        chat_ids = read_file.read().splitlines()
    return chat_ids
