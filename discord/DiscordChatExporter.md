# Data extraction from Discord : [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter)

To run the application in docker to avoid the tedious installation procedure, follow the instructions from [here](https://github.com/Tyrrrz/DiscordChatExporter/blob/master/.docs/Docker.md).

## Run-Through

For any further clarifications, the steps are to be walked through here.

### 1. Obtain Discord Token

**PLEASE BE CAREFUL REGARDING THE TOKEN.** 

**DO NOT SHARE YOUR TOKEN !!!** 

Follow this [instructions](https://github.com/Tyrrrz/DiscordChatExporter/blob/master/.docs/Token-and-IDs.md#using-the-network-monitor) to obtain the token.

### 2. Download docker image

```
docker pull tyrrrz/discordchatexporter:stable
```

### 3. Run the App CLI in docker
```
docker run --rm -it --user 1000:1000 -v $PWD:/out tyrrrz/discordchatexporter:stable export -t TOKEN -c CHANNELID -f csv
```

The file should be downloaded in your current working directory!