# SOFTSUSY3.4.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.1       # version number
Block MODSEL  # Select model
     1    2   # gmsb
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
Block MINPAR               # SUSY breaking input parameters
     3    1.50000000e+01   # tanb, DRbar, Feynman gauge
     4    1.00000000e+00   # sign(mu)
     1    1.17000000e+05   # lambda
     2    1.30000000e+05   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.00690604e-05
# MX=1.30000000e+05 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04003151e+01   # MW
        25     1.14214469e+02   # h0
        35     5.90786923e+02   # H0
        36     5.90520493e+02   # A0
        37     5.96224067e+02   # H+
   1000021     1.09537601e+03   # ~g
   1000022     1.90924068e+02   # ~neutralino(1)
   1000023     3.53353186e+02   # ~neutralino(2)
   1000024     3.52883777e+02   # ~chargino(1)
   1000025    -4.59626270e+02   # ~neutralino(3)
   1000035     4.91679331e+02   # ~neutralino(4)
   1000037     4.91554238e+02   # ~chargino(2)
   1000039     3.60477000e-09   # ~gravitino
   1000001     1.31061164e+03   # ~d_L
   1000002     1.30836936e+03   # ~u_L
   1000003     1.31060986e+03   # ~s_L
   1000004     1.30836758e+03   # ~c_L
   1000005     1.24250821e+03   # ~b_1
   1000006     1.15737166e+03   # ~t_1
   1000011     4.10082765e+02   # ~e_L
   1000012     4.02048610e+02   # ~nue_L
   1000013     4.10080995e+02   # ~mu_L
   1000014     4.02046806e+02   # ~numu_L
   1000015     1.98435210e+02   # ~stau_1
   1000016     4.01252895e+02   # ~nu_tau_L
   2000001     1.25097387e+03   # ~d_R
   2000002     1.25491738e+03   # ~u_R
   2000003     1.25097140e+03   # ~s_R
   2000004     1.25491611e+03   # ~c_R
   2000005     1.26202831e+03   # ~b_2
   2000006     1.27184050e+03   # ~t_2
   2000011     2.04125451e+02   # ~e_R
   2000013     2.04118260e+02   # ~mu_R
   2000015     4.10686127e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.33550788e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.89892321e-01   # N_{1,1}
  1  2    -2.78691624e-02   # N_{1,2}
  1  3     1.25570871e-01   # N_{1,3}
  1  4    -5.97365783e-02   # N_{1,4}
  2  1     8.98127822e-02   # N_{2,1}
  2  2     8.74544798e-01   # N_{2,2}
  2  3    -3.72523365e-01   # N_{2,3}
  2  4     2.97205994e-01   # N_{2,4}
  3  1    -4.43907635e-02   # N_{3,1}
  3  2     6.22240449e-02   # N_{3,2}
  3  3     7.01040336e-01   # N_{3,3}
  3  4     7.09013453e-01   # N_{3,4}
  4  1    -1.00380859e-01   # N_{4,1}
  4  2     4.80127976e-01   # N_{4,2}
  4  3     5.94979619e-01   # N_{4,3}
  4  4    -6.36710344e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.42114702e-01   # U_{1,1}
  1  2    -5.39298459e-01   # U_{1,2}
  2  1     5.39298459e-01   # U_{2,1}
  2  2     8.42114702e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.02318836e-01   # V_{1,1}
  1  2    -4.31069273e-01   # V_{1,2}
  2  1     4.31069273e-01   # V_{2,1}
  2  2     9.02318836e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.24832647e-01   # F_{11}
  1  2     9.74397394e-01   # F_{12}
  2  1     9.74397394e-01   # F_{21}
  2  2    -2.24832647e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     3.78481563e-01   # F_{11}
  1  2     9.25608830e-01   # F_{12}
  2  1     9.25608830e-01   # F_{21}
  2  2    -3.78481563e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     9.31357576e-02   # F_{11}
  1  2     9.95653419e-01   # F_{12}
  2  1     9.95653419e-01   # F_{21}
  2  2    -9.31357576e-02   # F_{22}
Block gauge Q= 1.18855444e+03  # SM gauge couplings
     1     3.63446809e-01   # g'(Q)MSSM DRbar
     2     6.43604184e-01   # g(Q)MSSM DRbar
     3     1.05287012e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.18855444e+03  
  3  3     8.58049602e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.18855444e+03  
  3  3     2.02180482e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.18855444e+03  
  3  3     1.51249870e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.18855444e+03 # Higgs mixing parameters
     1     4.51058351e+02    # mu(Q)MSSM DRbar
     2     1.44684269e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43363635e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     3.86174195e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.18855444e+03  # MSSM DRbar SUSY breaking parameters
     1     1.97798690e+02      # M_1(Q)
     2     3.70806088e+02      # M_2(Q)
     3     9.97189133e+02      # M_3(Q)
    21     1.43196321e+05      # mH1^2(Q)
    22    -1.75188914e+05      # mH2^2(Q)
    31     4.03313588e+02      # meL(Q)
    32     4.03311784e+02      # mmuL(Q)
    33     4.02759373e+02      # mtauL(Q)
    34     1.93654714e+02      # meR(Q)
    35     1.93647129e+02      # mmuR(Q)
    36     1.91310428e+02      # mtauR(Q)
    41     1.27538818e+03      # mqL1(Q)
    42     1.27538634e+03      # mqL2(Q)
    43     1.23139982e+03      # mqL3(Q)
    44     1.22177410e+03      # muR(Q)
    45     1.22177278e+03      # mcR(Q)
    46     1.13172751e+03      # mtR(Q)
    47     1.21657454e+03      # mdR(Q)
    48     1.21657198e+03      # msR(Q)
    49     1.21160054e+03      # mbR(Q)
Block au Q= 1.18855444e+03  
  1  1    -3.03358472e+02      # Au(Q)MSSM DRbar
  2  2    -3.03358043e+02      # Ac(Q)MSSM DRbar
  3  3    -2.85816784e+02      # At(Q)MSSM DRbar
Block ad Q= 1.18855444e+03  
  1  1    -3.22763165e+02      # Ad(Q)MSSM DRbar
  2  2    -3.22762567e+02      # As(Q)MSSM DRbar
  3  3    -3.16161920e+02      # Ab(Q)MSSM DRbar
Block ae Q= 1.18855444e+03  
  1  1    -3.17679254e+01      # Ae(Q)MSSM DRbar
  2  2    -3.17676908e+01      # Amu(Q)MSSM DRbar
  3  3    -3.16958568e+01      # Atau(Q)MSSM DRbar
