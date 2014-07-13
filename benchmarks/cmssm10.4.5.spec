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
     1    1.15000000e+03   # m0
     2    5.50000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.99386381e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=4.27662671e-04
# MX=1.99386381e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03950063e+01   # MW
        25     1.16162214e+02   # h0
        35     1.36254878e+03   # H0
        36     1.36248986e+03   # A0
        37     1.36498919e+03   # H+
   1000021     1.30908520e+03   # ~g
   1000022     2.29838965e+02   # ~neutralino(1)
   1000023     4.35622992e+02   # ~neutralino(2)
   1000024     4.35649465e+02   # ~chargino(1)
   1000025    -6.83300442e+02   # ~neutralino(3)
   1000035     6.97686607e+02   # ~neutralino(4)
   1000037     6.97783400e+02   # ~chargino(2)
   1000001     1.59820753e+03   # ~d_L
   1000002     1.59641122e+03   # ~u_L
   1000003     1.59820200e+03   # ~s_L
   1000004     1.59640569e+03   # ~c_L
   1000005     1.38885296e+03   # ~b_1
   1000006     1.11317476e+03   # ~t_1
   1000011     1.20326538e+03   # ~e_L
   1000012     1.20035646e+03   # ~nue_L
   1000013     1.20324920e+03   # ~mu_L
   1000014     1.20034025e+03   # ~numu_L
   1000015     1.15652137e+03   # ~stau_1
   1000016     1.19536169e+03   # ~nu_tau_L
   2000001     1.56691880e+03   # ~d_R
   2000002     1.56925208e+03   # ~u_R
   2000003     1.56691344e+03   # ~s_R
   2000004     1.56924611e+03   # ~c_R
   2000005     1.55636245e+03   # ~b_2
   2000006     1.40826920e+03   # ~t_2
   2000011     1.16750963e+03   # ~e_R
   2000013     1.16747615e+03   # ~mu_R
   2000015     1.19892577e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04580782e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96284361e-01   # N_{1,1}
  1  2    -1.48869863e-02   # N_{1,2}
  1  3     7.79816915e-02   # N_{1,3}
  1  4    -3.33871909e-02   # N_{1,4}
  2  1     3.44296294e-02   # N_{2,1}
  2  2     9.70439355e-01   # N_{2,2}
  2  3    -1.96378802e-01   # N_{2,3}
  2  4     1.36005237e-01   # N_{2,4}
  3  1    -3.07159456e-02   # N_{3,1}
  3  2     4.43232993e-02   # N_{3,2}
  3  3     7.04051040e-01   # N_{3,3}
  3  4     7.08098940e-01   # N_{3,4}
  4  1    -7.27227777e-02   # N_{4,1}
  4  2     2.36772634e-01   # N_{4,2}
  4  3     6.77986987e-01   # N_{4,3}
  4  4    -6.92086528e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.59533390e-01   # U_{1,1}
  1  2    -2.81594875e-01   # U_{1,2}
  2  1     2.81594875e-01   # U_{2,1}
  2  2     9.59533390e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.80638979e-01   # V_{1,1}
  1  2    -1.95824395e-01   # V_{1,2}
  2  1     1.95824395e-01   # V_{2,1}
  2  2     9.80638979e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.15127880e-01   # F_{11}
  1  2     9.76585887e-01   # F_{12}
  2  1     9.76585887e-01   # F_{21}
  2  2    -2.15127880e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.99288898e-01   # F_{11}
  1  2     3.77054098e-02   # F_{12}
  2  1    -3.77054098e-02   # F_{21}
  2  2     9.99288898e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.24856671e-01   # F_{11}
  1  2     9.92174789e-01   # F_{12}
  2  1     9.92174789e-01   # F_{21}
  2  2    -1.24856671e-01   # F_{22}
Block gauge Q= 1.21970563e+03  # SM gauge couplings
     1     3.62638401e-01   # g'(Q)MSSM DRbar
     2     6.41269057e-01   # g(Q)MSSM DRbar
     3     1.04700015e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.21970563e+03  
  3  3     8.54576138e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.21970563e+03  
  3  3     1.34621093e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.21970563e+03  
  3  3     9.94808250e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.21970563e+03 # Higgs mixing parameters
     1     6.75496244e+02    # mu(Q)MSSM DRbar
     2     9.63059460e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43514047e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     1.89484225e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.21970563e+03  # MSSM DRbar SUSY breaking parameters
     1     2.32874692e+02      # M_1(Q)
     2     4.29656897e+02      # M_2(Q)
     3     1.20216769e+03      # M_3(Q)
    21     1.37825882e+06      # mH1^2(Q)
    22    -4.12705218e+05      # mH2^2(Q)
    31     1.20003796e+03      # meL(Q)
    32     1.20002178e+03      # mmuL(Q)
    33     1.19519539e+03      # mtauL(Q)
    34     1.16516154e+03      # meR(Q)
    35     1.16512803e+03      # mmuR(Q)
    36     1.15511372e+03      # mtauR(Q)
    41     1.56287238e+03      # mqL1(Q)
    42     1.56286671e+03      # mqL2(Q)
    43     1.35812054e+03      # mqL3(Q)
    44     1.53688514e+03      # muR(Q)
    45     1.53687900e+03      # mcR(Q)
    46     1.08602202e+03      # mtR(Q)
    47     1.53382587e+03      # mdR(Q)
    48     1.53382035e+03      # msR(Q)
    49     1.52325660e+03      # mbR(Q)
Block au Q= 1.21970563e+03  
  1  1    -1.21854548e+03      # Au(Q)MSSM DRbar
  2  2    -1.21854008e+03      # Ac(Q)MSSM DRbar
  3  3    -9.41968994e+02      # At(Q)MSSM DRbar
Block ad Q= 1.21970563e+03  
  1  1    -1.48829982e+03      # Ad(Q)MSSM DRbar
  2  2    -1.48829484e+03      # As(Q)MSSM DRbar
  3  3    -1.39116787e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.21970563e+03  
  1  1    -3.25455149e+02      # Ae(Q)MSSM DRbar
  2  2    -3.25449391e+02      # Amu(Q)MSSM DRbar
  3  3    -3.23735827e+02      # Atau(Q)MSSM DRbar
