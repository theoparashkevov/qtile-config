# qtile-config
My QTile Configuration

## Installation

To install this Qtile configuration, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd qtile-config
   ```

2. **Install Qtile**:
   Ensure you have Qtile installed. You can install it using pip:
   ```bash
   pip install qtile
   ```

3. **Copy Configuration**:
   Copy the configuration files to your Qtile config directory:
   ```bash
   mkdir -p ~/.config/qtile
   cp config.py screens.py ~/.config/qtile/
   ```

4. **Start Qtile**:
   Log out and select Qtile as your window manager from the login screen.

## Debugging

To debug issues with this configuration:

1. **Check Logs**:
   Qtile logs can be found in `~/.local/share/qtile/qtile.log`. Check this file for any error messages.

2. **Reload Configuration**:
   You can reload the configuration without restarting Qtile by pressing `Mod + Ctrl + r`.

3. **Test Changes**:
   Make small changes and test frequently to isolate issues.

4. **Use a Terminal**:
   Run `qtile` from a terminal to see real-time error messages and logs.

5. **Consult Documentation**:
   Refer to the [Qtile documentation](http://docs.qtile.org/en/latest/) for more detailed troubleshooting steps.
