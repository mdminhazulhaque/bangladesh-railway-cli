# Bangladesh Railway CLI

CLI for Bangladesh Railway's Ticketing System

## Motivation

* 🔥 [Bangladesh Railway E-ticketing Service](https://eticket.railway.gov.bd/) is maintained by ~Computer Network Systems Limited (CNS)~ Shohoz-Synesis-Vincen Joint Venture
* 🚀 The new service has some Laravel based APIs to query for trains and seats
* 👨‍💻 Users no longer need to be logged in to check seat availablity
* 😎 Why not build a Python client to do that?

> I developed a CLI for the old system built by CNS as well. [Browse here](https://github.com/mdminhazulhaque/bangladesh-railway-cli/tree/master-cns) for the old version.

## Installation

```bash
# clone the repo
pip install .
bangladesh-railway-cli search --from Dhaka --to Kishorganj --date 26-Mar-1971
```

## How to Use

Use the `search` option to list trains by passing the `from`, `to` and `date` parameter. If you do not pass `date`, the app will use the current date in `d-b-Y` format.

```bash
$ bangladesh-railway-cli search --from Dhaka --to Kishorganj --date 26-Mar-1971
Train Name                  Departure Time    Duration    Seats
--------------------------  ----------------  ----------  ------------
EGAROSINDHUR PROVATI (737)  04 Mar, 07:15 am  03h 55m     F_SEAT (0)
                                                          F_CHAIR (7)
                                                          S_CHAIR (0)
                                                          SHOVAN (20)
KISHORGANJ EXPRESS (781)    04 Mar, 10:30 am  03h 40m     SNIGDHA (1)
                                                          S_CHAIR (2)
                                                          AC_S (4)
EGAROSINDHUR GODHULI (749)  04 Mar, 06:45 pm  03h 55m     F_SEAT (1)
                                                          F_CHAIR (20)
                                                          S_CHAIR (6)
                                                          SHOVAN (69)
```

## TODO

- [ ] Details of seat
- [ ] Book seat (never gonna happen though)