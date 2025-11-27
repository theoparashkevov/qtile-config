
# Author: Teo Parashkevov
# Email: theo.parashkevov@gmail.com

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from screens import *

mod = "mod4"
terminal = guess_terminal()

# Keybindings
keys = [
    
    # Window focus
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    # Window movement
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Window resizing
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Layout management
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),


    
    # Applications
    Key([mod], "d", lazy.spawn("dolphin"), desc="Spawn Dolphin File Manager"),

    Key([mod], "c", lazy.spawn("chromium"), desc="Spawn Chromium Web Browser"),

    Key([mod], "t", lazy.spawn("telegram-desktop"), desc="Spawn Telegram Desktop"),

    Key([mod], 'space', lazy.spawn('ulauncher'), desc='Run ULauncher'),

    # Keyboard layouts
    Key([mod], 'F1', lazy.spawn('setxkbmap us'), desc="Set Keyboard to US"),
    Key([mod], 'F2', lazy.spawn('setxkbmap bg bas_phonetic'), desc="Set Keyboard to BG Phonetic"),
    # Key([mod], 'F3', lazy.spawn('setxkbmap us'), desc="Set Keyboard to Chinese"),
    
    
    
]




#####################################################################
# Groups
#####################################################################
groups = [Group(i) for i in "zx123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


#####################################################################
# ScratchPads
#####################################################################
scratch_pad = ScratchPad(
    name = 'scratchpad',
    dropdowns = [
        DropDown('upgrade',  'kitty sudo pacman -Suy', width=0.8, height=0.6, x=0.1, y=0.2, opocity=0.8),
        DropDown('ranger', 'kitty ranger', width=0.5, height=0.45, x=0.25, y=0.2, opocity=0.8),
        DropDown('htop', 'kitty htop', width=0.7, height=0.8, x=0.15, y=0.1, opocity=0.8 ),
        DropDown('project-euler', 'kitty ranger /home/tcv/PycharmProjects/ProjectEulerAnswers/Python/', width=0.7, height=0.8, x=0.15, y=0.1, opocity=0.8 ),
        DropDown('python-learning-materials', 'kitty ranger /home/tcv/PycharmProjects/python-learning-materials/', width=0.7, height=0.8, x=0.15, y=0.1, opocity=0.8 ),

        # Emacs Notes
        DropDown('emacs-notes', 'kitty emacs -nw /home/tcv/Notes/',  width=0.7, height=0.8, x=0.15, y=0.1, opocity=0.8),
        # Emacs QTile Keybindings
        DropDown('emacs-qtile-keybindings', 'kitty emacs -nw ~/.config/qtile/keybindings.org',  width=0.4, height=0.85, x=0.25, y=0.05, opocity=0.8),

        
        # Emacs YouTube
        # North East
        DropDown('emacs-youtube-light-ne', 'kitty emacs -nw --load /home/tcv/.config/emacs/yt-live-text-light.el --file /home/tcv/Temporary/yt-notes-light.org', width=0.45, height=0.5, x=0.5, y=0.03, opocity=0.8),
        DropDown('emacs-youtube-dark-ne', 'kitty emacs -nw --load /home/tcv/.config/emacs/yt-live-text-dark.el --file /home/tcv/Temporary/yt-notes-dark.org', width=0.45, height=0.5, x=0.5, y=0.03, opocity=0.8),
        # North West
        DropDown('emacs-youtube-light-nw', 'kitty emacs -nw --load /home/tcv/.config/emacs/yt-live-text-light.el --file /home/tcv/Temporary/yt-notes-light.org', width=0.45, height=0.5, x=0.025, y=0.03, opocity=0.8),
        DropDown('emacs-youtube-dark-nw', 'kitty emacs -nw --load /home/tcv/.config/emacs/yt-live-text-dark.el --file /home/tcv/Temporary/yt-notes-dark.org', width=0.45, height=0.5, x=0.025, y=0.03, opocity=0.8),
        # South East
        DropDown('emacs-youtube-light-se', 'kitty emacs -nw --load /home/tcv/.config/emacs/yt-live-text-light.el --file /home/tcv/Temporary/yt-notes-light.org', width=0.45, height=0.5, x=0.5, y=0.43, opocity=0.8),
        DropDown('emacs-youtube-dark-se', 'kitty emacs -nw --load /home/tcv/.config/emacs/yt-live-text-dark.el --file /home/tcv/Temporary/yt-notes-dark.org', width=0.45, height=0.5, x=0.5, y=0.43, opocity=0.8),
        # South  West
        DropDown('emacs-youtube-light-sw', 'kitty emacs -nw --load /home/tcv/.config/emacs/yt-live-text-light.el --file /home/tcv/Temporary/yt-notes-light.org', width=0.45, height=0.5, x=0.025, y=0.43, opocity=0.8),
        DropDown('emacs-youtube-dark-sw', 'kitty emacs -nw --load /home/tcv/.config/emacs/yt-live-text-dark.el --file /home/tcv/Temporary/yt-notes-dark.org', width=0.45, height=0.5, x=0.025, y=0.43, opocity=0.8),

        
        
        # Terminal
        DropDown('term_2', 'kitty', width=0.4,  height=0.35, x=0.3, y=0.2, opocity=0.8),
        
    ]

)

# Append to the Groups
groups.append(scratch_pad)



# Add keybindings
keys.extend(
    [
        # YouTube Key Chords
        KeyChord([mod, "control"], "l", [
            Key([], "F1", lazy.group['scratchpad'].dropdown_toggle('emacs-youtube-light-nw')),
            Key([], "F2", lazy.group['scratchpad'].dropdown_toggle('emacs-youtube-light-ne')),
            Key([], "F3", lazy.group['scratchpad'].dropdown_toggle('emacs-youtube-light-sw')),
            Key([], "F4", lazy.group['scratchpad'].dropdown_toggle('emacs-youtube-light-se')),
        ]),
        
        KeyChord([mod, "control"], "d", [
            Key([], "F1", lazy.group['scratchpad'].dropdown_toggle('emacs-youtube-dark-nw')),
            Key([], "F2", lazy.group['scratchpad'].dropdown_toggle('emacs-youtube-dark-ne')),
            Key([], "F3", lazy.group['scratchpad'].dropdown_toggle('emacs-youtube-dark-sw')),
            Key([], "F4", lazy.group['scratchpad'].dropdown_toggle('emacs-youtube-dark-se')),
        ]),

        # Emacs Key Chords
        Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('emacs-notes')),
        Key([mod, "control"], "p", lazy.group['scratchpad'].dropdown_toggle('emacs-qtile-keybindings')),
     
        # System
        KeyChord( [mod], "s", [
            Key([], "h", lazy.group['scratchpad'].dropdown_toggle('htop')),
            Key([], "u", lazy.group['scratchpad'].dropdown_toggle('upgrade')),
        ]),

        # File Manager
        
        Key(["control"], "r", lazy.group['scratchpad'].dropdown_toggle('ranger')),
        Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('project-euler')),
        Key(["control"], "4", lazy.group['scratchpad'].dropdown_toggle('python-learning-materials'))
        ]
)

 


#####################################################################
# Layouts
#####################################################################
layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    
    layout.Stack(num_stacks=2),
    # layout.Bsp(),
    layout.Matrix(),
    # layout.MonadTall(),
    layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile(),
    layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()




#####################################################################
# Screens
#####################################################################
screens = [

    # check ./screens.py
    
    # Color palette
    # 1) Rich black        - 001524
    # 2) Caribbean Current - 15616D
    # 3) Papaya whip       - FFECD1
    # 4) Orange (wheel)    - FF7D00
    # 5) Sienna            - 78290F

    screen_0,
    screen_1
]






#####################################################################
# Mouse
#####################################################################
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]






dgroups_key_binder     = None
dgroups_app_rules      = []  # type: list
follow_mouse_focus     = True
bring_front_click      = False
cursor_warp            = False
floating_layout        = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen            = True
focus_on_window_activation = "smart"
reconfigure_screens        = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None







#####################################################################
#    █▀▀ █▄░█ █▀▄
#    ██▄ █░▀█ █▄▀
#####################################################################

# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
