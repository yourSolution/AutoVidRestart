import config
import ConfigService
userInfo = ConfigService.DeCrashService(config.loadAmount, config.vidRestart, config.loadButton)


def on_press(key):

    try:
        k = key.char
    except:
        k = key.name

    if k == config.closeService:
        raise SystemExit
    userInfo.vidRestart(k)
