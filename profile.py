from rubiran import *

auth = ["gilmsxajhikjzlawtdjwmimrzryognlr","daexoeigvpnakestqvdafyecfgcvzxqw","jaqvrnzhufqqhewfykxrivftgqairmjh"]

for x in auth:
      bot = rubiran(x)
      guid_acc = bot.sendMessage("u0D7Eim05409178b8dde53e6db47a14c",".")["data"]["message_update"]["message"]["author_object_guid"]
      bot.uploadAvatar(guid_acc"1.png")