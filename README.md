# led-scripts

A small project I conducted with my roommates in my last year of studies: controlling the LED strips we installed in our living room from a web app on your phone.

We did not take the time to deploy the webapp, so we just served it on local network with a Raspberry Pi.

Repo has multiple folders:
- A crappy web app made with **React** for the Frontend and **Flask** for the backend
- A cool interface of the LED library in Python
- A mock of the LED strips to emulate the LEDs in your terminal
- A quick telegram bot for... reasons

How it works:
- A single **Raspberry Pi** is responsible of controlling the LEDs and running the **Flask** server
- When launching the server, it's notifying us of the IP the website is hosted on through **Telegram** (this is crappy, but again, we did not have anything properly deployed, it was just for us lol)
- We select a LED mode from the web app
- It sends a POST request to the **Flask** server
- We update the **Pi** signals sent to the LED directly from the **Flask** server


<details>
  <summary>LED settings</summary>
  
LED indices (specific to our setup)
  * Up 1 - Segment 0 : 0-13
  * Side 1 - Segment 1 : 13-50
  * Side 2 - Segment 2 : 50-72
  * Down 2 - Segment 3 : 72-75
  * Up 2 - Segment 4 : 75-78
  * Side 3 - Segment 5 : 78-115
  * Side 4 - Segment 6 : 115-136
  * Down 3 - Segment 7 : 136-149
</details>
