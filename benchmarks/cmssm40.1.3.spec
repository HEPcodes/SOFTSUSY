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
     1    3.60000000e+02   # m0
     2    6.00000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.76223488e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=6.82061728e-05
# MX=1.76223488e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03891587e+01   # MW
        25     1.17909099e+02   # h0
        35     7.09048575e+02   # H0
        36     7.09055532e+02   # A0
        37     7.13912283e+02   # H+
   1000021     1.36311075e+03   # ~g
   1000022     2.50491135e+02   # ~neutralino(1)
   1000023     4.76950552e+02   # ~neutralino(2)
   1000024     4.77088170e+02   # ~chargino(1)
   1000025    -8.08657556e+02   # ~neutralino(3)
   1000035     8.16413375e+02   # ~neutralino(4)
   1000037     8.17392581e+02   # ~chargino(2)
   1000001     1.28924846e+03   # ~d_L
   1000002     1.28691099e+03   # ~u_L
   1000003     1.28921198e+03   # ~s_L
   1000004     1.28687442e+03   # ~c_L
   1000005     1.08433876e+03   # ~b_1
   1000006     9.34125474e+02   # ~t_1
   1000011     5.41168262e+02   # ~e_L
   1000012     5.35055609e+02   # ~nue_L
   1000013     5.41029353e+02   # ~mu_L
   1000014     5.34915226e+02   # ~numu_L
   1000015     2.51402215e+02   # ~stau_1
   1000016     4.86664584e+02   # ~nu_tau_L
   2000001     1.23763294e+03   # ~d_R
   2000002     1.24187317e+03   # ~u_R
   2000003     1.23756039e+03   # ~s_R
   2000004     1.24186857e+03   # ~c_R
   2000005     1.15072070e+03   # ~b_2
   2000006     1.15362225e+03   # ~t_2
   2000011     4.26418744e+02   # ~e_R
   2000013     4.26060861e+02   # ~mu_R
   2000015     5.13677116e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60393317e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97789724e-01   # N_{1,1}
  1  2    -7.78805479e-03   # N_{1,2}
  1  3     6.25037115e-02   # N_{1,3}
  1  4    -2.11730768e-02   # N_{1,4}
  2  1     1.88491054e-02   # N_{2,1}
  2  2     9.84771014e-01   # N_{2,2}
  2  3    -1.47912680e-01   # N_{2,3}
  2  4     8.94013469e-02   # N_{2,4}
  3  1    -2.87905753e-02   # N_{3,1}
  3  2     4.21297292e-02   # N_{3,2}
  3  3     7.04606607e-01   # N_{3,3}
  3  4     7.07761060e-01   # N_{3,4}
  4  1    -5.68461163e-02   # N_{4,1}
  4  2     1.68494755e-01   # N_{4,2}
  4  3     6.91190751e-01   # N_{4,3}
  4  4    -7.00452270e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.77585999e-01   # U_{1,1}
  1  2    -2.10536491e-01   # U_{1,2}
  2  1     2.10536491e-01   # U_{2,1}
  2  2     9.77585999e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91814097e-01   # V_{1,1}
  1  2    -1.27690235e-01   # V_{1,2}
  2  1     1.27690235e-01   # V_{2,1}
  2  2     9.91814097e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.35419113e-01   # F_{11}
  1  2     9.00227858e-01   # F_{12}
  2  1     9.00227858e-01   # F_{21}
  2  2    -4.35419113e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.10605926e-01   # F_{11}
  1  2     5.85592036e-01   # F_{12}
  2  1    -5.85592036e-01   # F_{21}
  2  2     8.10605926e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     3.19350967e-01   # F_{11}
  1  2     9.47636513e-01   # F_{12}
  2  1     9.47636513e-01   # F_{21}
  2  2    -3.19350967e-01   # F_{22}
Block gauge Q= 1.00889751e+03  # SM gauge couplings
     1     3.62517670e-01   # g'(Q)MSSM DRbar
     2     6.41504727e-01   # g(Q)MSSM DRbar
     3     1.05239336e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.00889751e+03  
  3  3     8.50573649e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.00889751e+03  
  3  3     4.90290745e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.00889751e+03  
  3  3     4.27806821e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.00889751e+03 # Higgs mixing parameters
     1     8.05569618e+02    # mu(Q)MSSM DRbar
     2     3.91933634e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43813851e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     6.36244688e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.00889751e+03  # MSSM DRbar SUSY breaking parameters
     1     2.54466595e+02      # M_1(Q)
     2     4.70473102e+02      # M_2(Q)
     3     1.32360741e+03      # M_3(Q)
    21    -1.47141484e+05      # mH1^2(Q)
    22    -6.37532597e+05      # mH2^2(Q)
    31     5.34816708e+02      # meL(Q)
    32     5.34675757e+02      # mmuL(Q)
    33     4.89445060e+02      # mtauL(Q)
    34     4.21534354e+02      # meR(Q)
    35     4.21172315e+02      # mmuR(Q)
    36     2.88516223e+02      # mtauR(Q)
    41     1.24858746e+03      # mqL1(Q)
    42     1.24855025e+03      # mqL2(Q)
    43     1.07784494e+03      # mqL3(Q)
    44     1.20437298e+03      # muR(Q)
    45     1.20436831e+03      # mcR(Q)
    46     9.40035083e+02      # mtR(Q)
    47     1.19903030e+03      # mdR(Q)
    48     1.19895655e+03      # msR(Q)
    49     1.09400694e+03      # mbR(Q)
Block au Q= 1.00889751e+03  
  1  1    -1.68706288e+03      # Au(Q)MSSM DRbar
  2  2    -1.68702276e+03      # Ac(Q)MSSM DRbar
  3  3    -1.17941727e+03      # At(Q)MSSM DRbar
Block ad Q= 1.00889751e+03  
  1  1    -1.95301531e+03      # Ad(Q)MSSM DRbar
  2  2    -1.95291315e+03      # As(Q)MSSM DRbar
  3  3    -1.64816461e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.00889751e+03  
  1  1    -6.66016480e+02      # Ae(Q)MSSM DRbar
  2  2    -6.65689799e+02      # Amu(Q)MSSM DRbar
  3  3    -5.56178254e+02      # Atau(Q)MSSM DRbar
