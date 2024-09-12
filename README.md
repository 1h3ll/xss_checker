**XSS Payload Testing Tool**

This is an automated XSS (Cross-Site Scripting) payload testing tool built with Python and Selenium. It is designed to test web applications by injecting a variety of XSS payloads into URLs and monitoring for alert pop-ups to detect potential vulnerabilities.


**Features**

Payload Injection: The tool automatically injects payloads into different parts of the URL (path segments, parameters, and fragments).

Headless Testing: It uses Selenium with Chrome in headless mode to simulate a browser and execute tests without launching a visible window.

Multi-Payload Support: The tool supports multiple payloads that can be injected into multiple URLs.

Error Handling: Handles alerts, timeouts, and web driver exceptions smoothly.

Threaded Execution: Allows testing of multiple URLs and payloads simultaneously with multi-threading to speed up the process.

PAYLOAD Placeholder: You can specify URLs with a PAYLOAD placeholder, and the tool will replace the PAYLOAD with the actual XSS payloads during testing.


**Requirements**

Python 3.x

Selenium (pip install selenium)

Google Chrome installed

Chrome WebDriver:https://googlechromelabs.github.io/chrome-for-testing/ (download matching version for your Chrome browser from here and place it in the project directory)


**Usage**

Command Line Options:

--url: Specify a single URL or a file containing a list of URLs (one per line).

--payload: Specify a file containing XSS payloads (one per line).

--thread: (Optional) Number of concurrent threads to use for testing (default is 10, max is 20).


**PAYLOAD Placeholder Functionality**

In URLs, the string PAYLOAD can be used as a placeholder for where the tool will inject the actual XSS payloads. For example:

URL: https://example.com/page?param=PAYLOAD

Payload: <script>alert('XSS')</script>

The tool will replace the PAYLOAD in the URL with the payload, resulting in:

Example:

To test a single URL with a file of payloads:

`python3 xss_tool.py --url "https://example.com/page?param=PAYLOAD" --payload payloads.txt`



To test multiple URLs from a file:

`python3 xss_tool.py --url urls.txt --payload payloads.txt`


**Injecting Payloads into URL Segments**


The tool automatically injects payloads into different parts of the URL:

Path Segments: It inserts payloads into the different path segments of the URL.

Query Parameters: Payloads are injected into parameters that appear in the query string (?param=value).

Fragments: Payloads are added after the # fragment in the URL if present.

Multi-Threading

To speed up the process, you can specify the number of concurrent threads to be used for testing. By default, the tool runs with 10 threads, but this can be modified using the --thread argument.


Example of setting the number of threads to 15:

`python3 xss_tool.py --url urls.txt --payload payloads.txt --thread 15`


**Output**

The tool provides colored output to distinguish between successful and failed tests:

Green Output: Indicates that an alert was found (potential XSS vulnerability).

Red Output: Indicates a timeout or failure (no XSS vulnerability detected).



**Thanks for https://ibrahimxss.store for given me this idea.**



##Happy Hunting


Buy Me a coffee: 
Paypal: navaneethan1@proton.me
