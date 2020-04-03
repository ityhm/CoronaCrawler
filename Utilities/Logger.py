import datetime
import traceback

logs_dir = "Logs"


# Creates log files in folder "Logs"
def log_to_file(name, data, info="ERROR"):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    file_name = f"{current_time}-{name}-{info}"
    log_file = open(f"{logs_dir}/{file_name}", "w")
    log_file.write(f"{data}\n\n{traceback.format_exc()}")
    log_file.close()
    print(f"Log written to {file_name}")


# Create a Log file if the data is empty
def log_if_data_empty(data, name, log_data=""):
    if (data is None) or (data == []):
        log_to_file(name, f"data is empty\n{log_data}")
        return True
    return False
