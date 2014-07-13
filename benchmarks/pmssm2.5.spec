# SOFTSUSY3.4.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.1       # version number
Block MODSEL  # Select model
     1    0   # nonUniversal
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
Block EXTPAR               # non-universal SUSY breaking parameters
     0    -1.00000000e+00  # Set MX=MSUSY
     1     1.35000000e+02  # M_1(MX)
     2     2.50000000e+03  # M_2(MX)
     3     2.50000000e+03  # M_3(MX)
     11    0.00000000e+00  # At(MX)
     12    0.00000000e+00  # Ab(MX)
     13    0.00000000e+00  # Atau(MX)
     23    2.50000000e+03  # mu(MX)
     26    2.50000000e+03  # mA(pole)
     31    1.80000000e+02  # meL(MX)
     32    1.80000000e+02  # mmuL(MX)
     33    2.50000000e+03  # mtauL(MX)
     34    1.80000000e+02  # meR(MX)
     35    1.80000000e+02  # mmuR(MX)
     36    2.50000000e+03  # mtauR(MX)
     41    2.50000000e+03  # mqL1(MX)
     42    2.50000000e+03  # mqL2(MX)
     43    2.50000000e+03  # mqL3(MX)
     44    2.50000000e+03  # muR(MX)
     45    2.50000000e+03  # mcR(MX)
     46    2.50000000e+03  # mtR(MX)
     47    2.50000000e+03  # mdR(MX)
     48    2.50000000e+03  # msR(MX)
     49    2.50000000e+03  # mbR(MX)
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=9.54288237e-04
# MX=2.50366729e+03 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04067965e+01   # MW
        25     1.17126575e+02   # h0
        35     2.50009614e+03   # H0
        36     2.49999181e+03   # A0
        37     2.50164878e+03   # H+
   1000021     2.64698268e+03   # ~g
   1000022     1.31856107e+02   # ~neutralino(1)
   1000023     2.45873425e+03   # ~neutralino(2)
   1000024     2.45891470e+03   # ~chargino(1)
   1000025    -2.53370947e+03   # ~neutralino(3)
   1000035     2.57984285e+03   # ~neutralino(4)
   1000037     2.58001106e+03   # ~chargino(2)
   1000001     2.60389086e+03   # ~d_L
   1000002     2.60285384e+03   # ~u_L
   1000003     2.60389086e+03   # ~s_L
   1000004     2.60285384e+03   # ~c_L
   1000005     2.58002073e+03   # ~b_1
   1000006     2.58165967e+03   # ~t_1
   1000011     2.83891459e+02   # ~e_L
   1000012     2.72798743e+02   # ~nue_L
   1000013     2.83891459e+02   # ~mu_L
   1000014     2.72798743e+02   # ~numu_L
   1000015     2.49899496e+03   # ~stau_1
   1000016     2.51704448e+03   # ~nu_tau_L
   2000001     2.58612271e+03   # ~d_R
   2000002     2.58540920e+03   # ~u_R
   2000003     2.58612271e+03   # ~s_R
   2000004     2.58540920e+03   # ~c_R
   2000005     2.60817207e+03   # ~b_2
   2000006     2.61253684e+03   # ~t_2
   2000011     1.99564937e+02   # ~e_R
   2000013     1.99564937e+02   # ~mu_R
   2000015     2.52258796e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04707507e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.99842142e-01   # N_{1,1}
  1  2    -2.44214871e-04   # N_{1,2}
  1  3     1.75527190e-02   # N_{1,3}
  1  4    -2.74480930e-03   # N_{1,4}
  2  1     7.74912037e-03   # N_{2,1}
  2  2     8.54583938e-01   # N_{2,2}
  2  3    -3.73032942e-01   # N_{2,3}
  2  4     3.61210005e-01   # N_{2,4}
  3  1    -1.04662982e-02   # N_{3,1}
  3  2     9.76350437e-03   # N_{3,2}
  3  3     7.06902779e-01   # N_{3,3}
  3  4     7.07165887e-01   # N_{3,4}
  4  1    -1.20871544e-02   # N_{4,1}
  4  2     5.19221443e-01   # N_{4,2}
  4  3     6.00688595e-01   # N_{4,3}
  4  4    -6.07812641e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     7.81080844e-01   # U_{1,1}
  1  2    -6.24429912e-01   # U_{1,2}
  2  1     6.24429912e-01   # U_{2,1}
  2  2     7.81080844e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     7.93195026e-01   # V_{1,1}
  1  2    -6.08967692e-01   # V_{1,2}
  2  1     6.08967692e-01   # V_{2,1}
  2  2     7.93195026e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.24973928e-01   # F_{11}
  1  2     9.05205590e-01   # F_{12}
  2  1     9.05205590e-01   # F_{21}
  2  2    -4.24973928e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     3.95952933e-01   # F_{11}
  1  2     9.18270807e-01   # F_{12}
  2  1     9.18270807e-01   # F_{21}
  2  2    -3.95952933e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     4.06100467e-01   # F_{11}
  1  2     9.13828436e-01   # F_{12}
  2  1     9.13828436e-01   # F_{21}
  2  2    -4.06100467e-01   # F_{22}
