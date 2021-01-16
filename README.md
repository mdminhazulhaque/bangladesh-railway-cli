# Bangladesh Railway CLI

CLI for Bangladesh Railway's Ticketing System

## Motivation

* [Bangladesh Railway's Ticketing System](https://www.esheba.cnsbd.com/#/) is maintained by Computer Network Systems Limited (CNS)
* Recently they revamped the whole website and exposed some backend APIs
* Users no longer need to be logged in to check seat availablity
* Why not build a Python client to do that?

## Installation

```bash
sudo pip3 install click tabulate
sudo install -m 775 main.py /usr/local/bin/brcli # or anything you prefer
```

## How to Use

Use the `search` option to list trains by passing the `from`, `to` and `date` parameter. If you do not pass `date`, the app will use the current date.

```
$ brcli search --from DA --to RJHI --date 2021-01-20
  Train #  Train Name        Departure Time    Duration            Train Left
---------  ----------------  ----------------  ------------------  ------------
      769  DHUMKATU_EXPRESS  06:00             5 hours 40 minutes  NO
      791  BANALATA_EXPRESS  13:30             5 hours 5 minutes   NO
      753  SILKCITY          14:45             5 hours 50 minutes  NO
      759  PADMA EXPRESS     23:00             5 hours 30 minutes  NO
```

Once you know the train number, use the `seats` option to list availablity and price for each classes.

```
$ brcli seats -f DA -t RJHI -d 2021-01-26 -n 791
Class      Fare (Adult)    Fare (Child)    Counter Seat    Mobile Seat
-------  --------------  --------------  --------------  -------------
AC_S                865             575              22             22
SNIGDHA             725             483              56             55
S_CHAIR             375             250             233            232 
```

In case you do not know the code for stations, you can use the command `from-stations` and `to-stations`.

```
$ brcli from-stations | head
Code    Station Name
------  ---------------
AUP     ABDULPUR
ACP     ACCALPUR
AHG     AHASANGANG
AKA     AKHAURA
ADG     ALAMDANGA
ASZ     ASHUGANJ
AZPR    AZAMPUR
BMSM    B SIRAJUL ISLAM

$ brcli to-stations --to RJHI | head
Code    Destination Name
------  ------------------
AUP     ABDULPUR
ACP     ACCALPUR
AZGR    AGIMNAGAR
AHG     AHASANGANG
ADG     ALAMDANGA
AIB     AMIRABAD
AUA     AMNURA
ARZ     ARANI
```

## TODO

- [ ] Book tickets via CLI
