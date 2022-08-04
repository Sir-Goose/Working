import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_convert_dict = {

        "1": "13",
        "2": "14",
        "3": "15",
        "4": "16",
        "5": "17",
        "6": "18",
        "7": "19",
        "8": "20",
        "9": "21",
        "10": "22",
        "11": "23",
        "12": "12"

    }

    # long format

    if ":" in s:
        s = s.split("to")
        time_1 = s[0]
        time_2 = s[1]

        time_1 = time_1.replace("AM", "")
        time_2 = time_2.replace("PM", "")
        time_1 = time_1.replace("PM", "")
        time_2 = time_2.replace("AM", "")
        time_1 = time_1.strip()
        time_2 = time_2.strip()



        if "PM" in s[0]:
            time_1 = time_1.split(":")
            if int(time_1[1]) > 59:
                raise ValueError
            time_1[0] = time_convert_dict[time_1[0]]
            time_1 = time_1[0] + ":" + time_1[1]
        else:
            time_1 = time_1.split(":")
            if int(time_1[1]) > 59:
                raise ValueError
            if len(time_1[0]) == 1:

                time_1 = "0" + str(time_1[0]) + ":" + time_1[1]





            if str(time_1[0]) == "12":
                time_1[0] = "00"

                time_1 = str(time_1[0]) + ":" + "00"







        if "PM" in s[1]:
            time_2 = time_2.split(":")
            if int(time_2[1]) > 59:
                raise ValueError
            time_2[0] = time_convert_dict[time_2[0]]
            time_2 = time_2[0] + ":" + time_2[1]
        else:
            time_2 = time_2.split(":")
            if int(time_2[1]) > 59:
                raise ValueError
            if str(time_2[0]) == "12":
                time_2[0] = "00"
            if len(time_2[0]) == 1:
                time_2 = "0" + time_2[0] + ":" + time_2[1]

        converted_time = (time_1 + " to " + str(time_2))
        return converted_time

# short format
    else:
        if "-" in s:
            raise ValueError

        s = s.split("to")

        time_1 = s[0]
        time_2 = s[1]
        time_1 = time_1.replace("AM", "")
        time_2 = time_2.replace("PM", "")
        time_1 = time_1.replace("PM", "")
        time_2 = time_2.replace("AM", "")
        time_1 = time_1.strip()
        time_2 = time_2.strip()

        if " " not in s[0]:
            raise ValueError
        if " " not in s[1]:
            raise ValueError



        if "PM" in s[0]:
            time_1 = time_convert_dict[time_1]
        else:
            if time_1 == "12":
                time_1 = "00"
            if len(time_1) == 1:
                time_1 = "0" + str(time_1)
        if "PM" in s[1]:

            time_2 = time_convert_dict[time_2]
        else:
            time_2 = "0" + str(time_2)

        time_1 = str(time_1) + ":00"
        time_2 = str(time_2) + ":00"

        return (time_1 + " to " + time_2)

if __name__ == "__main__":
    main()
