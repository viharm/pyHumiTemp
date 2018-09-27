# pyHumiTemp

|             |                                                          |
|:------------|:---------------------------------------------------------|
| Version     | 1.0.1                                                    |
| Changes     | https://github.com/viharm/pyHumiTemp/pull/3              |
| Download    | https://github.com/viharm/pyHumiTemp/releases            |
| Repository  | https://github.com/viharm/pyHumiTemp                     |
| Issues      | https://github.com/viharm/pyHumiTemp/issues              |
| License     | Modified BSD (3-clause)                                  |
| Language    | Python                                                   |

*pyHumiTemp* is a script to capture numeric humidity and temperature output from DHT22.


## Installation


### Pre-requisites

* *DHT22* humidity and temperature sensor
* ***tango*** binary (http://blog.e-photographer.net/?p=927) to interrogate *DHT22*
* Hardware drivers for *DHT22* specific to the platform


### Download

Download the script as an archive, clone as a *Git* repository and install with *pip* from *PyPI*


#### Archive

Download archive of the latest version from https://github.com/viharm/pyHumiTemp/releases/latest.


### PyPI

From version v1.0.1 onwards, *pyHumiTemp* is available on *[PyPI](https://pypi.org/)* and can be installed with *pip* (or *pip3*)

```
pip install pyhumitemp
```

Or if *pip* is not in the system path,

```
python3 -m pip install pyhumitemp
```


#### Clone repository

Clone the repository into the required location;
```
git clone https://github.com/viharm/pyHumiTemp.git
```


### Deploy

No specific deployment requirements.


## Configuration

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

For issues, queries, suggestions and comments please create an issue/ticket at https://github.com/viharm/pyHumiTemp/issues.


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


### Tools


#### tango

*tango* binary for interrogating *DHT22*


### Utilities


#### Notepad++

*Notepad++* text editor (https://notepad-plus-plus.org/), used under the GNU GPL.

Copyright (C) Don Ho.


#### Codiad

*Codiad* web based IDE (https://github.com/Codiad/Codiad), used under a MIT-style license.

Copyright (c) Codiad & Kent Safranski (codiad.com)


#### Ungit

*Ungit* web based interface for *Git* (https://github.com/FredrikNoren/ungit), used under the MIT license.

Copyright (C) 2013-2016 Fredrik Norén


#### GitHub

Hosted by *GitHub* code repository (github.com).

