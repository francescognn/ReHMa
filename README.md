# ReHMa

In order to run the code remember to add:
```
export PYTHONPATH="${PYTHONPATH}:$PWD"
```
## Runners
Class `Runner` is an Application Class implementing all the platform agnostic logics. Then in order to run the code two child class have been created: 
* `PlatformRunner` Uses libaries that can be run only on Raspberry (like GPIO).
* `IndependentRunner` Runner that can be used on any platform to run the core code.
## Emulator
Class `Emulator` is meant to emulate the behaviour of the heating system (i.e. when the heater is turned on, the temperature increases). Currently it gets a config string (default is `"constant"`) and so far three have been implemented in order to build up acceptance tests: 
* `constant` that keeps a constant temperature of 10°
* `winter` simulating a winter scenario with temperatures going to 2.0°
* `summer` that simulates increasing temperatures till `T_MAX` 
## Testing 
* unit tests implemented for each method
* acceptance tests to be run simulating raspberry input and output.
## Continuous integration
So far two pipelines have been set up: 
* ReHMa-Check performing black formatting over all python project
* ReHMa-Test running `main_test.py` to cover unit tests

## Deploy
* First we need to install Pyinstaller: 
```
pip3 install pyinstaller
```
* Then we can generate an executable for the main script: 
```
pyinstaller -F  project/main.py
```
Note that in order to work the script must contain absolute imports!
The generated executable will be available under `../ReHMa/dist`
Now we can create a service that runs our executable: 
```
sudo vi /lib/systemd/system/test-ReHMa.service
```
with the following content: 

```
[Unit]
Description=Test Service
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=/home/ubuntu/ReHMa/dist/main
StandardInput=tty-force

[Install]
WantedBy=multi-user.target
```
* Now we can enable out service: 
```
sudo systemctl enable test-ReHMa.service
```
* And start it:
```
sudo systemctl start test-ReHMa.service
```
To inspect the status use: 
```
sudo systemctl status test-ReHMa.service
```
