#!/usr/bin/env python

import os
import argparse

parser = argparse.ArgumentParser(
                    prog='ips',
                    description='Calculates the POT/spill and int/spill')

parser.add_argument('-i', '--maxint-file', help="The output file froma run of event_rate", required=True)
parser.add_argument('-e', '--beam-energy', help="The beam energy in GeV. [default: 30]")
parser.add_argument('-p', '--beam-power', help="The beam power in kW.", required=True)
parser.add_argument('-t', '--cycle-time', help="The beam cycle time in s.", required=True)
parser.add_argument('-v', '--verbose', help="Be verbose about it", action="store_true", required=False)


try:
    from ROOT import TFile
except:
    print("[ERROR]: Failed to import ROOT.")
    parser.print_help()
    exit(1)

args = parser.parse_args()

maxintf = TFile.Open(args.maxint_file, "READ")
nexp_all = maxintf["nExpInts"][0]

if args.verbose:
    print(f"nExpInts: {nexp_all} / 10^21 POT")

be_GeV = 30.0 if not args.beam_energy else float(args.beam_energy)

pps = float(args.beam_power) * 1E3 * float(args.cycle_time) / ( be_GeV * 1.60218e-10)
ips = (nexp_all / 1E21) * pps

print(f"{pps:.3g}\n{ips:.4g}")
