This is a tool to create DNS records in Cloudflare from a CSV file.

__Error handling has not been added to the tool yet.__

Your CSV file will need to have the following format:

`type,content,value`

EXAMPLE:

```
A,tom.example.com,1.2.3.4
CNAME,jerry.example.com,mouse.example.com
```

The python Cloudflare client is used in this script and can be installed via `pip`.

```
pip install cloudflare
```

More information on python-cloudflare can be found [here](https://github.com/cloudflare/python-cloudflare).

### How to use the tool.

#### Set your user's environment variables

```
export CF_API_EMAIL='user@example.com'
export CF_API_KEY='00000000000000000000000000000000'
```

#### Use the command line options -i and -z to specify the relative location of your CSV file and the name of the zone. The -a flag is used to specify the account that holds the zone at Cloudflare.

```
python dnsAddCSV.py -i ./file.csv -z example.com -a "Example Sites"
```

