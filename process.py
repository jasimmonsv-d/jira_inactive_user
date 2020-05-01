#! /usr/bin/env python3
import sys

USER_FILE = './users.jira.psql'
CHANGES_FILE = './changes.psql'


def main():
    with open(USER_FILE) as file:
        user_data = file.read().strip()
    with open(CHANGES_FILE) as file:
        change_data = file.read().strip()
    '''
    Assuming user data format as:
    username,email_address
    other_username,other_email_address
    ...
    '''
    user_data = user_data.split('\n')
    change_data = change_data.split('\n ')
    # for user in change_data:
    #     for user2 in change_data[count:]:
    print('dedup start: {}...'.format(len(change_data)))
    change_data = list(dict.fromkeys(change_data))
    print('dedup done: {}...'.format(len(change_data)))
    print('total user records: {}'.format(len(user_data)))
    for record in change_data:
        user_count = 0
        for user in user_data:
            user = user.strip()
            user = user.strip('()')
            username, email, active = user.split(',')
            if record == username or active == '0':
                del user_data[user_count]
            user_count += 1
    print('remaining user records: {}'.format(len(user_data)))
    file = open('./final_results.txt', 'w')
    for x in user_data:
        file.write('{}\n'.format(x.strip().strip('()')))
    file.close()


if __name__ == '__main__':
    print('Starting..')
    main()
    sys.exit()
