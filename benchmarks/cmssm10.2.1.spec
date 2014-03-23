# SOFTSUSY3.4.0 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.0       # version number
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
     1    2.00000000e+02   # m0
     2    5.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.90436443e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=6.91612842e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03961812e+01   # MW
        25     1.14915158e+02   # h0
        35     7.34344471e+02   # H0
        36     7.34055012e+02   # A0
        37     7.38710878e+02   # H+
   1000021     1.14926200e+03   # ~g
   1000022     2.04560121e+02   # ~neutralino(1)
   1000023     3.86569183e+02   # ~neutralino(2)
   1000024     3.86581562e+02   # ~chargino(1)
   1000025    -6.35557078e+02   # ~neutralino(3)
   1000035     6.49236413e+02   # ~neutralino(4)
   1000037     6.49557636e+02   # ~chargino(2)
   1000001     1.06658695e+03   # ~d_L
   1000002     1.06378142e+03   # ~u_L
   1000003     1.06658431e+03   # ~s_L
   1000004     1.06377876e+03   # ~c_L
   1000005     9.74449346e+02   # ~b_1
   1000006     8.10438839e+02   # ~t_1
   1000011     3.93674418e+02   # ~e_L
   1000012     3.85495586e+02   # ~nue_L
   1000013     3.93670560e+02   # ~mu_L
   1000014     3.85491649e+02   # ~numu_L
   1000015     2.70926592e+02   # ~stau_1
   1000016     3.84159963e+02   # ~nu_tau_L
   2000001     1.02261636e+03   # ~d_R
   2000002     1.02590032e+03   # ~u_R
   2000003     1.02261360e+03   # ~s_R
   2000004     1.02589749e+03   # ~c_R
   2000005     1.01898771e+03   # ~b_2
   2000006     1.01866248e+03   # ~t_2
   2000011     2.77579867e+02   # ~e_R
   2000013     2.77568756e+02   # ~mu_R
   2000015     3.94458918e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06643937e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95799213e-01   # N_{1,1}
  1  2    -1.74977221e-02   # N_{1,2}
  1  3     8.29946659e-02   # N_{1,3}
  1  4    -3.44912095e-02   # N_{1,4}
  2  1     3.81852870e-02   # N_{2,1}
  2  2     9.70343793e-01   # N_{2,2}
  2  3    -1.98481637e-01   # N_{2,3}
  2  4     1.32589018e-01   # N_{2,4}
  3  1    -3.32436327e-02   # N_{3,1}
  3  2     4.84096201e-02   # N_{3,2}
  3  3     7.03442054e-01   # N_{3,3}
  3  4     7.08322417e-01   # N_{3,4}
  4  1    -7.62933360e-02   # N_{4,1}
  4  2     2.36184805e-01   # N_{4,2}
  4  3     6.77411398e-01   # N_{4,3}
  4  4    -6.92466506e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.58757474e-01   # U_{1,1}
  1  2    -2.84225448e-01   # U_{1,2}
  2  1     2.84225448e-01   # U_{2,1}
  2  2     9.58757474e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.81681952e-01   # V_{1,1}
  1  2    -1.90527018e-01   # V_{1,2}
  2  1     1.90527018e-01   # V_{2,1}
  2  2     9.81681952e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.19838529e-01   # F_{11}
  1  2     9.07598816e-01   # F_{12}
  2  1     9.07598816e-01   # F_{21}
  2  2    -4.19838529e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.79705023e-01   # F_{11}
  1  2     2.00444676e-01   # F_{12}
  2  1    -2.00444676e-01   # F_{21}
  2  2     9.79705023e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.41740964e-01   # F_{11}
  1  2     9.89903783e-01   # F_{12}
  2  1     9.89903783e-01   # F_{21}
  2  2    -1.41740964e-01   # F_{22}
Block gauge Q= 8.80961234e+02  # SM gauge couplings
     1     3.62367711e-01   # g'(Q)MSSM DRbar
     2     6.42915588e-01   # g(Q)MSSM DRbar
     3     1.06063788e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.80961234e+02  
  3  3     8.61079306e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.80961234e+02  
  3  3     1.35327504e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.80961234e+02  
  3  3     1.00504610e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.80961234e+02 # Higgs mixing parameters
     1     6.30002464e+02    # mu(Q)MSSM DRbar
     2     9.67255686e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44095808e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     5.58453133e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.80961234e+02  # MSSM DRbar SUSY breaking parameters
     1     2.09313876e+02      # M_1(Q)
     2     3.88521131e+02      # M_2(Q)
     3     1.11326214e+03      # M_3(Q)
    21     1.32421915e+05      # mH1^2(Q)
    22    -3.83913736e+05      # mH2^2(Q)
    31     3.86766802e+02      # meL(Q)
    32     3.86762867e+02      # mmuL(Q)
    33     3.85575765e+02      # mtauL(Q)
    34     2.71213473e+02      # meR(Q)
    35     2.71202092e+02      # mmuR(Q)
    36     2.67751434e+02      # mtauR(Q)
    41     1.02951508e+03      # mqL1(Q)
    42     1.02951238e+03      # mqL2(Q)
    43     9.46561392e+02      # mqL3(Q)
    44     9.92026020e+02      # muR(Q)
    45     9.92023143e+02      # mcR(Q)
    46     8.11739873e+02      # mtR(Q)
    47     9.87495764e+02      # mdR(Q)
    48     9.87492952e+02      # msR(Q)
    49     9.82347002e+02      # mbR(Q)
Block au Q= 8.80961234e+02  
  1  1    -1.14046732e+03      # Au(Q)MSSM DRbar
  2  2    -1.14046220e+03      # Ac(Q)MSSM DRbar
  3  3    -8.79883074e+02      # At(Q)MSSM DRbar
Block ad Q= 8.80961234e+02  
  1  1    -1.39538694e+03      # Ad(Q)MSSM DRbar
  2  2    -1.39538220e+03      # As(Q)MSSM DRbar
  3  3    -1.30389363e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.80961234e+02  
  1  1    -2.99346732e+02      # Ae(Q)MSSM DRbar
  2  2    -2.99341354e+02      # Amu(Q)MSSM DRbar
  3  3    -2.97719925e+02      # Atau(Q)MSSM DRbar
