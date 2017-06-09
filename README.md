## OpenScienceRadio-Zenodo-Uploader

Small tool to upload [Open Science Radio](http://openscienceradio.de)
episodes to [Zenodo](https://zenodo.org). If you want to adapt this for
your own needs please be aware that some meta information is hard
coded.

### Example


Step 1 - Download the file and compile the meta data.

```
./osr-zenodo-uploader.py compile_data -u http://www.openscienceradio.de/2015/01/29/osr028-unseminars-mit-aidan-budd/ -o OSR028
```

This should lead to the following folde/file structure:
```
OSR028
├── meta.json
├── OSR028-unseminars-mit-aidan-budd
├── OSR028-unseminars-mit-aidan-budd.m4a
├── OSR028-unseminars-mit-aidan-budd.mp3
└── OSR028-unseminars-mit-aidan-budd.opus
```

You can edit the meta data file manually if needed.

Step 2 - Zenodo submission:

```
./osr-zenodo-uploader.py upload -i OSR028
```

### Links

Token creation at zenodo:
- https://zenodo.org/account/settings/applications/tokens/new/

Helpful documentation: 
- http://developers.zenodo.org/#quickstart-upload
