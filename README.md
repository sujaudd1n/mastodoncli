# MastodonCLI

## Setup

\<domain\_name\> refers to instance name such as: **mastodon.social** 
\<token\> refers to access token.

If you don't know your access token. Create one by following these
steps.

```console
$export DOMAIN=<domain_name>
$export TOKEN=<token>
```

## Run

```console
$python3 main.py
```

Notice the prompt **>**

## Docs

To post some text. Use ```!p``` command.

```console
> !p hello from the terminal.
Wait...
Success.
```

## Get access token

- Go the [settings/applications](https://mastodon.social/settings/applications).
- Click on **New application**.
- Give a name and click **submit**.
- Open newly created application.
- You can access you access token from here.
