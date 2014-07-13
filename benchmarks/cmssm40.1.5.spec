# SOFTSUSY3.4.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.1       # version number
     3   # Warning: stau LSP
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
     1    3.90000000e+02   # m0
     2    7.00000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.67495838e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.20639075e-04
# MX=1.67495838e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03883208e+01   # MW
        25     1.18668364e+02   # h0
        35     8.06912600e+02   # H0
        36     8.06915828e+02   # A0
        37     8.11186796e+02   # H+
   1000021     1.57094185e+03   # ~g
   1000022     2.94221413e+02   # ~neutralino(1)
   1000023     5.59329019e+02   # ~neutralino(2)
   1000024     5.59473239e+02   # ~chargino(1)
   1000025    -9.12545719e+02   # ~neutralino(3)
   1000035     9.20026025e+02   # ~neutralino(4)
   1000037     9.20858935e+02   # ~chargino(2)
   1000001     1.47782206e+03   # ~d_L
   1000002     1.47580140e+03   # ~u_L
   1000003     1.47778235e+03   # ~s_L
   1000004     1.47576162e+03   # ~c_L
   1000005     1.25369417e+03   # ~b_1
   1000006     1.08845448e+03   # ~t_1
   1000011     6.10397202e+02   # ~e_L
   1000012     6.04954903e+02   # ~nue_L
   1000013     6.10253644e+02   # ~mu_L
   1000014     6.04810149e+02   # ~numu_L
   1000015     2.92993516e+02   # ~stau_1
   1000016     5.54485894e+02   # ~nu_tau_L
   2000001     1.41690684e+03   # ~d_R
   2000002     1.42222707e+03   # ~u_R
   2000003     1.41682780e+03   # ~s_R
   2000004     1.42222203e+03   # ~c_R
   2000005     1.31849240e+03   # ~b_2
   2000006     1.31753550e+03   # ~t_2
   2000011     4.71619819e+02   # ~e_R
   2000013     4.71242438e+02   # ~mu_R
   2000015     5.78474451e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59709466e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.98236710e-01   # N_{1,1}
  1  2    -6.14352694e-03   # N_{1,2}
  1  3     5.57094762e-02   # N_{1,3}
  1  4    -1.95494585e-02   # N_{1,4}
  2  1     1.53964474e-02   # N_{2,1}
  2  2     9.86735026e-01   # N_{2,2}
  2  3    -1.36970814e-01   # N_{2,3}
  2  4     8.57667472e-02   # N_{2,4}
  3  1    -2.52706120e-02   # N_{3,1}
  3  2     3.67767525e-02   # N_{3,2}
  3  3     7.05185664e-01   # N_{3,3}
  3  4     7.07617161e-01   # N_{3,4}
  4  1    -5.14569292e-02   # N_{4,1}
  4  2     1.57999104e-01   # N_{4,2}
  4  3     6.93432499e-01   # N_{4,3}
  4  4    -7.01099021e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.80821730e-01   # U_{1,1}
  1  2    -1.94906987e-01   # U_{1,2}
  2  1     1.94906987e-01   # U_{2,1}
  2  2     9.80821730e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.92473968e-01   # V_{1,1}
  1  2    -1.22455798e-01   # V_{1,2}
  2  1     1.22455798e-01   # V_{2,1}
  2  2     9.92473968e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.01212825e-01   # F_{11}
  1  2     9.15984863e-01   # F_{12}
  2  1     9.15984863e-01   # F_{21}
  2  2    -4.01212825e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.07038089e-01   # F_{11}
  1  2     5.90499384e-01   # F_{12}
  2  1    -5.90499384e-01   # F_{21}
  2  2     8.07038089e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     2.87768609e-01   # F_{11}
  1  2     9.57699968e-01   # F_{12}
  2  1     9.57699968e-01   # F_{21}
  2  2    -2.87768609e-01   # F_{22}
Block gauge Q= 1.16478333e+03  # SM gauge couplings
     1     3.62839418e-01   # g'(Q)MSSM DRbar
     2     6.40796373e-01   # g(Q)MSSM DRbar
     3     1.04507683e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.16478333e+03  
  3  3     8.45801165e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.16478333e+03  
  3  3     4.89422649e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.16478333e+03  
  3  3     4.28067117e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.16478333e+03 # Higgs mixing parameters
     1     9.09606780e+02    # mu(Q)MSSM DRbar
     2     3.91595669e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43656049e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     8.26629302e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.16478333e+03  # MSSM DRbar SUSY breaking parameters
     1     2.98760501e+02      # M_1(Q)
     2     5.50316764e+02      # M_2(Q)
     3     1.52737111e+03      # M_3(Q)
    21    -1.79383620e+05      # mH1^2(Q)
    22    -8.09976269e+05      # mH2^2(Q)
    31     6.03178241e+02      # meL(Q)
    32     6.03032567e+02      # mmuL(Q)
    33     5.56003749e+02      # mtauL(Q)
    34     4.66340562e+02      # meR(Q)
    35     4.65958837e+02      # mmuR(Q)
    36     3.25964260e+02      # mtauR(Q)
    41     1.43151650e+03      # mqL1(Q)
    42     1.43147604e+03      # mqL2(Q)
    43     1.24318295e+03      # mqL3(Q)
    44     1.37920841e+03      # muR(Q)
    45     1.37920329e+03      # mcR(Q)
    46     1.08720005e+03      # mtR(Q)
    47     1.37283072e+03      # mdR(Q)
    48     1.37275042e+03      # msR(Q)
    49     1.25720357e+03      # mbR(Q)
Block au Q= 1.16478333e+03  
  1  1    -1.88756341e+03      # Au(Q)MSSM DRbar
  2  2    -1.88751971e+03      # Ac(Q)MSSM DRbar
  3  3    -1.33468309e+03      # At(Q)MSSM DRbar
Block ad Q= 1.16478333e+03  
  1  1    -2.17632412e+03      # Ad(Q)MSSM DRbar
  2  2    -2.17621285e+03      # As(Q)MSSM DRbar
  3  3    -1.84328055e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.16478333e+03  
  1  1    -7.06328304e+02      # Ae(Q)MSSM DRbar
  2  2    -7.05988914e+02      # Amu(Q)MSSM DRbar
  3  3    -5.91843723e+02      # Atau(Q)MSSM DRbar
