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
     1    5.50000000e+02   # m0
     2    4.50000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.02197931e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=7.41179761e-04
# MX=2.02197931e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03910855e+01   # MW
        25     1.16557355e+02   # h0
        35     6.30968553e+02   # H0
        36     6.30940542e+02   # A0
        37     6.36478918e+02   # H+
   1000021     1.06318953e+03   # ~g
   1000022     1.86425623e+02   # ~neutralino(1)
   1000023     3.55657107e+02   # ~neutralino(2)
   1000024     3.55774185e+02   # ~chargino(1)
   1000025    -6.44995656e+02   # ~neutralino(3)
   1000035     6.53679669e+02   # ~neutralino(4)
   1000037     6.54959509e+02   # ~chargino(2)
   1000001     1.09460447e+03   # ~d_L
   1000002     1.09186747e+03   # ~u_L
   1000003     1.09456947e+03   # ~s_L
   1000004     1.09183237e+03   # ~c_L
   1000005     8.95297069e+02   # ~b_1
   1000006     7.50184937e+02   # ~t_1
   1000011     6.27371873e+02   # ~e_L
   1000012     6.21995098e+02   # ~nue_L
   1000013     6.27202263e+02   # ~mu_L
   1000014     6.21824130e+02   # ~numu_L
   1000015     4.23327976e+02   # ~stau_1
   1000016     5.64264364e+02   # ~nu_tau_L
   2000001     1.06129824e+03   # ~d_R
   2000002     1.06354042e+03   # ~u_R
   2000003     1.06122956e+03   # ~s_R
   2000004     1.06353601e+03   # ~c_R
   2000005     9.69682035e+02   # ~b_2
   2000006     9.60087913e+02   # ~t_2
   2000011     5.76242642e+02   # ~e_R
   2000013     5.75870136e+02   # ~mu_R
   2000015     5.84014563e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60619969e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96575627e-01   # N_{1,1}
  1  2    -1.21174585e-02   # N_{1,2}
  1  3     7.79432380e-02   # N_{1,3}
  1  4    -2.47999873e-02   # N_{1,4}
  2  1     2.78878509e-02   # N_{2,1}
  2  2     9.79610375e-01   # N_{2,2}
  2  3    -1.73020895e-01   # N_{2,3}
  2  4     9.82321326e-02   # N_{2,4}
  3  1    -3.67056361e-02   # N_{3,1}
  3  2     5.42117821e-02   # N_{3,2}
  3  3     7.03052285e-01   # N_{3,3}
  3  4     7.08118114e-01   # N_{3,4}
  4  1    -6.86438968e-02   # N_{4,1}
  4  2     1.93074504e-01   # N_{4,2}
  4  3     6.85351082e-01   # N_{4,3}
  4  4    -6.98787625e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.69101005e-01   # U_{1,1}
  1  2    -2.46664229e-01   # U_{1,2}
  2  1     2.46664229e-01   # U_{2,1}
  2  2     9.69101005e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.90069264e-01   # V_{1,1}
  1  2    -1.40580413e-01   # V_{1,2}
  2  1     1.40580413e-01   # V_{2,1}
  2  2     9.90069264e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.51797262e-01   # F_{11}
  1  2     8.92120639e-01   # F_{12}
  2  1     8.92120639e-01   # F_{21}
  2  2    -4.51797262e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.88924319e-01   # F_{11}
  1  2     4.58054095e-01   # F_{12}
  2  1    -4.58054095e-01   # F_{21}
  2  2     8.88924319e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     3.13495411e-01   # F_{11}
  1  2     9.49589715e-01   # F_{12}
  2  1     9.49589715e-01   # F_{21}
  2  2    -3.13495411e-01   # F_{22}
Block gauge Q= 8.23120276e+02  # SM gauge couplings
     1     3.61863522e-01   # g'(Q)MSSM DRbar
     2     6.42453073e-01   # g(Q)MSSM DRbar
     3     1.06387650e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.23120276e+02  
  3  3     8.58488372e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.23120276e+02  
  3  3     4.97257523e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.23120276e+02  
  3  3     4.23649988e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.23120276e+02 # Higgs mixing parameters
     1     6.40361760e+02    # mu(Q)MSSM DRbar
     2     3.92489531e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44080496e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     5.09580503e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.23120276e+02  # MSSM DRbar SUSY breaking parameters
     1     1.88921479e+02      # M_1(Q)
     2     3.51466927e+02      # M_2(Q)
     3     1.01087107e+03      # M_3(Q)
    21    -2.98277555e+03      # mH1^2(Q)
    22    -4.04648880e+05      # mH2^2(Q)
    31     6.23756053e+02      # meL(Q)
    32     6.23585505e+02      # mmuL(Q)
    33     5.68099637e+02      # mtauL(Q)
    34     5.73354044e+02      # meR(Q)
    35     5.72980062e+02      # mmuR(Q)
    36     4.41201070e+02      # mtauR(Q)
    41     1.06299393e+03      # mqL1(Q)
    42     1.06295767e+03      # mqL2(Q)
    43     8.85967073e+02      # mqL3(Q)
    44     1.03452757e+03      # muR(Q)
    45     1.03452301e+03      # mcR(Q)
    46     7.58309564e+02      # mtR(Q)
    47     1.03117963e+03      # mdR(Q)
    48     1.03110862e+03      # msR(Q)
    49     9.26499545e+02      # mbR(Q)
Block au Q= 8.23120276e+02  
  1  1    -1.37478604e+03      # Au(Q)MSSM DRbar
  2  2    -1.37475164e+03      # Ac(Q)MSSM DRbar
  3  3    -9.37355184e+02      # At(Q)MSSM DRbar
Block ad Q= 8.23120276e+02  
  1  1    -1.60154698e+03      # Ad(Q)MSSM DRbar
  2  2    -1.60145937e+03      # As(Q)MSSM DRbar
  3  3    -1.33783249e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.23120276e+02  
  1  1    -6.02585586e+02      # Ae(Q)MSSM DRbar
  2  2    -6.02278363e+02      # Amu(Q)MSSM DRbar
  3  3    -5.01582549e+02      # Atau(Q)MSSM DRbar
