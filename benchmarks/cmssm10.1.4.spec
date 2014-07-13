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
     1    1.62500000e+02   # m0
     2    6.50000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.71847297e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.46892536e-04
# MX=1.71847297e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03938778e+01   # MW
        25     1.16587334e+02   # h0
        35     9.13245937e+02   # H0
        36     9.13029507e+02   # A0
        37     9.16777369e+02   # H+
   1000021     1.46095547e+03   # ~g
   1000022     2.69508474e+02   # ~neutralino(1)
   1000023     5.09957104e+02   # ~neutralino(2)
   1000024     5.10036347e+02   # ~chargino(1)
   1000025    -8.00033494e+02   # ~neutralino(3)
   1000035     8.11933267e+02   # ~neutralino(4)
   1000037     8.12151360e+02   # ~chargino(2)
   1000001     1.34148423e+03   # ~d_L
   1000002     1.33928645e+03   # ~u_L
   1000003     1.34148099e+03   # ~s_L
   1000004     1.33928321e+03   # ~c_L
   1000005     1.22965301e+03   # ~b_1
   1000006     1.03423033e+03   # ~t_1
   1000011     4.66794967e+02   # ~e_L
   1000012     4.59873228e+02   # ~nue_L
   1000013     4.66790794e+02   # ~mu_L
   1000014     4.59868994e+02   # ~numu_L
   1000015     2.89082769e+02   # ~stau_1
   1000016     4.58388082e+02   # ~nu_tau_L
   2000001     1.28307313e+03   # ~d_R
   2000002     1.28804487e+03   # ~u_R
   2000003     1.28306975e+03   # ~s_R
   2000004     1.28804139e+03   # ~c_R
   2000005     1.27806418e+03   # ~b_2
   2000006     1.26686215e+03   # ~t_2
   2000011     2.96258030e+02   # ~e_R
   2000013     2.96244689e+02   # ~mu_R
   2000015     4.67034794e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05698099e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97360034e-01   # N_{1,1}
  1  2    -1.10117993e-02   # N_{1,2}
  1  3     6.59546800e-02   # N_{1,3}
  1  4    -2.83140090e-02   # N_{1,4}
  2  1     2.53147372e-02   # N_{2,1}
  2  2     9.78267960e-01   # N_{2,2}
  2  3    -1.69164747e-01   # N_{2,3}
  2  4     1.17193222e-01   # N_{2,4}
  3  1    -2.60985603e-02   # N_{3,1}
  3  2     3.77592969e-02   # N_{3,2}
  3  3     7.04849288e-01   # N_{3,3}
  3  4     7.07870456e-01   # N_{3,4}
  4  1    -6.28569159e-02   # N_{4,1}
  4  2     2.03579898e-01   # N_{4,2}
  4  3     6.85726440e-01   # N_{4,3}
  4  4    -6.95976640e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.70473612e-01   # U_{1,1}
  1  2    -2.41207315e-01   # U_{1,2}
  2  1     2.41207315e-01   # U_{2,1}
  2  2     9.70473612e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.85869094e-01   # V_{1,1}
  1  2    -1.67517547e-01   # V_{1,2}
  2  1     1.67517547e-01   # V_{2,1}
  2  2     9.85869094e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.65959074e-01   # F_{11}
  1  2     9.30630945e-01   # F_{12}
  2  1     9.30630945e-01   # F_{21}
  2  2    -3.65959074e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.83401547e-01   # F_{11}
  1  2     1.81442545e-01   # F_{12}
  2  1    -1.81442545e-01   # F_{21}
  2  2     9.83401547e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.08724978e-01   # F_{11}
  1  2     9.94071868e-01   # F_{12}
  2  1     9.94071868e-01   # F_{21}
  2  2    -1.08724978e-01   # F_{22}
Block gauge Q= 1.11123522e+03  # SM gauge couplings
     1     3.62920031e-01   # g'(Q)MSSM DRbar
     2     6.41682884e-01   # g(Q)MSSM DRbar
     3     1.04832148e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.11123522e+03  
  3  3     8.52957186e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.11123522e+03  
  3  3     1.33649124e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.11123522e+03  
  3  3     1.00367690e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.11123522e+03 # Higgs mixing parameters
     1     7.94580924e+02    # mu(Q)MSSM DRbar
     2     9.64525136e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43828707e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     8.63715718e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.11123522e+03  # MSSM DRbar SUSY breaking parameters
     1     2.75273084e+02      # M_1(Q)
     2     5.07741332e+02      # M_2(Q)
     3     1.42112123e+03      # M_3(Q)
    21     1.84088578e+05      # mH1^2(Q)
    22    -6.07500407e+05      # mH2^2(Q)
    31     4.58313586e+02      # meL(Q)
    32     4.58309342e+02      # mmuL(Q)
    33     4.57025313e+02      # mtauL(Q)
    34     2.88221780e+02      # meR(Q)
    35     2.88208052e+02      # mmuR(Q)
    36     2.84029687e+02      # mtauR(Q)
    41     1.29598971e+03      # mqL1(Q)
    42     1.29598641e+03      # mqL2(Q)
    43     1.19534839e+03      # mqL3(Q)
    44     1.24587613e+03      # muR(Q)
    45     1.24587260e+03      # mcR(Q)
    46     1.02690595e+03      # mtR(Q)
    47     1.23973596e+03      # mdR(Q)
    48     1.23973253e+03      # msR(Q)
    49     1.23348378e+03      # mbR(Q)
Block au Q= 1.11123522e+03  
  1  1    -1.44272377e+03      # Au(Q)MSSM DRbar
  2  2    -1.44271736e+03      # Ac(Q)MSSM DRbar
  3  3    -1.11761550e+03      # At(Q)MSSM DRbar
Block ad Q= 1.11123522e+03  
  1  1    -1.75982246e+03      # Ad(Q)MSSM DRbar
  2  2    -1.75981654e+03      # As(Q)MSSM DRbar
  3  3    -1.64571968e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.11123522e+03  
  1  1    -3.84552454e+02      # Ae(Q)MSSM DRbar
  2  2    -3.84545654e+02      # Amu(Q)MSSM DRbar
  3  3    -3.82488517e+02      # Atau(Q)MSSM DRbar
