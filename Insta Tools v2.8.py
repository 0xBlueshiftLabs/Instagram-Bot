

##### Instagram Login Credentials ########

username = ""
password = ""

##########################################


#################
#  To decrease the chance of your account being shadowbanned, keep your unfollow limit to less than 60 per hour
#   with a gap of 25-30 seconds and a maximum of 100 unfollows per day.
#################



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime
import random
import math
import json



# command line user interface
def selection():
    selection.choice = int(input("\nWhich tool would you like to use?\n\n1 = New unfollow non followers\n2 = Old unfollow non followers\
 \n3 = Hashtag search, follow & like\n4 = Follow new accounts\n5 = Follow suggested\n6 = Follow followers\n7 = Wipe recent follow list\n\nEnter your selection (1-8) and press\
 enter: "))


    if selection.choice == 1:  # new unfollow tool
        print()
        print("It is not recommended to unfollow more than 100 users in 15 minutes.")
        print()
        num = int(input("How many non-followers would you like to unfollow: "))
        pause = int(input("Pause between each unfollow (seconds): "))
        print()
        my_bot = InstaBot(username, password)
        my_bot.unfollownew(num, pause)  # unfollows the people on the list of people not following you

    elif selection.choice == 2:  # old unfollow tool
        print()
        print("It is not recommended to unfollow more than 100 users in 15 minutes.")
        print()
        num = int(input("How many non-followers would you like to unfollow: "))
        pause = int(input("Pause between each unfollow (seconds): "))
        print()
        my_bot = InstaBot(username, password)
        my_bot.unfollowold(num, pause)  # unfollows the people on the list of people not following you

    elif selection.choice == 3:  # hashtag search tool
        print()
        print()
        print("#####  Hashtag Tool  #####")
        print()
        variety = int(input(
            "Would you like to:\n1. Like posts\n2. Follow posters\n3. Like & Follow\n\nEnter your selection (1, 2 or 3) and press enter: "))
        print()
        hashtag = str(input("Hashtag to search:  #"))
        number = int(input("Number of posts: "))
        pause = int(input("Pause between each post (seconds): "))
        print()
        my_bot = InstaBot(username, password)

        if variety == 1:
            my_bot.hashtagsearchlike(hashtag, number, pause)  # (the hashtag, number of posts)
        elif variety == 2:
            my_bot.hashtagsearchfollow(hashtag, number, pause)  # (the hashtag, number of posts)
        elif variety == 3:
            my_bot.hashtagsearch(hashtag, number, pause)  # (the hashtag, number of posts)
        else:
            print("Invalid selection. Please start over.")
            selection()

    elif selection.choice == 4:
        print()
        number = int(input("Number of new accounts to follow: "))
        pause = int(input("Pause between follows: "))
        print()
        my_bot = InstaBot(username, password)
        my_bot.follow_new(number, pause)

    elif selection.choice == 5:
        print()
        number = int(input("Number of suggested accounts to follow: "))
        pause = int(input("Pause between follows: "))
        print()
        my_bot = InstaBot(username, password)
        my_bot.follow_suggested(number, pause)

    elif selection.choice == 6:
        print()
        profilename = input("Profile's username:  @")
        num = int(input("Number of followers to follow: "))
        pause = int(input("Pause between follows: "))
        print()
        my_bot = InstaBot(username, password)
        my_bot.follow_followers(num, profilename, pause)

    elif selection.choice == 7:
        print()
        wipe_follow_list()
        print("Recent follows list wiped")

    elif selection.choice == 8:
        print()
        num = int(input("Number of followers to unfollow: "))
        skip_percent = int(input("Percentage of users to skip unfollowing: "))
        pause = int(input("Pause between unfollows: "))
        pause_between_batch = int(input("Pause between batch of 10 unfollows: "))
        print()
        my_bot = InstaBot(username, password)
        my_bot.unfollow_any(num, skip_percent, pause, pause_between_batch)

    else:
        print()
        print("Invalid selection. Please try again.")
        sleep(rando(1))
        selection()


