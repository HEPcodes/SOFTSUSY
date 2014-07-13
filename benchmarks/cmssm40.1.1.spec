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
     1    3.30000000e+02   # m0
     2    5.00000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.87271646e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=7.06072544e-04
# MX=1.87271646e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03906354e+01   # MW
        25     1.16990872e+02   # h0
        35     6.09571279e+02   # H0
        36     6.09585517e+02   # A0
        37     6.15228989e+02   # H+
   1000021     1.15306194e+03   # ~g
   1000022     2.07041651e+02   # ~neutralino(1)
   1000023     3.94704661e+02   # ~neutralino(2)
   1000024     3.94831665e+02   # ~chargino(1)
   1000025    -7.02938665e+02   # ~neutralino(3)
   1000035     7.10984848e+02   # ~neutralino(4)
   1000037     7.12169942e+02   # ~chargino(2)
   1000001     1.09880041e+03   # ~d_L
   1000002     1.09603203e+03   # ~u_L
   1000003     1.09876712e+03   # ~s_L
   1000004     1.09599863e+03   # ~c_L
   1000005     9.12855873e+02   # ~b_1
   1000006     7.76575903e+02   # ~t_1
   1000011     4.72695587e+02   # ~e_L
   1000012     4.65718679e+02   # ~nue_L
   1000013     4.72560312e+02   # ~mu_L
   1000014     4.65581512e+02   # ~numu_L
   1000015     2.08757278e+02   # ~stau_1
   1000016     4.19062981e+02   # ~nu_tau_L
   2000001     1.05637770e+03   # ~d_R
   2000002     1.05951722e+03   # ~u_R
   2000003     1.05631155e+03   # ~s_R
   2000004     1.05951306e+03   # ~c_R
   2000005     9.81138095e+02   # ~b_2
   2000006     9.89139666e+02   # ~t_2
   2000011     3.81824829e+02   # ~e_R
   2000013     3.81485120e+02   # ~mu_R
   2000015     4.49709828e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.61315939e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97115952e-01   # N_{1,1}
  1  2    -1.02791567e-02   # N_{1,2}
  1  3     7.15292025e-02   # N_{1,3}
  1  4    -2.31881715e-02   # N_{1,4}
  2  1     2.39129698e-02   # N_{2,1}
  2  2     9.82072939e-01   # N_{2,2}
  2  3    -1.61886490e-01   # N_{2,3}
  2  4     9.35610812e-02   # N_{2,4}
  3  1    -3.35080883e-02   # N_{3,1}
  3  2     4.93677474e-02   # N_{3,2}
  3  3     7.03707873e-01   # N_{3,3}
  3  4     7.07979705e-01   # N_{3,4}
  4  1    -6.37585842e-02   # N_{4,1}
  4  2     1.81631237e-01   # N_{4,2}
  4  3     6.88092702e-01   # N_{4,3}
  4  4    -6.99623735e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.73059149e-01   # U_{1,1}
  1  2    -2.30555616e-01   # U_{1,2}
  2  1     2.30555616e-01   # U_{2,1}
  2  2     9.73059149e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.91019157e-01   # V_{1,1}
  1  2    -1.33719968e-01   # V_{1,2}
  2  1     1.33719968e-01   # V_{2,1}
  2  2     9.91019157e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.73100280e-01   # F_{11}
  1  2     8.81008584e-01   # F_{12}
  2  1     8.81008584e-01   # F_{21}
  2  2    -4.73100280e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.12975012e-01   # F_{11}
  1  2     5.82298574e-01   # F_{12}
  2  1    -5.82298574e-01   # F_{21}
  2  2     8.12975012e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     3.55685297e-01   # F_{11}
  1  2     9.34605783e-01   # F_{12}
  2  1     9.34605783e-01   # F_{21}
  2  2    -3.55685297e-01   # F_{22}
Block gauge Q= 8.50963775e+02  # SM gauge couplings
     1     3.62132875e-01   # g'(Q)MSSM DRbar
     2     6.42336617e-01   # g(Q)MSSM DRbar
     3     1.06123651e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.50963775e+02  
  3  3     8.56328536e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.50963775e+02  
  3  3     4.91113460e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.50963775e+02  
  3  3     4.27416152e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.50963775e+02 # Higgs mixing parameters
     1     6.99528686e+02    # mu(Q)MSSM DRbar
     2     3.92347344e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44010879e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     4.69224291e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.50963775e+02  # MSSM DRbar SUSY breaking parameters
     1     2.10483081e+02      # M_1(Q)
     2     3.90867355e+02      # M_2(Q)
     3     1.11771360e+03      # M_3(Q)
    21    -1.16811228e+05      # mH1^2(Q)
    22    -4.83194817e+05      # mH2^2(Q)
    31     4.67134663e+02      # meL(Q)
    32     4.66997413e+02      # mmuL(Q)
    33     4.23247899e+02      # mtauL(Q)
    34     3.77269179e+02      # meR(Q)
    35     3.76925428e+02      # mmuR(Q)
    36     2.50970172e+02      # mtauR(Q)
    41     1.06388313e+03      # mqL1(Q)
    42     1.06384913e+03      # mqL2(Q)
    43     9.10624867e+02      # mqL3(Q)
    44     1.02771995e+03      # muR(Q)
    45     1.02771572e+03      # mcR(Q)
    46     7.90832028e+02      # mtR(Q)
    47     1.02339830e+03      # mdR(Q)
    48     1.02333099e+03      # msR(Q)
    49     9.28923928e+02      # mbR(Q)
Block au Q= 8.50963775e+02  
  1  1    -1.48305045e+03      # Au(Q)MSSM DRbar
  2  2    -1.48301399e+03      # Ac(Q)MSSM DRbar
  3  3    -1.02167631e+03      # At(Q)MSSM DRbar
Block ad Q= 8.50963775e+02  
  1  1    -1.72569854e+03      # Ad(Q)MSSM DRbar
  2  2    -1.72560567e+03      # As(Q)MSSM DRbar
  3  3    -1.44976123e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.50963775e+02  
  1  1    -6.25696361e+02      # Ae(Q)MSSM DRbar
  2  2    -6.25382342e+02      # Amu(Q)MSSM DRbar
  3  3    -5.20563113e+02      # Atau(Q)MSSM DRbar
