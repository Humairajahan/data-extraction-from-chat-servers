import os
import pandas as pd
from bs4 import BeautifulSoup


class ProcessHTMLFile:
    def __init__(self, fileName: str, output: dict):
        self.fileName = fileName
        self.output = output

    def load_file(self):
        with open(self.fileName, "r", encoding="utf-8") as file:
            contents = file.read()
            soup = BeautifulSoup(contents, "html.parser")
        return soup

    def extract_all_data(self):
        soup = self.load_file()
        msg_contents = soup.find_all(
            "div",
            class_=["message default clearfix", "message default clearfix joined"],
        )
        return msg_contents

    def extract_relevant_data(self):
        msg_contents = self.extract_all_data()
        for msg_content in msg_contents:

            if msg_content["class"] == ["message", "default", "clearfix"]:
                from_user = msg_content.find_all("div", class_="from_name")
            else:
                from_user = msg_content.find_all("div", class_="signature details")

            msg = msg_content.find_all("div", class_="text")
            date = msg_content.find_all("div", class_="pull_right date details")

            if len(from_user) == len(msg) == len(date) == 1:
                self.output["Username"].append(from_user[0].text.strip())
                self.output["Message"].append(msg[0].text.strip())
                self.output["Date"].append(date[0]["title"])
            else:
                pass

        return self.output


def processing(directory, csv_file_name):
    output = {"Username": [], "Message": [], "Date": []}
    for file in os.listdir(directory):
        fileName = os.path.join(directory, file)
        ProcessHTMLFile(fileName=fileName, output=output).extract_relevant_data()
    df = pd.DataFrame.from_dict(output)
    df.to_csv(csv_file_name, index=False)
    return df


df = processing(directory="data", csv_file_name = "messages.csv")
print(df.head(20))
