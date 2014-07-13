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
     1    4.00000000e+02   # m0
     2    6.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.83946879e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.10689875e-04
# MX=1.83946879e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03937844e+01   # MW
        25     1.16160916e+02   # h0
        35     9.23283242e+02   # H0
        36     9.22981651e+02   # A0
        37     9.26814172e+02   # H+
   1000021     1.36684188e+03   # ~g
   1000022     2.48797165e+02   # ~neutralino(1)
   1000023     4.70792369e+02   # ~neutralino(2)
   1000024     4.70853975e+02   # ~chargino(1)
   1000025    -7.45331123e+02   # ~neutralino(3)
   1000035     7.57876660e+02   # ~neutralino(4)
   1000037     7.58102601e+02   # ~chargino(2)
   1000001     1.29906504e+03   # ~d_L
   1000002     1.29679731e+03   # ~u_L
   1000003     1.29906169e+03   # ~s_L
   1000004     1.29679395e+03   # ~c_L
   1000005     1.18104840e+03   # ~b_1
   1000006     9.85310084e+02   # ~t_1
   1000011     5.67741386e+02   # ~e_L
   1000012     5.61992227e+02   # ~nue_L
   1000013     5.67735099e+02   # ~mu_L
   1000014     5.61985880e+02   # ~numu_L
   1000015     4.53530042e+02   # ~stau_1
   1000016     5.59923730e+02   # ~nu_tau_L
   2000001     1.24817988e+03   # ~d_R
   2000002     1.25239710e+03   # ~u_R
   2000003     1.24817642e+03   # ~s_R
   2000004     1.25239349e+03   # ~c_R
   2000005     1.24251756e+03   # ~b_2
   2000006     1.21665073e+03   # ~t_2
   2000011     4.60309560e+02   # ~e_R
   2000013     4.60293853e+02   # ~mu_R
   2000015     5.67110151e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05593805e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96942599e-01   # N_{1,1}
  1  2    -1.26891031e-02   # N_{1,2}
  1  3     7.09227493e-02   # N_{1,3}
  1  4    -3.02391153e-02   # N_{1,4}
  2  1     2.88549212e-02   # N_{2,1}
  2  2     9.75790072e-01   # N_{2,2}
  2  3    -1.78665362e-01   # N_{2,3}
  2  4     1.22799910e-01   # N_{2,4}
  3  1    -2.81250837e-02   # N_{3,1}
  3  2     4.07259732e-02   # N_{3,2}
  3  3     7.04493698e-01   # N_{3,3}
  3  4     7.07982347e-01   # N_{3,4}
  4  1    -6.69464487e-02   # N_{4,1}
  4  2     2.14509016e-01   # N_{4,2}
  4  3     6.83181734e-01   # N_{4,3}
  4  4    -6.94814201e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.66792587e-01   # U_{1,1}
  1  2    -2.55562309e-01   # U_{1,2}
  2  1     2.55562309e-01   # U_{2,1}
  2  2     9.66792587e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.84338131e-01   # V_{1,1}
  1  2    -1.76290792e-01   # V_{1,2}
  2  1     1.76290792e-01   # V_{2,1}
  2  2     9.84338131e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.57643746e-01   # F_{11}
  1  2     9.33858100e-01   # F_{12}
  2  1     9.33858100e-01   # F_{21}
  2  2    -3.57643746e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.90455474e-01   # F_{11}
  1  2     1.37833064e-01   # F_{12}
  2  1    -1.37833064e-01   # F_{21}
  2  2     9.90455474e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.17353331e-01   # F_{11}
  1  2     9.93090225e-01   # F_{12}
  2  1     9.93090225e-01   # F_{21}
  2  2    -1.17353331e-01   # F_{22}
Block gauge Q= 1.06239732e+03  # SM gauge couplings
     1     3.62643976e-01   # g'(Q)MSSM DRbar
     2     6.41805737e-01   # g(Q)MSSM DRbar
     3     1.05103316e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.06239732e+03  
  3  3     8.55048363e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.06239732e+03  
  3  3     1.34168347e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.06239732e+03  
  3  3     1.00302201e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.06239732e+03 # Higgs mixing parameters
     1     7.39583143e+02    # mu(Q)MSSM DRbar
     2     9.65005030e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43858853e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     8.79931924e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.06239732e+03  # MSSM DRbar SUSY breaking parameters
     1     2.53306381e+02      # M_1(Q)
     2     4.68050035e+02      # M_2(Q)
     3     1.31801370e+03      # M_3(Q)
    21     2.88434503e+05      # mH1^2(Q)
    22    -5.24233617e+05      # mH2^2(Q)
    31     5.61678089e+02      # meL(Q)
    32     5.61671719e+02      # mmuL(Q)
    33     5.59747406e+02      # mtauL(Q)
    34     4.55804864e+02      # meR(Q)
    35     4.55789006e+02      # mmuR(Q)
    36     4.50980968e+02      # mtauR(Q)
    41     1.25607355e+03      # mqL1(Q)
    42     1.25607012e+03      # mqL2(Q)
    43     1.14766546e+03      # mqL3(Q)
    44     1.21245302e+03      # muR(Q)
    45     1.21244934e+03      # mcR(Q)
    46     9.76379718e+02      # mtR(Q)
    47     1.20714919e+03      # mdR(Q)
    48     1.20714566e+03      # msR(Q)
    49     1.20066117e+03      # mbR(Q)
Block au Q= 1.06239732e+03  
  1  1    -1.34098822e+03      # Au(Q)MSSM DRbar
  2  2    -1.34098225e+03      # Ac(Q)MSSM DRbar
  3  3    -1.03739517e+03      # At(Q)MSSM DRbar
Block ad Q= 1.06239732e+03  
  1  1    -1.63731824e+03      # Ad(Q)MSSM DRbar
  2  2    -1.63731272e+03      # As(Q)MSSM DRbar
  3  3    -1.53074676e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.06239732e+03  
  1  1    -3.56143320e+02      # Ae(Q)MSSM DRbar
  2  2    -3.56136993e+02      # Amu(Q)MSSM DRbar
  3  3    -3.54227896e+02      # Atau(Q)MSSM DRbar
