# SOFTSUSY3.4.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.1       # version number
Block MODSEL  # Select model
     1    0   # nonUniversal
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
Block EXTPAR               # non-universal SUSY breaking parameters
     0    -1.00000000e+00  # Set MX=MSUSY
     1     4.00000000e+02  # M_1(MX)
     2     2.50000000e+03  # M_2(MX)
     3     4.80000000e+02  # M_3(MX)
     11    0.00000000e+00  # At(MX)
     12    0.00000000e+00  # Ab(MX)
     13    0.00000000e+00  # Atau(MX)
     23    2.50000000e+03  # mu(MX)
     26    2.50000000e+03  # mA(pole)
     31    2.50000000e+03  # meL(MX)
     32    2.50000000e+03  # mmuL(MX)
     33    2.50000000e+03  # mtauL(MX)
     34    2.50000000e+03  # meR(MX)
     35    2.50000000e+03  # mmuR(MX)
     36    2.50000000e+03  # mtauR(MX)
     41    4.80000000e+02  # mqL1(MX)
     42    4.80000000e+02  # mqL2(MX)
     43    2.50000000e+03  # mqL3(MX)
     44    4.80000000e+02  # muR(MX)
     45    4.80000000e+02  # mcR(MX)
     46    2.50000000e+03  # mtR(MX)
     47    4.80000000e+02  # mdR(MX)
     48    4.80000000e+02  # msR(MX)
     49    2.50000000e+03  # mbR(MX)
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=7.61512489e-04
# MX=2.50360530e+03 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04015174e+01   # MW
        25     1.16196123e+02   # h0
        35     2.50009873e+03   # H0
        36     2.49999171e+03   # A0
        37     2.50164392e+03   # H+
   1000021     5.69053815e+02   # ~g
   1000022     3.92877499e+02   # ~neutralino(1)
   1000023     2.44699607e+03   # ~neutralino(2)
   1000024     2.44715452e+03   # ~chargino(1)
   1000025    -2.53366945e+03   # ~neutralino(3)
   1000035     2.57427619e+03   # ~neutralino(4)
   1000037     2.57440251e+03   # ~chargino(2)
   1000001     5.76755578e+02   # ~d_L
   1000002     5.71730720e+02   # ~u_L
   1000003     5.76755578e+02   # ~s_L
   1000004     5.71730720e+02   # ~c_L
   1000005     2.51906442e+03   # ~b_1
   1000006     2.52314100e+03   # ~t_1
   1000011     2.51891320e+03   # ~e_L
   1000012     2.51737708e+03   # ~nue_L
   1000013     2.51891320e+03   # ~mu_L
   1000014     2.51737708e+03   # ~numu_L
   1000015     2.49910177e+03   # ~stau_1
   1000016     2.51715512e+03   # ~nu_tau_L
   2000001     5.27918724e+02   # ~d_R
   2000002     5.22129480e+02   # ~u_R
   2000003     5.27918724e+02   # ~s_R
   2000004     5.22129480e+02   # ~c_R
   2000005     2.54887480e+03   # ~b_2
   2000006     2.55013805e+03   # ~t_2
   2000011     2.50351172e+03   # ~e_R
   2000013     2.50351172e+03   # ~mu_R
   2000015     2.52269291e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04688861e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.99824048e-01   # N_{1,1}
  1  2    -2.20610706e-04   # N_{1,2}
  1  3     1.81702612e-02   # N_{1,3}
  1  4    -4.65472855e-03   # N_{1,4}
  2  1     7.24428179e-03   # N_{2,1}
  2  2     9.02183195e-01   # N_{2,2}
  2  3    -3.11158330e-01   # N_{2,3}
  2  4     2.98652804e-01   # N_{2,4}
  3  1    -9.55265132e-03   # N_{3,1}
  3  2     9.79140653e-03   # N_{3,2}
  3  3     7.06913561e-01   # N_{3,3}
  3  4     7.07167655e-01   # N_{3,4}
  4  1    -1.44270854e-02   # N_{4,1}
  4  2     4.31241884e-01   # N_{4,2}
  4  3     6.34920115e-01   # N_{4,3}
  4  4    -6.40857819e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.22902458e-01   # U_{1,1}
  1  2    -5.68182669e-01   # U_{1,2}
  2  1     5.68182669e-01   # U_{2,1}
  2  2     8.22902458e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     8.33931332e-01   # V_{1,1}
  1  2    -5.51868220e-01   # V_{1,2}
  2  1     5.51868220e-01   # V_{2,1}
  2  2     8.33931332e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.38826377e-01   # F_{11}
  1  2     9.40848918e-01   # F_{12}
  2  1     9.40848918e-01   # F_{21}
  2  2    -3.38826377e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     3.98358458e-01   # F_{11}
  1  2     9.17229818e-01   # F_{12}
  2  1     9.17229818e-01   # F_{21}
  2  2    -3.98358458e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     4.06107074e-01   # F_{11}
  1  2     9.13825500e-01   # F_{12}
  2  1     9.13825500e-01   # F_{21}
  2  2    -4.06107074e-01   # F_{22}