def wipe_follow_list():

    with open('follows_list.txt', 'r') as f:
        try:
            follows = json.loads(f.read())

        except:
            follows = []

        follows = []

    with open('follows_list.txt', 'w') as f:
        f.write(json.dumps(follows))
        f.close()


def save_follow(profile_name):

    with open('follows_list.txt', 'r') as f:
        try:
            follows = json.loads(f.read())

        except:
            follows = []

        follows.append(profile_name)

    with open('follows_list.txt', 'w') as f:
        print(follows)
        f.write(json.dumps(follows))
        f.close()



def verification(): # very rudimentary licence expiry

    date_today = datetime.datetime.now().date()
    expiry_date = datetime.date(2020, 12, 17)

    if date_today < expiry_date:
        selection()

    else:
        print()
        print("Software licence has expired. Please contact: [email address]")


def rando(time): # helps evade Instagram's bot detection by slightly varying every the time between code line execution

    rtime = random.uniform(time - 0.1, time + 0.3)
    return rtime

def no_non_followers(self):
    print("There are no accounts that do not follow you back.")


class InstaBot:

    def __init__(self, username, password):

        self.username = username
        self.password = password

        self.driver = webdriver.Chrome(executable_path="[INSERT CHROME WEBDRIVER FILE PATH]")

        self.driver.get("https://www.instagram.com/")
        sleep(rando(5))

        # gets around 'accept cookies' pop up
        try:
            self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
            sleep(rando(2))

        except:
            print()

        # enters username
        self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(username)
        sleep(rando(0.3))
        # enters password
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(password)
        sleep(rando(0.5))
        # presses submit
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(rando(5))

        print((datetime.datetime.now().strftime("%H:%M:%S")) + "  Logged in.")

        # presses not now button for both pop ups
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            sleep(rando(2))
        except:
            print()

        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            sleep(rando(2))
        except:
            print()


    def scrape_followers(self):

        # clicks on profile
        self.driver.get("https://www.instagram.com/" + username + "/")
        sleep(rando(4))

        # gets number of followers
        number_of_followers_string = self.driver.find_element_by_xpath("//a[contains(@href,'followers')]").text
        number_of_followers = number_of_followers_string[0:(number_of_followers_string.find(" "))]
        if number_of_followers.find(",") == True:
            # remove the comma
            number_of_followers = number_of_followers.replace(",", "")
        number_of_followers = int(number_of_followers)

        # clicks on followers
        self.driver.find_element_by_xpath("//a[contains(@href,'followers')]").click()
        sleep(rando(2.5))
        followers = self._get_names()
        followers = followers[0:number_of_followers]

        print(len(followers))

        if len(followers) != number_of_followers:
            print("Error in follower count.")

        print()
        print("Followers: " + str(number_of_followers))

        # saves followers list to text file
        with open('followers.txt', 'w') as f:
            f.write(json.dumps(followers))
            f.close()


    def unfollow_any(self,num,skip_percent,pause, pause_between_batch):

        print()

        # clicks on profile
        self.driver.get("https://www.instagram.com/" + username + "/")
        sleep(rando(4))

        # gets number of followers
        number_of_following_string = self.driver.find_element_by_xpath("//a[contains(@href,'followers')]").text
        number_of_following = number_of_following_string[0:(number_of_following_string.find(" "))]
        if number_of_following.find(",") == True:
            # removes the comma
            number_of_following = number_of_following.replace(",", "")
        pre_following_number = int(number_of_following)

        self.unfollow_iteration(num, skip_percent, pause)

        print()
        print("Finished")
        print()

        # clicks on profile
        self.driver.get("https://www.instagram.com/" + username + "/")
        sleep(rando(4))

        # gets number of followers
        number_of_following_string = self.driver.find_element_by_xpath("//a[contains(@href,'followers')]").text
        number_of_following = number_of_following_string[0:(number_of_following_string.find(" "))]
        if number_of_following.find(",") == True:
            # removes the comma
            number_of_following = number_of_following.replace(",", "")
        post_following_number = int(number_of_following)

        print("Number of following before: "+str(pre_following_number))
        print("Number of following after: "+str(post_following_number))
        print("Successful unfollows: "+str((pre_following_number-post_following_number)))
        print("Difference supposed to be "+str(num))


    def unfollow_iteration(self,num, skip_percent, pause, pause_between_batch):

        # clicks on profile
        self.driver.get("https://www.instagram.com/" + username + "/")
        sleep(rando(4))

        # clicks on following
        self.driver.find_element_by_xpath("//a[contains(@href,'following')]").click()
        sleep(rando(pause_between_batch))

        # scrolls down a bit to load enough users
        scroll_box = self.driver.find_element_by_class_name('isgrP')
        last_ht, ht = 0, 1
        for i in range(math.ceil(num / 10)):
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                                        arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                        return arguments[0].scrollHeight;
                                        """, scroll_box)

        # unfollow iteration
        i = 0
        pos = 1
        while i < num:

            if i > 9:
                print()
                sleep(rando(12))
                num = num - 10
                self.unfollow_iteration(num, skip_percent, pause)
                break


            elif random.uniform(0, 100) < skip_percent:
                pos = pos + 1
                continue


            else:

                # clicks unfollow
                try:
                    self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[' + str(pos) + ']/div/div[2]/\
                            button').click()
                    sleep(rando(1.5))

                    # clicks confirm unfollow
                    self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
                    print((datetime.datetime.now().strftime("%H:%M:%S")) + "  " + "Unfollowed user.")

                    i = i + 1

                except:

                    try:
                        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[' + str(pos) + ']/div/div\
                                [3]/button').click()
                        sleep(rando(1.5))

                        # clicks confirm unfollow
                        self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
                        print((datetime.datetime.now().strftime("%H:%M:%S")) + "  " + "Unfollowed user.")

                        i = i + 1

                    except:
                        print((datetime.datetime.now().strftime("%H:%M:%S")) + "  " + "Failed to unfollow user.")

                pos = pos + 1
                sleep(rando(pause))



    def get_unfollowers(self):

        # clicks on profile
        self.driver.get("https://www.instagram.com/" + username + "/")
        sleep(rando(4))

        # gets number of followers
        number_of_followers_string = self.driver.find_element_by_xpath("//a[contains(@href,'followers')]").text
        number_of_followers = number_of_followers_string[0:(number_of_followers_string.find(" "))]
        if number_of_followers.find(",") == True:
            # remove the comma
            number_of_followers = number_of_followers.replace(",", "")
        number_of_followers = int(number_of_followers)


        # gets number of following
        number_of_following_string = self.driver.find_element_by_xpath("//a[contains(@href,'following')]").text
        number_of_following = number_of_following_string[0:(number_of_following_string.find(" "))]
        if number_of_following.find(",") == True:
            # removes the comma
            number_of_following = number_of_following.replace(",", "")
        number_of_following = int(number_of_following)


        # clicks on followers
        self.driver.find_element_by_xpath("//a[contains(@href,'followers')]").click()
        sleep(rando(2.5))
        followers = self._get_names()
        followers = followers[0:number_of_followers]

        if len(followers) != number_of_followers:
            print("Error in follower count.")

        print()
        print("Followers: " + str(number_of_followers))

        # closes followers
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()

        # clicks on following
        self.driver.find_element_by_xpath("//a[contains(@href,'following')]").click()
        sleep(rando(2.5))
        following = self._get_names()

        print("Following: " + str(number_of_following))
        print()

        following = following[0:number_of_following]

        if len(following) != number_of_following:
            print("Error in following count.")

        non_followers = []
        # stores non followers in a list
        for user in following:
            if user not in followers:
                non_followers.append(user)

        if len(non_followers) == 0:
            print("Number of accounts that don't follow you back is 0")
            quit()

        print("Number of accounts that don't follow you back: " + str(len(non_followers)))
        print(non_followers)

        return non_followers, following


    def _get_names(self):

        # scrolls through following/follower list
        scroll_box = self.driver.find_element_by_class_name('isgrP')
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)  # adjust before sending to nik
            ht = self.driver.execute_script("""
                        arguments[0].scrollTo(0, arguments[0].scrollHeight);
                        return arguments[0].scrollHeight;
                        """, scroll_box)
            sleep(0.2)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']

        return names


    def unfollowold(self, num, pause):

        not_following_back, following = InstaBot.get_unfollowers(self)

        print()

        # incase number to unfollow is great than number of non followers
        if len(not_following_back) < num:
            print()
            print("Number to unfollow is greater than your number of non-followers.")
            print("Unfollowing all non-followers.")
            print()
            num = len(not_following_back)

        i = 1
        for name in not_following_back[0:num]:

            # opens profile of an unfollower
            self.driver.get("https://www.instagram.com/" + str(name) + "/")
            sleep(rando(5))

            try:
                # unfollow button
                self.driver.find_element_by_class_name("_6VtSN").click()
                sleep(rando(1))

                # confirm unfollow button
                self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()

                print((datetime.datetime.now().strftime("%H:%M:%S")) + "  " + str(i) + '. Unfollowed @' + name)


            except:
                print((datetime.datetime.now().strftime("%H:%M:%S")) + "  " + str(i) + ". Failed to unfollow user: @" \
                      + name)


            sleep(rando(pause))

        print()
        print((datetime.datetime.now().strftime("%H:%M:%S")) + "  " + "Finshed.")
        print()
        print("Number of non-follwers remaining: " + str(len(not_following_back)))

        self.driver.quit()

    def unfollownew(self, num, pause):

        not_following_back, following = InstaBot.get_unfollowers(self)

        print()

        # incase number to unfollow is great than number of non followers
        if len(not_following_back) < num:
            print()
            print("Number to unfollow is greater than your number of non-followers.")
            print("Unfollowing all non-followers.")
            print()
            num = len(not_following_back)


        for name in not_following_back[0:num]:

            # finds position of user to unfollow
            pos = str(int(following.index(name)) + 1)

            # clicks unfollow
            try:
                self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(pos)+']/div/div[2]/\
                button').click()
                sleep(rando(1.5))


                # clicks confirm unfollow
                self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
                print((datetime.datetime.now().strftime("%H:%M:%S")) + "  " + "Unfollowed user @" + name)

            except:

                try:
                    self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(pos)+']/div/div\
                    [3]/button').click()
                    sleep(rando(1.5))

                    # clicks confirm unfollow
                    self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
                    print((datetime.datetime.now().strftime("%H:%M:%S")) + "  " + "Unfollowed user @" + name)

                except:
                    print((datetime.datetime.now().strftime("%H:%M:%S")) + "  " + "Failed to unfollow user @" + name)

            sleep(rando(pause))

        print()
        print((datetime.datetime.now().strftime("%H:%M:%S")) + "  Finished.")

        self.driver.quit()
        quit()


    def hashtagsearch(self, hashtag, number, pause):

        print()

        # opens explore page for a hashtag and clicks on the first post
        self.driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        sleep(rando(5))

        # clicks on first post
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]").click() #clicks on first recent post
        sleep(rando(3))

        i = 0
        while i < number:

            # gets profile name
            try:
                profile_name = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a").text

            except:
                print("Couldn't get profile name.")
                # presses right arrow button to load next post
                self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
                sleep(rando(1.2))
                continue


            try:
                # checks if post has already been liked
                heart_fill = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span\
                            [1]/button/div/span").get_attribute('innerHTML')

            except:
                heart_fill = "undetermined"

            # checks if post is your own
            if profile_name == username:
                print((datetime.datetime.now().strftime("%H:%M:%S")) + ". Own post. Skipped.")
                print()

                # presses right arrow button to load next post
                self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
                sleep(rando(1.2))
                continue

            else:

                try:
                    # checks if you already follow the user
                    follow_button = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div\
                    [2]/div[1]/div[2]/button').text
                except:
                    follow_button = "error"

                if follow_button == "Following":
                    # presses right arrow button to load next post
                    self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
                    sleep(rando(1.2))
                    continue

                elif follow_button == "error":
                    print("Couldn't find follow button")
                    # presses right arrow button to load next post
                    self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
                    sleep(rando(1.2))
                    continue

                else:

                    try:
                        # follows poster
                        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()

                        try:
                            # checks for insta restrictions message
                            shadow = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/h3").text

                        except:
                            shadow = ""

                        if shadow == "Try Again Later":
                            print("Instagram may have placed restrictions on your account.")
                            quit()

                        else:
                            print()
                            print(str(i + 1) + ".")
                            print((datetime.datetime.now().strftime("%H:%M:%S")) + "  " + "Followed user @" + profile_name)
                            save_follow(profile_name)
                    except:
                        print()
                        print(str(i + 1) + ".")
                        print((datetime.datetime.now().strftime("%H:%M:%S")) + "  " + "Failed to follow user @" + profile_name)

                sleep(rando(1))

                if "aria-label=\"Unlike\"" in heart_fill:  # post already liked

                    print((datetime.datetime.now().strftime("%H:%M:%S")) + "  Already liked post.")
                    print()
                    # presses right arrow button to load next post
                    self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
                    sleep(rando(1.2))
                    continue

                elif heart_fill == "undetermined":

                    print((datetime.datetime.now().strftime("%H:%M:%S")) + "  Couldn't determine if post has previously been liked.")
                    print()
                    # presses right arrow button to load next post
                    self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
                    sleep(rando(1.2))
                    continue

                else:

                    try:
                        # likes post
                        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div').click()

                        print((datetime.datetime.now().strftime("%H:%M:%S")) + "  " + "Liked post from @" + profile_name)

                    except:
                        print((datetime.datetime.now().strftime("%H:%M:%S")) + "  " + "Failed to like post from @" + profile_name)

                sleep(rando(1))

            # presses right arrow button to load next post
            self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
            i = i+1

            sleep(rando(pause))

        self.driver.quit()
        print()
        print((datetime.datetime.now().strftime("%H:%M:%S"))+ "  Finshed")

    def hashtagsearchlike(self, hashtag, number, pause):

        print()

        # opens explore page for a hashtag and clicks on the first post
        self.driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        sleep(rando(5))

        # clicks on first post
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]").click()  # clicks on first recent post
        sleep(rando(3))

        i = 0
        while i < number:

            # gets profile name
            try:
                profile_name = self.driver.find_element_by_xpath(
                    "/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a").text

            except:
                print("Couldn't get profile name.")
                # presses right arrow button to load next post
                self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
                sleep(rando(1.2))
                continue

            try:
                # checks if post has already been liked
                heart_fill = self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span\
                                    [1]/button/div/span").get_attribute('innerHTML')

            except:
                heart_fill = "undetermined"

            # checks if post is your own
            if profile_name == username:
                print((datetime.datetime.now().strftime("%H:%M:%S")) + ". Own post. Skipped.")
                print()

                # presses right arrow button to load next post
                self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
                sleep(rando(1.2))
                continue

            else:

                if "aria-label=\"Unlike\"" in heart_fill:  # post already liked

                    print((datetime.datetime.now().strftime("%H:%M:%S")) + "  Already liked post.")
                    print()
                    # presses right arrow button to load next post
                    self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
                    sleep(rando(1.2))
                    continue

                elif heart_fill == "undetermined":

                    print((datetime.datetime.now().strftime(
                        "%H:%M:%S")) + "  Couldn't determine if post has previously been liked.")
                    print()
                    # presses right arrow button to load next post
                    self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
                    sleep(rando(1.2))
                    continue

                else:

                    try:
                        # likes post
                        self.driver.find_element_by_xpath(
                            '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div').click()

                        print(
                            (datetime.datetime.now().strftime("%H:%M:%S")) + "  " + "Liked post from @" + profile_name)

                    except:
                        print((datetime.datetime.now().strftime(
                            "%H:%M:%S")) + "  " + "Failed to like post from @" + profile_name)

                sleep(rando(1))

            # presses right arrow button to load next post
            self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
            i = i + 1

            sleep(rando(pause))

        self.driver.quit()
        print()
        print((datetime.datetime.now().strftime("%H:%M:%S")) + "  Finshed")


    def hashtagsearchfollow(self, hashtag, number, pause):

        print()

        # opens explore page for a hashtag and clicks on the first post
        self.driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        sleep(rando(5))

        # clicks on first post
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]").click()  # clicks on first recent post
        sleep(rando(3))

        i = 0
        while i < number:

            # gets profile name
            try:
                profile_name = self.driver.find_element_by_xpath(
                    "/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a").text

            except:
                print("Couldn't get profile name.")
                # presses right arrow button to load next post
                self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
                sleep(rando(1.2))
                continue


            # checks if post is your own
            if profile_name == username:
                print((datetime.datetime.now().strftime("%H:%M:%S")) + ". Own post. Skipped.")
                print()

                # presses right arrow button to load next post
                self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
                sleep(rando(1.2))
                continue

            else:

                try:
                    # checks if you already follow the user
                    follow_button = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div\
                            [2]/div[1]/div[2]/button').text
                except:
                    follow_button = "error"

                if follow_button == "Following":
                    # presses right arrow button to load next post
                    self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
                    sleep(rando(1.2))
                    continue

                elif follow_button == "error":
                    print("Couldn't find follow button")
                    # presses right arrow button to load next post
                    self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
                    sleep(rando(1.2))
                    continue

                else:

                    try:
                        # follows poster
                        self.driver.find_element_by_xpath(
                            '/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()

                        try:
                            # checks for insta restrictions message
                            shadow = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/h3").text
                        #  /html/body/div[6]/div/div/div/div[1]/h3
                        except:
                            shadow = ""

                        if shadow == "":
                            print()
                            print(str(i + 1) + ".")
                            print((datetime.datetime.now().strftime(
                                "%H:%M:%S")) + "  " + "Followed user @" + profile_name)
                            save_follow(profile_name)

                        else:
                            print("Instagram may have placed restrictions on your account.")
                            quit()
                    except:
                        print()
                        print(str(i + 1) + ".")
                        print((datetime.datetime.now().strftime(
                            "%H:%M:%S")) + "  " + "Failed to follow user @" + profile_name)

                sleep(rando(1))

            # presses right arrow button to load next post
            self.driver.find_element_by_tag_name("html").send_keys(Keys.RIGHT)
            i = i + 1

            sleep(rando(pause))

        self.driver.quit()
        print()
        print((datetime.datetime.now().strftime("%H:%M:%S")) + "  Finshed")


    def follow_new(self, number, pause):

        print()
        sleep(rando(1))
        self.driver.maximize_window()
        sleep(rando(2))

        # clicks on 'see all suggestions' button
        # /html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div").click()
        sleep(rando(3))

        i = 0
        n = 0
        followed = False
        while n < number:

            if i > 60:

                self.driver.refresh()
                sleep(rando(4))
                i = 0

                # checks if any accounts were followed since last page refresh
                if followed == False:
                    print()
                    print((datetime.datetime.now().strftime("%H:%M:%S")) + "  No more new accounts to follow at this time.")
                    print()
                    quit()

                followed = False

            # checks if new to instagram
            try:
                sub_text = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/div/div/div['+str(i+1)+']/div[2]/div[3]/div').text
            except:
                sub_text = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/div/div/div[5]/div[2]/div[2]/div').text

            if sub_text == "New to Instagram":

                # clicks follow button
                self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/div[2]/div/div/div[' + str(i + 1) + ']/\
                        div[3]/button').click()

                # gets username
                profile_name = self.driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/div[2]/div/div/div[' + \
                    str(i + 1) + ']/div[2]/div[1]/div/span/a').text

                self.save_follow(profile_name)

                print((datetime.datetime.now().strftime("%H:%M:%S")) + "  Followed user @" + profile_name)
                save_follow(profile_name)

                n = n + 1
                sleep(rando(pause))
                followed = True

            i = i + 1

        print()
        print((datetime.datetime.now().strftime("%H:%M:%S")) + "  Finshed")


    def follow_suggested(self, number, pause):

        print()
        sleep(rando(1))
        self.driver.maximize_window()
        sleep(rando(2))

        # clicks not now for save login info pop up
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            sleep(rando(2))
        except:
            print()

        # clicks not now for notifications pop up
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            sleep(rando(2))
        except:
            print()

        # clicks on 'see all suggestions' button
        # /html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div").click()
        sleep(rando(3))

        i = 0
        n = 0

        while n < number:

            if i > 60:

                self.driver.refresh()
                sleep(rando(4))
                i = 0


            # checks if new to instagram
            try:
                sub_text = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/div/div/div['+str(i+1)+']/div[2]/div[3]/div').text
            except:
                sub_text = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/div/div/div[5]/div[2]/div[2]/div').text

            # follows anny account unless they are "popular"
            if sub_text != "Popular":

                # clicks follow button
                self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/div[2]/div/div/div[' + str(i + 1) + ']/\
                        div[3]/button').click()

                # gets username
                profile_name = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/div/div/div[' + \
                    str(i + 1) + ']/div[2]/div[1]/div/span/a').text

                save_follow(profile_name)

                print((datetime.datetime.now().strftime("%H:%M:%S  ")) + str(n+1)+". Followed user @" + profile_name)

                n = n + 1
                sleep(rando(pause))

            i = i + 1

        print()
        print((datetime.datetime.now().strftime("%H:%M:%S")) + "  Finshed")


    def follow_followers(self, num, profilename, pause):

        print()

        # opens user's page
        self.driver.get("https://www.instagram.com/" + profilename + "/")
        sleep(rando(5))

        # clicks on followers
        self.driver.find_element_by_xpath("//a[contains(@href,'followers')]").click()
        sleep(rando(2.5))

        # scrolls through following/follower list
        scroll_box = self.driver.find_element_by_class_name('isgrP')
        last_ht, ht = 0, 1

        for i in range(math.ceil(num/10)):

            last_ht = ht
            sleep(1)  # adjust before sending to nik
            ht = self.driver.execute_script("""
                                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                return arguments[0].scrollHeight;
                                """, scroll_box)
            sleep(0.2)


        for i in range(num):

            try:
                follow_text = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li["+str(i+1)+"]/div/div[2]/button").text
            except:
                try:
                    follow_text = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li["+str(i+1)+"]/div/div[3]/button").text
                except:
                    follow_text = "error"


            # clicks follow
            if follow_text == "Following":
                print((datetime.datetime.now().strftime("%H:%M:%S  ")) + str(i+1) + ".  Already following user")
                sleep(0.1)
                continue

            elif follow_text == "Follow":

                # gets profile name
                try:
                    profile_name = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li["+str(i+1)+"]/div/div[1]/div[2]/div[1]/span/a").text
                except:
                    profile_name = ""

                # follows user
                try:
                    self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li["+str(i+1)+"]/div/div[2]/button").click()

                except:
                    self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li["+str(i+1)+ "]/div/div[3]/button").click()


                sleep(rando(0.5))
                print((datetime.datetime.now().strftime("%H:%M:%S  "))+ str(i+1) + ".  Followed user @" + profile_name)
                save_follow(profile_name)

            else:
                print((datetime.datetime.now().strftime("%H:%M:%S  "))+ str(i+1) + ".  Error in reading text of follow button")


            sleep(rando(pause))

        print()
        print((datetime.datetime.now().strftime("%H:%M:%S")) + "  Finished.")





#######################################


verification()






