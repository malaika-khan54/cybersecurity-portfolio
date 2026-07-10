from collections import defaultdict

LOG_FILE = "sample_log.txt"
FAILED_LOGIN_LIMIT = 3


def read_login_logs(filename):
    login_records = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                if not line:
                    continue

                parts = line.split(",")

                if len(parts) != 4:
                    print(f"Skipping invalid line {line_number}: {line}")
                    continue

                timestamp, ip_address, username, status = parts

                login_records.append(
                    {
                        "timestamp": timestamp.strip(),
                        "ip_address": ip_address.strip(),
                        "username": username.strip(),
                        "status": status.strip().upper(),
                    }
                )

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    return login_records


def analyze_login_logs(login_records):
    failed_attempts_by_ip = defaultdict(int)
    successful_logins = 0
    failed_logins = 0
    suspicious_successes = []

    for record in login_records:
        ip_address = record["ip_address"]
        status = record["status"]

        if status == "FAILED":
            failed_logins += 1
            failed_attempts_by_ip[ip_address] += 1

        elif status == "SUCCESS":
            successful_logins += 1

            if failed_attempts_by_ip[ip_address] >= FAILED_LOGIN_LIMIT:
                suspicious_successes.append(record)

    suspicious_ips = {
        ip_address: attempts
        for ip_address, attempts in failed_attempts_by_ip.items()
        if attempts >= FAILED_LOGIN_LIMIT
    }

    return {
        "total_logins": len(login_records),
        "successful_logins": successful_logins,
        "failed_logins": failed_logins,
        "suspicious_ips": suspicious_ips,
        "suspicious_successes": suspicious_successes,
    }


def display_report(report):
    print("\n" + "=" * 50)
    print("LOGIN SECURITY ANALYSIS REPORT")
    print("=" * 50)

    print(f"Total login attempts: {report['total_logins']}")
    print(f"Successful logins: {report['successful_logins']}")
    print(f"Failed logins: {report['failed_logins']}")

    print("\nSuspicious IP addresses:")

    if report["suspicious_ips"]:
        for ip_address, attempts in report["suspicious_ips"].items():
            print(f"- {ip_address}: {attempts} failed attempts")
    else:
        print("No suspicious IP addresses were detected.")

    print("\nSuccessful logins after repeated failures:")

    if report["suspicious_successes"]:
        for record in report["suspicious_successes"]:
            print(
                f"- {record['timestamp']} | "
                f"IP: {record['ip_address']} | "
                f"User: {record['username']}"
            )
    else:
        print("No suspicious successful logins were detected.")

    print("=" * 50)


def main():
    login_records = read_login_logs(LOG_FILE)

    if not login_records:
        print("No login records were available to analyze.")
        return

    report = analyze_login_logs(login_records)
    display_report(report)


if __name__ == "__main__":
    main()
