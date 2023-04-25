from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile import bar, layout, widget


#####################################################################
# Monitor 0: +*VGA-0 1920/508x1080/286+1920+0  VGA-0
screen_0 = Screen(
    wallpaper='~/.config/qtile/bg/MilkyWay/contents/images/5120x2880.png',
    wallpaper_mode='fill',
    top=bar.Bar(
    background="15616D",
    widgets=[
        widget.CurrentLayout(),
        widget.GroupBox( 
            # padding=10,
            highlight_method='block',
            active='001524',
            background='FFECD1',
            this_current_screen_border='FF7D00',
            this_screen_border='FF7D00'
            ),

        
        widget.Prompt(),

        # Window Name
        widget.Sep(padding=10),
        widget.WindowName(),
        widget.Sep(padding=10),

        
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
                },
            name_transform=lambda name: name.upper(),
            ),

        
        # Monitor Number
        widget.Sep(padding=10),
        widget.TextBox("Monitor 0", name="default"),
        widget.Sep(padding=10),
        
        # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),

        #
        # widget.LauchBar(),

        # Keyborad Layout
        widget.Sep(padding=10),
        widget.KeyboardLayout(),
        widget.Sep(padding=10),


        
        #widget.CheckUpdates(distro='Arch'),
        
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        # widget.Systray(),
        # widget.Clock(format="%Y-%m-%d %a %I:%M %p"),

        
        # Exit QTile
        widget.QuickExit(),
        ],
        size=24,
        # opocity=0.6,
        border_width=[0, 0, 1, 0],  # Draw top and bottom borders
        border_color=["001524", "000000", "001524", "000000"]  # Borders are magenta
    ),
)





#####################################################################
# Monitor 1: +HDMI-0 1920/477x1080/268+0+0  HDMI-0
screen_1 = Screen(
    wallpaper='~/.config/qtile/bg/MilkyWay/contents/images/5120x2880.png',
    wallpaper_mode='fill',
    top=bar.Bar(
    background="15616D",
    widgets=[
        widget.CurrentLayout(),
        widget.GroupBox(
            # padding=10,
            highlight_method='block',
            active='001524',
            background='FFECD1',
            this_current_screen_border='FF7D00',
            this_screen_border='FF7D00'
            ),
        widget.Prompt(),
        widget.WindowName(),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
                },
            name_transform=lambda name: name.upper(),
            ),
        widget.TextBox("Monitor 1", name="default"),
        widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),

        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        widget.Systray(),
        # widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
        widget.QuickExit(),
        ],
        size=24,
        # opocity=0.6,
        border_width=[0, 0, 1, 0],  # Draw top and bottom borders
        border_color=["001524", "000000", "001524", "000000"]  # Borders are magenta
    ),
)


