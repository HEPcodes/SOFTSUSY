# SOFTSUSY3.4.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.1       # version number
Block MODSEL  # Select model
     1    1   # sugra
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
Block MINPAR               # SUSY breaking input parameters
     3    4.00000000e+01   # tanb, DRbar, Feynman gauge
     4    1.00000000e+00   # sign(mu)
     1    7.00000000e+02   # m0
     2    6.00000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.84443301e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=9.30323213e-04
# MX=1.84443301e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03892158e+01   # MW
        25     1.18041084e+02   # h0
        35     8.07451207e+02   # H0
        36     8.07442921e+02   # A0
        37     8.11759646e+02   # H+
   1000021     1.38443749e+03   # ~g
   1000022     2.51959015e+02   # ~neutralino(1)
   1000023     4.79887074e+02   # ~neutralino(2)
   1000024     4.80022943e+02   # ~chargino(1)
   1000025    -8.00382048e+02   # ~neutralino(3)
   1000035     8.08690082e+02   # ~neutralino(4)
   1000037     8.09621888e+02   # ~chargino(2)
   1000001     1.41605850e+03   # ~d_L
   1000002     1.41397723e+03   # ~u_L
   1000003     1.41601710e+03   # ~s_L
   1000004     1.41393576e+03   # ~c_L
   1000005     1.17797872e+03   # ~b_1
   1000006     1.00406518e+03   # ~t_1
   1000011     8.05717945e+02   # ~e_L
   1000012     8.01474202e+02   # ~nue_L
   1000013     8.05521052e+02   # ~mu_L
   1000014     8.01276360e+02   # ~numu_L
   1000015     5.63229612e+02   # ~stau_1
   1000016     7.33644299e+02   # ~nu_tau_L
   2000001     1.37095570e+03   # ~d_R
   2000002     1.37464381e+03   # ~u_R
   2000003     1.37087432e+03   # ~s_R
   2000004     1.37463850e+03   # ~c_R
   2000005     1.25365394e+03   # ~b_2
   2000006     1.23008886e+03   # ~t_2
   2000011     7.35512238e+02   # ~e_R
   2000013     7.35077047e+02   # ~mu_R
   2000015     7.48860981e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59483143e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97722101e-01   # N_{1,1}
  1  2    -7.90239767e-03   # N_{1,2}
  1  3     6.33730277e-02   # N_{1,3}
  1  4    -2.17260230e-02   # N_{1,4}
  2  1     1.94544740e-02   # N_{2,1}
  2  2     9.83847653e-01   # N_{2,2}
  2  3    -1.51728441e-01   # N_{2,3}
  2  4     9.29720337e-02   # N_{2,4}
  3  1    -2.90066559e-02   # N_{3,1}
  3  2     4.23532457e-02   # N_{3,2}
  3  3     7.04589800e-01   # N_{3,3}
  3  4     7.07755628e-01   # N_{3,4}
  4  1    -5.77126152e-02   # N_{4,1}
  4  2     1.73745648e-01   # N_{4,2}
  4  3     6.90301059e-01   # N_{4,3}
  4  4    -6.99975822e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.76351794e-01   # U_{1,1}
  1  2    -2.16187824e-01   # U_{1,2}
  2  1     2.16187824e-01   # U_{2,1}
  2  2     9.76351794e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91118168e-01   # V_{1,1}
  1  2    -1.32984121e-01   # V_{1,2}
  2  1     1.32984121e-01   # V_{2,1}
  2  2     9.91118168e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.86636382e-01   # F_{11}
  1  2     9.22232242e-01   # F_{12}
  2  1     9.22232242e-01   # F_{21}
  2  2    -3.86636382e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.07945679e-01   # F_{11}
  1  2     4.19087871e-01   # F_{12}
  2  1    -4.19087871e-01   # F_{21}
  2  2     9.07945679e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     2.53750096e-01   # F_{11}
  1  2     9.67269812e-01   # F_{12}
  2  1     9.67269812e-01   # F_{21}
  2  2    -2.53750096e-01   # F_{22}
Block gauge Q= 1.07990421e+03  # SM gauge couplings
     1     3.62460529e-01   # g'(Q)MSSM DRbar
     2     6.41121265e-01   # g(Q)MSSM DRbar
     3     1.04982784e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.07990421e+03  
  3  3     8.49358498e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.07990421e+03  
  3  3     4.95983617e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.07990421e+03  
  3  3     4.23783397e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.07990421e+03 # Higgs mixing parameters
     1     7.95948262e+02    # mu(Q)MSSM DRbar
     2     3.91837757e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43758457e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     8.33264099e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.07990421e+03  # MSSM DRbar SUSY breaking parameters
     1     2.54876079e+02      # M_1(Q)
     2     4.70868770e+02      # M_2(Q)
     3     1.31978191e+03      # M_3(Q)
    21     3.01068038e+04      # mH1^2(Q)
    22    -6.19240329e+05      # mH2^2(Q)
    31     8.01543487e+02      # meL(Q)
    32     8.01345596e+02      # mmuL(Q)
    33     7.36123457e+02      # mtauL(Q)
    34     7.32531643e+02      # meR(Q)
    35     7.32095144e+02      # mmuR(Q)
    36     5.77307574e+02      # mtauR(Q)
    41     1.37567307e+03      # mqL1(Q)
    42     1.37563024e+03      # mqL2(Q)
    43     1.15996179e+03      # mqL3(Q)
    44     1.33677067e+03      # muR(Q)
    45     1.33676520e+03      # mcR(Q)
    46     9.99595844e+02      # mtR(Q)
    47     1.33211466e+03      # mdR(Q)
    48     1.33203069e+03      # msR(Q)
    49     1.20517491e+03      # mbR(Q)
Block au Q= 1.07990421e+03  
  1  1    -1.68092054e+03      # Au(Q)MSSM DRbar
  2  2    -1.68088067e+03      # Ac(Q)MSSM DRbar
  3  3    -1.17385042e+03      # At(Q)MSSM DRbar
Block ad Q= 1.07990421e+03  
  1  1    -1.94212989e+03      # Ad(Q)MSSM DRbar
  2  2    -1.94202836e+03      # As(Q)MSSM DRbar
  3  3    -1.63441011e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.07990421e+03  
  1  1    -6.62586901e+02      # Ae(Q)MSSM DRbar
  2  2    -6.62260817e+02      # Amu(Q)MSSM DRbar
  3  3    -5.54911774e+02      # Atau(Q)MSSM DRbar
