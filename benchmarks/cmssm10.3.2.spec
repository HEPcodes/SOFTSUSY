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
     1    3.50000000e+02   # m0
     2    5.25000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.92117710e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=7.57988812e-04
# MX=1.92117710e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03950360e+01   # MW
        25     1.15295774e+02   # h0
        35     8.15776428e+02   # H0
        36     8.15465791e+02   # A0
        37     8.19753920e+02   # H+
   1000021     1.20846387e+03   # ~g
   1000022     2.16027965e+02   # ~neutralino(1)
   1000023     4.08482374e+02   # ~neutralino(2)
   1000024     4.08509196e+02   # ~chargino(1)
   1000025    -6.63267286e+02   # ~neutralino(3)
   1000035     6.76696304e+02   # ~neutralino(4)
   1000037     6.76978255e+02   # ~chargino(2)
   1000001     1.14868222e+03   # ~d_L
   1000002     1.14609594e+03   # ~u_L
   1000003     1.14867924e+03   # ~s_L
   1000004     1.14609296e+03   # ~c_L
   1000005     1.04385548e+03   # ~b_1
   1000006     8.66905766e+02   # ~t_1
   1000011     4.97827610e+02   # ~e_L
   1000012     4.91298990e+02   # ~nue_L
   1000013     4.97822069e+02   # ~mu_L
   1000014     4.91293379e+02   # ~numu_L
   1000015     3.96928207e+02   # ~stau_1
   1000016     4.89475699e+02   # ~nu_tau_L
   2000001     1.10428597e+03   # ~d_R
   2000002     1.10771825e+03   # ~u_R
   2000003     1.10428289e+03   # ~s_R
   2000004     1.10771505e+03   # ~c_R
   2000005     1.09953234e+03   # ~b_2
   2000006     1.08349719e+03   # ~t_2
   2000011     4.03403463e+02   # ~e_R
   2000013     4.03389611e+02   # ~mu_R
   2000015     4.97677644e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06063528e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96136227e-01   # N_{1,1}
  1  2    -1.60423986e-02   # N_{1,2}
  1  3     7.96362118e-02   # N_{1,3}
  1  4    -3.33666487e-02   # N_{1,4}
  2  1     3.54783932e-02   # N_{2,1}
  2  2     9.71771774e-01   # N_{2,2}
  2  3    -1.93399356e-01   # N_{2,3}
  2  4     1.30374810e-01   # N_{2,4}
  3  1    -3.17958896e-02   # N_{3,1}
  3  2     4.62063414e-02   # N_{3,2}
  3  3     7.03764010e-01   # N_{3,3}
  3  4     7.08216219e-01   # N_{3,4}
  4  1    -7.37761686e-02   # N_{4,1}
  4  2     2.30796954e-01   # N_{4,2}
  4  3     6.78948437e-01   # N_{4,3}
  4  4    -6.93050404e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.60861646e-01   # U_{1,1}
  1  2    -2.77028692e-01   # U_{1,2}
  2  1     2.77028692e-01   # U_{2,1}
  2  2     9.60861646e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.82271015e-01   # V_{1,1}
  1  2    -1.87466405e-01   # V_{1,2}
  2  1     1.87466405e-01   # V_{2,1}
  2  2     9.82271015e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.89099944e-01   # F_{11}
  1  2     9.21195546e-01   # F_{12}
  2  1     9.21195546e-01   # F_{21}
  2  2    -3.89099944e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.88025159e-01   # F_{11}
  1  2     1.54292858e-01   # F_{12}
  2  1    -1.54292858e-01   # F_{21}
  2  2     9.88025159e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.34567999e-01   # F_{11}
  1  2     9.90904362e-01   # F_{12}
  2  1     9.90904362e-01   # F_{21}
  2  2    -1.34567999e-01   # F_{22}
Block gauge Q= 9.39845476e+02  # SM gauge couplings
     1     3.62388176e-01   # g'(Q)MSSM DRbar
     2     6.42474282e-01   # g(Q)MSSM DRbar
     3     1.05746412e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.39845476e+02  
  3  3     8.59241729e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.39845476e+02  
  3  3     1.35016872e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.39845476e+02  
  3  3     1.00391897e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.39845476e+02 # Higgs mixing parameters
     1     6.57541231e+02    # mu(Q)MSSM DRbar
     2     9.66452341e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44003864e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     6.87279313e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.39845476e+02  # MSSM DRbar SUSY breaking parameters
     1     2.20343590e+02      # M_1(Q)
     2     4.08443508e+02      # M_2(Q)
     3     1.16409254e+03      # M_3(Q)
    21     2.20900375e+05      # mH1^2(Q)
    22    -4.15901365e+05      # mH2^2(Q)
    31     4.92130365e+02      # meL(Q)
    32     4.92124745e+02      # mmuL(Q)
    33     4.90429690e+02      # mtauL(Q)
    34     3.98915631e+02      # meR(Q)
    35     3.98901627e+02      # mmuR(Q)
    36     3.94661393e+02      # mtauR(Q)
    41     1.11001881e+03      # mqL1(Q)
    42     1.11001577e+03      # mqL2(Q)
    43     1.01395875e+03      # mqL3(Q)
    44     1.07208767e+03      # muR(Q)
    45     1.07208441e+03      # mcR(Q)
    46     8.63039402e+02      # mtR(Q)
    47     1.06750515e+03      # mdR(Q)
    48     1.06750201e+03      # msR(Q)
    49     1.06172401e+03      # mbR(Q)
Block au Q= 9.39845476e+02  
  1  1    -1.18992612e+03      # Au(Q)MSSM DRbar
  2  2    -1.18992079e+03      # Ac(Q)MSSM DRbar
  3  3    -9.18657653e+02      # At(Q)MSSM DRbar
Block ad Q= 9.39845476e+02  
  1  1    -1.45511221e+03      # Ad(Q)MSSM DRbar
  2  2    -1.45510728e+03      # As(Q)MSSM DRbar
  3  3    -1.35986987e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.39845476e+02  
  1  1    -3.13508245e+02      # Ae(Q)MSSM DRbar
  2  2    -3.13502631e+02      # Amu(Q)MSSM DRbar
  3  3    -3.11810950e+02      # Atau(Q)MSSM DRbar
