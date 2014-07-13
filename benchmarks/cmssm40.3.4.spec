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
     1    1.15000000e+03   # m0
     2    4.25000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.12822133e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=3.39363362e-04
# MX=2.12822133e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03913929e+01   # MW
        25     1.16569483e+02   # h0
        35     9.02152719e+02   # H0
        36     9.02262388e+02   # A0
        37     9.05991888e+02   # H+
   1000021     1.04501980e+03   # ~g
   1000022     1.77577893e+02   # ~neutralino(1)
   1000023     3.39304378e+02   # ~neutralino(2)
   1000024     3.39407175e+02   # ~chargino(1)
   1000025    -5.96240630e+02   # ~neutralino(3)
   1000035     6.06782920e+02   # ~neutralino(4)
   1000037     6.07960539e+02   # ~chargino(2)
   1000001     1.43785714e+03   # ~d_L
   1000002     1.43578665e+03   # ~u_L
   1000003     1.43780712e+03   # ~s_L
   1000004     1.43573655e+03   # ~c_L
   1000005     1.12662288e+03   # ~b_1
   1000006     9.33638571e+02   # ~t_1
   1000011     1.18111796e+03   # ~e_L
   1000012     1.17810027e+03   # ~nue_L
   1000013     1.18082682e+03   # ~mu_L
   1000014     1.17780846e+03   # ~numu_L
   1000015     9.52308878e+02   # ~stau_1
   1000016     1.08256046e+03   # ~nu_tau_L
   2000001     1.41775088e+03   # ~d_R
   2000002     1.41882932e+03   # ~u_R
   2000003     1.41765528e+03   # ~s_R
   2000004     1.41882281e+03   # ~c_R
   2000005     1.25099827e+03   # ~b_2
   2000006     1.15883627e+03   # ~t_2
   2000011     1.16036970e+03   # ~e_R
   2000013     1.15977481e+03   # ~mu_R
   2000015     1.08898360e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59457971e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95885796e-01   # N_{1,1}
  1  2    -1.38327579e-02   # N_{1,2}
  1  3     8.51454034e-02   # N_{1,3}
  1  4    -2.77560182e-02   # N_{1,4}
  2  1     3.30688789e-02   # N_{2,1}
  2  2     9.74415404e-01   # N_{2,2}
  2  3    -1.91887466e-01   # N_{2,3}
  2  4     1.12250928e-01   # N_{2,4}
  3  1    -3.95174972e-02   # N_{3,1}
  3  2     5.80999049e-02   # N_{3,2}
  3  3     7.02508378e-01   # N_{3,3}
  3  4     7.08198240e-01   # N_{3,4}
  4  1    -7.45405803e-02   # N_{4,1}
  4  2     2.16674126e-01   # N_{4,2}
  4  3     6.80008411e-01   # N_{4,3}
  4  4    -6.96480140e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.61785994e-01   # U_{1,1}
  1  2    -2.73802305e-01   # U_{1,2}
  2  1     2.73802305e-01   # U_{2,1}
  2  2     9.61785994e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86997398e-01   # V_{1,1}
  1  2    -1.60736232e-01   # V_{1,2}
  2  1     1.60736232e-01   # V_{2,1}
  2  2     9.86997398e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.06491506e-01   # F_{11}
  1  2     9.51873393e-01   # F_{12}
  2  1     9.51873393e-01   # F_{21}
  2  2    -3.06491506e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.83053708e-01   # F_{11}
  1  2     1.83317778e-01   # F_{12}
  2  1    -1.83317778e-01   # F_{21}
  2  2     9.83053708e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.58190800e-01   # F_{11}
  1  2     9.87408563e-01   # F_{12}
  2  1     9.87408563e-01   # F_{21}
  2  2    -1.58190800e-01   # F_{22}
Block gauge Q= 1.01597921e+03  # SM gauge couplings
     1     3.62147675e-01   # g'(Q)MSSM DRbar
     2     6.41963782e-01   # g(Q)MSSM DRbar
     3     1.05665842e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.01597921e+03  
  3  3     8.55903574e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.01597921e+03  
  3  3     5.16712634e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.01597921e+03  
  3  3     4.12829303e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.01597921e+03 # Higgs mixing parameters
     1     5.88389321e+02    # mu(Q)MSSM DRbar
     2     3.92187799e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43665963e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     9.80451971e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.01597921e+03  # MSSM DRbar SUSY breaking parameters
     1     1.79435950e+02      # M_1(Q)
     2     3.32931573e+02      # M_2(Q)
     3     9.45469909e+02      # M_3(Q)
    21     4.90100642e+05      # mH1^2(Q)
    22    -3.31665528e+05      # mH2^2(Q)
    31     1.17826158e+03      # meL(Q)
    32     1.17797058e+03      # mmuL(Q)
    33     1.08512605e+03      # mtauL(Q)
    34     1.15825158e+03      # meR(Q)
    35     1.15765648e+03      # mmuR(Q)
    36     9.57559512e+02      # mtauR(Q)
    41     1.41174316e+03      # mqL1(Q)
    42     1.41169227e+03      # mqL2(Q)
    43     1.10917952e+03      # mqL3(Q)
    44     1.39583362e+03      # muR(Q)
    45     1.39582698e+03      # mcR(Q)
    46     9.19972395e+02      # mtR(Q)
    47     1.39406855e+03      # mdR(Q)
    48     1.39397115e+03      # msR(Q)
    49     1.22584818e+03      # mbR(Q)
Block au Q= 1.01597921e+03  
  1  1    -1.30190596e+03      # Au(Q)MSSM DRbar
  2  2    -1.30187333e+03      # Ac(Q)MSSM DRbar
  3  3    -8.79634082e+02      # At(Q)MSSM DRbar
Block ad Q= 1.01597921e+03  
  1  1    -1.50811753e+03      # Ad(Q)MSSM DRbar
  2  2    -1.50803445e+03      # As(Q)MSSM DRbar
  3  3    -1.24473335e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.01597921e+03  
  1  1    -5.82686298e+02      # Ae(Q)MSSM DRbar
  2  2    -5.82384801e+02      # Amu(Q)MSSM DRbar
  3  3    -4.88501076e+02      # Atau(Q)MSSM DRbar
