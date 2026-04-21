#!/usr/bin/env python

import os
import argparse

parser = argparse.ArgumentParser(
                    prog='ips',
                    description='Calculates the POT/spill and int/spill')

parser.add_argument('-i', '--maxint-file', help="The output file froma run of event_rate", required=True)
parser.add_argument('-p', '--pot-per-spill', help="The POT per spill", required=False)
parser.add_argument('-r', '--t2k-run', help="The T2K run number", required=False)
parser.add_argument('-v', '--verbose', help="Be verbose about it", action="store_true", required=False)


try:
    from ROOT import TFile
except:
    print("[ERROR]: Failed to import ROOT.")
    parser.print_help()
    exit(1)

args = parser.parse_args()

pps = 0

if not args.pot_per_spill and not args.t2k_run:
  print("[ERROR]: one of -p or -r must be supplied")
  exit(2)

run_pps = {
        1: 3.25133e+13,
        2: 7.60003e+13,
        3: 9.01931e+13,
        4: 1.09209e+14,
        5: 1.00443e+14,
        6: 1.48711e+14,
        7: 1.95327e+14,
        8: 2.17696e+14,
        9: 2.3759e+14,
        10: 2.53211e+14,
        11: 2.54134e+14,
        12: 1.34033e+14,
        13: 1.93413e+14,
        14: 2.0619e+14,
        15: 2.28046e+14,
    }

if args.pot_per_spill:
  pps = float(args.pot_per_spill)
else:
  pps = run_pps[int(args.t2k_run)]

maxintf = TFile.Open(args.maxint_file, "READ")
nexp_all = maxintf["nExpInts"][0]

if args.verbose:
    print(f"nExpInts: {nexp_all} / 10^21 POT")

ips = (nexp_all / 1E21) * pps

print(f"{pps:.3g}\n{ips:.4g}")
