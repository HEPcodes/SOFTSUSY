# SOFTSUSY3.4.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.1       # version number
     3   # Warning: stau LSP
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
     1    3.75000000e+02   # m0
     2    6.50000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.71624068e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=9.24513280e-05
# MX=1.71624068e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03886885e+01   # MW
        25     1.18305472e+02   # h0
        35     7.58165603e+02   # H0
        36     7.58170463e+02   # A0
        37     7.62714833e+02   # H+
   1000021     1.46727872e+03   # ~g
   1000022     2.72324045e+02   # ~neutralino(1)
   1000023     5.18125064e+02   # ~neutralino(2)
   1000024     5.18266344e+02   # ~chargino(1)
   1000025    -8.60816740e+02   # ~neutralino(3)
   1000035     8.68431967e+02   # ~neutralino(4)
   1000037     8.69332069e+02   # ~chargino(2)
   1000001     1.38375652e+03   # ~d_L
   1000002     1.38158867e+03   # ~u_L
   1000003     1.38371842e+03   # ~s_L
   1000004     1.38155050e+03   # ~c_L
   1000005     1.16925903e+03   # ~b_1
   1000006     1.01167516e+03   # ~t_1
   1000011     5.75708694e+02   # ~e_L
   1000012     5.69951318e+02   # ~nue_L
   1000013     5.75567567e+02   # ~mu_L
   1000014     5.69808869e+02   # ~numu_L
   1000015     2.72312920e+02   # ~stau_1
   1000016     5.20556665e+02   # ~nu_tau_L
   2000001     1.32750271e+03   # ~d_R
   2000002     1.33228473e+03   # ~u_R
   2000003     1.32742692e+03   # ~s_R
   2000004     1.33227991e+03   # ~c_R
   2000005     1.23481787e+03   # ~b_2
   2000006     1.23565493e+03   # ~t_2
   2000011     4.48955354e+02   # ~e_R
   2000013     4.48587863e+02   # ~mu_R
   2000015     5.45986779e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60025458e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.98034200e-01   # N_{1,1}
  1  2    -6.88737559e-03   # N_{1,2}
  1  3     5.88846044e-02   # N_{1,3}
  1  4    -2.03200401e-02   # N_{1,4}
  2  1     1.69707196e-02   # N_{2,1}
  2  2     9.85825357e-01   # N_{2,2}
  2  3    -1.42128779e-01   # N_{2,3}
  2  4     8.75201115e-02   # N_{2,4}
  3  1    -2.69115786e-02   # N_{3,1}
  3  2     3.92670683e-02   # N_{3,2}
  3  3     7.04925393e-01   # N_{3,3}
  3  4     7.07682170e-01   # N_{3,4}
  4  1    -5.39953537e-02   # N_{4,1}
  4  2     1.62969403e-01   # N_{4,2}
  4  3     6.92395988e-01   # N_{4,3}
  4  4    -7.00794743e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.79329709e-01   # U_{1,1}
  1  2    -2.02270416e-01   # U_{1,2}
  2  1     2.02270416e-01   # U_{2,1}
  2  2     9.79329709e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.92159509e-01   # V_{1,1}
  1  2    -1.24978034e-01   # V_{1,2}
  2  1     1.24978034e-01   # V_{2,1}
  2  2     9.92159509e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.17852060e-01   # F_{11}
  1  2     9.08515083e-01   # F_{12}
  2  1     9.08515083e-01   # F_{21}
  2  2    -4.17852060e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.08968056e-01   # F_{11}
  1  2     5.87852605e-01   # F_{12}
  2  1    -5.87852605e-01   # F_{21}
  2  2     8.08968056e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     3.02979577e-01   # F_{11}
  1  2     9.52997049e-01   # F_{12}
  2  1     9.52997049e-01   # F_{21}
  2  2    -3.02979577e-01   # F_{22}
Block gauge Q= 1.08706751e+03  # SM gauge couplings
     1     3.62685103e-01   # g'(Q)MSSM DRbar
     2     6.41137394e-01   # g(Q)MSSM DRbar
     3     1.04857629e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.08706751e+03  
  3  3     8.48084965e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.08706751e+03  
  3  3     4.89857558e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.08706751e+03  
  3  3     4.27949274e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.08706751e+03 # Higgs mixing parameters
     1     8.57820294e+02    # mu(Q)MSSM DRbar
     2     3.91756859e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43730983e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     7.28571836e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.08706751e+03  # MSSM DRbar SUSY breaking parameters
     1     2.76578065e+02      # M_1(Q)
     2     5.10367832e+02      # M_2(Q)
     3     1.42573057e+03      # M_3(Q)
    21    -1.63037052e+05      # mH1^2(Q)
    22    -7.21536505e+05      # mH2^2(Q)
    31     5.68931001e+02      # meL(Q)
    32     5.68787795e+02      # mmuL(Q)
    33     5.22691091e+02      # mtauL(Q)
    34     4.43880527e+02      # meR(Q)
    35     4.43508794e+02      # mmuR(Q)
    36     3.07250171e+02      # mtauR(Q)
    41     1.34026173e+03      # mqL1(Q)
    42     1.34022289e+03      # mqL2(Q)
    43     1.16072895e+03      # mqL3(Q)
    44     1.29200539e+03      # muR(Q)
    45     1.29200049e+03      # mcR(Q)
    46     1.01384518e+03      # mtR(Q)
    47     1.28614682e+03      # mdR(Q)
    48     1.28606980e+03      # msR(Q)
    49     1.17582454e+03      # mbR(Q)
Block au Q= 1.08706751e+03  
  1  1    -1.78771004e+03      # Au(Q)MSSM DRbar
  2  2    -1.78766812e+03      # Ac(Q)MSSM DRbar
  3  3    -1.25732899e+03      # At(Q)MSSM DRbar
Block ad Q= 1.08706751e+03  
  1  1    -2.06512585e+03      # Ad(Q)MSSM DRbar
  2  2    -2.06501911e+03      # As(Q)MSSM DRbar
  3  3    -1.74609834e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.08706751e+03  
  1  1    -6.86175655e+02      # Ae(Q)MSSM DRbar
  2  2    -6.85842622e+02      # Amu(Q)MSSM DRbar
  3  3    -5.74008094e+02      # Atau(Q)MSSM DRbar
