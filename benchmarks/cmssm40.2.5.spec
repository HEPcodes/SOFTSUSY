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
     1    7.50000000e+02   # m0
     2    6.50000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.79841451e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=8.97857570e-05
# MX=1.79841451e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03886374e+01   # MW
        25     1.18443381e+02   # h0
        35     8.65312455e+02   # H0
        36     8.65304624e+02   # A0
        37     8.69330175e+02   # H+
   1000021     1.49024642e+03   # ~g
   1000022     2.73950129e+02   # ~neutralino(1)
   1000023     5.21376199e+02   # ~neutralino(2)
   1000024     5.21515834e+02   # ~chargino(1)
   1000025    -8.51065761e+02   # ~neutralino(3)
   1000035     8.59253435e+02   # ~neutralino(4)
   1000037     8.60106305e+02   # ~chargino(2)
   1000001     1.52213597e+03   # ~d_L
   1000002     1.52020983e+03   # ~u_L
   1000003     1.52209241e+03   # ~s_L
   1000004     1.52016621e+03   # ~c_L
   1000005     1.27100387e+03   # ~b_1
   1000006     1.08717250e+03   # ~t_1
   1000011     8.65185220e+02   # ~e_L
   1000012     8.61214020e+02   # ~nue_L
   1000013     8.64978751e+02   # ~mu_L
   1000014     8.61006687e+02   # ~numu_L
   1000015     6.09138755e+02   # ~stau_1
   1000016     7.89866307e+02   # ~nu_tau_L
   2000001     1.47304564e+03   # ~d_R
   2000002     1.47720346e+03   # ~u_R
   2000003     1.47295998e+03   # ~s_R
   2000004     1.47719785e+03   # ~c_R
   2000005     1.34733051e+03   # ~b_2
   2000006     1.31987754e+03   # ~t_2
   2000011     7.88645479e+02   # ~e_R
   2000013     7.88188429e+02   # ~mu_R
   2000015     8.03959029e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59197682e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97966844e-01   # N_{1,1}
  1  2    -7.00705023e-03   # N_{1,2}
  1  3     5.97990107e-02   # N_{1,3}
  1  4    -2.09083198e-02   # N_{1,4}
  2  1     1.75982158e-02   # N_{2,1}
  2  2     9.84844758e-01   # N_{2,2}
  2  3    -1.46316128e-01   # N_{2,3}
  2  4     9.14477839e-02   # N_{2,4}
  3  1    -2.71347728e-02   # N_{3,1}
  3  2     3.94997921e-02   # N_{3,2}
  3  3     7.04907231e-01   # N_{3,3}
  3  4     7.07678788e-01   # N_{3,4}
  4  1    -5.49198068e-02   # N_{4,1}
  4  2     1.68734914e-01   # N_{4,2}
  4  3     6.91463278e-01   # N_{4,3}
  4  4    -7.00279143e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.78026512e-01   # U_{1,1}
  1  2    -2.08480556e-01   # U_{1,2}
  2  1     2.08480556e-01   # U_{2,1}
  2  2     9.78026512e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91407303e-01   # V_{1,1}
  1  2    -1.30811156e-01   # V_{1,2}
  2  1     1.30811156e-01   # V_{2,1}
  2  2     9.91407303e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.67699032e-01   # F_{11}
  1  2     9.29944849e-01   # F_{12}
  2  1     9.29944849e-01   # F_{21}
  2  2    -3.67699032e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.13130107e-01   # F_{11}
  1  2     4.07668256e-01   # F_{12}
  2  1    -4.07668256e-01   # F_{21}
  2  2     9.13130107e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     2.37665850e-01   # F_{11}
  1  2     9.71346974e-01   # F_{12}
  2  1     9.71346974e-01   # F_{21}
  2  2    -2.37665850e-01   # F_{22}
Block gauge Q= 1.16443447e+03  # SM gauge couplings
     1     3.62625154e-01   # g'(Q)MSSM DRbar
     2     6.40749673e-01   # g(Q)MSSM DRbar
     3     1.04601368e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.16443447e+03  
  3  3     8.46875347e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.16443447e+03  
  3  3     4.95519710e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.16443447e+03  
  3  3     4.23793474e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.16443447e+03 # Higgs mixing parameters
     1     8.46599767e+02    # mu(Q)MSSM DRbar
     2     3.91663003e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43672815e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     9.57161941e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.16443447e+03  # MSSM DRbar SUSY breaking parameters
     1     2.77018475e+02      # M_1(Q)
     2     5.10792660e+02      # M_2(Q)
     3     1.42163409e+03      # M_3(Q)
    21     4.47432325e+04      # mH1^2(Q)
    22    -6.99021669e+05      # mH2^2(Q)
    31     8.60786187e+02      # meL(Q)
    32     8.60578682e+02      # mmuL(Q)
    33     7.91968170e+02      # mtauL(Q)
    34     7.85602272e+02      # meR(Q)
    35     7.85143935e+02      # mmuR(Q)
    36     6.22324273e+02      # mtauR(Q)
    41     1.47887346e+03      # mqL1(Q)
    42     1.47882841e+03      # mqL2(Q)
    43     1.25026358e+03      # mqL3(Q)
    44     1.43647399e+03      # muR(Q)
    45     1.43646821e+03      # mcR(Q)
    46     1.07895980e+03      # mtR(Q)
    47     1.43137589e+03      # mdR(Q)
    48     1.43128756e+03      # msR(Q)
    49     1.29699862e+03      # mbR(Q)
Block au Q= 1.16443447e+03  
  1  1    -1.78111472e+03      # Au(Q)MSSM DRbar
  2  2    -1.78107306e+03      # Ac(Q)MSSM DRbar
  3  3    -1.25136966e+03      # At(Q)MSSM DRbar
Block ad Q= 1.16443447e+03  
  1  1    -2.05356768e+03      # Ad(Q)MSSM DRbar
  2  2    -2.05346161e+03      # As(Q)MSSM DRbar
  3  3    -1.73156882e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.16443447e+03  
  1  1    -6.82598230e+02      # Ae(Q)MSSM DRbar
  2  2    -6.82265817e+02      # Amu(Q)MSSM DRbar
  3  3    -5.72714057e+02      # Atau(Q)MSSM DRbar
