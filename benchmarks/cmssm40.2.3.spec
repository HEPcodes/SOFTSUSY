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
     3    4.00000000e+01   # tanb, DRbar, Feynman gauge
     4    1.00000000e+00   # sign(mu)
     1    6.00000000e+02   # m0
     2    5.50000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.88704685e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=7.86831927e-04
# MX=1.88704685e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03898002e+01   # MW
        25     1.17592595e+02   # h0
        35     7.31055246e+02   # H0
        36     7.31061225e+02   # A0
        37     7.35826144e+02   # H+
   1000021     1.27464343e+03   # ~g
   1000022     2.29843524e+02   # ~neutralino(1)
   1000023     4.38019457e+02   # ~neutralino(2)
   1000024     4.38150983e+02   # ~chargino(1)
   1000025    -7.50580981e+02   # ~neutralino(3)
   1000035     7.58908272e+02   # ~neutralino(4)
   1000037     7.59944097e+02   # ~chargino(2)
   1000001     1.28682531e+03   # ~d_L
   1000002     1.28451642e+03   # ~u_L
   1000003     1.28678697e+03   # ~s_L
   1000004     1.28447800e+03   # ~c_L
   1000005     1.06785062e+03   # ~b_1
   1000006     9.07726996e+02   # ~t_1
   1000011     7.03599192e+02   # ~e_L
   1000012     6.98786771e+02   # ~nue_L
   1000013     7.03420953e+02   # ~mu_L
   1000014     6.98607409e+02   # ~numu_L
   1000015     4.72234490e+02   # ~stau_1
   1000016     6.37428676e+02   # ~nu_tau_L
   2000001     1.24462179e+03   # ~d_R
   2000002     1.24793451e+03   # ~u_R
   2000003     1.24454602e+03   # ~s_R
   2000004     1.24792961e+03   # ~c_R
   2000005     1.14080215e+03   # ~b_2
   2000006     1.12642877e+03   # ~t_2
   2000011     6.35100592e+02   # ~e_R
   2000013     6.34701902e+02   # ~mu_R
   2000015     6.55518225e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59913337e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97437313e-01   # N_{1,1}
  1  2    -8.97889318e-03   # N_{1,2}
  1  3     6.73108488e-02   # N_{1,3}
  1  4    -2.25263331e-02   # N_{1,4}
  2  1     2.15730622e-02   # N_{2,1}
  2  2     9.82863414e-01   # N_{2,2}
  2  3    -1.57134320e-01   # N_{2,3}
  2  4     9.39303838e-02   # N_{2,4}
  3  1    -3.11251558e-02   # N_{3,1}
  3  2     4.56184436e-02   # N_{3,2}
  3  3     7.04199719e-01   # N_{3,3}
  3  4     7.07850930e-01   # N_{3,4}
  4  1    -6.07011880e-02   # N_{4,1}
  4  2     1.78375574e-01   # N_{4,2}
  4  3     6.89115964e-01   # N_{4,3}
  4  4    -6.99726167e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.74611983e-01   # U_{1,1}
  1  2    -2.23900608e-01   # U_{1,2}
  2  1     2.23900608e-01   # U_{2,1}
  2  2     9.74611983e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.90932740e-01   # V_{1,1}
  1  2    -1.34358866e-01   # V_{1,2}
  2  1     1.34358866e-01   # V_{2,1}
  2  2     9.90932740e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.16066285e-01   # F_{11}
  1  2     9.09334288e-01   # F_{12}
  2  1     9.09334288e-01   # F_{21}
  2  2    -4.16066285e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.88686010e-01   # F_{11}
  1  2     4.58516276e-01   # F_{12}
  2  1    -4.58516276e-01   # F_{21}
  2  2     8.88686010e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     2.82877210e-01   # F_{11}
  1  2     9.59156131e-01   # F_{12}
  2  1     9.59156131e-01   # F_{21}
  2  2    -2.82877210e-01   # F_{22}
Block gauge Q= 9.81988629e+02  # SM gauge couplings
     1     3.62276481e-01   # g'(Q)MSSM DRbar
     2     6.41583991e-01   # g(Q)MSSM DRbar
     3     1.05451469e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.81988629e+02  
  3  3     8.52295960e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.81988629e+02  
  3  3     4.95350717e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.81988629e+02  
  3  3     4.24636457e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.81988629e+02 # Higgs mixing parameters
     1     7.46396970e+02    # mu(Q)MSSM DRbar
     2     3.92051113e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43871732e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     6.83774740e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.81988629e+02  # MSSM DRbar SUSY breaking parameters
     1     2.32721355e+02      # M_1(Q)
     2     4.30923019e+02      # M_2(Q)
     3     1.21817699e+03      # M_3(Q)
    21    -1.33277371e+04      # mH1^2(Q)
    22    -5.46551865e+05      # mH2^2(Q)
    31     6.99420150e+02      # meL(Q)
    32     6.99240811e+02      # mmuL(Q)
    33     6.40398047e+02      # mtauL(Q)
    34     6.32007171e+02      # meR(Q)
    35     6.31606923e+02      # mmuR(Q)
    36     4.89396042e+02      # mtauR(Q)
    41     1.24910209e+03      # mqL1(Q)
    42     1.24906246e+03      # mqL2(Q)
    43     1.05429753e+03      # mqL3(Q)
    44     1.21280711e+03      # muR(Q)
    45     1.21280208e+03      # mcR(Q)
    46     9.08901042e+02      # mtR(Q)
    47     1.20847749e+03      # mdR(Q)
    48     1.20839966e+03      # msR(Q)
    49     1.09289275e+03      # mbR(Q)
Block au Q= 9.81988629e+02  
  1  1    -1.58110794e+03      # Au(Q)MSSM DRbar
  2  2    -1.58106983e+03      # Ac(Q)MSSM DRbar
  3  3    -1.09682641e+03      # At(Q)MSSM DRbar
Block ad Q= 9.81988629e+02  
  1  1    -1.83180539e+03      # Ad(Q)MSSM DRbar
  2  2    -1.83170833e+03      # As(Q)MSSM DRbar
  3  3    -1.53904015e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.81988629e+02  
  1  1    -6.43179960e+02      # Ae(Q)MSSM DRbar
  2  2    -6.42860058e+02      # Amu(Q)MSSM DRbar
  3  3    -5.37252116e+02      # Atau(Q)MSSM DRbar
