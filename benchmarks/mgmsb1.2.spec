# SOFTSUSY3.4.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.1       # version number
Block MODSEL  # Select model
     1    2   # gmsb
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
Block MINPAR               # SUSY breaking input parameters
     3    1.50000000e+01   # tanb, DRbar, Feynman gauge
     4    1.00000000e+00   # sign(mu)
     1    4.00000000e+04   # lambda
     2    8.00000000e+04   # M_mess
     5    3.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.95930803e-04
# MX=8.00000000e+04 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04057405e+01   # MW
        25     1.11154903e+02   # h0
        35     3.86026870e+02   # H0
        36     3.85677365e+02   # A0
        37     3.94231416e+02   # H+
   1000021     9.46337226e+02   # ~g
   1000022     1.62902693e+02   # ~neutralino(1)
   1000023     2.68746951e+02   # ~neutralino(2)
   1000024     2.65482002e+02   # ~chargino(1)
   1000025    -3.15506774e+02   # ~neutralino(3)
   1000035     3.86477891e+02   # ~neutralino(4)
   1000037     3.86223865e+02   # ~chargino(2)
   1000039     7.58400000e-10   # ~gravitino
   1000001     9.02056625e+02   # ~d_L
   1000002     8.98670859e+02   # ~u_L
   1000003     9.02055489e+02   # ~s_L
   1000004     8.98669717e+02   # ~c_L
   1000005     8.58349326e+02   # ~b_1
   1000006     8.05237869e+02   # ~t_1
   1000011     2.62668404e+02   # ~e_L
   1000012     2.50063770e+02   # ~nue_L
   1000013     2.62667360e+02   # ~mu_L
   1000014     2.50062675e+02   # ~numu_L
   1000015     1.24147509e+02   # ~stau_1
   1000016     2.49563284e+02   # ~nu_tau_L
   2000001     8.66763164e+02   # ~d_R
   2000002     8.68146077e+02   # ~u_R
   2000003     8.66761576e+02   # ~s_R
   2000004     8.68145270e+02   # ~c_R
   2000005     8.73282624e+02   # ~b_2
   2000006     8.90069373e+02   # ~t_2
   2000011     1.30907881e+02   # ~e_R
   2000013     1.30903629e+02   # ~mu_R
   2000015     2.64600938e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.89223163e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.64851916e-01   # N_{1,1}
  1  2    -6.51685412e-02   # N_{1,2}
  1  3     2.20673655e-01   # N_{1,3}
  1  4    -1.26952662e-01   # N_{1,4}
  2  1    -2.33230477e-01   # N_{2,1}
  2  2    -6.35464695e-01   # N_{2,2}
  2  3     5.51919495e-01   # N_{2,3}
  2  4    -4.87004145e-01   # N_{2,4}
  3  1    -6.00513144e-02   # N_{3,1}
  3  2     8.12339486e-02   # N_{3,2}
  3  3     6.95699385e-01   # N_{3,3}
  3  4     7.11194242e-01   # N_{3,4}
  4  1    -1.05157804e-01   # N_{4,1}
  4  2     7.65074328e-01   # N_{4,2}
  4  3     4.03348948e-01   # N_{4,3}
  4  4    -4.90828620e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1    -5.68950187e-01   # U_{1,1}
  1  2     8.22371987e-01   # U_{1,2}
  2  1    -8.22371987e-01   # U_{2,1}
  2  2    -5.68950187e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1    -6.93734320e-01   # V_{1,1}
  1  2     7.20231000e-01   # V_{1,2}
  2  1    -7.20231000e-01   # V_{2,1}
  2  2    -6.93734320e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.62127960e-01   # F_{11}
  1  2     9.32128393e-01   # F_{12}
  2  1     9.32128393e-01   # F_{21}
  2  2    -3.62127960e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     5.69608839e-01   # F_{11}
  1  2     8.21915915e-01   # F_{12}
  2  1     8.21915915e-01   # F_{21}
  2  2    -5.69608839e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.52550055e-01   # F_{11}
  1  2     9.88295746e-01   # F_{12}
  2  1     9.88295746e-01   # F_{21}
  2  2    -1.52550055e-01   # F_{22}
Block gauge Q= 8.20582492e+02  # SM gauge couplings
     1     3.62662312e-01   # g'(Q)MSSM DRbar
     2     6.45029863e-01   # g(Q)MSSM DRbar
     3     1.06791208e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.20582492e+02  
  3  3     8.68564001e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.20582492e+02  
  3  3     2.06164281e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.20582492e+02  
  3  3     1.52102939e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.20582492e+02 # Higgs mixing parameters
     1     3.06454332e+02    # mu(Q)MSSM DRbar
     2     1.45355702e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43925175e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     1.70066849e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.20582492e+02  # MSSM DRbar SUSY breaking parameters
     1     1.73047350e+02      # M_1(Q)
     2     3.27235279e+02      # M_2(Q)
     3     9.01438937e+02      # M_3(Q)
    21     5.57300250e+04      # mH1^2(Q)
    22    -8.42643450e+04      # mH2^2(Q)
    31     2.53786345e+02      # meL(Q)
    32     2.53785267e+02      # mmuL(Q)
    33     2.53454526e+02      # mtauL(Q)
    34     1.18735353e+02      # meR(Q)
    35     1.18730675e+02      # mmuR(Q)
    36     1.17285888e+02      # mtauR(Q)
    41     8.66831112e+02      # mqL1(Q)
    42     8.66829941e+02      # mqL2(Q)
    43     8.39045240e+02      # mqL3(Q)
    44     8.36112163e+02      # muR(Q)
    45     8.36111336e+02      # mcR(Q)
    46     7.79721674e+02      # mtR(Q)
    47     8.33361831e+02      # mdR(Q)
    48     8.33360201e+02      # msR(Q)
    49     8.30181370e+02      # mbR(Q)
Block au Q= 8.20582492e+02  
  1  1    -2.73808191e+02      # Au(Q)MSSM DRbar
  2  2    -2.73807803e+02      # Ac(Q)MSSM DRbar
  3  3    -2.57999801e+02      # At(Q)MSSM DRbar
Block ad Q= 8.20582492e+02  
  1  1    -2.91459832e+02      # Ad(Q)MSSM DRbar
  2  2    -2.91459290e+02      # As(Q)MSSM DRbar
  3  3    -2.85498273e+02      # Ab(Q)MSSM DRbar
Block ae Q= 8.20582492e+02  
  1  1    -2.73067059e+01      # Ae(Q)MSSM DRbar
  2  2    -2.73065066e+01      # Amu(Q)MSSM DRbar
  3  3    -2.72453391e+01      # Atau(Q)MSSM DRbar
