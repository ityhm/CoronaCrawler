import datetime
import sys
import traceback

logs_dir = "/home/itay/repositories/Practice/Logs"
html_dir = "/home/itay/repositories/Practice/htmls"
info_file = f"{logs_dir}/log_success.txt"


# Creates log files in folder "Logs"
def log_to_file(name, data, info="ERROR"):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    file_name = f"{logs_dir}/{current_time}-{name}-{info}"
    data = f"{data}\n\n{traceback.format_exc()}"

    write_file(file_name, data)

    print_flush(f"Log written to {file_name}")


# Create a Log file if the data is empty
def log_if_data_empty(data, name, log_data=""):
    if (data is None) or (data == []):
        log_to_file(name, f"data is empty\n{log_data}")
        return True
    return False


def log_info_line(data, file=info_file):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    string = f"{date} : {data.strip()}\n"

    print_flush(string)
    log_info(string, file)


def log_info(data, file=info_file):
    f = open(file, "a+")
    f.write(data)
    f.close()


def reset_log_info():
    f = open(info_file, "w+")
    f.write("")
    f.close()


def print_flush(string=""):
    print(string)
    sys.stdout.flush()


def write_file(file_name, data):
    with open(file_name, "w") as f:
        f.write(data)

