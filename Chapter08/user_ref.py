def build_profile(first, last, **user_info):
    """create a dictionary including everything 
    we know about client
    """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value

    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

user_profile = build_profile('junfeng', 'xue',
                             location='Wuhan',
                             feild='CS',
                             term=3)
print(user_profile)
