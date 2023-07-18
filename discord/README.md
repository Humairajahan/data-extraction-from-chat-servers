# Extract data from discord channel

Unlike `telegram`, where further processing was required after data extraction, `discord` unfortunately does not offer any in-built methods towards this end.

There are multiple other ways of achieving this objective such as:

- Third party softwares and tools (DiscordChatExporter)
- YAGPDB (Yet Another General Purpose Discord Bot)
- MEE6
- Chrome extensions

## Using chrome extension

There are quite a lot of chrome extensions available for this task. The one used in this lesson was [Discord Exporter - Backup discord chat logs](https://chrome.google.com/webstore/detail/discord-exporter-backup-d/fhpffpldicgekaenjieffeonehhijhjg?hl=en)

Click one the `Add to Chrome` option.

You now have successfully added this extension to your web browser.

## Run-Through

1. In the top-right corner, the extensions will be visible. Click on the extension we just added.

2. For first time users, the extension will require of you to signup/login with your gmail account.

3. After following through the previous step, once the extension button is clicked again, it will show a prompt with the `Start Date` and `End Date`.

4. After filling out the dates, click on `START EXPORT`.

5. If any chat logs are found in the chosen timeline, a prompt will appear. Otherwise, nothing will happen. Now, click on the `Export chat logs` button. 

6. Another prompt appears now with the following 3 options.

    - EXPORT TO XLSX
    - EXPORT TO CSV
    - EXPORT TO HTML

    Click on your preferred file type. That's it! You have now successfully exported data from your discord channel.