Block gauge Q= 2.50360530e+03  # SM gauge couplings
     1     3.64767785e-01   # g'(Q)MSSM DRbar
     2     6.37583677e-01   # g(Q)MSSM DRbar
     3     1.05156486e+00   # g3(Q)MSSM DRbar
Block yu Q= 2.50360530e+03  
  3  3     8.27103416e-01   # Yt(Q)MSSM DRbar
Block yd Q= 2.50360530e+03  
  3  3     1.29809411e-01   # Yb(Q)MSSM DRbar
Block ye Q= 2.50360530e+03  
  3  3     9.97422793e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 2.50360530e+03 # Higgs mixing parameters
     1     2.53454087e+03    # mu(Q)MSSM DRbar
     2     9.55021855e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43820668e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     6.15895613e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 2.50360530e+03  # MSSM DRbar SUSY breaking parameters
     1     4.00000000e+02      # M_1(Q)
     2     2.50000000e+03      # M_2(Q)
     3     4.80000000e+02      # M_3(Q)
    21    -3.42533518e+05      # mH1^2(Q)
    22    -6.24658824e+06      # mH2^2(Q)
    31     2.50000000e+03      # meL(Q)
    32     2.50000000e+03      # mmuL(Q)
    33     2.50000000e+03      # mtauL(Q)
    34     2.50000000e+03      # meR(Q)
    35     2.50000000e+03      # mmuR(Q)
    36     2.50000000e+03      # mtauR(Q)
    41     4.79999999e+02      # mqL1(Q)
    42     4.79999999e+02      # mqL2(Q)
    43     2.50000000e+03      # mqL3(Q)
    44     4.79999999e+02      # muR(Q)
    45     4.79999999e+02      # mcR(Q)
    46     2.50000000e+03      # mtR(Q)
    47     4.79999999e+02      # mdR(Q)
    48     4.79999999e+02      # msR(Q)
    49     2.50000000e+03      # mbR(Q)
Block au Q= 2.50360530e+03  
  1  1     2.04509925e-06      # Au(Q)MSSM DRbar
  2  2     2.04510401e-06      # Ac(Q)MSSM DRbar
  3  3     2.78615424e-06      # At(Q)MSSM DRbar
Block ad Q= 2.50360530e+03  
  1  1     1.42049641e-06      # Ad(Q)MSSM DRbar
  2  2     1.42049749e-06      # As(Q)MSSM DRbar
  3  3     1.59229809e-06      # Ab(Q)MSSM DRbar
Block ae Q= 2.50360530e+03  
  1  1     0.00000000e+00      # Ae(Q)MSSM DRbar
  2  2     1.83778335e-08      # Amu(Q)MSSM DRbar
  3  3     1.82502364e-08      # Atau(Q)MSSM DRbar
