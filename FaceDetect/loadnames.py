 # Get instance
import instaloader
import os
L = instaloader.Instaloader()

# Login or load session
username = input("Instagram username: ")
password = input("Instagram password: ")
L.login(username, password)        # (login)


# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, "brenner_little")

# Print list of followees



follow_list = []
count=0
c = 0

for followee in profile.get_followers():
    follow_list.append(followee.username)
    file = open(username + "followers.txt","a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    L.download_profile(profile_pic_only=True,profile_name=follow_list[count])

    test = os.listdir(follow_list[count])
    os.remove((follow_list[count]+ "//id"))
    print(test)


    for item in test:
        if item.endswith(".xz" or "id"):
            print(item)
            os.remove(follow_list[count]+ "//" +item)

    count+=1

