import nextcord
from nextcord.ext import commands
import os
import io
import textwrap
import traceback
from contextlib import redirect_stdout

botver = "Placeholder-Chan v1.0"

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_result = None

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def adminhelp(self, ctx):
        embed = nextcord.Embed(title=botver, description="Administrator commands for Placeholder-Chan. \n The command prefix is `p-`. To run a command, you must begin a message with `p-`.", color=0x7289da)
        embed.add_field(name="Commands:", value="**p-shutdown** - Shuts down the bot. Aliases: **p-logout** \n**p-changestatus** - Changes the bot's Playing status. \n**p-reload** - Reloads all cogs.\n**p-serverlist** - Outputs a list of servers the bot is in to the terminal. \n**p-clearterm** - Clears the terminal. \n**p-eval** - Evaluate provided Python code.", inline=False)
        embed.set_footer(text=botver + " by PrincessLillie#2523", icon_url=self.bot.user.avatar.url)
        await ctx.message.author.send(embed=embed)
        await ctx.message.add_reaction("✅")

    @commands.command()
    @commands.is_owner()
    async def changestatus(self, ctx, *, arg):
        await self.bot.change_presence(activity=nextcord.Game(name=arg))
        await ctx.send(":ok_hand: Done.")

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def clearterm(self, ctx):
        os.system('clear')
        print('Logged into: ' + self.bot.user.name + "#" + self.bot.user.discriminator)
        print('------')
        await ctx.send("✅ Done! Check your console!")

    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    @commands.command()
    @commands.is_owner()
    async def eval(self, ctx, *, body: str):
        msg = await ctx.send("<a:loading:598027019447435285> Evaluating...")
        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '__': self._last_result
        }
        env.update(globals())
        body = self.cleanup_code(body)
        stdout = io.StringIO()
        to_compile = (f'async def func():\n{textwrap.indent(body, "  ")}')
        try:
            exec(to_compile, env)
        except Exception as e:
            return await msg.edit(content=f'```py\n{e.__class__.__name__}: {e}\n```')
        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await msg.edit(content=f':x: An error occurred while evaluating the code.\nTraceback is shown below.```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await msg.delete()
                await ctx.message.add_reaction('\u2705')
            except Exception: 
                pass

    @commands.command()
    @commands.is_owner()
    async def serverlist(self, ctx):
        print('------')
        print('A list of servers was requested.')
        print('Connected to:')
        async for guild in self.bot.fetch_guilds(limit=150):
            print(guild.name)
        print('------')
        await ctx.send("✅ Done! Check your console!")

def setup(bot):
    bot.add_cog(Admin(bot))
