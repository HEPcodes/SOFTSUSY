# SOFTSUSY3.4.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.1       # version number
Block MODSEL  # Select model
     1    2   # gmsb
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
Block MINPAR               # SUSY breaking input parameters
     3    1.50000000e+01   # tanb, DRbar, Feynman gauge
     4    1.00000000e+00   # sign(mu)
     1    6.00000000e+04   # lambda
     2    1.20000000e+05   # M_mess
     5    3.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=2.38786354e-05
# MX=1.20000000e+05 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03990167e+01   # MW
        25     1.14086795e+02   # h0
        35     5.65152054e+02   # H0
        36     5.64914629e+02   # A0
        37     5.70801251e+02   # H+
   1000021     1.36522885e+03   # ~g
   1000022     2.50311034e+02   # ~neutralino(1)
   1000023     4.09496985e+02   # ~neutralino(2)
   1000024     4.06923057e+02   # ~chargino(1)
   1000025    -4.44865338e+02   # ~neutralino(3)
   1000035     5.37814741e+02   # ~neutralino(4)
   1000037     5.37619491e+02   # ~chargino(2)
   1000039     1.70640000e-09   # ~gravitino
   1000001     1.30435642e+03   # ~d_L
   1000002     1.30207025e+03   # ~u_L
   1000003     1.30435478e+03   # ~s_L
   1000004     1.30206862e+03   # ~c_L
   1000005     1.24242323e+03   # ~b_1
   1000006     1.16143665e+03   # ~t_1
   1000011     3.88735875e+02   # ~e_L
   1000012     3.80258543e+02   # ~nue_L
   1000013     3.88734297e+02   # ~mu_L
   1000014     3.80256931e+02   # ~numu_L
   1000015     1.85397875e+02   # ~stau_1
   1000016     3.79522846e+02   # ~nu_tau_L
   2000001     1.25095139e+03   # ~d_R
   2000002     1.25415085e+03   # ~u_R
   2000003     1.25094911e+03   # ~s_R
   2000004     1.25414968e+03   # ~c_R
   2000005     1.25996326e+03   # ~b_2
   2000006     1.27149821e+03   # ~t_2
   2000011     1.91221856e+02   # ~e_R
   2000013     1.91215345e+02   # ~mu_R
   2000015     3.89527638e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.37138289e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.81577384e-01   # N_{1,1}
  1  2    -3.44148540e-02   # N_{1,2}
  1  3     1.60135078e-01   # N_{1,3}
  1  4    -9.83779112e-02   # N_{1,4}
  2  1    -1.73762793e-01   # N_{2,1}
  2  2    -5.35968689e-01   # N_{2,2}
  2  3     6.02938667e-01   # N_{2,3}
  2  4    -5.64808835e-01   # N_{2,4}
  3  1    -4.14532609e-02   # N_{3,1}
  3  2     5.54996500e-02   # N_{3,2}
  3  3     7.01670062e-01   # N_{3,3}
  3  4     7.09126604e-01   # N_{3,4}
  4  1    -6.77787402e-02   # N_{4,1}
  4  2     8.41708365e-01   # N_{4,2}
  4  3     3.44210467e-01   # N_{4,3}
  4  4    -4.10429319e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1    -4.84020237e-01   # U_{1,1}
  1  2     8.75056804e-01   # U_{1,2}
  2  1    -8.75056804e-01   # U_{2,1}
  2  2    -4.84020237e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1    -5.77643048e-01   # V_{1,1}
  1  2     8.16289476e-01   # V_{1,2}
  2  1    -8.16289476e-01   # V_{2,1}
  2  2    -5.77643048e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.64841886e-01   # F_{11}
  1  2     9.64291852e-01   # F_{12}
  2  1     9.64291852e-01   # F_{21}
  2  2    -2.64841886e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.34656678e-01   # F_{11}
  1  2     9.00596232e-01   # F_{12}
  2  1     9.00596232e-01   # F_{21}
  2  2    -4.34656678e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.00000101e-01   # F_{11}
  1  2     9.94987427e-01   # F_{12}
  2  1     9.94987427e-01   # F_{21}
  2  2    -1.00000101e-01   # F_{22}
Block gauge Q= 1.17949436e+03  # SM gauge couplings
     1     3.63433460e-01   # g'(Q)MSSM DRbar
     2     6.42959313e-01   # g(Q)MSSM DRbar
     3     1.04859137e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.17949436e+03  
  3  3     8.55658120e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.17949436e+03  
  3  3     2.02302792e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.17949436e+03  
  3  3     1.51720783e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.17949436e+03 # Higgs mixing parameters
     1     4.36021430e+02    # mu(Q)MSSM DRbar
     2     1.44735901e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43500815e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     3.63125289e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.17949436e+03  # MSSM DRbar SUSY breaking parameters
     1     2.60778151e+02      # M_1(Q)
     2     4.87972996e+02      # M_2(Q)
     3     1.30408337e+03      # M_3(Q)
    21     1.25539027e+05      # mH1^2(Q)
    22    -1.64235990e+05      # mH2^2(Q)
    31     3.78643391e+02      # meL(Q)
    32     3.78641776e+02      # mmuL(Q)
    33     3.78143968e+02      # mtauL(Q)
    34     1.79277426e+02      # meR(Q)
    35     1.79270499e+02      # mmuR(Q)
    36     1.77122443e+02      # mtauR(Q)
    41     1.25642343e+03      # mqL1(Q)
    42     1.25642175e+03      # mqL2(Q)
    43     1.21664105e+03      # mqL3(Q)
    44     1.20922292e+03      # muR(Q)
    45     1.20922173e+03      # mcR(Q)
    46     1.12829149e+03      # mtR(Q)
    47     1.20487602e+03      # mdR(Q)
    48     1.20487369e+03      # msR(Q)
    49     1.20035064e+03      # mbR(Q)
Block au Q= 1.17949436e+03  
  1  1    -3.89561519e+02      # Au(Q)MSSM DRbar
  2  2    -3.89560974e+02      # Ac(Q)MSSM DRbar
  3  3    -3.67431043e+02      # At(Q)MSSM DRbar
Block ad Q= 1.17949436e+03  
  1  1    -4.14038063e+02      # Ad(Q)MSSM DRbar
  2  2    -4.14037304e+02      # As(Q)MSSM DRbar
  3  3    -4.05704276e+02      # Ab(Q)MSSM DRbar
Block ae Q= 1.17949436e+03  
  1  1    -4.10939848e+01      # Ae(Q)MSSM DRbar
  2  2    -4.10936855e+01      # Amu(Q)MSSM DRbar
  3  3    -4.10014705e+01      # Atau(Q)MSSM DRbar
