## Shared vmail BLFs

running this service checks a list of users for new voicemails, and lights up a BLF button (or turns it off) if there are new messages



### How?
well, we just check if there are new voicemails when there weren't any previously (or if there aren't when there were previously)

and we update the DND status of a target user in the same domain based on the new voicemail status... all you need to do is build a BLF button for the target user and viola, a button that lights up when there are voicemails, and turns off when there are no voicemails

### instructions

copy the repo:
```bash
git clone https://github.com/DallanL/ns-shared-vmail-blf.git
cd ns-shared-vmail-blf
```

update the mailboxes.csv file to have a list of:
user (the username of the voicemailbox you want to monitor)
domain (the domain of the user)
last_count (set to 0 to start, this tracks the last voicemail count so we don't need to make as many API calls)
target_user (this is the user where we will turn on and off DND, you can make it the same as the voicemailbox's user if you are ok with their DND being turned on and off all the time)

copy the env-example file into a .env file:
```bash
cp env-example .env
```

update the .env file with your appropriate level permission API key and the url of your server

start a virtual environment for python and install required packages:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

and then setup a cronjob to run this program regularly:
```bash
sudo crontab -e
```

```
* * * * * /home/user/ns-shared-vmail-blf/venv/bin/python3 /home/user/ns-shared-vmail-blf/main.py
```
and there you have it, this checks for voicemail changes every minute
