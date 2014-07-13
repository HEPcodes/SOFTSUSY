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
     1    1.70000000e+05   # lambda
     2    1.00000000e+14   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.36621885e-04
# MX=1.00000000e+14 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03954590e+01   # MW
        25     1.16189305e+02   # h0
        35     1.11960428e+03   # H0
        36     1.11956176e+03   # A0
        37     1.12264126e+03   # H+
   1000021     1.26309125e+03   # ~g
   1000022     2.27572911e+02   # ~neutralino(1)
   1000023     4.38363473e+02   # ~neutralino(2)
   1000024     4.38499949e+02   # ~chargino(1)
   1000025    -8.78017873e+02   # ~neutralino(3)
   1000035     8.84575794e+02   # ~neutralino(4)
   1000037     8.85312235e+02   # ~chargino(2)
   1000039     4.02900000e+00   # ~gravitino
   1000001     1.55536684e+03   # ~d_L
   1000002     1.55349387e+03   # ~u_L
   1000003     1.55536069e+03   # ~s_L
   1000004     1.55348772e+03   # ~c_L
   1000005     1.37521428e+03   # ~b_1
   1000006     1.09372519e+03   # ~t_1
   1000011     7.52700338e+02   # ~e_L
   1000012     7.48204750e+02   # ~nue_L
   1000013     7.52684488e+02   # ~mu_L
   1000014     7.48188813e+02   # ~numu_L
   1000015     4.95085567e+02   # ~stau_1
   1000016     7.42987581e+02   # ~nu_tau_L
   2000001     1.39757456e+03   # ~d_R
   2000002     1.42654834e+03   # ~u_R
   2000003     1.39756544e+03   # ~s_R
   2000004     1.42654382e+03   # ~c_R
   2000005     1.40782782e+03   # ~b_2
   2000006     1.41879935e+03   # ~t_2
   2000011     5.11970802e+02   # ~e_R
   2000013     5.11923868e+02   # ~mu_R
   2000015     7.48686278e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.00210670e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.98214770e-01   # N_{1,1}
  1  2    -8.06664815e-03   # N_{1,2}
  1  3     5.62695046e-02   # N_{1,3}
  1  4    -1.83288179e-02   # N_{1,4}
  2  1     1.60195289e-02   # N_{2,1}
  2  2     9.90365110e-01   # N_{2,2}
  2  3    -1.20750698e-01   # N_{2,3}
  2  4     6.58755831e-02   # N_{2,4}
  3  1    -2.64274488e-02   # N_{3,1}
  3  2     3.93093869e-02   # N_{3,2}
  3  3     7.04963380e-01   # N_{3,3}
  3  4     7.07660226e-01   # N_{3,4}
  4  1    -5.11100594e-02   # N_{4,1}
  4  2     1.32539240e-01   # N_{4,2}
  4  3     6.96620159e-01   # N_{4,3}
  4  4    -7.03236423e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.85132529e-01   # U_{1,1}
  1  2    -1.71796101e-01   # U_{1,2}
  2  1     1.71796101e-01   # U_{2,1}
  2  2     9.85132529e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.95564679e-01   # V_{1,1}
  1  2    -9.40795929e-02   # V_{1,2}
  2  1     9.40795929e-02   # V_{2,1}
  2  2     9.95564679e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     1.76677822e-01   # F_{11}
  1  2     9.84268737e-01   # F_{12}
  2  1     9.84268737e-01   # F_{21}
  2  2    -1.76677822e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     3.87290240e-01   # F_{11}
  1  2     9.21957846e-01   # F_{12}
  2  1     9.21957846e-01   # F_{21}
  2  2    -3.87290240e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     7.40860072e-02   # F_{11}
  1  2     9.97251856e-01   # F_{12}
  2  1     9.97251856e-01   # F_{21}
  2  2    -7.40860072e-02   # F_{22}
Block gauge Q= 1.21064805e+03  # SM gauge couplings
     1     3.62925554e-01   # g'(Q)MSSM DRbar
     2     6.41435485e-01   # g(Q)MSSM DRbar
     3     1.04842905e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.21064805e+03  
  3  3     8.52151475e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.21064805e+03  
  3  3     1.96428791e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.21064805e+03  
  3  3     1.50656353e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.21064805e+03 # Higgs mixing parameters
     1     8.71565097e+02    # mu(Q)MSSM DRbar
     2     1.44703564e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43741096e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     1.30816704e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.21064805e+03  # MSSM DRbar SUSY breaking parameters
     1     2.31054099e+02      # M_1(Q)
     2     4.26885290e+02      # M_2(Q)
     3     1.16096875e+03      # M_3(Q)
    21     4.80650332e+05      # mH1^2(Q)
    22    -7.33081035e+05      # mH2^2(Q)
    31     7.48885995e+02      # meL(Q)
    32     7.48870070e+02      # mmuL(Q)
    33     7.44004537e+02      # mtauL(Q)
    34     5.06910702e+02      # meR(Q)
    35     5.06863330e+02      # mmuR(Q)
    36     4.92221293e+02      # mtauR(Q)
    41     1.52040304e+03      # mqL1(Q)
    42     1.52039673e+03      # mqL2(Q)
    43     1.37304760e+03      # mqL3(Q)
    44     1.39180543e+03      # muR(Q)
    45     1.39180076e+03      # mcR(Q)
    46     1.05712282e+03      # mtR(Q)
    47     1.36060893e+03      # mdR(Q)
    48     1.36059947e+03      # msR(Q)
    49     1.34335702e+03      # mbR(Q)
Block au Q= 1.21064805e+03  
  1  1    -1.07296517e+03      # Au(Q)MSSM DRbar
  2  2    -1.07295981e+03      # Ac(Q)MSSM DRbar
  3  3    -8.55313037e+02      # At(Q)MSSM DRbar
Block ad Q= 1.21064805e+03  
  1  1    -1.27996180e+03      # Ad(Q)MSSM DRbar
  2  2    -1.27995438e+03      # As(Q)MSSM DRbar
  3  3    -1.19804919e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.21064805e+03  
  1  1    -2.40134814e+02      # Ae(Q)MSSM DRbar
  2  2    -2.40126637e+02      # Amu(Q)MSSM DRbar
  3  3    -2.37635338e+02      # Atau(Q)MSSM DRbar
