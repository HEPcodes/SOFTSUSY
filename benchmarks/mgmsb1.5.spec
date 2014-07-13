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
     1    5.50000000e+04   # lambda
     2    1.10000000e+05   # M_mess
     5    3.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.28727615e-05
# MX=1.10000000e+05 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04003441e+01   # MW
        25     1.13487707e+02   # h0
        35     5.21244181e+02   # H0
        36     5.20987246e+02   # A0
        37     5.27360444e+02   # H+
   1000021     1.26173537e+03   # ~g
   1000022     2.28536270e+02   # ~neutralino(1)
   1000023     3.75235068e+02   # ~neutralino(2)
   1000024     3.72564574e+02   # ~chargino(1)
   1000025    -4.13392373e+02   # ~neutralino(3)
   1000035     4.99916375e+02   # ~neutralino(4)
   1000037     4.99685568e+02   # ~chargino(2)
   1000039     1.43385000e-09   # ~gravitino
   1000001     1.20490136e+03   # ~d_L
   1000002     1.20241264e+03   # ~u_L
   1000003     1.20489985e+03   # ~s_L
   1000004     1.20241112e+03   # ~c_L
   1000005     1.14763457e+03   # ~b_1
   1000006     1.07335353e+03   # ~t_1
   1000011     3.57185814e+02   # ~e_L
   1000012     3.47962450e+02   # ~nue_L
   1000013     3.57184369e+02   # ~mu_L
   1000014     3.47960968e+02   # ~numu_L
   1000015     1.70019790e+02   # ~stau_1
   1000016     3.47284562e+02   # ~nu_tau_L
   2000001     1.15609474e+03   # ~d_R
   2000002     1.15885508e+03   # ~u_R
   2000003     1.15609263e+03   # ~s_R
   2000004     1.15885400e+03   # ~c_R
   2000005     1.16431480e+03   # ~b_2
   2000006     1.17679702e+03   # ~t_2
   2000011     1.75959416e+02   # ~e_R
   2000013     1.75953463e+02   # ~mu_R
   2000015     3.58201951e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.44795161e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.79039395e-01   # N_{1,1}
  1  2    -3.93646069e-02   # N_{1,2}
  1  3     1.70909305e-01   # N_{1,3}
  1  4    -1.03548544e-01   # N_{1,4}
  2  1    -1.83717989e-01   # N_{2,1}
  2  2    -5.63236209e-01   # N_{2,2}
  2  3     5.90960652e-01   # N_{2,3}
  2  4    -5.47520028e-01   # N_{2,4}
  3  1    -4.48702213e-02   # N_{3,1}
  3  2     6.02091965e-02   # N_{3,2}
  3  3     7.00739148e-01   # N_{3,3}
  3  4     7.09454835e-01   # N_{3,4}
  4  1    -7.56057394e-02   # N_{4,1}
  4  2     8.23158705e-01   # N_{4,2}
  4  3     3.61275745e-01   # N_{4,3}
  4  4    -4.31478105e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1    -5.08300480e-01   # U_{1,1}
  1  2     8.61179785e-01   # U_{1,2}
  2  1    -8.61179785e-01   # U_{2,1}
  2  2    -5.08300480e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1    -6.07680651e-01   # V_{1,1}
  1  2     7.94181482e-01   # V_{1,2}
  2  1    -7.94181482e-01   # V_{2,1}
  2  2    -6.07680651e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.84783459e-01   # F_{11}
  1  2     9.58591874e-01   # F_{12}
  2  1     9.58591874e-01   # F_{21}
  2  2    -2.84783459e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.68294432e-01   # F_{11}
  1  2     8.83572479e-01   # F_{12}
  2  1     8.83572479e-01   # F_{21}
  2  2    -4.68294432e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.09750491e-01   # F_{11}
  1  2     9.93959169e-01   # F_{12}
  2  1     9.93959169e-01   # F_{21}
  2  2    -1.09750491e-01   # F_{22}
Block gauge Q= 1.09054768e+03  # SM gauge couplings
     1     3.63267418e-01   # g'(Q)MSSM DRbar
     2     6.43394095e-01   # g(Q)MSSM DRbar
     3     1.05266439e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.09054768e+03  
  3  3     8.58368639e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.09054768e+03  
  3  3     2.03113023e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.09054768e+03  
  3  3     1.51806275e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.09054768e+03 # Higgs mixing parameters
     1     4.04626469e+02    # mu(Q)MSSM DRbar
     2     1.44867317e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43591257e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     3.09094287e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.09054768e+03  # MSSM DRbar SUSY breaking parameters
     1     2.38808716e+02      # M_1(Q)
     2     4.47862589e+02      # M_2(Q)
     3     1.20463537e+03      # M_3(Q)
    21     1.05469613e+05      # mH1^2(Q)
    22    -1.42379117e+05      # mH2^2(Q)
    31     3.47483341e+02      # meL(Q)
    32     3.47481860e+02      # mmuL(Q)
    33     3.47025792e+02      # mtauL(Q)
    34     1.64108715e+02      # meR(Q)
    35     1.64102346e+02      # mmuR(Q)
    36     1.62129276e+02      # mtauR(Q)
    41     1.16012226e+03      # mqL1(Q)
    42     1.16012070e+03      # mqL2(Q)
    43     1.12329107e+03      # mqL3(Q)
    44     1.11707459e+03      # muR(Q)
    45     1.11707349e+03      # mcR(Q)
    46     1.04218594e+03      # mtR(Q)
    47     1.11313381e+03      # mdR(Q)
    48     1.11313165e+03      # msR(Q)
    49     1.10893868e+03      # mbR(Q)
Block au Q= 1.09054768e+03  
  1  1    -3.61154633e+02      # Au(Q)MSSM DRbar
  2  2    -3.61154126e+02      # Ac(Q)MSSM DRbar
  3  3    -3.40565975e+02      # At(Q)MSSM DRbar
Block ad Q= 1.09054768e+03  
  1  1    -3.83972601e+02      # Ad(Q)MSSM DRbar
  2  2    -3.83971895e+02      # As(Q)MSSM DRbar
  3  3    -3.76217063e+02      # Ab(Q)MSSM DRbar
Block ae Q= 1.09054768e+03  
  1  1    -3.76470690e+01      # Ae(Q)MSSM DRbar
  2  2    -3.76467948e+01      # Amu(Q)MSSM DRbar
  3  3    -3.75623344e+01      # Atau(Q)MSSM DRbar
