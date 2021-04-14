# investment-interface v1.0
A way to monitor investments on Vanguard with Python

Still fairly primitive.  No idea how well it would work with browsers other than Firefox.

If you're interested, you'll need to aquire geckodriver.  You'll also need to create a keys.py file which contains variables storing the path to the geckodriver executable as well as your Vanguard username and password.

At the top of the driver, you do need to specify the exact number of stocks/ETFs listed in the account (sorry, I'll try and figure something out there).  The driver also allows you to specify whether you want to run headless or with the browser display (for troubleshooting, primarily).

For now, just prints stock/ETF ticker symbols along with 1-day percentage change and total cost basis earnings.  I intend to create a physical interface using a Raspberry Pi Zero at some point but the info could be used numerous ways.
