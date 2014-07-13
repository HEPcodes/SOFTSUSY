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
     1    2.00000000e+02   # m0
     2    5.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.90436488e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=6.91612578e-04
# MX=1.90436488e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03961813e+01   # MW
        25     1.14915163e+02   # h0
        35     7.34346599e+02   # H0
        36     7.34057137e+02   # A0
        37     7.38712991e+02   # H+
   1000021     1.14926202e+03   # ~g
   1000022     2.04560117e+02   # ~neutralino(1)
   1000023     3.86569181e+02   # ~neutralino(2)
   1000024     3.86581560e+02   # ~chargino(1)
   1000025    -6.35557220e+02   # ~neutralino(3)
   1000035     6.49236546e+02   # ~neutralino(4)
   1000037     6.49557771e+02   # ~chargino(2)
   1000001     1.06658695e+03   # ~d_L
   1000002     1.06378142e+03   # ~u_L
   1000003     1.06658430e+03   # ~s_L
   1000004     1.06377876e+03   # ~c_L
   1000005     9.74450243e+02   # ~b_1
   1000006     8.10438871e+02   # ~t_1
   1000011     3.93674416e+02   # ~e_L
   1000012     3.85495584e+02   # ~nue_L
   1000013     3.93670559e+02   # ~mu_L
   1000014     3.85491647e+02   # ~numu_L
   1000015     2.70923944e+02   # ~stau_1
   1000016     3.84159425e+02   # ~nu_tau_L
   2000001     1.02261636e+03   # ~d_R
   2000002     1.02590032e+03   # ~u_R
   2000003     1.02261360e+03   # ~s_R
   2000004     1.02589749e+03   # ~c_R
   2000005     1.01898840e+03   # ~b_2
   2000006     1.01866291e+03   # ~t_2
   2000011     2.77579872e+02   # ~e_R
   2000013     2.77568760e+02   # ~mu_R
   2000015     3.94459201e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06643928e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95799215e-01   # N_{1,1}
  1  2    -1.74977159e-02   # N_{1,2}
  1  3     8.29946432e-02   # N_{1,3}
  1  4    -3.44911953e-02   # N_{1,4}
  2  1     3.81852649e-02   # N_{2,1}
  2  2     9.70343822e-01   # N_{2,2}
  2  3    -1.98481549e-01   # N_{2,3}
  2  4     1.32588938e-01   # N_{2,4}
  3  1    -3.32436272e-02   # N_{3,1}
  3  2     4.84096127e-02   # N_{3,2}
  3  3     7.03442055e-01   # N_{3,3}
  3  4     7.08322417e-01   # N_{3,4}
  4  1    -7.62933169e-02   # N_{4,1}
  4  2     2.36184685e-01   # N_{4,2}
  4  3     6.77411426e-01   # N_{4,3}
  4  4    -6.92466522e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.58757511e-01   # U_{1,1}
  1  2    -2.84225325e-01   # U_{1,2}
  2  1     2.84225325e-01   # U_{2,1}
  2  2     9.58757511e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.81681974e-01   # V_{1,1}
  1  2    -1.90526906e-01   # V_{1,2}
  2  1     1.90526906e-01   # V_{2,1}
  2  2     9.81681974e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.19837663e-01   # F_{11}
  1  2     9.07599216e-01   # F_{12}
  2  1     9.07599216e-01   # F_{21}
  2  2    -4.19837663e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.79709020e-01   # F_{11}
  1  2     2.00425136e-01   # F_{12}
  2  1    -2.00425136e-01   # F_{21}
  2  2     9.79709020e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.41766890e-01   # F_{11}
  1  2     9.89900070e-01   # F_{12}
  2  1     9.89900070e-01   # F_{21}
  2  2    -1.41766890e-01   # F_{22}
Block gauge Q= 8.80961416e+02  # SM gauge couplings
     1     3.62367712e-01   # g'(Q)MSSM DRbar
     2     6.42915589e-01   # g(Q)MSSM DRbar
     3     1.06063788e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.80961416e+02  
  3  3     8.61079312e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.80961416e+02  
  3  3     1.35314370e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.80961416e+02  
  3  3     1.00524638e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.80961416e+02 # Higgs mixing parameters
     1     6.30002617e+02    # mu(Q)MSSM DRbar
     2     9.67255568e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44095806e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     5.58455996e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.80961416e+02  # MSSM DRbar SUSY breaking parameters
     1     2.09313874e+02      # M_1(Q)
     2     3.88521123e+02      # M_2(Q)
     3     1.11326211e+03      # M_3(Q)
    21     1.32424678e+05      # mH1^2(Q)
    22    -3.83913867e+05      # mH2^2(Q)
    31     3.86766801e+02      # meL(Q)
    32     3.86762866e+02      # mmuL(Q)
    33     3.85575287e+02      # mtauL(Q)
    34     2.71213474e+02      # meR(Q)
    35     2.71202092e+02      # mmuR(Q)
    36     2.67750040e+02      # mtauR(Q)
    41     1.02951507e+03      # mqL1(Q)
    42     1.02951236e+03      # mqL2(Q)
    43     9.46561874e+02      # mqL3(Q)
    44     9.92026006e+02      # muR(Q)
    45     9.92023130e+02      # mcR(Q)
    46     8.11739804e+02      # mtR(Q)
    47     9.87495751e+02      # mdR(Q)
    48     9.87492938e+02      # msR(Q)
    49     9.82347984e+02      # mbR(Q)
Block au Q= 8.80961416e+02  
  1  1    -1.14046730e+03      # Au(Q)MSSM DRbar
  2  2    -1.14046218e+03      # Ac(Q)MSSM DRbar
  3  3    -8.79883465e+02      # At(Q)MSSM DRbar
Block ad Q= 8.80961416e+02  
  1  1    -1.39538805e+03      # Ad(Q)MSSM DRbar
  2  2    -1.39538330e+03      # As(Q)MSSM DRbar
  3  3    -1.30389600e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.80961416e+02  
  1  1    -2.99347845e+02      # Ae(Q)MSSM DRbar
  2  2    -2.99342468e+02      # Amu(Q)MSSM DRbar
  3  3    -2.97720388e+02      # Atau(Q)MSSM DRbar
