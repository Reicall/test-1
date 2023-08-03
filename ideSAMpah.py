@bot.command()
async def idesampah(ctx):
    img_name = random.choice(os.listdir('sampah'))
    with open(f'Sampah/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send('berikut saran kerajinan dari aku')
    await ctx.send(file=picture)


bot.run("random word and number code you have")
