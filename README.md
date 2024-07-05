##**XSS Checker**

Xss checker is a basic xss checking tool. It uses list of payloads which are saved in the payload.txt and inject those payloads in the URL. 

##**Requirements**

It needs the Google Chrome browser installed and the exact same version of Chromedriver (https://googlechromelabs.github.io/chrome-for-testing/). Download the chromedriver and unzip it.
Make sure the Google Chrome browser and Chromedriver are the same version.
Before running the Python program, please update the chromedriver path in the Python file. Make sure that you have provided the permissions for Chromedriver.

##**Usage**

![image](https://github.com/1h3ll/xss_checker/assets/93440634/8af06e2b-a087-48a5-9f75-722c0494f923)

python3 python.py --url "http://testphp.vulnweb.com/hpp/params.php?p=PAYLOAD" --file payload.txt

Keyword **PAYLOAD** in the URL, where the payload have to be injected, --file /path/to/payload_file

##**Output Example**

![image](https://github.com/1h3ll/xss_checker/assets/93440634/4a25fdfd-4449-423f-942f-4f432720c71b)
!!Payload executed

![image](https://github.com/1h3ll/xss_checker/assets/93440634/cac9fa11-a6a2-43a4-8230-dc8b184dce4e)
!!No pop-up

##**NOTE**

The script doesn't give me any false positive. But there were some true negatives, Checking them manually will be Good.

##**HAPPY HUNTING**
