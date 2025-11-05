# XSS Hunter Pro

**Advanced Web Vulnerability Scanner (XSS-focused)**

A lightweight, Selenium-backed XSS testing utility that injects payloads into query parameters, path segments and fragments (optionally), validates the result using a real browser (Chrome via Chromedriver), and can send Telegram alerts when an alert() popup is triggered.

> ⚠️ **IMPORTANT — Legal & Ethical Notice**
>
> This tool is intended for use on systems you own or have explicit permission to test. Unauthorized scanning or exploitation of websites is illegal and unethical. Always obtain written permission before testing third-party systems.

---

## Features

* `PAYLOAD` placeholder substitution in target URLs
* Parameter injection (query string)
* Optional path / fragment injection (`--path`)
* Real browser validation using Selenium + ChromeDriver (headless by default)
* Optional Telegram alerting for confirmed XSS with basic URL encoding
* Multi-threaded scanning using Python `concurrent.futures`
* Pretty console output with `rich` and colored status via `colorama`

---

## Requirements

* Python 3.8+
* Google Chrome (matching your Chromedriver version)
* Chromedriver (binary accessible by the script)

Python packages (install via pip):

```bash
pip install selenium requests colorama rich
```

---

## Files

* `xss_hunter_pro.py` — main scanner script (the code you provided)
* `payloads.txt` — newline-delimited list of XSS payloads (example below)
* `targets.txt` — optional, newline-delimited list of target URLs. URLs may contain the literal `PAYLOAD` placeholder.

---

## Example payloads (`payloads.txt`)

```"><script>alert(1)</script>
'";alert(1);//
"><img src=x onerror=alert(1)>
<script>confirm(1)</script>
```

(Use a curated list appropriate to your targets.)

---

## Usage

Basic usage (single URL):

```bash
python xss_hunter_pro.py --url "https://example.com/search?q=PAYLOAD" --payload payloads.txt
```

Using a file with multiple targets:

```bash
python xss_hunter_pro.py --url targets.txt --payload payloads.txt
```

Enable path / fragment injection (when `PAYLOAD` placeholder is not present):

```bash
python xss_hunter_pro.py --url targets.txt --payload payloads.txt --path
```

Change number of concurrent threads (default 10):

```bash
python xss_hunter_pro.py --url targets.txt --payload payloads.txt --thread 20
```

---

## Configuration & Notes

* **Chromedriver path**: The script uses `Service('./chromedriver')` by default. Either place the `chromedriver` binary in the same folder, or modify the `Service()` path in `setup_browser()` to point to the binary location on your machine.

* **Headless toggle**: The script configures Chrome to run headless. If you want to debug visually, remove or comment out `chrome_options.add_argument("--headless")` in `setup_browser()`.

* **Timeouts**: HTTP requests use a short timeout (`requests.get(..., timeout=5)`) and Selenium waits for an alert with 5 seconds. Increase these values if you target slow hosts or complex pages.

* **Telegram**: Replace `your_telegram_BOT_ID` and `your_CHAT_ID` in the script with your bot token and chat id to enable notifications. The script encodes some characters for URL-safe Telegram messages but keep in mind very long URLs or special characters may still need `urllib.parse.quote_plus()` for robust encoding.

* **Resource usage**: Running many concurrent Selenium-driven browser instances is resource-heavy. Consider lowering `--thread` or using a single driver cycle per thread if system memory/CPU is limited.

---

## Suggested Improvements (optional)

* Add randomized `User-Agent` strings and request headers for HTTP request pre-checks.
* Reuse browser instances per thread (pool of drivers) rather than creating a new Chrome process for every test case to reduce overhead.
* Add more robust Telegram encoding using `urllib.parse.quote_plus()` and send additional context (payload, param name, snapshot link).
* Add logging to a file (CSV/JSON) with discovered issues, timestamps, and response snapshots.
* Provide an option to take screenshots of successful pages for manual triage.
* Add integration with Burp/OWASP ZAP for deeper analysis.

---

## Example quick checklist before scanning

1. Confirm you have explicit permission to test the targets.
2. Ensure Chromedriver version matches your installed Chrome browser.
3. Test a single URL locally to confirm Selenium and Chromedriver are working.
4. Adjust timeouts and thread count to match target performance and your machine capacity.

---

## Contribution & License

Feel free to fork and improve this repo. Add an appropriate OSS license (MIT/Apache-2.0) depending on how you want to distribute it.

---

If you'd like, I can also:

* Generate a `requirements.txt` for you
* Produce a sample `payloads.txt` with a curated list
* Convert the script into a more efficient worker-pool that reuses browser instances

Tell me which of these you want next and I will prepare it.
