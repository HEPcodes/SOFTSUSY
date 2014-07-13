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
     1    1.60000000e+05   # lambda
     2    1.00000000e+14   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.13225604e-04
# MX=1.00000000e+14 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03958350e+01   # MW
        25     1.15798114e+02   # h0
        35     1.05795299e+03   # H0
        36     1.05790933e+03   # A0
        37     1.06115846e+03   # H+
   1000021     1.19552391e+03   # ~g
   1000022     2.13897764e+02   # ~neutralino(1)
   1000023     4.12140705e+02   # ~neutralino(2)
   1000024     4.12272384e+02   # ~chargino(1)
   1000025    -8.31789660e+02   # ~neutralino(3)
   1000035     8.38638971e+02   # ~neutralino(4)
   1000037     8.39411425e+02   # ~chargino(2)
   1000039     3.79200000e+00   # ~gravitino
   1000001     1.46950089e+03   # ~d_L
   1000002     1.46750973e+03   # ~u_L
   1000003     1.46949507e+03   # ~s_L
   1000004     1.46750390e+03   # ~c_L
   1000005     1.29925675e+03   # ~b_1
   1000006     1.03325506e+03   # ~t_1
   1000011     7.09724725e+02   # ~e_L
   1000012     7.04972868e+02   # ~nue_L
   1000013     7.09709747e+02   # ~mu_L
   1000014     7.04957799e+02   # ~numu_L
   1000015     4.66283581e+02   # ~stau_1
   1000016     7.00040795e+02   # ~nu_tau_L
   2000001     1.32104329e+03   # ~d_R
   2000002     1.34815334e+03   # ~u_R
   2000003     1.32103465e+03   # ~s_R
   2000004     1.34814907e+03   # ~c_R
   2000005     1.33051230e+03   # ~b_2
   2000006     1.34216419e+03   # ~t_2
   2000011     4.82458910e+02   # ~e_R
   2000013     4.82414532e+02   # ~mu_R
   2000015     7.06078125e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.00914474e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.98006960e-01   # N_{1,1}
  1  2    -8.99168170e-03   # N_{1,2}
  1  3     5.94225322e-02   # N_{1,3}
  1  4    -1.92411133e-02   # N_{1,4}
  2  1     1.77840457e-02   # N_{2,1}
  2  2     9.89395614e-01   # N_{2,2}
  2  3    -1.26721974e-01   # N_{2,3}
  2  4     6.87138196e-02   # N_{2,4}
  3  1    -2.79397216e-02   # N_{3,1}
  3  2     4.16097819e-02   # N_{3,2}
  3  3     7.04708776e-01   # N_{3,3}
  3  4     7.07724197e-01   # N_{3,4}
  4  1    -5.37141303e-02   # N_{4,1}
  4  2     1.38867187e-01   # N_{4,2}
  4  3     6.95554487e-01   # N_{4,3}
  4  4    -7.02875986e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.83600484e-01   # U_{1,1}
  1  2    -1.80360993e-01   # U_{1,2}
  2  1     1.80360993e-01   # U_{2,1}
  2  2     9.83600484e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.95169276e-01   # V_{1,1}
  1  2    -9.81738881e-02   # V_{1,2}
  2  1     9.81738881e-02   # V_{2,1}
  2  2     9.95169276e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     1.87087542e-01   # F_{11}
  1  2     9.82343245e-01   # F_{12}
  2  1     9.82343245e-01   # F_{21}
  2  2    -1.87087542e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.10007357e-01   # F_{11}
  1  2     9.12082215e-01   # F_{12}
  2  1     9.12082215e-01   # F_{21}
  2  2    -4.10007357e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     7.87893998e-02   # F_{11}
  1  2     9.96891283e-01   # F_{12}
  2  1     9.96891283e-01   # F_{21}
  2  2    -7.87893998e-02   # F_{22}
Block gauge Q= 1.14416625e+03  # SM gauge couplings
     1     3.62806277e-01   # g'(Q)MSSM DRbar
     2     6.41730820e-01   # g(Q)MSSM DRbar
     3     1.05131141e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.14416625e+03  
  3  3     8.54040201e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.14416625e+03  
  3  3     1.96964261e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.14416625e+03  
  3  3     1.50714982e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.14416625e+03 # Higgs mixing parameters
     1     8.25430244e+02    # mu(Q)MSSM DRbar
     2     1.44798109e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43807349e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     1.16824002e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.14416625e+03  # MSSM DRbar SUSY breaking parameters
     1     2.17279029e+02      # M_1(Q)
     2     4.02026147e+02      # M_2(Q)
     3     1.09852142e+03      # M_3(Q)
    21     4.26660395e+05      # mH1^2(Q)
    22    -6.58236641e+05      # mH2^2(Q)
    31     7.06001185e+02      # meL(Q)
    32     7.05986133e+02      # mmuL(Q)
    33     7.01390322e+02      # mtauL(Q)
    34     4.77466340e+02      # meR(Q)
    35     4.77421527e+02      # mmuR(Q)
    36     4.63578276e+02      # mtauR(Q)
    41     1.43615822e+03      # mqL1(Q)
    42     1.43615224e+03      # mqL2(Q)
    43     1.29673478e+03      # mqL3(Q)
    44     1.31512796e+03      # muR(Q)
    45     1.31512354e+03      # mcR(Q)
    46     9.98572286e+02      # mtR(Q)
    47     1.28584025e+03      # mdR(Q)
    48     1.28583129e+03      # msR(Q)
    49     1.26949449e+03      # mbR(Q)
Block au Q= 1.14416625e+03  
  1  1    -1.01776160e+03      # Au(Q)MSSM DRbar
  2  2    -1.01775649e+03      # Ac(Q)MSSM DRbar
  3  3    -8.10600727e+02      # At(Q)MSSM DRbar
Block ad Q= 1.14416625e+03  
  1  1    -1.21491432e+03      # Ad(Q)MSSM DRbar
  2  2    -1.21490727e+03      # As(Q)MSSM DRbar
  3  3    -1.13693898e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.14416625e+03  
  1  1    -2.26845892e+02      # Ae(Q)MSSM DRbar
  2  2    -2.26838140e+02      # Amu(Q)MSSM DRbar
  3  3    -2.24477633e+02      # Atau(Q)MSSM DRbar
