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
     1    3.45000000e+02   # m0
     2    5.50000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.81391363e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=8.77354589e-04
# MX=1.81391363e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03898654e+01   # MW
        25     1.17473403e+02   # h0
        35     6.59526515e+02   # H0
        36     6.59531474e+02   # A0
        37     6.64751752e+02   # H+
   1000021     1.25838616e+03   # ~g
   1000022     2.28730132e+02   # ~neutralino(1)
   1000023     4.35809446e+02   # ~neutralino(2)
   1000024     4.35942428e+02   # ~chargino(1)
   1000025    -7.56036436e+02   # ~neutralino(3)
   1000035     7.63937135e+02   # ~neutralino(4)
   1000037     7.65010200e+02   # ~chargino(2)
   1000001     1.19426740e+03   # ~d_L
   1000002     1.19173226e+03   # ~u_L
   1000003     1.19423252e+03   # ~s_L
   1000004     1.19169729e+03   # ~c_L
   1000005     9.98885123e+02   # ~b_1
   1000006     8.55785669e+02   # ~t_1
   1000011     5.06813291e+02   # ~e_L
   1000012     5.00297358e+02   # ~nue_L
   1000013     5.06676350e+02   # ~mu_L
   1000014     5.00158756e+02   # ~numu_L
   1000015     2.30231004e+02   # ~stau_1
   1000016     4.52825676e+02   # ~nu_tau_L
   2000001     1.14726375e+03   # ~d_R
   2000002     1.15095715e+03   # ~u_R
   2000003     1.14719442e+03   # ~s_R
   2000004     1.15095278e+03   # ~c_R
   2000005     1.06616759e+03   # ~b_2
   2000006     1.07144361e+03   # ~t_2
   2000011     4.04032464e+02   # ~e_R
   2000013     4.03683864e+02   # ~mu_R
   2000015     4.81573576e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60821188e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97489970e-01   # N_{1,1}
  1  2    -8.89519843e-03   # N_{1,2}
  1  3     6.66721968e-02   # N_{1,3}
  1  4    -2.21236082e-02   # N_{1,4}
  2  1     2.11216189e-02   # N_{2,1}
  2  2     9.83535782e-01   # N_{2,2}
  2  3    -1.54447894e-01   # N_{2,3}
  2  4     9.14171224e-02   # N_{2,4}
  3  1    -3.09642357e-02   # N_{3,1}
  3  2     4.54558082e-02   # N_{3,2}
  3  3     7.04210037e-01   # N_{3,3}
  3  4     7.07858185e-01   # N_{3,4}
  4  1    -6.00737358e-02   # N_{4,1}
  4  2     1.74676873e-01   # N_{4,2}
  4  3     6.89774521e-01   # N_{4,3}
  4  4    -7.00064458e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.75524740e-01   # U_{1,1}
  1  2    -2.19889703e-01   # U_{1,2}
  2  1     2.19889703e-01   # U_{2,1}
  2  2     9.75524740e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91434416e-01   # V_{1,1}
  1  2    -1.30605508e-01   # V_{1,2}
  2  1     1.30605508e-01   # V_{2,1}
  2  2     9.91434416e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.53851990e-01   # F_{11}
  1  2     8.91077085e-01   # F_{12}
  2  1     8.91077085e-01   # F_{21}
  2  2    -4.53851990e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.11943210e-01   # F_{11}
  1  2     5.83736434e-01   # F_{12}
  2  1    -5.83736434e-01   # F_{21}
  2  2     8.11943210e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     3.36919511e-01   # F_{11}
  1  2     9.41533453e-01   # F_{12}
  2  1     9.41533453e-01   # F_{21}
  2  2    -3.36919511e-01   # F_{22}
Block gauge Q= 9.30216098e+02  # SM gauge couplings
     1     3.62334672e-01   # g'(Q)MSSM DRbar
     2     6.41902540e-01   # g(Q)MSSM DRbar
     3     1.05658757e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.30216098e+02  
  3  3     8.53304105e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.30216098e+02  
  3  3     4.90713421e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.30216098e+02  
  3  3     4.27631619e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.30216098e+02 # Higgs mixing parameters
     1     7.52814468e+02    # mu(Q)MSSM DRbar
     2     3.92129120e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43906725e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     5.49749739e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.30216098e+02  # MSSM DRbar SUSY breaking parameters
     1     2.32434394e+02      # M_1(Q)
     2     4.30638381e+02      # M_2(Q)
     3     1.22094983e+03      # M_3(Q)
    21    -1.31720107e+05      # mH1^2(Q)
    22    -5.58045893e+05      # mH2^2(Q)
    31     5.00868951e+02      # meL(Q)
    32     5.00730002e+02      # mmuL(Q)
    33     4.56287180e+02      # mtauL(Q)
    34     3.99322101e+02      # meR(Q)
    35     3.98969413e+02      # mmuR(Q)
    36     2.69759356e+02      # mtauR(Q)
    41     1.15646500e+03      # mqL1(Q)
    42     1.15642940e+03      # mqL2(Q)
    43     9.94488661e+02      # mqL3(Q)
    44     1.11628189e+03      # muR(Q)
    45     1.11627744e+03      # mcR(Q)
    46     8.65715658e+02      # mtR(Q)
    47     1.11145161e+03      # mdR(Q)
    48     1.11138110e+03      # msR(Q)
    49     1.01171485e+03      # mbR(Q)
Block au Q= 9.30216098e+02  
  1  1    -1.58553608e+03      # Au(Q)MSSM DRbar
  2  2    -1.58549778e+03      # Ac(Q)MSSM DRbar
  3  3    -1.10088821e+03      # At(Q)MSSM DRbar
Block ad Q= 9.30216098e+02  
  1  1    -1.83989873e+03      # Ad(Q)MSSM DRbar
  2  2    -1.83980119e+03      # As(Q)MSSM DRbar
  3  3    -1.54940628e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.30216098e+02  
  1  1    -6.45854191e+02      # Ae(Q)MSSM DRbar
  2  2    -6.45533854e+02      # Amu(Q)MSSM DRbar
  3  3    -5.38360870e+02      # Atau(Q)MSSM DRbar
