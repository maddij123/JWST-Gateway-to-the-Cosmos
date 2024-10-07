from earsketch import *

setTempo(60)
fitMedia(YG_GOSPEL_PERC_1, 1, 1, 33)  # A futuristic pad sound to create a deep, ambient feel
fitMedia(RD_UK_HOUSE__WARMPIANO_2, 2, 5, 25)  # Adds a melodic piano layer that’s uplifting
fitMedia(HIPHOP_DUSTYPERCUSSION_001, 3, 15, 33)  # Light percussion for a sense of curiosity and progression
fitMedia(YG_ALT_POP_SYNTH_1, 4, 10, 33)  # A subtle backing synth to add futuristic texture
fitMedia(RD_RNB_SFX_WIND_1, 5, 8, 9)  # Whoosh effect for dramatic transitions
fitMedia(YG_TECHNO_SYNTH_2, 6, 18, 33)  # Arpeggiated synth to enhance the atmosphere
fitMedia(RD_TRAP_ANALOGSINELEAD_1, 7, 20, 33)
fitMedia(AK_UNDOG_OOHS_1, 8, 12, 30)  # Adds an 'ooh' vocal sample to enrich the atmosphere

setEffect(1, VOLUME, GAIN, -10)  # Lower volume of pad to create a background atmosphere
setEffect(2, VOLUME, GAIN, -60, 1, 0, 10)  # Fade in piano
setEffect(2, VOLUME, GAIN, 0, 25, -60, 33)  # Fade out piano towards the end

setEffect(1, VOLUME, GAIN, -12)
setEffect(2, VOLUME, GAIN, -20, 1, -5, 10)
setEffect(2, VOLUME, GAIN, -5, 25, -60, 33)
setEffect(4, VOLUME, GAIN, -2)
setEffect(6, VOLUME, GAIN, -10)
setEffect(7, VOLUME, GAIN, -6)
setEffect(8, VOLUME, GAIN, -5)  

# setEffect(1, PAN, LEFT_RIGHT, -50)
# setEffect(4, PAN, LEFT_RIGHT, 50)
# setEffect(6, PAN, LEFT_RIGHT, -25)
# setEffect(7, PAN, LEFT_RIGHT, 25)

# setEffect(6, REVERB, REVERB_TIME, 200)
# setEffect(1, REVERB, REVERB_TIME, 150)
# setEffect(2, DELAY, DELAY_TIME, 300)

finish()


