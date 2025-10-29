import csv
from tempfile import NamedTemporaryFile
import shutil

from config import Config
from functions.check_voicemail import check_voicemail
from functions.answering_rules import update_answer_rule


def main():
    print("Tool Starting...")
    tempfile = NamedTemporaryFile(mode="w", delete=False)

    with open(Config.CSV_FILE, "r") as csvfile:
        csvreader = csv.reader(
            csvfile,
        )
        csvwriter = csv.writer(tempfile)
        fields = next(csvreader)
        print(fields)
        csvwriter.writerow(fields)
        for row in csvreader:
            user = row[0]
            domain = row[1]
            last_count = int(row[2])
            target_user = row[3]
            try:
                new_count = int(
                    check_voicemail(
                        Config.API_KEY, user=user, domain=domain, folder="new"
                    )["count"]
                )
                if last_count == 0 and new_count > 0:
                    update_answer_rule(
                        Config.API_KEY, user=target_user, domain=domain, dnd="yes"
                    )
                    row[2] = new_count
                    print(f"New Voicemail for {user}@{domain}: {new_count}")
                elif last_count > 0 and new_count == 0:
                    update_answer_rule(
                        Config.API_KEY, user=target_user, domain=domain, dnd="no"
                    )
                    row[2] = new_count
                    print(f"Voicemails cleaned up for {user}@{domain}: {new_count}")
                else:
                    print(f"No change for {user}@{domain}: {new_count}")
            except Exception as e:
                print(f"ERROR: {e}")
            csvwriter.writerow(row)
    shutil.move(tempfile.name, Config.CSV_FILE)


main()
