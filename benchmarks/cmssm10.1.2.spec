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
     3    1.00000000e+01   # tanb, DRbar, Feynman gauge
     4    1.00000000e+00   # sign(mu)
     1    1.37500000e+02   # m0
     2    5.50000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.81512863e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=8.79897206e-04
# MX=1.81512863e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03955001e+01   # MW
        25     1.15524531e+02   # h0
        35     7.83716954e+02   # H0
        36     7.83464599e+02   # A0
        37     7.87808315e+02   # H+
   1000021     1.25180886e+03   # ~g
   1000022     2.25931438e+02   # ~neutralino(1)
   1000023     4.27307772e+02   # ~neutralino(2)
   1000024     4.27348719e+02   # ~chargino(1)
   1000025    -6.90897625e+02   # ~neutralino(3)
   1000035     7.03889666e+02   # ~neutralino(4)
   1000037     7.04170382e+02   # ~chargino(2)
   1000001     1.15134188e+03   # ~d_L
   1000002     1.14875402e+03   # ~u_L
   1000003     1.15133908e+03   # ~s_L
   1000004     1.14875122e+03   # ~c_L
   1000005     1.05451588e+03   # ~b_1
   1000006     8.81640211e+02   # ~t_1
   1000011     3.96770164e+02   # ~e_L
   1000012     3.88649495e+02   # ~nue_L
   1000013     3.96766593e+02   # ~mu_L
   1000014     3.88645851e+02   # ~numu_L
   1000015     2.44847842e+02   # ~stau_1
   1000016     3.87372577e+02   # ~nu_tau_L
   2000001     1.10217880e+03   # ~d_R
   2000002     1.10605651e+03   # ~u_R
   2000003     1.10217587e+03   # ~s_R
   2000004     1.10605352e+03   # ~c_R
   2000005     1.09829117e+03   # ~b_2
   2000006     1.09684446e+03   # ~t_2
   2000011     2.51946172e+02   # ~e_R
   2000013     2.51934758e+02   # ~mu_R
   2000015     3.97573680e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06320002e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96463723e-01   # N_{1,1}
  1  2    -1.47776577e-02   # N_{1,2}
  1  3     7.62531079e-02   # N_{1,3}
  1  4    -3.20489140e-02   # N_{1,4}
  2  1     3.28392049e-02   # N_{2,1}
  2  2     9.73559816e-01   # N_{2,2}
  2  3    -1.87206464e-01   # N_{2,3}
  2  4     1.26714682e-01   # N_{2,4}
  3  1    -3.04435963e-02   # N_{3,1}
  3  2     4.42376275e-02   # N_{3,2}
  3  3     7.04031973e-01   # N_{3,3}
  3  4     7.08135016e-01   # N_{3,4}
  4  1    -7.10972755e-02   # N_{4,1}
  4  2     2.23620074e-01   # N_{4,2}
  4  3     6.80792321e-01   # N_{4,3}
  4  4    -6.93873948e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.63578939e-01   # U_{1,1}
  1  2    -2.67424059e-01   # U_{1,2}
  2  1     2.67424059e-01   # U_{2,1}
  2  2     9.63578939e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.83388902e-01   # V_{1,1}
  1  2    -1.81511070e-01   # V_{1,2}
  2  1     1.81511070e-01   # V_{2,1}
  2  2     9.83388902e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.04713807e-01   # F_{11}
  1  2     9.14443402e-01   # F_{12}
  2  1     9.14443402e-01   # F_{21}
  2  2    -4.04713807e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.78897997e-01   # F_{11}
  1  2     2.04349483e-01   # F_{12}
  2  1    -2.04349483e-01   # F_{21}
  2  2     9.78897997e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.29029562e-01   # F_{11}
  1  2     9.91640748e-01   # F_{12}
  2  1     9.91640748e-01   # F_{21}
  2  2    -1.29029562e-01   # F_{22}
Block gauge Q= 9.53955807e+02  # SM gauge couplings
     1     3.62600632e-01   # g'(Q)MSSM DRbar
     2     6.42519994e-01   # g(Q)MSSM DRbar
     3     1.05630116e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.53955807e+02  
  3  3     8.58162309e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.53955807e+02  
  3  3     1.34699961e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.53955807e+02  
  3  3     1.00473882e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.53955807e+02 # Higgs mixing parameters
     1     6.85472848e+02    # mu(Q)MSSM DRbar
     2     9.66316661e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44005295e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     6.36456831e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.53955807e+02  # MSSM DRbar SUSY breaking parameters
     1     2.31219567e+02      # M_1(Q)
     2     4.28191253e+02      # M_2(Q)
     3     1.21653516e+03      # M_3(Q)
    21     1.31962406e+05      # mH1^2(Q)
    22    -4.53883530e+05      # mH2^2(Q)
    31     3.88977041e+02      # meL(Q)
    32     3.88973402e+02      # mmuL(Q)
    33     3.87874606e+02      # mtauL(Q)
    34     2.44085714e+02      # meR(Q)
    35     2.44073919e+02      # mmuR(Q)
    36     2.40490308e+02      # mtauR(Q)
    41     1.11150425e+03      # mqL1(Q)
    42     1.11150139e+03      # mqL2(Q)
    43     1.02471171e+03      # mqL3(Q)
    44     1.06947134e+03      # muR(Q)
    45     1.06946830e+03      # mcR(Q)
    46     8.80808000e+02      # mtR(Q)
    47     1.06436286e+03      # mdR(Q)
    48     1.06435988e+03      # msR(Q)
    49     1.05893579e+03      # mbR(Q)
Block au Q= 9.53955807e+02  
  1  1    -1.24227302e+03      # Au(Q)MSSM DRbar
  2  2    -1.24226747e+03      # Ac(Q)MSSM DRbar
  3  3    -9.59891784e+02      # At(Q)MSSM DRbar
Block ad Q= 9.53955807e+02  
  1  1    -1.51822759e+03      # Ad(Q)MSSM DRbar
  2  2    -1.51822244e+03      # As(Q)MSSM DRbar
  3  3    -1.41909758e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.53955807e+02  
  1  1    -3.27858552e+02      # Ae(Q)MSSM DRbar
  2  2    -3.27852697e+02      # Amu(Q)MSSM DRbar
  3  3    -3.26084507e+02      # Atau(Q)MSSM DRbar
