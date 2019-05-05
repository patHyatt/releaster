# Releaster
CLI to retrieve version differences from GitHub repositories

## Use 

```bash
#Differences for https://github.com/sass/node-sass/releases/ between version 4.9.2 and 4.12.0
releaster.py -r "sass/node-sass" -c "v4.9.2" -p "v4.12.0"