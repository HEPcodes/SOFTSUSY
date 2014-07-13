# SOFTSUSY3.4.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.1       # version number
Block MODSEL  # Select model
     1    0   # nonUniversal
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
Block MINPAR               # SUSY breaking input parameters
     3    1.00000000e+01   # tanb, DRbar, Feynman gauge
Block EXTPAR               # non-universal SUSY breaking parameters
     0    -1.00000000e+00  # Set MX=MSUSY
     1     5.00000000e+02  # M_1(MX)
     2     2.50000000e+03  # M_2(MX)
     3     6.00000000e+02  # M_3(MX)
     11    0.00000000e+00  # At(MX)
     12    0.00000000e+00  # Ab(MX)
     13    0.00000000e+00  # Atau(MX)
     23    2.50000000e+03  # mu(MX)
     26    2.50000000e+03  # mA(pole)
     31    2.50000000e+03  # meL(MX)
     32    2.50000000e+03  # mmuL(MX)
     33    2.50000000e+03  # mtauL(MX)
     34    2.50000000e+03  # meR(MX)
     35    2.50000000e+03  # mmuR(MX)
     36    2.50000000e+03  # mtauR(MX)
     41    6.00000000e+02  # mqL1(MX)
     42    6.00000000e+02  # mqL2(MX)
     43    2.50000000e+03  # mqL3(MX)
     44    6.00000000e+02  # muR(MX)
     45    6.00000000e+02  # mcR(MX)
     46    2.50000000e+03  # mtR(MX)
     47    6.00000000e+02  # mdR(MX)
     48    6.00000000e+02  # msR(MX)
     49    2.50000000e+03  # mbR(MX)
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=7.73624857e-04
# MX=2.50362275e+03 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04024332e+01   # MW
        25     1.16443333e+02   # h0
        35     2.50009867e+03   # H0
        36     2.49999168e+03   # A0
        37     2.50164691e+03   # H+
   1000021     7.00894860e+02   # ~g
   1000022     4.91919312e+02   # ~neutralino(1)
   1000023     2.44607393e+03   # ~neutralino(2)
   1000024     2.44622212e+03   # ~chargino(1)
   1000025    -2.53386215e+03   # ~neutralino(3)
   1000035     2.57391378e+03   # ~neutralino(4)
   1000037     2.57401851e+03   # ~chargino(2)
   1000001     6.95229833e+02   # ~d_L
   1000002     6.91073325e+02   # ~u_L
   1000003     6.95229833e+02   # ~s_L
   1000004     6.91073325e+02   # ~c_L
   1000005     2.52001990e+03   # ~b_1
   1000006     2.52386697e+03   # ~t_1
   1000011     2.51891950e+03   # ~e_L
   1000012     2.51738066e+03   # ~nue_L
   1000013     2.51891950e+03   # ~mu_L
   1000014     2.51738066e+03   # ~numu_L
   1000015     2.49916120e+03   # ~stau_1
   1000016     2.51715876e+03   # ~nu_tau_L
   2000001     6.53816028e+02   # ~d_R
   2000002     6.49481594e+02   # ~u_R
   2000003     6.53816028e+02   # ~s_R
   2000004     6.49481594e+02   # ~c_R
   2000005     2.54969833e+03   # ~b_2
   2000006     2.55122283e+03   # ~t_2
   2000011     2.50357985e+03   # ~e_R
   2000013     2.50357985e+03   # ~mu_R
   2000015     2.52270814e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04702606e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.99813865e-01   # N_{1,1}
  1  2    -2.69333671e-04   # N_{1,2}
  1  3     1.85108500e-02   # N_{1,3}
  1  4    -5.43244176e-03   # N_{1,4}
  2  1     7.96746571e-03   # N_{2,1}
  2  2     8.92169832e-01   # N_{2,2}
  2  3    -3.25470402e-01   # N_{2,3}
  2  4     3.13111046e-01   # N_{2,4}
  3  1    -9.24306919e-03   # N_{3,1}
  3  2     9.78738145e-03   # N_{3,2}
  3  3     7.06917056e-01   # N_{3,3}
  3  4     7.07168331e-01   # N_{3,4}
  4  1    -1.49439183e-02   # N_{4,1}
  4  2     4.51593983e-01   # N_{4,2}
  4  3     6.27689924e-01   # N_{4,3}
  4  4    -6.33912386e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.26507626e-01   # U_{1,1}
  1  2    -5.62925522e-01   # U_{1,2}
  2  1     5.62925522e-01   # U_{2,1}
  2  2     8.26507626e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     8.37427534e-01   # V_{1,1}
  1  2    -5.46548375e-01   # V_{1,2}
  2  1     5.46548375e-01   # V_{2,1}
  2  2     8.37427534e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.49178875e-01   # F_{11}
  1  2     9.37056089e-01   # F_{12}
  2  1     9.37056089e-01   # F_{21}
  2  2    -3.49178875e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     3.98012910e-01   # F_{11}
  1  2     9.17379814e-01   # F_{12}
  2  1     9.17379814e-01   # F_{21}
  2  2    -3.98012910e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     4.06986614e-01   # F_{11}
  1  2     9.13434122e-01   # F_{12}
  2  1     9.13434122e-01   # F_{21}
  2  2    -4.06986614e-01   # F_{22}
