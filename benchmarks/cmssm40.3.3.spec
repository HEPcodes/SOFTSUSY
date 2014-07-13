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
     1    1.10000000e+03   # m0
     2    4.00000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.16984734e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=3.16541191e-04
# MX=2.16984734e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03920298e+01   # MW
        25     1.16233196e+02   # h0
        35     8.61557604e+02   # H0
        36     8.61674698e+02   # A0
        37     8.65572063e+02   # H+
   1000021     9.89071486e+02   # ~g
   1000022     1.66665602e+02   # ~neutralino(1)
   1000023     3.18507229e+02   # ~neutralino(2)
   1000024     3.18604781e+02   # ~chargino(1)
   1000025    -5.72308026e+02   # ~neutralino(3)
   1000035     5.82858053e+02   # ~neutralino(4)
   1000037     5.84125067e+02   # ~chargino(2)
   1000001     1.36943681e+03   # ~d_L
   1000002     1.36725411e+03   # ~u_L
   1000003     1.36938856e+03   # ~s_L
   1000004     1.36720578e+03   # ~c_L
   1000005     1.06959062e+03   # ~b_1
   1000006     8.83942499e+02   # ~t_1
   1000011     1.12883140e+03   # ~e_L
   1000012     1.12568746e+03   # ~nue_L
   1000013     1.12855079e+03   # ~mu_L
   1000014     1.12540614e+03   # ~numu_L
   1000015     9.09278058e+02   # ~stau_1
   1000016     1.03377726e+03   # ~nu_tau_L
   2000001     1.35073712e+03   # ~d_R
   2000002     1.35164029e+03   # ~u_R
   2000003     1.35064493e+03   # ~s_R
   2000004     1.35163401e+03   # ~c_R
   2000005     1.19071085e+03   # ~b_2
   2000006     1.10341291e+03   # ~t_2
   2000011     1.10966058e+03   # ~e_R
   2000013     1.10908756e+03   # ~mu_R
   2000015     1.04050890e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59715488e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.95558037e-01   # N_{1,1}
  1  2    -1.49996881e-02   # N_{1,2}
  1  3     8.85351147e-02   # N_{1,3}
  1  4    -2.82972950e-02   # N_{1,4}
  2  1     3.52644188e-02   # N_{2,1}
  2  2     9.73578728e-01   # N_{2,2}
  2  3    -1.95736017e-01   # N_{2,3}
  2  4     1.12197562e-01   # N_{2,4}
  3  1    -4.13827525e-02   # N_{3,1}
  3  2     6.10215024e-02   # N_{3,2}
  3  3     7.02059840e-01   # N_{3,3}
  3  4     7.08290778e-01   # N_{3,4}
  4  1    -7.68640531e-02   # N_{4,1}
  4  2     2.19535524e-01   # N_{4,2}
  4  3     6.78941033e-01   # N_{4,3}
  4  4    -6.96372849e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.60186809e-01   # U_{1,1}
  1  2    -2.79358714e-01   # U_{1,2}
  2  1     2.79358714e-01   # U_{2,1}
  2  2     9.60186809e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.87004332e-01   # V_{1,1}
  1  2    -1.60693648e-01   # V_{1,2}
  2  1     1.60693648e-01   # V_{2,1}
  2  2     9.87004332e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.17837916e-01   # F_{11}
  1  2     9.48145062e-01   # F_{12}
  2  1     9.48145062e-01   # F_{21}
  2  2    -3.17837916e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.81694109e-01   # F_{11}
  1  2     1.90464368e-01   # F_{12}
  2  1    -1.90464368e-01   # F_{21}
  2  2     9.81694109e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.65729001e-01   # F_{11}
  1  2     9.86171333e-01   # F_{12}
  2  1     9.86171333e-01   # F_{21}
  2  2    -1.65729001e-01   # F_{22}
Block gauge Q= 9.64471843e+02  # SM gauge couplings
     1     3.62031063e-01   # g'(Q)MSSM DRbar
     2     6.42228091e-01   # g(Q)MSSM DRbar
     3     1.05942680e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.64471843e+02  
  3  3     8.57737714e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.64471843e+02  
  3  3     5.17430544e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.64471843e+02  
  3  3     4.12737170e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.64471843e+02 # Higgs mixing parameters
     1     5.64445465e+02    # mu(Q)MSSM DRbar
     2     3.92312238e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43731179e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     8.94460194e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.64471843e+02  # MSSM DRbar SUSY breaking parameters
     1     1.68500704e+02      # M_1(Q)
     2     3.13075220e+02      # M_2(Q)
     3     8.93584129e+02      # M_3(Q)
    21     4.44511000e+05      # mH1^2(Q)
    22    -3.06149036e+05      # mH2^2(Q)
    31     1.12606066e+03      # meL(Q)
    32     1.12578018e+03      # mmuL(Q)
    33     1.03644660e+03      # mtauL(Q)
    34     1.10757475e+03      # meR(Q)
    35     1.10700148e+03      # mmuR(Q)
    36     9.14526484e+02      # mtauR(Q)
    41     1.34463248e+03      # mqL1(Q)
    42     1.34458342e+03      # mqL2(Q)
    43     1.05344584e+03      # mqL3(Q)
    44     1.32993384e+03      # muR(Q)
    45     1.32992746e+03      # mcR(Q)
    46     8.71830950e+02      # mtR(Q)
    47     1.32831371e+03      # mdR(Q)
    48     1.32821982e+03      # msR(Q)
    49     1.16648284e+03      # mbR(Q)
Block au Q= 9.64471843e+02  
  1  1    -1.25023321e+03      # Au(Q)MSSM DRbar
  2  2    -1.25020151e+03      # Ac(Q)MSSM DRbar
  3  3    -8.39789584e+02      # At(Q)MSSM DRbar
Block ad Q= 9.64471843e+02  
  1  1    -1.45065874e+03      # Ad(Q)MSSM DRbar
  2  2    -1.45057803e+03      # As(Q)MSSM DRbar
  3  3    -1.19481302e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.64471843e+02  
  1  1    -5.72740677e+02      # Ae(Q)MSSM DRbar
  2  2    -5.72442271e+02      # Amu(Q)MSSM DRbar
  3  3    -4.79626641e+02      # Atau(Q)MSSM DRbar
