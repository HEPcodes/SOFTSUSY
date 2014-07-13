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
     1    4.50000000e+04   # lambda
     2    9.00000000e+04   # M_mess
     5    3.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=4.13376859e-04
# MX=9.00000000e+04 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04022028e+01   # MW
        25     1.12043794e+02   # h0
        35     4.31797595e+02   # H0
        36     4.31486991e+02   # A0
        37     4.39152449e+02   # H+
   1000021     1.05245695e+03   # ~g
   1000022     1.84859547e+02   # ~neutralino(1)
   1000023     3.04851007e+02   # ~neutralino(2)
   1000024     3.01861042e+02   # ~chargino(1)
   1000025    -3.48795963e+02   # ~neutralino(3)
   1000035     4.24312691e+02   # ~neutralino(4)
   1000037     4.24054745e+02   # ~chargino(2)
   1000039     9.59850000e-10   # ~gravitino
   1000001     1.00383710e+03   # ~d_L
   1000002     1.00081431e+03   # ~u_L
   1000003     1.00383584e+03   # ~s_L
   1000004     1.00081305e+03   # ~c_L
   1000005     9.55685719e+02   # ~b_1
   1000006     8.95299163e+02   # ~t_1
   1000011     2.94135214e+02   # ~e_L
   1000012     2.82913712e+02   # ~nue_L
   1000013     2.94134036e+02   # ~mu_L
   1000014     2.82912488e+02   # ~numu_L
   1000015     1.39381084e+02   # ~stau_1
   1000016     2.82353103e+02   # ~nu_tau_L
   2000001     9.64096472e+02   # ~d_R
   2000002     9.65952831e+02   # ~u_R
   2000003     9.64094709e+02   # ~s_R
   2000004     9.65951932e+02   # ~c_R
   2000005     9.71063377e+02   # ~b_2
   2000006     9.86096578e+02   # ~t_2
   2000011     1.45768252e+02   # ~e_R
   2000013     1.45763426e+02   # ~mu_R
   2000015     2.95710588e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.69038419e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.71225673e-01   # N_{1,1}
  1  2    -5.39598298e-02   # N_{1,2}
  1  3     2.00087467e-01   # N_{1,3}
  1  4    -1.17362832e-01   # N_{1,4}
  2  1    -2.12026392e-01   # N_{2,1}
  2  2    -6.13822090e-01   # N_{2,2}
  2  3     5.65302716e-01   # N_{2,3}
  2  4    -5.08625688e-01   # N_{2,4}
  3  1    -5.38952657e-02   # N_{3,1}
  3  2     7.26909673e-02   # N_{3,2}
  3  3     6.97921802e-01   # N_{3,3}
  3  4     7.10434010e-01   # N_{3,4}
  4  1    -9.41318304e-02   # N_{4,1}
  4  2     7.84236445e-01   # N_{4,2}
  4  3     3.91539275e-01   # N_{4,3}
  4  4    -4.72026898e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1    -5.51746024e-01   # U_{1,1}
  1  2     8.34012185e-01   # U_{1,2}
  2  1    -8.34012185e-01   # U_{2,1}
  2  2    -5.51746024e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1    -6.66166290e-01   # V_{1,1}
  1  2     7.45803240e-01   # V_{1,2}
  2  1    -7.45803240e-01   # V_{2,1}
  2  2    -6.66166290e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.32990965e-01   # F_{11}
  1  2     9.42930017e-01   # F_{12}
  2  1     9.42930017e-01   # F_{21}
  2  2    -3.32990965e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     5.36917936e-01   # F_{11}
  1  2     8.43634476e-01   # F_{12}
  2  1     8.43634476e-01   # F_{21}
  2  2    -5.36917936e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.35388821e-01   # F_{11}
  1  2     9.90792545e-01   # F_{12}
  2  1     9.90792545e-01   # F_{21}
  2  2    -1.35388821e-01   # F_{22}
Block gauge Q= 9.11118102e+02  # SM gauge couplings
     1     3.62885651e-01   # g'(Q)MSSM DRbar
     2     6.44415091e-01   # g(Q)MSSM DRbar
     3     1.06221077e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.11118102e+02  
  3  3     8.64761316e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.11118102e+02  
  3  3     2.05023651e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.11118102e+02  
  3  3     1.51999677e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.11118102e+02 # Higgs mixing parameters
     1     3.39955788e+02    # mu(Q)MSSM DRbar
     2     1.45173631e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43796736e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     2.12500507e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.11118102e+02  # MSSM DRbar SUSY breaking parameters
     1     1.94940792e+02      # M_1(Q)
     2     3.67497827e+02      # M_2(Q)
     3     1.00341291e+03      # M_3(Q)
    21     7.05631825e+04      # mH1^2(Q)
    22    -1.02349621e+05      # mH2^2(Q)
    31     2.85058009e+02      # meL(Q)
    32     2.85056798e+02      # mmuL(Q)
    33     2.84684244e+02      # mtauL(Q)
    34     1.33835481e+02      # meR(Q)
    35     1.33830237e+02      # mmuR(Q)
    36     1.32208675e+02      # mtauR(Q)
    41     9.65416695e+02      # mqL1(Q)
    42     9.65415395e+02      # mqL2(Q)
    43     9.34578217e+02      # mqL3(Q)
    44     9.30612581e+02      # muR(Q)
    45     9.30611661e+02      # mcR(Q)
    46     8.67983469e+02      # mtR(Q)
    47     9.27470552e+02      # mdR(Q)
    48     9.27468743e+02      # msR(Q)
    49     9.23947213e+02      # mbR(Q)
Block au Q= 9.11118102e+02  
  1  1    -3.03324756e+02      # Au(Q)MSSM DRbar
  2  2    -3.03324327e+02      # Ac(Q)MSSM DRbar
  3  3    -2.85892709e+02      # At(Q)MSSM DRbar
Block ad Q= 9.11118102e+02  
  1  1    -3.22735694e+02      # Ad(Q)MSSM DRbar
  2  2    -3.22735096e+02      # As(Q)MSSM DRbar
  3  3    -3.16164581e+02      # Ab(Q)MSSM DRbar
Block ae Q= 9.11118102e+02  
  1  1    -3.07533618e+01      # Ae(Q)MSSM DRbar
  2  2    -3.07531374e+01      # Amu(Q)MSSM DRbar
  3  3    -3.06841972e+01      # Atau(Q)MSSM DRbar
