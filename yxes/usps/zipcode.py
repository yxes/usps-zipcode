#!/usr/bin/env python

from yxes.config.find_dir import FindDir

from configparser import ConfigParser
import requests
import os
import xmltodict
import json


class USPSZipCode(FindDir):

    conf = ConfigParser()
    api = {
        "name": 'CityStateLookup',
        "url": 'https://secure.shippingapis.com/ShippingAPI.dll'
    }

    def __init__(self, config_file='usps.ini'):
        fd = FindDir()
        if config_file.startswith('/'):
            self.conf.read(config_file)
        else:
            self.conf.read(os.path.join(fd.conf_dir, config_file))

    def lookup(self, zipcode: str) -> dict:
        """Given zipcode --> { city: ,state: }

        Args:
            zipcode (str): 5 digit zip code required

        Returns:
            dict:
              - success: { city: 'WASHINGTON', state: 'DC' }
              - failure: { error: 'Invalid Zip Code.' }
                * 'Zip Code must be 5 numbers.'
                * 'Network Error.'

        Note:
            This might be too forgiving. If the length of your zip code is
            longer than 5 digits it will only use the first 5 without warning.
        """
        error = {'error': 'Invalid Zip Code.'}

        if len(zipcode) > 5:
            zipcode = zipcode[0:5]

        if len(zipcode) < 5:
            return {"error": 'Zip Code must be 5 numbers.'}

        xml_data = (
            f"<CityStateLookupRequest USERID='{self.conf['access']['username']}'>"
            f"<ZipCode ID='0'><Zip5>{zipcode}</Zip5></ZipCode>"
            "</CityStateLookupRequest>"
        )

        api_url = f"{self.api['url']}?API={self.api['name']}&XML={xml_data}"
        req = requests.get(api_url, headers={'Content-Type': 'aplication/xml'})

        json_data = json.loads(json.dumps(xmltodict.parse(req.text)))

        results = None
        if 'CityStateLookupResponse' in json_data:
            if 'ZipCode' in json_data['CityStateLookupResponse']:
                results = json_data['CityStateLookupResponse']['ZipCode']

        if results is None:
            return {"error": 'Network Error.'}

        # Any Error: usually invalid zip code
        if 'Error' in results:
            return {'error': results['Error']['Description']}

        return {
            'city': results['City'],
            'state': results['State']
        }


if __name__ == "__main__":
    zip = USPSZipCode()
    print(zip.lookup('20024'))
