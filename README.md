# HumidityCatcher

![Python](https://www.python.org/static/community_logos/python-powered-w-70x28.png)

Script to capture numeric humidity and temperature output from DHT22.


## Pre-requisites

* *DHT22* humidity and temperature sensor
* ***tango*** binary (http://blog.e-photographer.net/?p=927) to interrogate *DHT22*
* Hardware drivers for *DHT22* specific to the platform


### Download

Download the script


#### Archive

Download archive of the latest version from https://github.com/viharm/HumidityCatcher/releases/latest.


#### Clone repository

Clone the repository into the required location;
```
git clone https://github.com/viharm/HumidityCatcher.git
```


### Deploy

No specific deployment requirements.


## Configure

No configuration necessary.


## Usage

Simply run the script and pass the required quantity to be measured as a parameter

### Temperature
```
/usr/bin/python3 DHT22.py --param=temperature
```


### Humidity
```
/usr/bin/python3 DHT22.py --param=humidity
```




## Known issues ##

* Only one parameter can be measured in one instance. This is by design as the numeric output can be used by other scripts.


## Support

For issues, queries, suggestions and comments please create an issue/ticket at https://github.com/viharm/HumidityCatcher/issues.


## Contribute

Please feel free to clone/fork and contribute via pull requests. Donations also welcome, simply raise an issue as described above.

Please make contact for more information.


## Development environment ##
Developed on..

* *Raspberry Pi* model B (rev 1) and model A+
* *Raspbian*
* *`python-rpi.gpio`* 0.5.11-1
* *`python3-rpi.gpio`* 0.5.11-1
* *Python* 2.7, 3.2


## License

Licensed under the modified BSD (3-clause) license.

A copy of the license is available...
* in the enclosed `LICENSE` file.
* at http://opensource.org/licenses/BSD-3-Clause


## Credits


### tango

*tango* binary for interrogating *DHT22*


### Notepad++

*Notepad++* text editor (https://notepad-plus-plus.org/), used under the GNU GPL.

Copyright (C) Don Ho.


### GitHub

Hosted by *GitHub* code repository (github.com).
