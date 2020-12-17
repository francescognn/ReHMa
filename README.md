# ReHMa

In order to run the code remember to add:
```
export PYTHONPATH="${PYTHONPATH}:$PWD"
```
## Runners
Class `Runner` is an Application Class implementing all the platform agnostic logics. Then in order to run the code two child class have been created: 
* `PlatformRunner` Uses libaries that can be run only on Raspberry (like GPIO).
* `AgnosticRunner` Runner that can be used on any platform to run the core code.
## Testing 
* unit tests implemented for each method
* integration tests to be run simulating raspberry input and output.
## Continuous integration
So far two pipelines have been set up: 
* ReHMa-Check performing black formatting over all python project
* ReHMa-Test running `main_test.py` to cover unit tests
