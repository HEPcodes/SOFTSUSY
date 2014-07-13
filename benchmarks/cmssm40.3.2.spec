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
     1    1.05000000e+03   # m0
     2    3.75000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.21528516e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=2.93431609e-04
# MX=2.21528516e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03927721e+01   # MW
        25     1.15871809e+02   # h0
        35     8.20817363e+02   # H0
        36     8.20943217e+02   # A0
        37     8.25022272e+02   # H+
   1000021     9.32886808e+02   # ~g
   1000022     1.55779624e+02   # ~neutralino(1)
   1000023     2.97728823e+02   # ~neutralino(2)
   1000024     2.97820260e+02   # ~chargino(1)
   1000025    -5.48133823e+02   # ~neutralino(3)
   1000035     5.58690511e+02   # ~neutralino(4)
   1000037     5.60058414e+02   # ~chargino(2)
   1000001     1.30092486e+03   # ~d_L
   1000002     1.29861768e+03   # ~u_L
   1000003     1.30087838e+03   # ~s_L
   1000004     1.29857112e+03   # ~c_L
   1000005     1.01243537e+03   # ~b_1
   1000006     8.34107381e+02   # ~t_1
   1000011     1.07656018e+03   # ~e_L
   1000012     1.07327753e+03   # ~nue_L
   1000013     1.07629007e+03   # ~mu_L
   1000014     1.07300666e+03   # ~numu_L
   1000015     8.66222766e+02   # ~stau_1
   1000016     9.84989161e+02   # ~nu_tau_L
   2000001     1.28362164e+03   # ~d_R
   2000002     1.28434693e+03   # ~u_R
   2000003     1.28353286e+03   # ~s_R
   2000004     1.28434090e+03   # ~c_R
   2000005     1.13033047e+03   # ~b_2
   2000006     1.04801243e+03   # ~t_2
   2000011     1.05896007e+03   # ~e_R
   2000013     1.05840882e+03   # ~mu_R
   2000015     9.92057517e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60006920e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95179929e-01   # N_{1,1}
  1  2    -1.63435891e-02   # N_{1,2}
  1  3     9.22831813e-02   # N_{1,3}
  1  4    -2.88723077e-02   # N_{1,4}
  2  1     3.77711954e-02   # N_{2,1}
  2  2     9.72628140e-01   # N_{2,2}
  2  3    -1.99987618e-01   # N_{2,3}
  2  4     1.12128459e-01   # N_{2,4}
  3  1    -4.34462254e-02   # N_{3,1}
  3  2     6.42677826e-02   # N_{3,2}
  3  3     7.01538659e-01   # N_{3,3}
  3  4     7.08396490e-01   # N_{3,4}
  4  1    -7.93893626e-02   # N_{4,1}
  4  2     2.22703931e-01   # N_{4,2}
  4  3     6.77740568e-01   # N_{4,3}
  4  4    -6.96252835e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.58373505e-01   # U_{1,1}
  1  2    -2.85517469e-01   # U_{1,2}
  2  1     2.85517469e-01   # U_{2,1}
  2  2     9.58373505e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.87012566e-01   # V_{1,1}
  1  2    -1.60643068e-01   # V_{1,2}
  2  1     1.60643068e-01   # V_{2,1}
  2  2     9.87012566e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.29838795e-01   # F_{11}
  1  2     9.44037271e-01   # F_{12}
  2  1     9.44037271e-01   # F_{21}
  2  2    -3.29838795e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.80174054e-01   # F_{11}
  1  2     1.98138393e-01   # F_{12}
  2  1    -1.98138393e-01   # F_{21}
  2  2     9.80174054e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.73876140e-01   # F_{11}
  1  2     9.84767530e-01   # F_{12}
  2  1     9.84767530e-01   # F_{21}
  2  2    -1.73876140e-01   # F_{22}
Block gauge Q= 9.12890031e+02  # SM gauge couplings
     1     3.61907590e-01   # g'(Q)MSSM DRbar
     2     6.42508667e-01   # g(Q)MSSM DRbar
     3     1.06238014e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.12890031e+02  
  3  3     8.59694612e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.12890031e+02  
  3  3     5.18198547e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.12890031e+02  
  3  3     4.12628306e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.12890031e+02 # Higgs mixing parameters
     1     5.40233347e+02    # mu(Q)MSSM DRbar
     2     3.92445257e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43801230e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     8.12162023e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.12890031e+02  # MSSM DRbar SUSY breaking parameters
     1     1.57594201e+02      # M_1(Q)
     2     2.93241627e+02      # M_2(Q)
     3     8.41485531e+02      # M_3(Q)
    21     4.01194362e+05      # mH1^2(Q)
    22    -2.81385586e+05      # mH2^2(Q)
    31     1.07387016e+03      # meL(Q)
    32     1.07360015e+03      # mmuL(Q)
    33     9.87769842e+02      # mtauL(Q)
    34     1.05690281e+03      # meR(Q)
    35     1.05635130e+03      # mmuR(Q)
    36     8.71480769e+02      # mtauR(Q)
    41     1.27743156e+03      # mqL1(Q)
    42     1.27738431e+03      # mqL2(Q)
    43     9.97612478e+02      # mqL3(Q)
    44     1.26393994e+03      # muR(Q)
    45     1.26393380e+03      # mcR(Q)
    46     8.23576918e+02      # mtR(Q)
    47     1.26246372e+03      # mdR(Q)
    48     1.26237334e+03      # msR(Q)
    49     1.10701323e+03      # mbR(Q)
Block au Q= 9.12890031e+02  
  1  1    -1.19820768e+03      # Au(Q)MSSM DRbar
  2  2    -1.19817691e+03      # Ac(Q)MSSM DRbar
  3  3    -7.99688474e+02      # At(Q)MSSM DRbar
Block ad Q= 9.12890031e+02  
  1  1    -1.39279023e+03      # Ad(Q)MSSM DRbar
  2  2    -1.39271189e+03      # As(Q)MSSM DRbar
  3  3    -1.14454311e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.12890031e+02  
  1  1    -5.62786321e+02      # Ae(Q)MSSM DRbar
  2  2    -5.62490995e+02      # Amu(Q)MSSM DRbar
  3  3    -4.70748774e+02      # Atau(Q)MSSM DRbar
