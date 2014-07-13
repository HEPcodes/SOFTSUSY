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
     1    1.20000000e+05   # lambda
     2    1.00000000e+14   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=4.64751910e-05
# MX=1.00000000e+14 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03985753e+01   # MW
        25     1.13838262e+02   # h0
        35     8.08002360e+02   # H0
        36     8.07963277e+02   # A0
        37     8.12151238e+02   # H+
   1000021     9.21461872e+02   # ~g
   1000022     1.59245123e+02   # ~neutralino(1)
   1000023     3.06689193e+02   # ~neutralino(2)
   1000024     3.06784713e+02   # ~chargino(1)
   1000025    -6.43471153e+02   # ~neutralino(3)
   1000035     6.51881502e+02   # ~neutralino(4)
   1000037     6.52866284e+02   # ~chargino(2)
   1000039     2.84400000e+00   # ~gravitino
   1000001     1.12290984e+03   # ~d_L
   1000002     1.12025521e+03   # ~u_L
   1000003     1.12290536e+03   # ~s_L
   1000004     1.12025072e+03   # ~c_L
   1000005     9.91884448e+02   # ~b_1
   1000006     7.89270133e+02   # ~t_1
   1000011     5.37215740e+02   # ~e_L
   1000012     5.31012272e+02   # ~nue_L
   1000013     5.37204298e+02   # ~mu_L
   1000014     5.31000705e+02   # ~numu_L
   1000015     3.50835003e+02   # ~stau_1
   1000016     5.27232445e+02   # ~nu_tau_L
   2000001     1.01166212e+03   # ~d_R
   2000002     1.03130412e+03   # ~u_R
   2000003     1.01165546e+03   # ~s_R
   2000004     1.03130085e+03   # ~c_R
   2000005     1.01894675e+03   # ~b_2
   2000006     1.03463329e+03   # ~t_2
   2000011     3.64330034e+02   # ~e_R
   2000013     3.64296045e+02   # ~mu_R
   2000015     5.35189080e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.06305031e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96602115e-01   # N_{1,1}
  1  2    -1.50955665e-02   # N_{1,2}
  1  3     7.72360920e-02   # N_{1,3}
  1  4    -2.43091471e-02   # N_{1,4}
  2  1     2.92496580e-02   # N_{2,1}
  2  2     9.83311115e-01   # N_{2,2}
  2  3    -1.58924743e-01   # N_{2,3}
  2  4     8.35860938e-02   # N_{2,4}
  3  1    -3.63849410e-02   # N_{3,1}
  3  2     5.45103290e-02   # N_{3,2}
  3  3     7.03020274e-01   # N_{3,3}
  3  4     7.08143527e-01   # N_{3,4}
  4  1    -6.78588110e-02   # N_{4,1}
  4  2     1.72916163e-01   # N_{4,2}
  4  3     6.88868642e-01   # N_{4,3}
  4  4    -7.00681936e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.73938121e-01   # U_{1,1}
  1  2    -2.26813880e-01   # U_{1,2}
  2  1     2.26813880e-01   # U_{2,1}
  2  2     9.73938121e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.92799581e-01   # V_{1,1}
  1  2    -1.19787277e-01   # V_{1,2}
  2  1     1.19787277e-01   # V_{2,1}
  2  2     9.92799581e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.42898420e-01   # F_{11}
  1  2     9.70051729e-01   # F_{12}
  2  1     9.70051729e-01   # F_{21}
  2  2    -2.42898420e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     5.09742167e-01   # F_{11}
  1  2     8.60327219e-01   # F_{12}
  2  1     8.60327219e-01   # F_{21}
  2  2    -5.09742167e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.05172258e-01   # F_{11}
  1  2     9.94454019e-01   # F_{12}
  2  1     9.94454019e-01   # F_{21}
  2  2    -1.05172258e-01   # F_{22}
Block gauge Q= 8.76516485e+02  # SM gauge couplings
     1     3.62244541e-01   # g'(Q)MSSM DRbar
     2     6.43150186e-01   # g(Q)MSSM DRbar
     3     1.06527452e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.76516485e+02  
  3  3     8.63202475e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.76516485e+02  
  3  3     1.99556312e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.76516485e+02  
  3  3     1.50985806e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.76516485e+02 # Higgs mixing parameters
     1     6.37177315e+02    # mu(Q)MSSM DRbar
     2     1.45253921e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44133074e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     6.82102743e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.76516485e+02  # MSSM DRbar SUSY breaking parameters
     1     1.62306138e+02      # M_1(Q)
     2     3.02419761e+02      # M_2(Q)
     3     8.45276945e+02      # M_3(Q)
    21     2.42375698e+05      # mH1^2(Q)
    22    -3.94890074e+05      # mH2^2(Q)
    31     5.33709034e+02      # meL(Q)
    32     5.33697519e+02      # mmuL(Q)
    33     5.30192059e+02      # mtauL(Q)
    34     3.59426193e+02      # meR(Q)
    35     3.59391761e+02      # mmuR(Q)
    36     3.48785081e+02      # mtauR(Q)
    41     1.09610462e+03      # mqL1(Q)
    42     1.09610001e+03      # mqL2(Q)
    43     9.88867802e+02      # mqL3(Q)
    44     1.00535793e+03      # muR(Q)
    45     1.00535455e+03      # mcR(Q)
    46     7.62300641e+02      # mtR(Q)
    47     9.83660733e+02      # mdR(Q)
    48     9.83653814e+02      # msR(Q)
    49     9.71004548e+02      # mbR(Q)
Block au Q= 8.76516485e+02  
  1  1    -7.92290673e+02      # Au(Q)MSSM DRbar
  2  2    -7.92286641e+02      # Ac(Q)MSSM DRbar
  3  3    -6.28398476e+02      # At(Q)MSSM DRbar
Block ad Q= 8.76516485e+02  
  1  1    -9.48766358e+02      # Ad(Q)MSSM DRbar
  2  2    -9.48760770e+02      # As(Q)MSSM DRbar
  3  3    -8.87035857e+02      # Ab(Q)MSSM DRbar
Block ae Q= 8.76516485e+02  
  1  1    -1.73129462e+02      # Ae(Q)MSSM DRbar
  2  2    -1.73123443e+02      # Amu(Q)MSSM DRbar
  3  3    -1.71296375e+02      # Atau(Q)MSSM DRbar