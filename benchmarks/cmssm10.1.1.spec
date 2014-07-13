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
     1    1.25000000e+02   # m0
     2    5.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.87397069e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=6.98753914e-04
# MX=1.87397069e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03966439e+01   # MW
        25     1.14890715e+02   # h0
        35     7.18024045e+02   # H0
        36     7.17746883e+02   # A0
        37     7.22476236e+02   # H+
   1000021     1.14697657e+03   # ~g
   1000022     2.04229990e+02   # ~neutralino(1)
   1000023     3.85953862e+02   # ~neutralino(2)
   1000024     3.85965532e+02   # ~chargino(1)
   1000025    -6.35418783e+02   # ~neutralino(3)
   1000035     6.49081836e+02   # ~neutralino(4)
   1000037     6.49407183e+02   # ~chargino(2)
   1000001     1.05534270e+03   # ~d_L
   1000002     1.05250366e+03   # ~u_L
   1000003     1.05534013e+03   # ~s_L
   1000004     1.05250108e+03   # ~c_L
   1000005     9.66107583e+02   # ~b_1
   1000006     8.04557512e+02   # ~t_1
   1000011     3.61732190e+02   # ~e_L
   1000012     3.52830133e+02   # ~nue_L
   1000013     3.61728923e+02   # ~mu_L
   1000014     3.52826786e+02   # ~numu_L
   1000015     2.22713267e+02   # ~stau_1
   1000016     3.51659167e+02   # ~nu_tau_L
   2000001     1.01074954e+03   # ~d_R
   2000002     1.01406928e+03   # ~u_R
   2000003     1.01074684e+03   # ~s_R
   2000004     1.01406653e+03   # ~c_R
   2000005     1.00746258e+03   # ~b_2
   2000006     1.01149258e+03   # ~t_2
   2000011     2.29854534e+02   # ~e_R
   2000013     2.29844099e+02   # ~mu_R
   2000015     3.62872398e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06795639e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95806098e-01   # N_{1,1}
  1  2    -1.74952848e-02   # N_{1,2}
  1  3     8.29355237e-02   # N_{1,3}
  1  4    -3.44358681e-02   # N_{1,4}
  2  1     3.81442476e-02   # N_{2,1}
  2  2     9.70405105e-01   # N_{2,2}
  2  3    -1.98316530e-01   # N_{2,3}
  2  4     1.32399027e-01   # N_{2,4}
  3  1    -3.32405136e-02   # N_{3,1}
  3  2     4.84230186e-02   # N_{3,2}
  3  3     7.03438779e-01   # N_{3,3}
  3  4     7.08324900e-01   # N_{3,4}
  4  1    -7.62253221e-02   # N_{4,1}
  4  2     2.35930197e-01   # N_{4,2}
  4  3     6.77470396e-01   # N_{4,3}
  4  4    -6.92503072e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.58915128e-01   # U_{1,1}
  1  2    -2.83693104e-01   # U_{1,2}
  2  1     2.83693104e-01   # U_{2,1}
  2  2     9.58915128e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.81791794e-01   # V_{1,1}
  1  2    -1.89960190e-01   # V_{1,2}
  2  1     1.89960190e-01   # V_{2,1}
  2  2     9.81791794e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.26562903e-01   # F_{11}
  1  2     9.04457898e-01   # F_{12}
  2  1     9.04457898e-01   # F_{21}
  2  2    -4.26562903e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.75802538e-01   # F_{11}
  1  2     2.18653623e-01   # F_{12}
  2  1    -2.18653623e-01   # F_{21}
  2  2     9.75802538e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.42056037e-01   # F_{11}
  1  2     9.89858617e-01   # F_{12}
  2  1     9.89858617e-01   # F_{21}
  2  2    -1.42056037e-01   # F_{22}
Block gauge Q= 8.74650592e+02  # SM gauge couplings
     1     3.62418838e-01   # g'(Q)MSSM DRbar
     2     6.43002750e-01   # g(Q)MSSM DRbar
     3     1.06092721e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.74650592e+02  
  3  3     8.61186165e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.74650592e+02  
  3  3     1.35309488e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.74650592e+02  
  3  3     1.00533808e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.74650592e+02 # Higgs mixing parameters
     1     6.29931542e+02    # mu(Q)MSSM DRbar
     2     9.67352073e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44108728e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     5.34463357e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.74650592e+02  # MSSM DRbar SUSY breaking parameters
     1     2.09311195e+02      # M_1(Q)
     2     3.88509034e+02      # M_2(Q)
     3     1.11339800e+03      # M_3(Q)
    21     1.09122241e+05      # mH1^2(Q)
    22    -3.84359126e+05      # mH2^2(Q)
    31     3.54224755e+02      # meL(Q)
    32     3.54221423e+02      # mmuL(Q)
    33     3.53216087e+02      # mtauL(Q)
    34     2.22002006e+02      # meR(Q)
    35     2.21991190e+02      # mmuR(Q)
    36     2.18708191e+02      # mtauR(Q)
    41     1.01835260e+03      # mqL1(Q)
    42     1.01834998e+03      # mqL2(Q)
    43     9.38585570e+02      # mqL3(Q)
    44     9.80337407e+02      # muR(Q)
    45     9.80334617e+02      # mcR(Q)
    46     8.07037794e+02      # mtR(Q)
    47     9.75738733e+02      # mdR(Q)
    48     9.75735991e+02      # msR(Q)
    49     9.70732212e+02      # mbR(Q)
Block au Q= 8.74650592e+02  
  1  1    -1.14073241e+03      # Au(Q)MSSM DRbar
  2  2    -1.14072729e+03      # Ac(Q)MSSM DRbar
  3  3    -8.80143420e+02      # At(Q)MSSM DRbar
Block ad Q= 8.74650592e+02  
  1  1    -1.39567007e+03      # Ad(Q)MSSM DRbar
  2  2    -1.39566532e+03      # As(Q)MSSM DRbar
  3  3    -1.30417812e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.74650592e+02  
  1  1    -2.99341366e+02      # Ae(Q)MSSM DRbar
  2  2    -2.99335989e+02      # Amu(Q)MSSM DRbar
  3  3    -2.97714107e+02      # Atau(Q)MSSM DRbar
