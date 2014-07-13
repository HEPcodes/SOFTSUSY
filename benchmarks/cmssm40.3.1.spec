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
     1    1.00000000e+03   # m0
     2    3.50000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.26520061e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=2.70010521e-04
# MX=2.26520061e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03936439e+01   # MW
        25     1.15481762e+02   # h0
        35     7.79921531e+02   # H0
        36     7.80058381e+02   # A0
        37     7.84327843e+02   # H+
   1000021     8.76446735e+02   # ~g
   1000022     1.44921590e+02   # ~neutralino(1)
   1000023     2.76971954e+02   # ~neutralino(2)
   1000024     2.77056208e+02   # ~chargino(1)
   1000025    -5.23713684e+02   # ~neutralino(3)
   1000035     5.34274106e+02   # ~neutralino(4)
   1000037     5.35756622e+02   # ~chargino(2)
   1000001     1.23232309e+03   # ~d_L
   1000002     1.22987704e+03   # ~u_L
   1000003     1.23227839e+03   # ~s_L
   1000004     1.22983225e+03   # ~c_L
   1000005     9.55151146e+02   # ~b_1
   1000006     7.84128403e+02   # ~t_1
   1000011     1.02430730e+03   # ~e_L
   1000012     1.02087154e+03   # ~nue_L
   1000013     1.02404763e+03   # ~mu_L
   1000014     1.02061108e+03   # ~numu_L
   1000015     8.23138206e+02   # ~stau_1
   1000016     9.36195255e+02   # ~nu_tau_L
   2000001     1.21640455e+03   # ~d_R
   2000002     1.21694885e+03   # ~u_R
   2000003     1.21631917e+03   # ~s_R
   2000004     1.21694306e+03   # ~c_R
   2000005     1.06985733e+03   # ~b_2
   2000006     9.92647693e+02   # ~t_2
   2000011     1.00826953e+03   # ~e_R
   2000013     1.00773997e+03   # ~mu_R
   2000015     9.43632223e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60337465e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.94739825e-01   # N_{1,1}
  1  2    -1.79039917e-02   # N_{1,2}
  1  3     9.64514618e-02   # N_{1,3}
  1  4    -2.94829176e-02   # N_{1,4}
  2  1     4.06541248e-02   # N_{2,1}
  2  2     9.71544435e-01   # N_{2,2}
  2  3    -2.04693309e-01   # N_{2,3}
  2  4     1.12023669e-01   # N_{2,4}
  3  1    -4.57413500e-02   # N_{3,1}
  3  2     6.78960838e-02   # N_{3,2}
  3  3     7.00928014e-01   # N_{3,3}
  3  4     7.08518009e-01   # N_{3,4}
  4  1    -8.21440860e-02   # N_{4,1}
  4  2     2.26210035e-01   # N_{4,2}
  4  3     6.76385750e-01   # N_{4,3}
  4  4    -6.96120453e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.56308489e-01   # U_{1,1}
  1  2    -2.92359493e-01   # U_{1,2}
  2  1     2.92359493e-01   # U_{2,1}
  2  2     9.56308489e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.87026169e-01   # V_{1,1}
  1  2    -1.60559462e-01   # V_{1,2}
  2  1     1.60559462e-01   # V_{2,1}
  2  2     9.87026169e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.42525390e-01   # F_{11}
  1  2     9.39508572e-01   # F_{12}
  2  1     9.39508572e-01   # F_{21}
  2  2    -3.42525390e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.78468045e-01   # F_{11}
  1  2     2.06398366e-01   # F_{12}
  2  1    -2.06398366e-01   # F_{21}
  2  2     9.78468045e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.82693866e-01   # F_{11}
  1  2     9.83169849e-01   # F_{12}
  2  1     9.83169849e-01   # F_{21}
  2  2    -1.82693866e-01   # F_{22}
Block gauge Q= 8.61233316e+02  # SM gauge couplings
     1     3.61776397e-01   # g'(Q)MSSM DRbar
     2     6.42807665e-01   # g(Q)MSSM DRbar
     3     1.06554317e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.61233316e+02  
  3  3     8.61790682e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.61233316e+02  
  3  3     5.19023553e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.61233316e+02  
  3  3     4.12499578e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.61233316e+02 # Higgs mixing parameters
     1     5.15743791e+02    # mu(Q)MSSM DRbar
     2     3.92587993e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43876804e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     7.33585375e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.61233316e+02  # MSSM DRbar SUSY breaking parameters
     1     1.46718304e+02      # M_1(Q)
     2     2.73432414e+02      # M_2(Q)
     3     7.89157469e+02      # M_3(Q)
    21     3.60141648e+05      # mH1^2(Q)
    22    -2.57403542e+05      # mH2^2(Q)
    31     1.02169229e+03      # meL(Q)
    32     1.02143271e+03      # mmuL(Q)
    33     9.39096089e+02      # mtauL(Q)
    34     1.00623656e+03      # meR(Q)
    35     1.00570671e+03      # mmuR(Q)
    36     8.28418592e+02      # mtauR(Q)
    41     1.21014104e+03      # mqL1(Q)
    42     1.21009561e+03      # mqL2(Q)
    43     9.41675747e+02      # mqL3(Q)
    44     1.19785187e+03      # muR(Q)
    45     1.19784598e+03      # mcR(Q)
    46     7.75201592e+02      # mtR(Q)
    47     1.19651844e+03      # mdR(Q)
    48     1.19643156e+03      # msR(Q)
    49     1.04743680e+03      # mbR(Q)
Block au Q= 8.61233316e+02  
  1  1    -1.14580108e+03      # Au(Q)MSSM DRbar
  2  2    -1.14577126e+03      # Ac(Q)MSSM DRbar
  3  3    -7.59308945e+02      # At(Q)MSSM DRbar
Block ad Q= 8.61233316e+02  
  1  1    -1.33448010e+03      # Ad(Q)MSSM DRbar
  2  2    -1.33440416e+03      # As(Q)MSSM DRbar
  3  3    -1.09389591e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.61233316e+02  
  1  1    -5.52822968e+02      # Ae(Q)MSSM DRbar
  2  2    -5.52530709e+02      # Amu(Q)MSSM DRbar
  3  3    -4.61867859e+02      # Atau(Q)MSSM DRbar
