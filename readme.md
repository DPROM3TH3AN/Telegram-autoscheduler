# Telegram Message Scheduler

A desktop application that allows you to schedule and send messages to multiple Telegram groups with anti-spam safeguards.

## Features

- **Authentication & Setup**
  - OAuth or phone-number login via Telethon
  - Session persistence (no need to re-authenticate each launch)

- **Group Management**
  - Dynamically fetched list of joined groups
  - Multi-select groups via checkboxes
  - Manual group ID addition

- **Message Configuration**
  - Multi-line message composer
  - File/image attachment support
  - Message preview

- **Scheduling & Timer**
  - Date and time picker
  - Flexible repeat options (one-time, daily, weekly, custom interval)
  - Countdown display

- **Anti-Spam Safeguards**
  - Maximum messages per hour limit
  - Minimum delay between messages
  - Message validation

- **Persistence**
  - Save and load message presets
  - Configuration persistence

- **Logging & Monitoring**
  - Real-time activity log
  - Error handling and retry logic

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/telegram-message-scheduler.git
   cd telegram-message-scheduler
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python telegram_scheduler.py
   ```

## Setup

1. **Telegram API Credentials**:
   - On first launch, you'll need to enter your Telegram API credentials
   - Get these from https://my.telegram.org by creating a new application

2. **Authentication**:
   - After entering API credentials, you'll need to authenticate your Telegram account
   - Follow the prompts to enter your phone number and verification code

## Usage

### Group Selection
1. Launch the application
2. All your joined groups are automatically loaded
3. Select the groups you want to send messages to
4. You can also add groups manually by entering the group ID and name

### Message Setup
1. Compose your message in the message editor
2. Optionally attach an image or file
3. Preview your message in the preview panel

### Scheduling
1. Set the date and time for the first message
2. Choose a repeat option (one-time, daily, weekly, or custom interval)
3. For custom interval, specify the frequency in minutes or hours

### Starting the Scheduler
1. Review your settings
2. Click "Start Scheduler" to begin
3. The countdown display will show time until the next message
4. You can stop the scheduler at any time

### Presets
1. Save your current setup as a preset for future use
2. Load, modify, or delete saved presets

## Settings

Access settings from the File menu:

- **Anti-Spam Settings**:
  - Maximum messages per hour
  - Minimum delay between messages
  - Maximum message length

- **API Credentials**:
  - Update your Telegram API credentials if needed

## Requirements

- Python 3.6+
- Telethon
- Tkinter
- tkcalendar
- Pillow

## License

MIT License

## Disclaimer

This tool is intended for legitimate messaging purposes only. Users are responsible for complying with Telegram's terms of service and respecting anti-spam policies. Misuse of this tool may result in account limitations by Telegram.
