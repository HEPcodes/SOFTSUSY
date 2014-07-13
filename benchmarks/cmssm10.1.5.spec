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
     1    1.75000000e+02   # m0
     2    7.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.67790076e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.86741976e-04
# MX=1.67790076e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03934020e+01   # MW
        25     1.17040207e+02   # h0
        35     9.77203306e+02   # H0
        36     9.77000284e+02   # A0
        37     9.80512665e+02   # H+
   1000021     1.56472042e+03   # ~g
   1000022     2.91383729e+02   # ~neutralino(1)
   1000023     5.51268608e+02   # ~neutralino(2)
   1000024     5.51360730e+02   # ~chargino(1)
   1000025    -8.53787988e+02   # ~neutralino(3)
   1000035     8.65237047e+02   # ~neutralino(4)
   1000037     8.65432856e+02   # ~chargino(2)
   1000001     1.43572556e+03   # ~d_L
   1000002     1.43368235e+03   # ~u_L
   1000003     1.43572210e+03   # ~s_L
   1000004     1.43367889e+03   # ~c_L
   1000005     1.31647518e+03   # ~b_1
   1000006     1.10970144e+03   # ~t_1
   1000011     5.01771931e+02   # ~e_L
   1000012     4.95320224e+02   # ~nue_L
   1000013     5.01767460e+02   # ~mu_L
   1000014     4.95315697e+02   # ~numu_L
   1000015     3.11184639e+02   # ~stau_1
   1000016     4.93732401e+02   # ~nu_tau_L
   2000001     1.37264716e+03   # ~d_R
   2000002     1.37815906e+03   # ~u_R
   2000003     1.37264356e+03   # ~s_R
   2000004     1.37815535e+03   # ~c_R
   2000005     1.36710824e+03   # ~b_2
   2000006     1.35152557e+03   # ~t_2
   2000011     3.18456604e+02   # ~e_R
   2000013     3.18442312e+02   # ~mu_R
   2000015     5.01769936e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05491893e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97675634e-01   # N_{1,1}
  1  2    -9.67123272e-03   # N_{1,2}
  1  3     6.18910570e-02   # N_{1,3}
  1  4    -2.68196444e-02   # N_{1,4}
  2  1     2.25767951e-02   # N_{2,1}
  2  2     9.80061113e-01   # N_{2,2}
  2  3    -1.61744165e-01   # N_{2,3}
  2  4     1.13178307e-01   # N_{2,4}
  3  1    -2.43756923e-02   # N_{3,1}
  3  2     3.51992789e-02   # N_{3,2}
  3  3     7.05138297e-01   # N_{3,3}
  3  4     7.07775967e-01   # N_{3,4}
  4  1    -5.94932177e-02   # N_{4,1}
  4  2     1.95314346e-01   # N_{4,2}
  4  3     6.87596033e-01   # N_{4,3}
  4  4    -6.96795923e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.73075639e-01   # U_{1,1}
  1  2    -2.30486009e-01   # U_{1,2}
  2  1     2.30486009e-01   # U_{2,1}
  2  2     9.73075639e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86845617e-01   # V_{1,1}
  1  2    -1.61665480e-01   # V_{1,2}
  2  1     1.61665480e-01   # V_{2,1}
  2  2     9.86845617e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.48679726e-01   # F_{11}
  1  2     9.37241937e-01   # F_{12}
  2  1     9.37241937e-01   # F_{21}
  2  2    -3.48679726e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.85075428e-01   # F_{11}
  1  2     1.72123216e-01   # F_{12}
  2  1    -1.72123216e-01   # F_{21}
  2  2     9.85075428e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.00685290e-01   # F_{11}
  1  2     9.94918325e-01   # F_{12}
  2  1     9.94918325e-01   # F_{21}
  2  2    -1.00685290e-01   # F_{22}
Block gauge Q= 1.18926665e+03  # SM gauge couplings
     1     3.63062042e-01   # g'(Q)MSSM DRbar
     2     6.41314550e-01   # g(Q)MSSM DRbar
     3     1.04483359e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.18926665e+03  
  3  3     8.50684697e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.18926665e+03  
  3  3     1.33190049e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.18926665e+03  
  3  3     1.00319980e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.18926665e+03 # Higgs mixing parameters
     1     8.48266838e+02    # mu(Q)MSSM DRbar
     2     9.63740184e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43752791e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     9.88731850e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.18926665e+03  # MSSM DRbar SUSY breaking parameters
     1     2.97409295e+02      # M_1(Q)
     2     5.47600224e+02      # M_2(Q)
     3     1.52266574e+03      # M_3(Q)
    21     2.13366130e+05      # mH1^2(Q)
    22    -6.91376848e+05      # mH2^2(Q)
    31     4.92904758e+02      # meL(Q)
    32     4.92900214e+02      # mmuL(Q)
    33     4.91524341e+02      # mtauL(Q)
    34     3.10275173e+02      # meR(Q)
    35     3.10260490e+02      # mmuR(Q)
    36     3.05787702e+02      # mtauR(Q)
    41     1.38742509e+03      # mqL1(Q)
    42     1.38742157e+03      # mqL2(Q)
    43     1.27994992e+03      # mqL3(Q)
    44     1.33325162e+03      # muR(Q)
    45     1.33324785e+03      # mcR(Q)
    46     1.09931676e+03      # mtR(Q)
    47     1.32659022e+03      # mdR(Q)
    48     1.32658656e+03      # msR(Q)
    49     1.31993256e+03      # mbR(Q)
Block au Q= 1.18926665e+03  
  1  1    -1.54178086e+03      # Au(Q)MSSM DRbar
  2  2    -1.54177404e+03      # Ac(Q)MSSM DRbar
  3  3    -1.19569081e+03      # At(Q)MSSM DRbar
Block ad Q= 1.18926665e+03  
  1  1    -1.87905620e+03      # Ad(Q)MSSM DRbar
  2  2    -1.87904990e+03      # As(Q)MSSM DRbar
  3  3    -1.75760197e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.18926665e+03  
  1  1    -4.12743368e+02      # Ae(Q)MSSM DRbar
  2  2    -4.12736102e+02      # Amu(Q)MSSM DRbar
  3  3    -4.10536166e+02      # Atau(Q)MSSM DRbar
