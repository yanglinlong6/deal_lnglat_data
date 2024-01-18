import itchat, json

# hotReload表示热部署，这样调试的时候就不用频繁登录了hotReload=True
itchat.auto_login()

# 获取好友列表
friends = itchat.get_friends()

# 我们可以使用json库将好友列表转换成json格式
print(json.dumps(friends))


# 运行程序
itchat.run()
