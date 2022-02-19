# Infrastructure Setup

Infrastructure automation scripts, created by developer, for the developers. Be patient, look around and get yourself
comfortable. If you feel anything needs to be changed - contribution PRs are welcome.

## Contents

* [config.sh](config.sh) file is responsible to set the environment variables for gcp project, datastore emulator, and
  gui
* [start.sh](start.sh) file is responsible to start the gcp datastore emulator
* [stop.sh](stop.sh) will be responsible to unset the environment variables

These scripts combine or inherit the ones mentioned above.

## Recipes and Examples

___

### Pre-Requisites

* Install the Google Cloud SDK from [here](https://cloud.google.com/sdk/docs/install)
* Once the SDK is installed, install the emulator from a command prompt

```shell
gcloud components update
gcloud components install cloud-datastore-emulator
```

### Quick Start from Zero to Hero

Starting from scratch? Let's go!

```shell
# Open the terminal (say terminal1)
$ sh start.sh
```

### Tear Down

It's OK if you want to kill few servers. Here's how:

```shell
# Navigate back to the terminal2
$ press Control+C

# Navigate back to the terminal1
$ press Control+C
$ sh stop.sh
```
