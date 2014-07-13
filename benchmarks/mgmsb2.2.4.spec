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
     1    1.50000000e+05   # lambda
     2    1.00000000e+14   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=9.27116790e-05
# MX=1.00000000e+14 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03963039e+01   # MW
        25     1.15373525e+02   # h0
        35     9.95997200e+02   # H0
        36     9.95952216e+02   # A0
        37     9.99392766e+02   # H+
   1000021     1.12760634e+03   # ~g
   1000022     2.00228136e+02   # ~neutralino(1)
   1000023     3.85869075e+02   # ~neutralino(2)
   1000024     3.85994768e+02   # ~chargino(1)
   1000025    -7.85245969e+02   # ~neutralino(3)
   1000035     7.92419267e+02   # ~neutralino(4)
   1000037     7.93233121e+02   # ~chargino(2)
   1000039     3.55500000e+00   # ~gravitino
   1000001     1.38334502e+03   # ~d_L
   1000002     1.38122034e+03   # ~u_L
   1000003     1.38333953e+03   # ~s_L
   1000004     1.38121485e+03   # ~c_L
   1000005     1.22297062e+03   # ~b_1
   1000006     9.72562096e+02   # ~t_1
   1000011     6.66690672e+02   # ~e_L
   1000012     6.61648442e+02   # ~nue_L
   1000013     6.66676571e+02   # ~mu_L
   1000014     6.61634243e+02   # ~numu_L
   1000015     4.37459364e+02   # ~stau_1
   1000016     6.57002554e+02   # ~nu_tau_L
   2000001     1.24421147e+03   # ~d_R
   2000002     1.26945732e+03   # ~u_R
   2000003     1.24420333e+03   # ~s_R
   2000004     1.26945330e+03   # ~c_R
   2000005     1.25298437e+03   # ~b_2
   2000006     1.26541824e+03   # ~t_2
   2000011     4.52937055e+02   # ~e_R
   2000013     4.52895248e+02   # ~mu_R
   2000015     6.63423773e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.01805987e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97757343e-01   # N_{1,1}
  1  2    -1.00954574e-02   # N_{1,2}
  1  3     6.29890000e-02   # N_{1,3}
  1  4    -2.02670223e-02   # N_{1,4}
  2  1     1.98791311e-02   # N_{2,1}
  2  2     9.88257213e-01   # N_{2,2}
  2  3    -1.33380105e-01   # N_{2,3}
  2  4     7.18487900e-02   # N_{2,4}
  3  1    -2.96449081e-02   # N_{3,1}
  3  2     4.42073545e-02   # N_{3,2}
  3  3     7.04404338e-01   # N_{3,3}
  3  4     7.07800408e-01   # N_{3,4}
  4  1    -5.66240598e-02   # N_{4,1}
  4  2     1.45915978e-01   # N_{4,2}
  4  3     6.94303004e-01   # N_{4,3}
  4  4    -7.02456819e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.81798225e-01   # U_{1,1}
  1  2    -1.89926949e-01   # U_{1,2}
  2  1     1.89926949e-01   # U_{2,1}
  2  2     9.81798225e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.94711752e-01   # V_{1,1}
  1  2    -1.02706039e-01   # V_{1,2}
  2  1     1.02706039e-01   # V_{2,1}
  2  2     9.94711752e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     1.98687951e-01   # F_{11}
  1  2     9.80062803e-01   # F_{12}
  2  1     9.80062803e-01   # F_{21}
  2  2    -1.98687951e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.33841277e-01   # F_{11}
  1  2     9.00989315e-01   # F_{12}
  2  1     9.00989315e-01   # F_{21}
  2  2    -4.33841277e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     8.41060415e-02   # F_{11}
  1  2     9.96456810e-01   # F_{12}
  2  1     9.96456810e-01   # F_{21}
  2  2    -8.41060415e-02   # F_{22}
Block gauge Q= 1.07751846e+03  # SM gauge couplings
     1     3.62679621e-01   # g'(Q)MSSM DRbar
     2     6.42046519e-01   # g(Q)MSSM DRbar
     3     1.05440286e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.07751846e+03  
  3  3     8.56066947e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.07751846e+03  
  3  3     1.97538533e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.07751846e+03  
  3  3     1.50776873e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.07751846e+03 # Higgs mixing parameters
     1     7.78955140e+02    # mu(Q)MSSM DRbar
     2     1.44899351e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43878809e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     1.03560318e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.07751846e+03  # MSSM DRbar SUSY breaking parameters
     1     2.03515827e+02      # M_1(Q)
     2     3.77151033e+02      # M_2(Q)
     3     1.03575567e+03      # M_3(Q)
    21     3.75829804e+05      # mH1^2(Q)
    22    -5.86942468e+05      # mH2^2(Q)
    31     6.63046255e+02      # meL(Q)
    32     6.63032080e+02      # mmuL(Q)
    33     6.58707055e+02      # mtauL(Q)
    34     4.47997547e+02      # meR(Q)
    35     4.47955307e+02      # mmuR(Q)
    36     4.34914686e+02      # mtauR(Q)
    41     1.35162975e+03      # mqL1(Q)
    42     1.35162412e+03      # mqL2(Q)
    43     1.22018073e+03      # mqL3(Q)
    44     1.23816843e+03      # muR(Q)
    45     1.23816427e+03      # mcR(Q)
    46     9.39831484e+02      # mtR(Q)
    47     1.21078539e+03      # mdR(Q)
    48     1.21077694e+03      # msR(Q)
    49     1.19535176e+03      # mbR(Q)
Block au Q= 1.07751846e+03  
  1  1    -9.62128958e+02      # Au(Q)MSSM DRbar
  2  2    -9.62124116e+02      # Ac(Q)MSSM DRbar
  3  3    -7.65579060e+02      # At(Q)MSSM DRbar
Block ad Q= 1.07751846e+03  
  1  1    -1.14931832e+03      # Ad(Q)MSSM DRbar
  2  2    -1.14931163e+03      # As(Q)MSSM DRbar
  3  3    -1.07532575e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.07751846e+03  
  1  1    -2.13504724e+02      # Ae(Q)MSSM DRbar
  2  2    -2.13497399e+02      # Amu(Q)MSSM DRbar
  3  3    -2.11268634e+02      # Atau(Q)MSSM DRbar
