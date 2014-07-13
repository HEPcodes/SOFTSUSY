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
     1    3.50000000e+04   # lambda
     2    7.00000000e+04   # M_mess
     5    3.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=7.61728303e-05
# MX=7.00000000e+04 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04108409e+01   # MW
        25     1.10108124e+02   # h0
        35     3.39347594e+02   # H0
        36     3.38944950e+02   # A0
        37     3.48645101e+02   # H+
   1000021     8.39053596e+02   # ~g
   1000022     1.40798169e+02   # ~neutralino(1)
   1000023     2.32121647e+02   # ~neutralino(2)
   1000024     2.28419350e+02   # ~chargino(1)
   1000025    -2.81440100e+02   # ~neutralino(3)
   1000035     3.48501291e+02   # ~neutralino(4)
   1000037     3.48281221e+02   # ~chargino(2)
   1000039     5.80650000e-10   # ~gravitino
   1000001     7.99294032e+02   # ~d_L
   1000002     7.95446018e+02   # ~u_L
   1000003     7.99293025e+02   # ~s_L
   1000004     7.95445005e+02   # ~c_L
   1000005     7.59954123e+02   # ~b_1
   1000006     7.14432799e+02   # ~t_1
   1000011     2.31279538e+02   # ~e_L
   1000012     2.16884653e+02   # ~nue_L
   1000013     2.31278630e+02   # ~mu_L
   1000014     2.16883685e+02   # ~numu_L
   1000015     1.09006170e+02   # ~stau_1
   1000016     2.16445949e+02   # ~nu_tau_L
   2000001     7.68369042e+02   # ~d_R
   2000002     7.69254403e+02   # ~u_R
   2000003     7.68367632e+02   # ~s_R
   2000004     7.69253688e+02   # ~c_R
   2000005     7.74569899e+02   # ~b_2
   2000006     7.93598390e+02   # ~t_2
   2000011     1.16276751e+02   # ~e_R
   2000013     1.16273080e+02   # ~mu_R
   2000015     2.33642063e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -8.19972725e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.55294211e-01   # N_{1,1}
  1  2    -8.09318323e-02   # N_{1,2}
  1  3     2.47855122e-01   # N_{1,3}
  1  4    -1.39394573e-01   # N_{1,4}
  2  1    -2.62559134e-01   # N_{2,1}
  2  2    -6.53314914e-01   # N_{2,2}
  2  3     5.37964085e-01   # N_{2,3}
  2  4    -4.63505089e-01   # N_{2,4}
  3  1    -6.79272001e-02   # N_{3,1}
  3  2     9.21924520e-02   # N_{3,2}
  3  3     6.92496938e-01   # N_{3,3}
  3  4     7.12274131e-01   # N_{3,4}
  4  1    -1.17735155e-01   # N_{4,1}
  4  2     7.47081129e-01   # N_{4,2}
  4  3     4.11837920e-01   # N_{4,3}
  4  4    -5.08328386e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1    -5.81564453e-01   # U_{1,1}
  1  2     8.13500330e-01   # U_{1,2}
  2  1    -8.13500330e-01   # U_{2,1}
  2  2    -5.81564453e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1    -7.19858111e-01   # V_{1,1}
  1  2     6.94121243e-01   # V_{1,2}
  2  1    -6.94121243e-01   # V_{2,1}
  2  2    -7.19858111e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.95221049e-01   # F_{11}
  1  2     9.18586045e-01   # F_{12}
  2  1     9.18586045e-01   # F_{21}
  2  2    -3.95221049e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     5.99486803e-01   # F_{11}
  1  2     8.00384641e-01   # F_{12}
  2  1     8.00384641e-01   # F_{21}
  2  2    -5.99486803e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.73886367e-01   # F_{11}
  1  2     9.84765724e-01   # F_{12}
  2  1     9.84765724e-01   # F_{21}
  2  2    -1.73886367e-01   # F_{22}
Block gauge Q= 7.29473664e+02  # SM gauge couplings
     1     3.62409657e-01   # g'(Q)MSSM DRbar
     2     6.45744583e-01   # g(Q)MSSM DRbar
     3     1.07446075e+00   # g3(Q)MSSM DRbar
Block yu Q= 7.29473664e+02  
  3  3     8.72937133e-01   # Yt(Q)MSSM DRbar
Block yd Q= 7.29473664e+02  
  3  3     2.07478880e-01   # Yb(Q)MSSM DRbar
Block ye Q= 7.29473664e+02  
  3  3     1.52212602e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 7.29473664e+02 # Higgs mixing parameters
     1     2.71990014e+02    # mu(Q)MSSM DRbar
     2     1.45563634e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44072369e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     1.31666978e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 7.29473664e+02  # MSSM DRbar SUSY breaking parameters
     1     1.51185262e+02      # M_1(Q)
     2     2.86912197e+02      # M_2(Q)
     3     7.98376707e+02      # M_3(Q)
    21     4.26450717e+04      # mH1^2(Q)
    22    -6.75544479e+04      # mH2^2(Q)
    31     2.22469665e+02      # meL(Q)
    32     2.22468723e+02      # mmuL(Q)
    33     2.22179825e+02      # mtauL(Q)
    34     1.03663238e+02      # meR(Q)
    35     1.03659128e+02      # mmuR(Q)
    36     1.02391865e+02      # mtauR(Q)
    41     7.67260020e+02      # mqL1(Q)
    42     7.67258979e+02      # mqL2(Q)
    43     7.42571212e+02      # mqL3(Q)
    44     7.40596903e+02      # muR(Q)
    45     7.40596171e+02      # mcR(Q)
    46     6.90530911e+02      # mtR(Q)
    47     7.38232345e+02      # mdR(Q)
    48     7.38230897e+02      # msR(Q)
    49     7.35400295e+02      # mbR(Q)
Block au Q= 7.29473664e+02  
  1  1    -2.43801982e+02      # Au(Q)MSSM DRbar
  2  2    -2.43801635e+02      # Ac(Q)MSSM DRbar
  3  3    -2.29653959e+02      # At(Q)MSSM DRbar
Block ad Q= 7.29473664e+02  
  1  1    -2.59649227e+02      # Ad(Q)MSSM DRbar
  2  2    -2.59648741e+02      # As(Q)MSSM DRbar
  3  3    -2.54311267e+02      # Ab(Q)MSSM DRbar
Block ae Q= 7.29473664e+02  
  1  1    -2.38600995e+01      # Ae(Q)MSSM DRbar
  2  2    -2.38599253e+01      # Amu(Q)MSSM DRbar
  3  3    -2.38065388e+01      # Atau(Q)MSSM DRbar
