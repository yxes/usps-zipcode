# USPS: Zip Code Lookup
Armed with a UserID from USPS and a zip code, return the city and state

## INSTALLATION

### Signup

Obtain your username from the email you received after signing up at:

https://www.usps.com/business/web-tools-apis/#developers

### Configuration

Create a configuration directory if you don't already have one called `conf/`
from the place you plan on running your code. Then place the following file
in that directory `usps.ini`. The contents of that file will be:

```
[access]
username=<YOUR USERNAME>
password=<YOUR EMAIL>
```

### Setup

`pip install . --upgrade` is what I use

## USAGE

```
from yxes.usps.zipcode import USPSZipCode()
zip = USPSZipCode()
print(zip.lookup('20024'))
```

## LICENSE

The contents of this repository are covered by the [MIT License](LICENSE)

## AUTHOR

[Steve Wells](https://www.stephendwells.com/) All Rights Reserved.