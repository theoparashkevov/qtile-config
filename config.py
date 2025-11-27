
# Author: Teo Parashkevov
# Email: theo.parashkevov@gmail.com

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from screens import screen_0, screen_1

# ---------------------------------------------------------------------
# Constants / colors / basic settings
# ---------------------------------------------------------------------
MOD = "mod4"
TERMINAL = guess_terminal()
GROUP_NAMES = "zx123456789"

COLOR_PALETTE = {
    "rich_black": "001524",
    "caribbean_current": "15616D",
    "papaya_whip": "FFECD1",
    "orange": "FF7D00",
    "sienna": "78290F",
}

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def make_keys(mod=MOD, terminal=TERMINAL):
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
        Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle split/unsplit"),
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
        Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

        # Applications
        Key([mod], "d", lazy.spawn("dolphin"), desc="Spawn Dolphin File Manager"),
        Key([mod], "c", lazy.spawn("chromium"), desc="Spawn Chromium Web Browser"),
        Key([mod], "t", lazy.spawn("telegram-desktop"), desc="Spawn Telegram Desktop"),
        Key([mod], "p", lazy.spawn("ulauncher"), desc="Run ULauncher"),

        # Keyboard layouts
        Key([mod], "F1", lazy.spawn("setxkbmap us"), desc="Set Keyboard to US"),
        Key([mod], "F2", lazy.spawn("setxkbmap bg bas_phonetic"), desc="Set Keyboard to BG Phonetic"),
    ]
    return keys




def make_groups(names=GROUP_NAMES):
    return [Group(name) for name in names]

def group_keybindings(groups, mod=MOD):
    k = []
    for g in groups:
        k.extend(
            [
                Key([mod], g.name, lazy.group[g.name].toscreen(), desc=f"Switch to group {g.name}"),
                Key([mod, "shift"], g.name, lazy.window.togroup(g.name, switch_group=True),
                    desc=f"Switch to & move focused window to group {g.name}"),
            ]
        )
    return k


def make_scratchpad():
    return ScratchPad(
        name="scratchpad",
        dropdowns=[
            DropDown("upgrade", "kitty sudo pacman -Suy", width=0.8, height=0.6, x=0.1, y=0.2, opacity=0.8),
            DropDown("ranger", "kitty ranger", width=0.5, height=0.45, x=0.25, y=0.2, opacity=0.8),
            DropDown("htop", "kitty htop", width=0.7, height=0.8, x=0.15, y=0.1, opacity=0.8),
            DropDown("project-euler", "kitty ranger /home/tcv/PycharmProjects/ProjectEulerAnswers/Python/",
                     width=0.7, height=0.8, x=0.15, y=0.1, opacity=0.8),
            DropDown("python-learning-materials", "kitty ranger /home/tcv/PycharmProjects/python-learning-materials/",
                     width=0.7, height=0.8, x=0.15, y=0.1, opacity=0.8),

            # Emacs Notes
            DropDown("emacs-notes", "kitty emacs -nw /home/tcv/Notes/", width=0.7, height=0.8, x=0.15, y=0.1, opacity=0.8),
            # Emacs QTile Keybindings
            DropDown("emacs-qtile-keybindings", "kitty emacs -nw ~/.config/qtile/keybindings.org",
                     width=0.4, height=0.85, x=0.25, y=0.05, opacity=0.8),

            # Emacs YouTube (various positions)
            DropDown("emacs-youtube-light-ne",
                     "kitty emacs -nw --load /home/tcv/.config/emacs/yt-live-text-light.el --file /home/tcv/Temporary/yt-notes-light.org",
                     width=0.45, height=0.5, x=0.5, y=0.03, opacity=0.8),
            DropDown("emacs-youtube-dark-ne",
                     "kitty emacs -nw --load /home/tcv/.config/emacs/yt-live-text-dark.el --file /home/tcv/Temporary/yt-notes-dark.org",
                     width=0.45, height=0.5, x=0.5, y=0.03, opacity=0.8),
            DropDown("emacs-youtube-light-nw",
                     "kitty emacs -nw --load /home/tcv/.config/emacs/yt-live-text-light.el --file /home/tcv/Temporary/yt-notes-light.org",
                     width=0.45, height=0.5, x=0.025, y=0.03, opacity=0.8),
            DropDown("emacs-youtube-dark-nw",
                     "kitty emacs -nw --load /home/tcv/.config/emacs/yt-live-text-dark.el --file /home/tcv/Temporary/yt-notes-dark.org",
                     width=0.45, height=0.5, x=0.025, y=0.03, opacity=0.8),
            DropDown("emacs-youtube-light-se",
                     "kitty emacs -nw --load /home/tcv/.config/emacs/yt-live-text-light.el --file /home/tcv/Temporary/yt-notes-light.org",
                     width=0.45, height=0.5, x=0.5, y=0.43, opacity=0.8),
            DropDown("emacs-youtube-dark-se",
                     "kitty emacs -nw --load /home/tcv/.config/emacs/yt-live-text-dark.el --file /home/tcv/Temporary/yt-notes-dark.org",
                     width=0.45, height=0.5, x=0.5, y=0.43, opacity=0.8),
            DropDown("emacs-youtube-light-sw",
                     "kitty emacs -nw --load /home/tcv/.config/emacs/yt-live-text-light.el --file /home/tcv/Temporary/yt-notes-light.org",
                     width=0.45, height=0.5, x=0.025, y=0.43, opacity=0.8),
            DropDown("emacs-youtube-dark-sw",
                     "kitty emacs -nw --load /home/tcv/.config/emacs/yt-live-text-dark.el --file /home/tcv/Temporary/yt-notes-dark.org",
                     width=0.45, height=0.5, x=0.025, y=0.43, opacity=0.8),

            # Terminal
            DropDown("term_2", "kitty", width=0.4, height=0.35, x=0.3, y=0.2, opacity=0.8),
        ],
    )

