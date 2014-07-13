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
     1    2.25000000e+02   # m0
     2    5.50000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.84678132e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=8.70324599e-04
# MX=1.84678132e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03950921e+01   # MW
        25     1.15549978e+02   # h0
        35     8.03090161e+02   # H0
        36     8.02828833e+02   # A0
        37     8.07096001e+02   # H+
   1000021     1.25474382e+03   # ~g
   1000022     2.26322387e+02   # ~neutralino(1)
   1000023     4.28040727e+02   # ~neutralino(2)
   1000024     4.28082072e+02   # ~chargino(1)
   1000025    -6.90977795e+02   # ~neutralino(3)
   1000035     7.03992097e+02   # ~neutralino(4)
   1000037     7.04268254e+02   # ~chargino(2)
   1000001     1.16475381e+03   # ~d_L
   1000002     1.16219940e+03   # ~u_L
   1000003     1.16475092e+03   # ~s_L
   1000004     1.16219651e+03   # ~c_L
   1000005     1.06445448e+03   # ~b_1
   1000006     8.88690427e+02   # ~t_1
   1000011     4.34554128e+02   # ~e_L
   1000012     4.27134174e+02   # ~nue_L
   1000013     4.34549862e+02   # ~mu_L
   1000014     4.27129837e+02   # ~numu_L
   1000015     3.01535051e+02   # ~stau_1
   1000016     4.25661726e+02   # ~nu_tau_L
   2000001     1.11633696e+03   # ~d_R
   2000002     1.12016846e+03   # ~u_R
   2000003     1.11633395e+03   # ~s_R
   2000004     1.12016537e+03   # ~c_R
   2000005     1.11207729e+03   # ~b_2
   2000006     1.10554808e+03   # ~t_2
   2000011     3.08208835e+02   # ~e_R
   2000013     3.08196622e+02   # ~mu_R
   2000015     4.34978009e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06183153e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96456134e-01   # N_{1,1}
  1  2    -1.47835454e-02   # N_{1,2}
  1  3     7.63243889e-02   # N_{1,3}
  1  4    -3.21124164e-02   # N_{1,4}
  2  1     3.28907363e-02   # N_{2,1}
  2  2     9.73482605e-01   # N_{2,2}
  2  3    -1.87431944e-01   # N_{2,3}
  2  4     1.26960956e-01   # N_{2,4}
  3  1    -3.04492072e-02   # N_{3,1}
  3  2     4.42276110e-02   # N_{3,2}
  3  3     7.04034457e-01   # N_{3,3}
  3  4     7.08132930e-01   # N_{3,4}
  4  1    -7.11773706e-02   # N_{4,1}
  4  2     2.23957549e-01   # N_{4,2}
  4  3     6.80719720e-01   # N_{4,3}
  4  4    -6.93828121e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.63400306e-01   # U_{1,1}
  1  2    -2.68066876e-01   # U_{1,2}
  2  1     2.68066876e-01   # U_{2,1}
  2  2     9.63400306e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.83264882e-01   # V_{1,1}
  1  2    -1.82181700e-01   # V_{1,2}
  2  1     1.82181700e-01   # V_{2,1}
  2  2     9.83264882e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.97150487e-01   # F_{11}
  1  2     9.17753502e-01   # F_{12}
  2  1     9.17753502e-01   # F_{21}
  2  2    -3.97150487e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.82676946e-01   # F_{11}
  1  2     1.85326790e-01   # F_{12}
  2  1    -1.85326790e-01   # F_{21}
  2  2     9.82676946e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.28724603e-01   # F_{11}
  1  2     9.91680380e-01   # F_{12}
  2  1     9.91680380e-01   # F_{21}
  2  2    -1.28724603e-01   # F_{22}
Block gauge Q= 9.61499518e+02  # SM gauge couplings
     1     3.62546416e-01   # g'(Q)MSSM DRbar
     2     6.42427804e-01   # g(Q)MSSM DRbar
     3     1.05598973e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.61499518e+02  
  3  3     8.58048322e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.61499518e+02  
  3  3     1.34704873e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.61499518e+02  
  3  3     1.00461676e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.61499518e+02 # Higgs mixing parameters
     1     6.85470488e+02    # mu(Q)MSSM DRbar
     2     9.66211721e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43991016e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     6.67573460e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.61499518e+02  # MSSM DRbar SUSY breaking parameters
     1     2.31222588e+02      # M_1(Q)
     2     4.28205314e+02      # M_2(Q)
     3     1.21637149e+03      # M_3(Q)
    21     1.62293805e+05      # mH1^2(Q)
    22    -4.53186536e+05      # mH2^2(Q)
    31     4.27415559e+02      # meL(Q)
    32     4.27411212e+02      # mmuL(Q)
    33     4.26098183e+02      # mtauL(Q)
    34     3.01932425e+02      # meR(Q)
    35     3.01919948e+02      # mmuR(Q)
    36     2.98132237e+02      # mtauR(Q)
    41     1.12481306e+03      # mqL1(Q)
    42     1.12481011e+03      # mqL2(Q)
    43     1.03424098e+03      # mqL3(Q)
    44     1.08341272e+03      # muR(Q)
    45     1.08340958e+03      # mcR(Q)
    46     8.86461815e+02      # mtR(Q)
    47     1.07838689e+03      # mdR(Q)
    48     1.07838383e+03      # msR(Q)
    49     1.07279248e+03      # mbR(Q)
Block au Q= 9.61499518e+02  
  1  1    -1.24195613e+03      # Au(Q)MSSM DRbar
  2  2    -1.24195058e+03      # Ac(Q)MSSM DRbar
  3  3    -9.59582489e+02      # At(Q)MSSM DRbar
Block ad Q= 9.61499518e+02  
  1  1    -1.51788948e+03      # Ad(Q)MSSM DRbar
  2  2    -1.51788434e+03      # As(Q)MSSM DRbar
  3  3    -1.41875994e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.61499518e+02  
  1  1    -3.27866433e+02      # Ae(Q)MSSM DRbar
  2  2    -3.27860577e+02      # Amu(Q)MSSM DRbar
  3  3    -3.26092245e+02      # Atau(Q)MSSM DRbar
