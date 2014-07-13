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
     1     8.00000000e+02  # M_1(MX)
     2     2.50000000e+03  # M_2(MX)
     3     9.60000000e+02  # M_3(MX)
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
     41    9.60000000e+02  # mqL1(MX)
     42    9.60000000e+02  # mqL2(MX)
     43    2.50000000e+03  # mqL3(MX)
     44    9.60000000e+02  # muR(MX)
     45    9.60000000e+02  # mcR(MX)
     46    2.50000000e+03  # mtR(MX)
     47    9.60000000e+02  # mdR(MX)
     48    9.60000000e+02  # msR(MX)
     49    2.50000000e+03  # mbR(MX)
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=8.10708450e-04
# MX=2.50365290e+03 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04043537e+01   # MW
        25     1.16902575e+02   # h0
        35     2.50009840e+03   # H0
        36     2.49999157e+03   # A0
        37     2.50165321e+03   # H+
   1000021     1.08706554e+03   # ~g
   1000022     7.89619949e+02   # ~neutralino(1)
   1000023     2.44394894e+03   # ~neutralino(2)
   1000024     2.44406190e+03   # ~chargino(1)
   1000025    -2.53409705e+03   # ~neutralino(3)
   1000035     2.57296805e+03   # ~neutralino(4)
   1000037     2.57299576e+03   # ~chargino(2)
   1000001     1.05761252e+03   # ~d_L
   1000002     1.05490606e+03   # ~u_L
   1000003     1.05761252e+03   # ~s_L
   1000004     1.05490606e+03   # ~c_L
   1000005     2.52503522e+03   # ~b_1
   1000006     2.52815758e+03   # ~t_1
   1000011     2.51897155e+03   # ~e_L
   1000012     2.51742719e+03   # ~nue_L
   1000013     2.51897155e+03   # ~mu_L
   1000014     2.51742719e+03   # ~numu_L
   1000015     2.49944687e+03   # ~stau_1
   1000016     2.51720545e+03   # ~nu_tau_L
   2000001     1.02747099e+03   # ~d_R
   2000002     1.02546995e+03   # ~u_R
   2000003     1.02747099e+03   # ~s_R
   2000004     1.02546995e+03   # ~c_R
   2000005     2.55432534e+03   # ~b_2
   2000006     2.55667516e+03   # ~t_2
   2000011     2.50390656e+03   # ~e_R
   2000013     2.50390656e+03   # ~mu_R
   2000015     2.52280204e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.04723485e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.99767377e-01   # N_{1,1}
  1  2    -4.50703157e-04   # N_{1,2}
  1  3     1.99950820e-02   # N_{1,3}
  1  4    -8.07374858e-03   # N_{1,4}
  2  1     1.03691003e-02   # N_{2,1}
  2  2     8.66476457e-01   # N_{2,2}
  2  3    -3.58864437e-01   # N_{2,3}
  2  4     3.46882324e-01   # N_{2,4}
  3  1    -8.42308539e-03   # N_{3,1}
  3  2     9.77900310e-03   # N_{3,2}
  3  3     7.06926030e-01   # N_{3,3}
  3  4     7.07169718e-01   # N_{3,4}
  4  1    -1.69329633e-02   # N_{4,1}
  4  2     4.99121946e-01   # N_{4,2}
  4  3     6.09156877e-01   # N_{4,3}
  4  4    -6.16050694e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.33912599e-01   # U_{1,1}
  1  2    -5.51896527e-01   # U_{1,2}
  2  1     5.51896527e-01   # U_{2,1}
  2  2     8.33912599e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     8.44602799e-01   # V_{1,1}
  1  2    -5.35393418e-01   # V_{1,2}
  2  1     5.35393418e-01   # V_{2,1}
  2  2     8.44602799e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.80129533e-01   # F_{11}
  1  2     9.24933261e-01   # F_{12}
  2  1     9.24933261e-01   # F_{21}
  2  2    -3.80129533e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     3.97363691e-01   # F_{11}
  1  2     9.17661210e-01   # F_{12}
  2  1     9.17661210e-01   # F_{21}
  2  2    -3.97363691e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     4.10983590e-01   # F_{11}
  1  2     9.11642742e-01   # F_{12}
  2  1     9.11642742e-01   # F_{21}
  2  2    -4.10983590e-01   # F_{22}
Block gauge Q= 2.50365290e+03  # SM gauge couplings
     1     3.64482998e-01   # g'(Q)MSSM DRbar
     2     6.36771436e-01   # g(Q)MSSM DRbar
     3     1.03567116e+00   # g3(Q)MSSM DRbar
Block yu Q= 2.50365290e+03  
  3  3     8.32167865e-01   # Yt(Q)MSSM DRbar
Block yd Q= 2.50365290e+03  
  3  3     1.27745806e-01   # Yb(Q)MSSM DRbar
Block ye Q= 2.50365290e+03  
  3  3     9.96911395e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 2.50365290e+03 # Higgs mixing parameters
     1     2.53529589e+03    # mu(Q)MSSM DRbar
     2     9.54709005e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43743447e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     6.15561552e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 2.50365290e+03  # MSSM DRbar SUSY breaking parameters
     1     8.00000000e+02      # M_1(Q)
     2     2.50000000e+03      # M_2(Q)
     3     9.60000000e+02      # M_3(Q)
    21    -3.46765471e+05      # mH1^2(Q)
    22    -6.24793051e+06      # mH2^2(Q)
    31     2.50000000e+03      # meL(Q)
    32     2.50000000e+03      # mmuL(Q)
    33     2.50000000e+03      # mtauL(Q)
    34     2.50000000e+03      # meR(Q)
    35     2.50000000e+03      # mmuR(Q)
    36     2.50000000e+03      # mtauR(Q)
    41     9.59999997e+02      # mqL1(Q)
    42     9.59999997e+02      # mqL2(Q)
    43     2.50000000e+03      # mqL3(Q)
    44     9.59999997e+02      # muR(Q)
    45     9.59999997e+02      # mcR(Q)
    46     2.50000000e+03      # mtR(Q)
    47     9.59999997e+02      # mdR(Q)
    48     9.59999997e+02      # msR(Q)
    49     2.50000000e+03      # mbR(Q)
Block au Q= 2.50365290e+03  
  1  1     3.16463968e-06      # Au(Q)MSSM DRbar
  2  2     3.16466338e-06      # Ac(Q)MSSM DRbar
  3  3     4.85521682e-06      # At(Q)MSSM DRbar
Block ad Q= 2.50365290e+03  
  1  1     1.56814540e-06      # Ad(Q)MSSM DRbar
  2  2     1.56816765e-06      # As(Q)MSSM DRbar
  3  3     2.07727987e-06      # Ab(Q)MSSM DRbar
Block ae Q= 2.50365290e+03  
  1  1     0.00000000e+00      # Ae(Q)MSSM DRbar
  2  2     4.86762415e-08      # Amu(Q)MSSM DRbar
  3  3     4.86431249e-08      # Atau(Q)MSSM DRbar
