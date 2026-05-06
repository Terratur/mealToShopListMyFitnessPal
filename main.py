from pathlib import Path
import myfitnesspal
import browser_cookie3

cookiejar = browser_cookie3.firefox()
client = myfitnesspal.Client(
    cookiejar=cookiejar,
    log_requests_to=Path("mfp_logs"),
)

day = client.get_date(2026, 5, 6)

print("totals:", day.totals)
print("water:", day.water)
print("meals repr:", repr(day.meals))
print("keys:", list(day.keys()))