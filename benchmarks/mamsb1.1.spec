# SOFTSUSY3.4.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.1       # version number
Block MODSEL  # Select model
     1    3   # amsb
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
     1    3.00000000e+02   # m0
     2    4.00000000e+04   # m3/2
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.64784454e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=3.40034097e-04
# MX=2.64784454e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04004781e+01   # MW
        25     1.12473212e+02   # h0
        35     7.25683819e+02   # H0
        36     7.25458146e+02   # A0
        37     7.30111278e+02   # H+
   1000021    -8.88554532e+02   # ~g
   1000022     1.30622542e+02   # ~neutralino(1)
   1000023     3.63264235e+02   # ~neutralino(2)
   1000024     1.30804798e+02   # ~chargino(1)
   1000025    -7.02189671e+02   # ~neutralino(3)
   1000035     7.10002724e+02   # ~neutralino(4)
   1000037     7.08658840e+02   # ~chargino(2)
   1000039     4.00000000e+04   # ~gravitino
   1000001     8.80778848e+02   # ~d_L
   1000002     8.77360560e+02   # ~u_L
   1000003     8.80773592e+02   # ~s_L
   1000004     8.77355277e+02   # ~c_L
   1000005     7.66905016e+02   # ~b_1
   1000006     6.31833655e+02   # ~t_1
   1000011     2.59783048e+02   # ~e_L
   1000012     2.47229757e+02   # ~nue_L
   1000013     2.59771728e+02   # ~mu_L
   1000014     2.47217885e+02   # ~numu_L
   1000015     2.25918015e+02   # ~stau_1
   1000016     2.43592243e+02   # ~nu_tau_L
   2000001     8.89128021e+02   # ~d_R
   2000002     8.82344994e+02   # ~u_R
   2000003     8.89122350e+02   # ~s_R
   2000004     8.82340189e+02   # ~c_R
   2000005     8.77494299e+02   # ~b_2
   2000006     8.12730412e+02   # ~t_2
   2000011     2.52006702e+02   # ~e_R
   2000013     2.51983293e+02   # ~mu_R
   2000015     2.73094171e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.07945099e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1    -8.12285698e-03   # N_{1,1}
  1  2     9.92466317e-01   # N_{1,2}
  1  3    -1.17812604e-01   # N_{1,3}
  1  4     3.26315732e-02   # N_{1,4}
  2  1     9.94606754e-01   # N_{2,1}
  2  2     2.02357862e-02   # N_{2,2}
  2  3     8.75433169e-02   # N_{2,3}
  2  4    -5.18081586e-02   # N_{2,4}
  3  1    -2.62788520e-02   # N_{3,1}
  3  2     6.00262002e-02   # N_{3,2}
  3  3     7.03490651e-01   # N_{3,3}
  3  4     7.07677315e-01   # N_{3,4}
  4  1    -1.00004229e-01   # N_{4,1}
  4  2     1.04871246e-01   # N_{4,2}
  4  3     6.95382817e-01   # N_{4,3}
  4  4    -7.03877769e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.86298480e-01   # U_{1,1}
  1  2    -1.64970632e-01   # U_{1,2}
  2  1     1.64970632e-01   # U_{2,1}
  2  2     9.86298480e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.98948835e-01   # V_{1,1}
  1  2    -4.58391192e-02   # V_{1,2}
  2  1     4.58391192e-02   # V_{2,1}
  2  2     9.98948835e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1    -4.53179113e-01   # F_{11}
  1  2     8.91419481e-01   # F_{12}
  2  1     8.91419481e-01   # F_{21}
  2  2     4.53179113e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.97281456e-01   # F_{11}
  1  2     7.36864792e-02   # F_{12}
  2  1    -7.36864792e-02   # F_{21}
  2  2     9.97281456e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     6.14224725e-01   # F_{11}
  1  2     7.89131160e-01   # F_{12}
  2  1     7.89131160e-01   # F_{21}
  2  2    -6.14224725e-01   # F_{22}
Block gauge Q= 6.89368649e+02  # SM gauge couplings
     1     3.61743627e-01   # g'(Q)MSSM DRbar
     2     6.46140339e-01   # g(Q)MSSM DRbar
     3     1.07367129e+00   # g3(Q)MSSM DRbar
Block yu Q= 6.89368649e+02  
  3  3     8.70671645e-01   # Yt(Q)MSSM DRbar
Block yd Q= 6.89368649e+02  
  3  3     1.50865708e-01   # Yb(Q)MSSM DRbar
Block ye Q= 6.89368649e+02  
  3  3     9.95048017e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 6.89368649e+02 # Higgs mixing parameters
     1     7.00124601e+02    # mu(Q)MSSM DRbar
     2     9.70362013e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44678267e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     5.26207509e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 6.89368649e+02  # MSSM DRbar SUSY breaking parameters
     1     3.71695221e+02      # M_1(Q)
     2     1.28383168e+02      # M_2(Q)
     3    -8.44098091e+02      # M_3(Q)
    21     3.01121056e+04      # mH1^2(Q)
    22    -4.82301302e+05      # mH2^2(Q)
    31     2.54921618e+02      # meL(Q)
    32     2.54910085e+02      # mmuL(Q)
    33     2.51531105e+02      # mtauL(Q)
    34     2.44771522e+02      # meR(Q)
    35     2.44747490e+02      # mmuR(Q)
    36     2.37649699e+02      # mtauR(Q)
    41     8.52464913e+02      # mqL1(Q)
    42     8.52459478e+02      # mqL2(Q)
    43     7.40266435e+02      # mqL3(Q)
    44     8.57466855e+02      # muR(Q)
    45     8.57461892e+02      # mcR(Q)
    46     6.28464292e+02      # mtR(Q)
    47     8.63409047e+02      # mdR(Q)
    48     8.63403178e+02      # msR(Q)
    49     8.51108988e+02      # mbR(Q)
Block au Q= 6.89368649e+02  
  1  1     1.32582449e+03      # Au(Q)MSSM DRbar
  2  2     1.32581337e+03      # Ac(Q)MSSM DRbar
  3  3     7.52883218e+02      # At(Q)MSSM DRbar
Block ad Q= 6.89368649e+02  
  1  1     1.87473868e+03      # Ad(Q)MSSM DRbar
  2  2     1.87472835e+03      # As(Q)MSSM DRbar
  3  3     1.66978812e+03      # Ab(Q)MSSM DRbar
Block ae Q= 6.89368649e+02  
  1  1     3.92885175e+02      # Ae(Q)MSSM DRbar
  2  2     3.92859648e+02      # Amu(Q)MSSM DRbar
  3  3     3.85347672e+02      # Atau(Q)MSSM DRbar
