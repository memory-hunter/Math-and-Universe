
define config.name = _("Math and Universe")

define gui.show_name = True

define config.version = "1.02"


define gui.about = _p("""
""")

define build.name = "MathUniverse"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True




define config.enter_transition = dissolve
define config.exit_transition = dissolve

define config.intra_transition = dissolve

define config.after_load_transition = fade


define config.end_game_transition = Fade(2.0, 0.0, 2.0)

define config.end_splash_transition = Fade(2.0, 0.0, 2.0)


define config.window = "auto"

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


default preferences.text_cps = 35


default preferences.afm_time = 15


define config.save_directory = "mathuniverse-1611740565"


define config.window_icon = "gui/window_icon.png"


init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.documentation('*.html')
    build.documentation('*.txt')
    config.tts_voice = "Mark"

    def geoVoice():
        config.auto_voice = "voice/georgian/{id}.mp3"
    def engVoice():
        config.auto_voice = "voice/english/{id}.mp3"

    def get_auto_voice_file_name(identifier):
        return "voice/{}/{}.mp3".format(_preferences.language or "english", identifier)

    config.auto_voice = get_auto_voice_file_name


