## OpenScienceRadio-Zenodo-Uploader

Small tool to upload [Open Science Radio](http://openscienceradio.de)
episodes to [Zenodo](https://zenodo.org). If you want to adapt this for
you own needs please be aware that some meta information is hard
coded.

Example:


```
./osr-zenodo-uploader.py compile_data -u http://www.openscienceradio.de/2015/01/29/osr028-unseminars-mit-aidan-budd/ -o OSR028

./osr-zenodo-uploader.py upload -i OSR028
```

Token creation at zenodo:
- https://zenodo.org/account/settings/applications/tokens/new/

Helpful documentation: 
- http://developers.zenodo.org/#quickstart-upload
