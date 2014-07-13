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
     1    5.00000000e+02   # m0
     2    7.50000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.71307008e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=2.32298688e-04
# MX=1.71307008e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03926121e+01   # MW
        25     1.17524023e+02   # h0
        35     1.13477993e+03   # H0
        36     1.13456126e+03   # A0
        37     1.13767775e+03   # H+
   1000021     1.68018663e+03   # ~g
   1000022     3.14733882e+02   # ~neutralino(1)
   1000023     5.95355208e+02   # ~neutralino(2)
   1000024     5.95456103e+02   # ~chargino(1)
   1000025    -9.05523093e+02   # ~neutralino(3)
   1000035     9.16744127e+02   # ~neutralino(4)
   1000037     9.16901859e+02   # ~chargino(2)
   1000001     1.59622561e+03   # ~d_L
   1000002     1.59440890e+03   # ~u_L
   1000003     1.59622152e+03   # ~s_L
   1000004     1.59440480e+03   # ~c_L
   1000005     1.45220929e+03   # ~b_1
   1000006     1.21849114e+03   # ~t_1
   1000011     7.07467655e+02   # ~e_L
   1000012     7.02805872e+02   # ~nue_L
   1000013     7.07459894e+02   # ~mu_L
   1000014     7.02798064e+02   # ~numu_L
   1000015     5.66697582e+02   # ~stau_1
   1000016     7.00254930e+02   # ~nu_tau_L
   2000001     1.53218980e+03   # ~d_R
   2000002     1.53794160e+03   # ~u_R
   2000003     1.53218559e+03   # ~s_R
   2000004     1.53793717e+03   # ~c_R
   2000005     1.52483544e+03   # ~b_2
   2000006     1.48162854e+03   # ~t_2
   2000011     5.74251800e+02   # ~e_R
   2000013     5.74232437e+02   # ~mu_R
   2000015     7.06026694e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05087072e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97909247e-01   # N_{1,1}
  1  2    -8.60378511e-03   # N_{1,2}
  1  3     5.86533023e-02   # N_{1,3}
  1  4    -2.57468465e-02   # N_{1,4}
  2  1     2.05329879e-02   # N_{2,1}
  2  2     9.81172527e-01   # N_{2,2}
  2  3    -1.56657143e-01   # N_{2,3}
  2  4     1.11073883e-01   # N_{2,4}
  3  1    -2.29156915e-02   # N_{3,1}
  3  2     3.29869690e-02   # N_{3,2}
  3  3     7.05374360e-01   # N_{3,3}
  3  4     7.07696081e-01   # N_{3,4}
  4  1    -5.68366306e-02   # N_{4,1}
  4  2     1.90100779e-01   # N_{4,2}
  4  3     6.88814446e-01   # N_{4,3}
  4  4    -6.97256015e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.74641729e-01   # U_{1,1}
  1  2    -2.23771089e-01   # U_{1,2}
  2  1     2.23771089e-01   # U_{2,1}
  2  2     9.74641729e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.87245568e-01   # V_{1,1}
  1  2    -1.59204866e-01   # V_{1,2}
  2  1     1.59204866e-01   # V_{2,1}
  2  2     9.87245568e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.05634125e-01   # F_{11}
  1  2     9.52149033e-01   # F_{12}
  2  1     9.52149033e-01   # F_{21}
  2  2    -3.05634125e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.93475935e-01   # F_{11}
  1  2     1.14041947e-01   # F_{12}
  2  1    -1.14041947e-01   # F_{21}
  2  2     9.93475935e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     9.29823638e-02   # F_{11}
  1  2     9.95667756e-01   # F_{12}
  2  1     9.95667756e-01   # F_{21}
  2  2    -9.29823638e-02   # F_{22}
Block gauge Q= 1.30491919e+03  # SM gauge couplings
     1     3.63073611e-01   # g'(Q)MSSM DRbar
     2     6.40701404e-01   # g(Q)MSSM DRbar
     3     1.04051838e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.30491919e+03  
  3  3     8.48204208e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.30491919e+03  
  3  3     1.32782164e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.30491919e+03  
  3  3     1.00149065e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.30491919e+03 # Higgs mixing parameters
     1     8.99472585e+02    # mu(Q)MSSM DRbar
     2     9.62629660e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43627040e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     1.32846117e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.30491919e+03  # MSSM DRbar SUSY breaking parameters
     1     3.19733695e+02      # M_1(Q)
     2     5.87648122e+02      # M_2(Q)
     3     1.62241666e+03      # M_3(Q)
    21     4.50349896e+05      # mH1^2(Q)
    22    -7.71702967e+05      # mH2^2(Q)
    31     7.00513034e+02      # meL(Q)
    32     7.00505177e+02      # mmuL(Q)
    33     6.98126772e+02      # mtauL(Q)
    34     5.69545976e+02      # meR(Q)
    35     5.69526457e+02      # mmuR(Q)
    36     5.63595577e+02      # mtauR(Q)
    41     1.54467523e+03      # mqL1(Q)
    42     1.54467104e+03      # mqL2(Q)
    43     1.41196988e+03      # mqL3(Q)
    44     1.48960731e+03      # muR(Q)
    45     1.48960280e+03      # mcR(Q)
    46     1.20031565e+03      # mtR(Q)
    47     1.48283992e+03      # mdR(Q)
    48     1.48283562e+03      # msR(Q)
    49     1.47497023e+03      # mbR(Q)
Block au Q= 1.30491919e+03  
  1  1    -1.63774564e+03      # Au(Q)MSSM DRbar
  2  2    -1.63773842e+03      # Ac(Q)MSSM DRbar
  3  3    -1.27125808e+03      # At(Q)MSSM DRbar
Block ad Q= 1.30491919e+03  
  1  1    -1.99454602e+03      # Ad(Q)MSSM DRbar
  2  2    -1.99453936e+03      # As(Q)MSSM DRbar
  3  3    -1.86593668e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.30491919e+03  
  1  1    -4.40697038e+02      # Ae(Q)MSSM DRbar
  2  2    -4.40689313e+02      # Amu(Q)MSSM DRbar
  3  3    -4.38353150e+02      # Atau(Q)MSSM DRbar