def make_scratchpad_keybindings(mod=MOD):
    k = []
    # YouTube Key Chords (light)
    k.append(
        KeyChord([mod, "control"], "l", [
            Key([], "F1", lazy.group['scratchpad'].dropdown_toggle('emacs-youtube-light-nw')),
            Key([], "F2", lazy.group['scratchpad'].dropdown_toggle('emacs-youtube-light-ne')),
            Key([], "F3", lazy.group['scratchpad'].dropdown_toggle('emacs-youtube-light-sw')),
            Key([], "F4", lazy.group['scratchpad'].dropdown_toggle('emacs-youtube-light-se')),
        ])
    )
    # YouTube Key Chords (dark)
    k.append(
        KeyChord([mod, "control"], "d", [
            Key([], "F1", lazy.group['scratchpad'].dropdown_toggle('emacs-youtube-dark-nw')),
            Key([], "F2", lazy.group['scratchpad'].dropdown_toggle('emacs-youtube-dark-ne')),
            Key([], "F3", lazy.group['scratchpad'].dropdown_toggle('emacs-youtube-dark-sw')),
            Key([], "F4", lazy.group['scratchpad'].dropdown_toggle('emacs-youtube-dark-se')),
        ])
    )
    # Emacs & System shortcuts
    k.extend([
        Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('emacs-notes')),
        Key([mod, "control"], "p", lazy.group['scratchpad'].dropdown_toggle('emacs-qtile-keybindings')),
        KeyChord([mod], "s", [
            Key([], "h", lazy.group['scratchpad'].dropdown_toggle('htop')),
            Key([], "u", lazy.group['scratchpad'].dropdown_toggle('upgrade')),
        ]),
        Key(["control"], "r", lazy.group['scratchpad'].dropdown_toggle('ranger')),
        Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('project-euler')),
        Key(["control"], "4", lazy.group['scratchpad'].dropdown_toggle('python-learning-materials')),
    ])
    return k

 


def make_layouts():
    return [
        layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
        layout.Max(),
        layout.Stack(num_stacks=2),
        layout.Matrix(),
        layout.MonadWide(),
        layout.Tile(),
        layout.TreeTab(),
    ]

# Build primary config objects
keys = make_keys()
groups = make_groups()
# group keybindings for the (non-scratchpad) groups
keys.extend(group_keybindings(groups))

scratchpad = make_scratchpad()
groups.append(scratchpad)

# scratchpad keybindings
keys.extend(make_scratchpad_keybindings())

# layouts / screens / mouse / floating
layouts = make_layouts()

# widget defaults are defined earlier near the top of the file
screens = [screen_0, screen_1]

# Mouse (using centralized MOD)
mouse = [
    Drag([MOD], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([MOD], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]

# Floating rules (preserve original rules)
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

# Behavioural toggles (unchanged)
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None

# wmname (unchanged)
wmname = "LG3D"
