import dracula.draw

# Load existing settings made via :set
config.load_autoconfig()

dracula.draw.blood(c, {
    'spacing': {
        'vertical': 6,
        'horizontal': 8
    }
})

# c.colors.webpage.bg = base00
# If a config.py file exists, this file is ignored unless it's explicitly loaded
# via config.load_autoconfig(). For more information, see:
# https://github.com/qutebrowser/qutebrowser/blob/master/doc/help/configuring.asciidoc#loading-autoconfigyml
# DO NOT edit this file by hand, qutebrowser will overwrite it.
# Instead, create a config.py - see :help for details.

config.load_autoconfig()
#c.content.host_blocking.lists.append( str(config.configdir) + "/blockedHosts")

#adding https everywhere bindings
# config.bind('<Ctrl-v>', 'spawn mpv {url}')


config.bind('<o>', 'set-cmd-text -s :open -s')
config.bind('<Shift-o>', 'set-cmd-text -s :open -st')

config.bind('<v>', 'hint links spawn mpv --force-window=immediate {hint-url}')
