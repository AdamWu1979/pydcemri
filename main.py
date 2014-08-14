import argparse
#import pydce

print 'TODO: calling syntax is wrong'

parser = argparse.ArgumentParser(description='Process DCE-MRI data.',
                                epilog='For questions and bug reports, contact David Smith <david.smith@gmail.com>')
parser.add_argument('-x', dest='extended', action='store_true',
                   help='Use Extended Tofts-Kety instead of Standard')
parser.add_argument('-p', dest='plotting', action='store_true',
                   help='plot intermediate results')
parser.add_argument('-R', help='Contrast agent relaxivity')
parser.add_argument('--TR', help='Repetition time (ms)')
parser.add_argument('--dce-flip', metavar='angle', help='Flip angle (deg) of DCE data')
parser.add_argument('--t1-flip', metavar='angle', help='Flip angles (deg) of T1 data', nargs='+')
parser.add_argument('t1file', type=file, help='path to T1 data file in MAT format')
parser.add_argument('dcefile', type=file, help='path to DCE data file in MAT format')
parser.add_argument('aiffile', type=file, help='path to AIF data file in MAT format')



#if __name__ == '__main__':
    ## SCAN PARAMETERS
    #parms = 'ex1/data_dce.mat ex1/data_t1.mat ex1/AIF.mat -R 4.76 --TR 7.939 --TE 4.6 --dce-flip 20.0 --t1-flip 20 18 16 14 12 10 8 6 4 2 -p'
    ##scan_time = 16.42   # s
    #args = parser.parse_args(parms.split())
#else:
args = parser.parse_args()

print args


#pydce.run_model(args.dcefile, args.t1file, args.t1_flip, R=args.R, 
#               TR=args.TR, dce_flip=args.dce_flip, 
#               extended=args.extended, plotting=args.plotting)
