#!/usr/bin/env python

languages = (
    "en",
    "fr",
    "se",
    "it",
    "cz",
    "de",
    "pt",
    "es",
    "pl",
    "nl"
)

tts_languages = {
    "en",
    "fr",
    "it",
    "cz",
    "de",
    "pt"
}

options_i6x = {
    "heli": ("HELI", "NO", "YES"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "gvars": ("GVARS", "YES", "NO"),
    "lua": ("LUA", "NO", "NO_MODEL_SCRIPTS"),
    "nographics": ("GRAPHICS", "NO", "YES"),
    "sqt5font": ("FONT", "SQT5", None),
    "imperial": ("UNITS", "IMPERIAL", "METRIC"),
    "multimodule": ("MULTIMODULE", "NO", "YES")
}


options_sky9x = {
    "heli": ("HELI", "YES", "NO"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "gvars": ("GVARS", "YES", "NO"),
    "potscroll": ("NAVIGATION", "POTS", "NO"),
    "autosource": ("AUTOSOURCE", "YES", "NO"),
    "autoswitch": ("AUTOSWITCH", "YES", "NO"),
    "dblkeys": ("DBLKEYS", "YES", "NO"),
    "nographics": ("GRAPHICS", "NO", "YES"),
    "battgraph": ("BATTGRAPH", "YES", "NO"),
    "nobold": ("BOLD", "NO", "YES"),
    "sqt5font": ("FONT", "SQT5", None),
    "imperial": ("UNITS", "IMPERIAL", "METRIC"),
    "bluetooth": ("BLUETOOTH", "YES", "NO"),
    "faimode": ("FAI", "YES", None),
    "faichoice": ("FAI", "CHOICE", None),
    "nooverridech": ("OVERRIDE_CHANNEL_FUNCTION", "NO", "YES"),
    "flexr9m": ("MODULE_PROTOCOL_FLEX", "YES", None)
}

options_ar9x = {
    "heli": ("HELI", "YES", "NO"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "gvars": ("GVARS", "YES", "NO"),
    "potscroll": ("NAVIGATION", "POTS", "NO"),
    "autosource": ("AUTOSOURCE", "YES", "NO"),
    "autoswitch": ("AUTOSWITCH", "YES", "NO"),
    "dblkeys": ("DBLKEYS", "YES", "NO"),
    "nographics": ("GRAPHICS", "NO", "YES"),
    "battgraph": ("BATTGRAPH", "YES", "NO"),
    "nobold": ("BOLD", "NO", "YES"),
    "sqt5font": ("FONT", "SQT5", None),
    "imperial": ("UNITS", "IMPERIAL", "METRIC"),
    "bluetooth": ("BLUETOOTH", "YES", "NO"),
    "faimode": ("FAI", "YES", None),
    "faichoice": ("FAI", "CHOICE", None),
    "nooverridech": ("OVERRIDE_CHANNEL_FUNCTION", "NO", "YES"),
    # "rtc": ("RTCLOCK", "YES", "NO"),
    "flexr9m": ("MODULE_PROTOCOL_FLEX", "YES", None)
}

options_taranis_x9d = {
    "noheli": ("HELI", "NO", "YES"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "lua": ("LUA", "YES", "NO_MODEL_SCRIPTS"),
    "haptic": ("HAPTIC", "YES", "NO"),
    "nogvars": ("GVARS", "NO", "YES"),
    "sqt5font": ("FONT", "SQT5", None),
    "faimode": ("FAI", "YES", None),
    "faichoice": ("FAI", "CHOICE", None),
    "nooverridech": ("OVERRIDE_CHANNEL_FUNCTION", "NO", "YES"),
    "internalppm": ("INTERNAL_MODULE_PPM", "YES", "NO"),
    "shutdownconfirm": ("SHUTDOWN_CONFIRMATION", "YES", "NO"),
    "eu": ("MODULE_PROTOCOL_D8", "NO", "YES"),
    "flexr9m": ("MODULE_PROTOCOL_FLEX", "YES", None)
}

options_taranis_x9dp = {
    "noheli": ("HELI", "NO", "YES"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "lua": ("LUA", "YES", "NO_MODEL_SCRIPTS"),
    "nogvars": ("GVARS", "NO", "YES"),
    "sqt5font": ("FONT", "SQT5", None),
    "noras": ("RAS", "NO", "YES"),
    "faimode": ("FAI", "YES", None),
    "faichoice": ("FAI", "CHOICE", None),
    "nooverridech": ("OVERRIDE_CHANNEL_FUNCTION", "NO", "YES"),
    "internalppm": ("INTERNAL_MODULE_PPM", "YES", "NO"),
    "shutdownconfirm": ("SHUTDOWN_CONFIRMATION", "YES", "NO"),
    "eu": ("MODULE_PROTOCOL_D8", "NO", "YES"),
    "flexr9m": ("MODULE_PROTOCOL_FLEX", "YES", None)
}

options_taranis_x9lite = {
    "noheli": ("HELI", "NO", "YES"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "lua": ("LUA", "YES", "NO_MODEL_SCRIPTS"),
    "nogvars": ("GVARS", "NO", "YES"),
    "autoupdate": ("AUTOUPDATE", "YES", None),
    "sqt5font": ("FONT", "SQT5", None),
    "noras": ("RAS", "NO", "YES"),
    "faimode": ("FAI", "YES", None),
    "faichoice": ("FAI", "CHOICE", None),
    "nooverridech": ("OVERRIDE_CHANNEL_FUNCTION", "NO", "YES"),
    "shutdownconfirm": ("SHUTDOWN_CONFIRMATION", "YES", "NO"),
    "eu": ("MODULE_PROTOCOL_D8", "NO", "YES"),
    "internalpxx1": ("INTERNAL_MODULE_PXX1", "YES", "NO"),
    "flexr9m": ("MODULE_PROTOCOL_FLEX", "YES", None)
}

options_taranis_xlite = {
    "noheli": ("HELI", "NO", "YES"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "lua": ("LUA", "YES", "NO_MODEL_SCRIPTS"),
    "nogvars": ("GVARS", "NO", "YES"),
    "sqt5font": ("FONT", "SQT5", None),
    "faimode": ("FAI", "YES", None),
    "faichoice": ("FAI", "CHOICE", None),
    "nooverridech": ("OVERRIDE_CHANNEL_FUNCTION", "NO", "YES"),
    "shutdownconfirm": ("SHUTDOWN_CONFIRMATION", "YES", "NO"),
    "eu": ("MODULE_PROTOCOL_D8", "NO", "YES"),
    "flexr9m": ("MODULE_PROTOCOL_FLEX", "YES", None)
}

options_taranis_xlites = {
    "noheli": ("HELI", "NO", "YES"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "lua": ("LUA", "YES", "NO_MODEL_SCRIPTS"),
    "nogvars": ("GVARS", "NO", "YES"),
    "autoupdate": ("AUTOUPDATE", "YES", None),
    "sqt5font": ("FONT", "SQT5", None),
    "faimode": ("FAI", "YES", None),
    "faichoice": ("FAI", "CHOICE", None),
    "nooverridech": ("OVERRIDE_CHANNEL_FUNCTION", "NO", "YES"),
    "shutdownconfirm": ("SHUTDOWN_CONFIRMATION", "YES", "NO"),
    "eu": ("MODULE_PROTOCOL_D8", "NO", "YES"),
    "internalpxx1": ("INTERNAL_MODULE_PXX1", "YES", "NO"),
    "flexr9m": ("MODULE_PROTOCOL_FLEX", "YES", None)
}

options_taranis_x9e = {
    "noheli": ("HELI", "NO", "YES"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "lua": ("LUA", "YES", "NO_MODEL_SCRIPTS"),
    "nogvars": ("GVARS", "NO", "YES"),
    "sqt5font": ("FONT", "SQT5", None),
    "faimode": ("FAI", "YES", None),
    "faichoice": ("FAI", "CHOICE", None),
    "nooverridech": ("OVERRIDE_CHANNEL_FUNCTION", "NO", "YES"),
    "internalppm": ("INTERNAL_MODULE_PPM", "YES", "NO"),
    "shutdownconfirm": ("SHUTDOWN_CONFIRMATION", "YES", "NO"),
    "eu": ("MODULE_PROTOCOL_D8", "NO", "YES"),
    "horussticks": ("STICKS", "HORUS", "STANDARD"),
    "flexr9m": ("MODULE_PROTOCOL_FLEX", "YES", None)
}

options_horus_x12s = {
    "noheli": ("HELI", "NO", "YES"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "lua": ("LUA", "YES", "NO_MODEL_SCRIPTS"),
    "nogvars": ("GVARS", "NO", "YES"),
    "faimode": ("FAI", "YES", None),
    "faichoice": ("FAI", "CHOICE", None),
    "nooverridech": ("OVERRIDE_CHANNEL_FUNCTION", "NO", "YES"),
    "eu": ("MODULE_PROTOCOL_D8", "NO", "YES"),
    "pcbdev": ("PCBREV", "10", None),
    "flexr9m": ("MODULE_PROTOCOL_FLEX", "YES", None),
    "internalaccess": [("INTERNAL_MODULE_PXX1", "NO", None), ("INTERNAL_MODULE_PXX2", "YES", None)]
}

options_horus_x10 = {
    "noheli": ("HELI", "NO", "YES"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "lua": ("LUA", "YES", "NO_MODEL_SCRIPTS"),
    "nogvars": ("GVARS", "NO", "YES"),
    "faimode": ("FAI", "YES", None),
    "faichoice": ("FAI", "CHOICE", None),
    "nooverridech": ("OVERRIDE_CHANNEL_FUNCTION", "NO", "YES"),
    "eu": ("MODULE_PROTOCOL_D8", "NO", "YES"),
    "flexr9m": ("MODULE_PROTOCOL_FLEX", "YES", None),
    "internalaccess": [("INTERNAL_MODULE_PXX1", "NO", None), ("INTERNAL_MODULE_PXX2", "YES", None)]
}

options_horus_x10express = {
    "noheli": ("HELI", "NO", "YES"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "lua": ("LUA", "YES", "NO_MODEL_SCRIPTS"),
    "luac": ("LUA_COMPILER", "YES", "NO"),
    "nogvars": ("GVARS", "NO", "YES"),
    "faimode": ("FAI", "YES", None),
    "faichoice": ("FAI", "CHOICE", None),
    "nooverridech": ("OVERRIDE_CHANNEL_FUNCTION", "NO", "YES"),
    "eu": ("MODULE_PROTOCOL_D8", "NO", "YES"),
    "flexr9m": ("MODULE_PROTOCOL_FLEX", "YES", None)
}

options_jumper_t12 = {
    "noheli": ("HELI", "NO", "YES"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "lua": ("LUA", "YES", "NO_MODEL_SCRIPTS"),
    "nogvars": ("GVARS", "NO", "YES"),
    "faimode": ("FAI", "YES", None),
    "faichoice": ("FAI", "CHOICE", None),
    "nooverridech": ("OVERRIDE_CHANNEL_FUNCTION", "NO", "YES"),
    "flexr9m": ("MODULE_PROTOCOL_FLEX", "YES", None),
    "internalmulti": ("INTERNAL_MODULE_MULTI", "YES", "NO"),
}

options_jumper_t16 = {
    "noheli": ("HELI", "NO", "YES"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "lua": ("LUA", "YES", "NO_MODEL_SCRIPTS"),
    "nogvars": ("GVARS", "NO", "YES"),
    "faimode": ("FAI", "YES", None),
    "faichoice": ("FAI", "CHOICE", None),
    "nooverridech": ("OVERRIDE_CHANNEL_FUNCTION", "NO", "YES"),
    "flexr9m": ("MODULE_PROTOCOL_FLEX", "YES", None),
    "internalmulti": ("INTERNAL_MODULE_MULTI", "YES", "NO"),
    "bluetooth": ("BLUETOOTH", "YES", "NO"),
}

options_radiomaster_tx16s = {
    "noheli": ("HELI", "NO", "YES"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "lua": ("LUA", "YES", "NO_MODEL_SCRIPTS"),
    "nogvars": ("GVARS", "NO", "YES"),
    "faimode": ("FAI", "YES", None),
    "faichoice": ("FAI", "CHOICE", None),
    "nooverridech": ("OVERRIDE_CHANNEL_FUNCTION", "NO", "YES"),
    "flexr9m": ("MODULE_PROTOCOL_FLEX", "YES", None),
    "bluetooth": ("BLUETOOTH", "YES", "NO"),
    "internalgps": ("INTERNAL_GPS", "YES", "NO"),
}

options_jumper_t18 = {
    "noheli": ("HELI", "NO", "YES"),
    "ppmus": ("PPM_UNIT", "US", "PERCENT_PREC1"),
    "lua": ("LUA", "YES", "NO_MODEL_SCRIPTS"),
    "nogvars": ("GVARS", "NO", "YES"),
    "faimode": ("FAI", "YES", None),
    "faichoice": ("FAI", "CHOICE", None),
    "nooverridech": ("OVERRIDE_CHANNEL_FUNCTION", "NO", "YES"),
    "flexr9m": ("MODULE_PROTOCOL_FLEX", "YES", None),
    "bluetooth": ("BLUETOOTH", "YES", "NO"),
    "afhds3": ("AFHDS3", "YES", "NO")
}