Block gauge Q= 2.50366729e+03  # SM gauge couplings
     1     3.64712363e-01   # g'(Q)MSSM DRbar
     2     6.36076034e-01   # g(Q)MSSM DRbar
     3     1.01384350e+00   # g3(Q)MSSM DRbar
Block yu Q= 2.50366729e+03  
  3  3     8.33687162e-01   # Yt(Q)MSSM DRbar
Block yd Q= 2.50366729e+03  
  3  3     1.25591832e-01   # Yb(Q)MSSM DRbar
Block ye Q= 2.50366729e+03  
  3  3     9.97866364e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 2.50366729e+03 # Higgs mixing parameters
     1     2.53486845e+03    # mu(Q)MSSM DRbar
     2     9.54823680e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43712866e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     6.15226537e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 2.50366729e+03  # MSSM DRbar SUSY breaking parameters
     1     1.35000000e+02      # M_1(Q)
     2     2.50000000e+03      # M_2(Q)
     3     2.50000000e+03      # M_3(Q)
    21    -3.41720697e+05      # mH1^2(Q)
    22    -6.24389558e+06      # mH2^2(Q)
    31     1.79999999e+02      # meL(Q)
    32     1.79999999e+02      # mmuL(Q)
    33     2.50000000e+03      # mtauL(Q)
    34     1.80000001e+02      # meR(Q)
    35     1.80000001e+02      # mmuR(Q)
    36     2.50000000e+03      # mtauR(Q)
    41     2.49999999e+03      # mqL1(Q)
    42     2.49999999e+03      # mqL2(Q)
    43     2.49999999e+03      # mqL3(Q)
    44     2.49999999e+03      # muR(Q)
    45     2.49999999e+03      # mcR(Q)
    46     2.49999999e+03      # mtR(Q)
    47     2.49999999e+03      # mdR(Q)
    48     2.49999999e+03      # msR(Q)
    49     2.49999999e+03      # mbR(Q)
Block au Q= 2.50366729e+03  
  1  1     6.10950819e-06      # Au(Q)MSSM DRbar
  2  2     6.10958045e-06      # Ac(Q)MSSM DRbar
  3  3     1.02275246e-05      # At(Q)MSSM DRbar
Block ad Q= 2.50366729e+03  
  1  1     2.09651985e-06      # Ad(Q)MSSM DRbar
  2  2     2.09659461e-06      # As(Q)MSSM DRbar
  3  3     3.43650247e-06      # Ab(Q)MSSM DRbar
Block ae Q= 2.50366729e+03  
  1  1     0.00000000e+00      # Ae(Q)MSSM DRbar
  2  2     1.21577039e-07      # Amu(Q)MSSM DRbar
  3  3     1.21880456e-07      # Atau(Q)MSSM DRbar
