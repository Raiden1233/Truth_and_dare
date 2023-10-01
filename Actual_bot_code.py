import class_truth


# Truth and dare game implementation
@Raiden.tree.command(name='truth_or_dare', description='Generic truth and dare game smh') # repelace @Raien with your client name or leave it as @bot
async def truth(ctx: discord.Interaction):
  # \n\n**RULES**\n** ♡˗ˏ✎ ➔ You have only 7 seconds to answer and 10 to do the dare**\n**♡˗ˏ✎ ➔ You have to answer honestly**\n** ♡˗ˏ✎ ➔You have to do the dare as well (NO CHEATING)**\n
   em = discord.Embed(description = '⌦ 𓊈𒆜 𝕎𝔼𝕃ℂ𝕆𝕄𝔼 𝕋𝕆 𝕋ℝ𝕌𝕋ℍ 𝕆ℝ 𝔻𝔸ℝ𝔼 𒆜𓊉࿐ ☠️\n\n**RULE**\n** ♡˗ˏ✎ ➔ No cheating answer honestly and do your dares :p **\n')
   em.set_author(name=f'requested by {ctx.user.name}', icon_url=ctx.user.avatar)
   em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=820&height=10')
# 
   
   await ctx.response.send_message(embed= em, view= class_truth.Truth(ctx.user.avatar, ctx.user.name))