Block gauge Q= 2.50362275e+03  # SM gauge couplings
     1     3.64673794e-01   # g'(Q)MSSM DRbar
     2     6.37359975e-01   # g(Q)MSSM DRbar
     3     1.04644592e+00   # g3(Q)MSSM DRbar
Block yu Q= 2.50362275e+03  
  3  3     8.28970900e-01   # Yt(Q)MSSM DRbar
Block yd Q= 2.50362275e+03  
  3  3     1.29202751e-01   # Yb(Q)MSSM DRbar
Block ye Q= 2.50362275e+03  
  3  3     9.97274545e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 2.50362275e+03 # Higgs mixing parameters
     1     2.53484042e+03    # mu(Q)MSSM DRbar
     2     9.54898816e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43792344e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     6.15802870e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 2.50362275e+03  # MSSM DRbar SUSY breaking parameters
     1     5.00000000e+02      # M_1(Q)
     2     2.50000000e+03      # M_2(Q)
     3     6.00000000e+02      # M_3(Q)
    21    -3.44126864e+05      # mH1^2(Q)
    22    -6.24729870e+06      # mH2^2(Q)
    31     2.50000000e+03      # meL(Q)
    32     2.50000000e+03      # mmuL(Q)
    33     2.50000000e+03      # mtauL(Q)
    34     2.50000000e+03      # meR(Q)
    35     2.50000000e+03      # mmuR(Q)
    36     2.50000000e+03      # mtauR(Q)
    41     5.99999998e+02      # mqL1(Q)
    42     5.99999998e+02      # mqL2(Q)
    43     2.50000000e+03      # mqL3(Q)
    44     5.99999998e+02      # muR(Q)
    45     5.99999998e+02      # mcR(Q)
    46     2.50000000e+03      # mtR(Q)
    47     5.99999998e+02      # mdR(Q)
    48     5.99999998e+02      # msR(Q)
    49     2.50000000e+03      # mbR(Q)
Block au Q= 2.50362275e+03  
  1  1     2.33873702e-06      # Au(Q)MSSM DRbar
  2  2     2.33874689e-06      # Ac(Q)MSSM DRbar
  3  3     3.33621639e-06      # At(Q)MSSM DRbar
Block ad Q= 2.50362275e+03  
  1  1     1.45020139e-06      # Ad(Q)MSSM DRbar
  2  2     1.45020831e-06      # As(Q)MSSM DRbar
  3  3     1.71450334e-06      # Ab(Q)MSSM DRbar
Block ae Q= 2.50362275e+03  
  1  1     0.00000000e+00      # Ae(Q)MSSM DRbar
  2  2     2.68283787e-08      # Amu(Q)MSSM DRbar
  3  3     2.67276038e-08      # Atau(Q)MSSM DRbar