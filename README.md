<div align="center">

# 🤖 Zenny Discord RAT 🤖

**Disclaimer: This project is for educational purposes only. I am not responsible for any misuse or illegal activities conducted with this tool.**

Author: synthetic#2368

</div>

## 📝 Description

The Zenny Discord RAT is a powerful and versatile bot-based C2 (Command and Control) tool designed to provide remote access and control over multiple computer connections. With this tool, you can perform various tasks and manage computers from anywhere, enabling remote administration over long distances.

![Screenshot](https://cdn.discordapp.com/attachments/1113978822384173128/1113992782948880444/image.png)

## ✨ Features

- **Remote Desktop**: Access and control the desktop of connected computers remotely, allowing you to perform actions as if you were physically present.
- **Information Gathering**: Gather information from connected computers to gain insights into system details, network configurations, and more.
- **Remote Shell Commands**: Execute shell commands on connected computers, enabling you to run scripts, perform system operations, and manage processes remotely.
- **File Management**: Upload and download files between your local machine and connected computers, facilitating easy transfer of data and resources.
- **Troll Features**: Engage in light-hearted pranks and jokes with built-in troll features, including fake error messages, message floods, and other entertaining interactions.
- **System Monitoring**: Monitor system resources, including CPU usage, memory utilization, and network activity, providing insights into the performance and health of connected computers.

## 📋 TODO

- Less file size
- Anti debug
- Hidden bot token
- More commands for all categories
- Error handling
- No bugs

## 📋 Requirements

- Python 3.x
- Discord.py library
- Operating System: Windows/Linux/macOS

## 💻 Usage

<details>
<summary>Remote Desktop</summary>

- `.screenshot <sessionkey>`: Takes a screenshot of the user's PC.
- `.record <sessionkey>`: Records the user's screen for 30 seconds.
- `.webcam <sessionkey>`: Captures a picture from the user's webcam.
</details>

<details>
<summary>Information Gathering</summary>

- `.time <sessionkey>`: Retrieves the user's date and time.
- `.Ipinfo <sessionkey>`: Retrieves the user's IP information.
- `.sysinfo <sessionkey>`: Retrieves the user's system information.
- `.usage <sessionkey>`: Tells you the user's disk and CPU usage.
</details>

<details>
<summary>Remote Shell Commands</summary>

- `.shell <session> <command>`: Executes a command on the victim's computer.
</details>

<details>
<summary>File Management</summary>

- `.website <sessionkey> <https://example.com>`: Sends the user to a website of choice.
- `.getdownloads <sessionkey>`: Gets all user's files in the downloads folder.
- `.download <sessionkey>`: Can download any file in their downloads folder.
</details>

<details>
<summary>System Control</summary>

- `.restart <sessionkey>`: Restarts the user's computer.
- `.shutdown <sessionkey>`: Shuts down the user's computer.
</details>

<details>
<summary>Malware Commands</summary>

- `.upload <session> <filelink>`: Uploads and downloads a file and then runs it on the victim's PC.
- `.startup <session>`: Puts the RAT on startup.
- `.ddos <website>`: COMING SOON.
- `.spread <session>`: COMING SOON.
- `.roblox <session>`: COMING SOON.
- `.exodus <session>`: COMING SOON.
</details>

<details>
<summary>Troll Commands</summary>

- `.rickroll <session>`: Rickrolls them for 30 seconds, and they cannot escape.
- `.music <session> <file_attachment>`: Plays music on their computer.
- `.bluescreen <session>`: COMING SOON.
</details>

## 🔧 Setup

1. Go to [Discord Developer Portal](https://discord.com/developers/applications) and sign in.
2. Create a new application and set up your bot.
3. In the bot settings, ensure the required options as shown below:

![Bot Settings Image](https://cdn.discordapp.com/attachments/1113445608691335181/1114385999766749184/image.png)

4. Go to the OAuth section, select the bot and administrator permissions, scroll down, and copy the generated link.
5. Go back to the bot settings, reset the token, and copy it.
6. Update the necessary configuration files with your bot token.
7.Run the Zenny Discord RAT script using Python 3.x.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
