# SOFTSUSY3.4.0 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
# B.C. Allanach and M.A. Bernhardt, Comput. Phys. Commun. 181 (2010) 232,
# arXiv:0903.1805
# B.C. Allanach, M. Hanussek and C.H. Kom, arXiv:1109.3735
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.0       # version number
Block MODSEL  # Select model
     1    1   # sugra
     4    1   # R-parity violating
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
    21    4.75000000e-03   # Mdown(2 GeV) MSbar
    22    2.40000000e-03   # Mup(2 GeV) MSbar
    23    1.04000000e-01   # Mstrange(2 GeV) MSbar
    24    1.27000000e+00   # Mcharm(Mcharm) MSbar
    11    5.10998902e-04   # Me(pole)
    13    1.05658357e-01   # Mmu(pole)
Block VCKMIN               # input CKM mixing matrix parameters
     1    2.27200000e-01   # lambda_W
     2    8.18000000e-01   # A
     3    2.21000000e-01   # rhobar
     4    3.40000000e-01   # etabar (no phases used in SOFTSUSY yet though)
Block MINPAR               # SUSY breaking input parameters
     3    1.00000000e+01   # tanb, DRbar, Feynman gauge
     4    1.00000000e+00   # sign(mu)
     1    1.25000000e+02   # m0
     2    5.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.58173673e+16   # MX scale
Block RVLAMLLEIN           # input LLE couplings at MSUSY
  1 2 1   1.00000000e-02   # lambda_{121}
  2 1 1  -1.00000000e-02   # lambda_{211}
# SOFTSUSY-specific non SLHA information:
# MIXING=1 Desired accuracy=1.00000000e-03 Achieved accuracy=6.51833265e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.05003178e+01   # MW
        25     1.14769963e+02   # CP even neutral scalar
        35     3.50852232e+02   # CP even neutral scalar
        36     3.50852232e+02   # CP odd neutral scalar
        37     2.22530529e+02   # charged scalar
   1000021     1.14758774e+03   # ~g
   1000022     2.05311890e+02   # ~neutralino(1)
   1000023     3.86888704e+02   # ~neutralino(2)
   1000024     3.86905098e+02   # ~chargino(1)
   1000025    -6.41584040e+02   # ~neutralino(3)
   1000035     6.54958966e+02   # ~neutralino(4)
   1000037     6.55287348e+02   # ~chargino(2)
   1000011     2.29693259e+02   # charged scalar
   1000013     2.29698746e+02   # charged scalar
   1000015     3.60786949e+02   # charged scalar
   2000011     3.60791630e+02   # charged scalar
   2000013     3.61213530e+02   # charged scalar
   2000015     7.20395061e+02   # charged scalar
   1000012     3.51848550e+02   # CP even neutral scalar
   1000014     3.51851890e+02   # CP even neutral scalar
   1000016     7.15653527e+02   # CP even neutral scalar
   1000017     3.51848550e+02   # CP odd neutral scalar
   1000018     3.51851890e+02   # CP odd neutral scalar
   1000019     7.15653527e+02   # CP odd neutral scalar
   1000001     9.67146744e+02   # ~d_1
   1000003     1.00410717e+03   # ~d_2
   1000005     1.01148453e+03   # ~d_3
   2000001     1.01148814e+03   # ~d_4
   2000003     1.05572761e+03   # ~d_5
   2000005     1.05574623e+03   # ~d_6
   1000002     8.06780832e+02   # ~u_1
   1000004     1.00252917e+03   # ~u_2
   1000006     1.01478252e+03   # ~u_3
   2000002     1.01478818e+03   # ~u_4
   2000004     1.05290128e+03   # ~u_5
   2000006     1.05290480e+03   # ~u_6
        12     3.37840519e-43   # Mnu1 inverted hierarchy output
        14     2.42368163e-14   # Mnu2 inverted hierarchy output
        16     0.00000000e+00   # Mnu3 inverted hierarchy output
Block RVNMIX  # neutrino-neutralino mixing matrix 
  1 1    0.00000000e+00   # N_{11}
  1 2    0.00000000e+00   # N_{12}
  1 3    1.00000000e+00   # N_{13}
  1 4    0.00000000e+00   # N_{14}
  1 5    0.00000000e+00   # N_{15}
  1 6    0.00000000e+00   # N_{16}
  1 7    0.00000000e+00   # N_{17}
  2 1    1.00000000e+00   # N_{21}
  2 2    1.52539803e-15   # N_{22}
  2 3    0.00000000e+00   # N_{23}
  2 4   -8.52268830e-25   # N_{24}
  2 5   -1.22548833e-24   # N_{25}
  2 6    4.61552738e-24   # N_{26}
  2 7   -9.00889464e-28   # N_{27}
  3 1   -1.52539803e-15   # N_{31}
  3 2    1.00000000e+00   # N_{32}
  3 3    0.00000000e+00   # N_{33}
  3 4   -5.11525626e-10   # N_{34}
  3 5    5.31896299e-10   # N_{35}
  3 6   -2.48771903e-09   # N_{36}
  3 7    5.49514791e-12   # N_{37}
  4 1   -6.56058253e-25   # N_{41}
  4 2    7.23542194e-10   # N_{42}
  4 3    0.00000000e+00   # N_{43}
  4 4    9.95874960e-01   # N_{44}
  4 5   -1.74472526e-02   # N_{45}
  4 6    8.22678482e-02   # N_{46}
  4 7   -3.40684254e-02   # N_{47}
  5 1    3.62210954e-24   # N_{51}
  5 2   -9.83169562e-10   # N_{52}
  5 3    0.00000000e+00   # N_{53}
  5 4    3.75467246e-02   # N_{54}
  5 5    9.71531750e-01   # N_{55}
  5 6   -1.94921908e-01   # N_{56}
  5 7    1.29312611e-01   # N_{57}
  6 1   -5.81429494e-24   # N_{61}
  6 2    1.70368450e-09   # N_{62}
  6 3    0.00000000e+00   # N_{63}
  6 4   -3.30401642e-02   # N_{64}
  6 5    4.81443058e-02   # N_{65}
  6 6    7.03489975e-01   # N_{66}
  6 7    7.08302428e-01   # N_{67}
  7 1    5.24698393e-24   # N_{71}
  7 2   -1.52992540e-09   # N_{72}
  7 3    0.00000000e+00   # N_{73}
  7 4    7.57076886e-02   # N_{74}
  7 5   -2.31308835e-01   # N_{75}
  7 6   -6.78483092e-01   # N_{76}
  7 7    6.93127162e-01   # N_{77}
Block RVUMIX  # lepton-chargino mixing matrix U
  1 1   -1.00000000e+00   # U_{11}
  1 2   -9.12669037e-32   # U_{12}
  1 3    0.00000000e+00   # U_{13}
  1 4    3.37842252e-24   # U_{14}
  1 5   -4.36431387e-23   # U_{15}
  2 1    9.12447326e-32   # U_{21}
  2 2    1.00000000e+00   # U_{22}
  2 3    0.00000000e+00   # U_{23}
  2 4    3.56086554e-10   # U_{24}
  2 5   -4.15434432e-09   # U_{25}
  3 1    0.00000000e+00   # U_{31}
  3 2    0.00000000e+00   # U_{32}
  3 3    1.00000000e+00   # U_{33}
  3 4    0.00000000e+00   # U_{34}
  3 5    0.00000000e+00   # U_{35}
  4 1    1.54487133e-23   # U_{41}
  4 2   -1.50366833e-09   # U_{42}
  4 3    0.00000000e+00   # U_{43}
  4 4    9.60100107e-01   # U_{44}
  4 5   -2.79656548e-01   # U_{45}
  5 1   -4.09569842e-23   # U_{51}
  5 2    3.88900449e-09   # U_{52}
  5 3    0.00000000e+00   # U_{53}
  5 4    2.79656548e-01   # U_{54}
  5 5    9.60100107e-01   # U_{55}
Block RVVMIX  # lepton-chargino mixing matrix V
  1 1   -1.00000000e+00   # V_{11}
  1 2   -2.54787511e-17   # V_{12}
  1 3    0.00000000e+00   # V_{13}
  1 4    0.00000000e+00   # V_{14}
  1 5   -9.80711886e-46   # V_{15}
  2 1    2.54787511e-17   # V_{21}
  2 2    1.00000000e+00   # V_{22}
  2 3    0.00000000e+00   # V_{23}
  2 4    6.91477936e-13   # V_{24}
  2 5   -2.01624076e-12   # V_{25}
  3 1    0.00000000e+00   # V_{31}
  3 2    0.00000000e+00   # V_{32}
  3 3    1.00000000e+00   # V_{33}
  3 4    0.00000000e+00   # V_{34}
  3 5    0.00000000e+00   # V_{35}
  4 1   -2.66913266e-29   # V_{41}
  4 2   -1.04759164e-12   # V_{42}
  4 3    0.00000000e+00   # V_{43}
  4 4    9.83229191e-01   # V_{44}
  4 5   -1.82374226e-01   # V_{45}
  5 1    4.72966901e-29   # V_{51}
  5 2    1.85631902e-12   # V_{52}
  5 3    0.00000000e+00   # V_{53}
  5 4    1.82374226e-01   # V_{54}
  5 5    9.83229191e-01   # V_{55}
Block gauge Q= 8.76220364e+02  # SM gauge couplings
     1     3.62703247e-01   # g'(Q)MSSM DRbar
     2     6.42357202e-01   # g(Q)MSSM DRbar
     3     1.06432991e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.76220364e+02   # diagonal Up Yukawa matrix
  1  1     7.33179817e-06    # YU_{11}(Q)MSSM DRbar
  2  2     3.35849907e-03    # YU_{22}(Q)MSSM DRbar
  3  3     8.57821167e-01    # YU_{33}(Q)MSSM DRbar
Block yd Q= 8.76220364e+02   # diagonal down Yukawa matrix
  1  1     1.41236806e-04    # YD_{11}(Q)MSSM DRbar
  2  2     3.09240166e-03    # YD_{22}(Q)MSSM DRbar
  3  3     1.34889327e-01    # YD_{33}(Q)MSSM DRbar
Block ye Q= 8.76220364e+02   # diagonal lepton Yukawa matrix
  1  1     2.79077885e-05    # YE_{11}(Q)MSSM DRbar
  2  2     5.77044454e-03    # YE_{22}(Q)MSSM DRbar
  3  3     1.00319809e-01    # YE_{33}(Q)MSSM DRbar
Block hmix Q= 8.76220364e+02 # Higgs mixing parameters
     1     6.36136793e+02    # mu(Q)MSSM DRbar
     2     9.67533424e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44501981e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     5.31425745e+05    # mA^2(Q)MSSM DRbar
Block RVLAMLLE Q= 8.76220364e+02 # non-zero R-Parity violating LLE couplings 
  1 2 1    1.00000173e-02   # lambda_{121}
  1 2 2   -2.73559803e-29   # lambda_{122}
  1 3 3   -1.57831173e-28   # lambda_{133}
  2 1 1   -1.00000173e-02   # lambda_{211}
  2 1 2    2.73559803e-29   # lambda_{212}
  2 3 3    2.99592535e-14   # lambda_{233}
  3 1 3    1.57831173e-28   # lambda_{313}
  3 2 3   -2.99592535e-14   # lambda_{323}
Block RVLAMLQD Q= 8.76220364e+02 # non-zero R-Parity violating LQD couplings 
  1 1 1   -2.22203762e-31   # lambda'_{111}
  1 1 2    1.28144172e-35   # lambda'_{112}
  1 1 3   -1.29576113e-32   # lambda'_{113}
  1 2 1    5.85273781e-37   # lambda'_{121}
  1 2 2   -4.86518714e-30   # lambda'_{122}
  1 2 3    9.53954437e-32   # lambda'_{123}
  1 3 1   -1.37220876e-35   # lambda'_{131}
  1 3 2    2.21188561e-33   # lambda'_{132}
  1 3 3   -2.12218137e-28   # lambda'_{133}
  2 1 1    4.21783525e-17   # lambda'_{211}
  2 1 2   -2.43241157e-21   # lambda'_{212}
  2 1 3    2.45959242e-18   # lambda'_{213}
  2 2 1   -1.11095705e-22   # lambda'_{221}
  2 2 2    9.23501818e-16   # lambda'_{222}
  2 2 3   -1.81078060e-17   # lambda'_{223}
  2 3 1    2.60470406e-21   # lambda'_{231}
  2 3 2   -4.19856483e-19   # lambda'_{232}
  2 3 3    4.02828975e-14   # lambda'_{233}
Block RVLAMUDD Q= 8.76220364e+02 # non-zero R-Parity violating UDD couplings 
Block RVTLLE Q= 8.76220364e+02 # non-zero R-Parity violating LLE soft terms 
  1 2 1   -1.20879633e-05   # T_{121}
  1 2 2    1.89013411e-26   # T_{122}
  1 3 3    1.40573066e-25   # T_{133}
  2 1 1    1.20879633e-05   # T_{211}
  2 1 2   -1.89013411e-26   # T_{212}
  2 3 3   -2.66836669e-11   # T_{233}
  3 1 3   -1.40573066e-25   # T_{313}
  3 2 3    2.66836669e-11   # T_{323}
Block RVTLQD Q= 8.76220364e+02 # non-zero R-Parity violating LQD soft terms 
  1 1 1    4.42113683e-28   # T'_{111}
  1 1 2    7.80281397e-32   # T'_{112}
  1 1 3   -7.91415271e-29   # T'_{113}
  1 2 1    3.56379977e-33   # T'_{121}
  1 2 2    9.67941681e-27   # T'_{122}
  1 2 3    5.82652915e-28   # T'_{123}
  1 3 1   -8.40032176e-32   # T'_{131}
  1 3 2    1.35406456e-29   # T'_{132}
  1 3 3    4.03129317e-25   # T'_{133}
  2 1 1   -8.39217410e-14   # T'_{211}
  2 1 2   -1.48111475e-17   # T'_{212}
  2 1 3    1.50224886e-14   # T'_{213}
  2 2 1   -6.76473440e-19   # T'_{221}
  2 2 2   -1.83734081e-12   # T'_{222}
  2 2 3   -1.10598027e-13   # T'_{223}
  2 3 1    1.59453251e-17   # T'_{231}
  2 3 2   -2.57025865e-15   # T'_{232}
  2 3 3   -7.65217726e-11   # T'_{233}
Block RVTUDD Q= 8.76220364e+02 # non-zero R-Parity violating UDD soft terms 
Block RVKAPPA Q= 8.76220364e+02 # R-Parity violating kappa 
     1   -1.00082270e-24   # kappa_{1}
     2    1.89974519e-10   # kappa_{2}
     3    0.00000000e+00   # kappa_{3}
Block RVD Q= 8.76220364e+02 # R-Parity violating D 
     1    5.09849802e-22   # D_{1}
     2   -9.67808729e-08   # D_{2}
     3    0.00000000e+00   # D_{3}
Block RVSNVEV Q= 8.76220364e+02 # sneutrino VEVs D 
     1    1.02991695e-21   # SneutrinoVev_{1}
     2   -1.97515101e-07   # SneutrinoVev_{2}
     3    0.00000000e+00   # SneutrinoVev_{3}
Block RVM2LH1 Q= 8.76220364e+02 # M2LH1 
     1   -9.14629930e-22   # M2LH1_{1}
     2    1.73617073e-07   # M2LH1_{2}
     3    0.00000000e+00   # M2LH1_{3}
Block UPMNS Q= 9.11876000e+01 # neutrino mixing matrix (inverted  hierarchy)
  1  1     1.00000000e+00   # UPMNS_{11} matrix element
  1  2    -1.52564449e-15   # UPMNS_{12} matrix element
  1  3     0.00000000e+00   # UPMNS_{13} matrix element
  2  1     1.52564449e-15   # UPMNS_{21} matrix element
  2  2     1.00000000e+00   # UPMNS_{22} matrix element
  2  3     0.00000000e+00   # UPMNS_{23} matrix element
  3  1     0.00000000e+00   # UPMNS_{31} matrix element
  3  2     0.00000000e+00   # UPMNS_{32} matrix element
  3  3     1.00000000e+00   # UPMNS_{33} matrix element
Block msq2 Q= 8.76220364e+02 # super CKM squark mass^2 matrix - DRbar
  1  1     1.03725672e+06    # (m^_Q^2)_{11}
  1  2     3.57018484e+01    # (m^_Q^2)_{12}
  1  3    -8.43986356e+02    # (m^_Q^2)_{13}
  2  1     3.57018484e+01    # (m^_Q^2)_{21}
  2  2     1.03699799e+06    # (m^_Q^2)_{22}
  2  3     6.21359298e+03    # (m^_Q^2)_{23}
  3  1    -8.43986356e+02    # (m^_Q^2)_{31}
  3  2     6.21359298e+03    # (m^_Q^2)_{32}
  3  3     8.82909842e+05    # (m^_Q^2)_{33}
Block msl2 Q= 8.76220364e+02 # super MNS slepton mass^2 matrix - DRbar
  1  1     1.24785848e+05    # (m^_L^2)_{11}
  1  2    -7.92628243e-24    # (m^_L^2)_{12}
  1  3     0.00000000e+00    # (m^_L^2)_{13}
  2  1    -7.92628243e-24    # (m^_L^2)_{21}
  2  2     1.24783523e+05    # (m^_L^2)_{22}
  2  3     0.00000000e+00    # (m^_L^2)_{23}
  3  1     0.00000000e+00    # (m^_L^2)_{31}
  3  2     0.00000000e+00    # (m^_L^2)_{32}
  3  3     1.24090740e+05    # (m^_L^2)_{33}
Block msd2 Q= 8.76220364e+02 # super CKM squark mass^2 matrix - DRbar
  1  1     9.52928921e+05    # (m^_d^2)_{11}
  1  2    -2.55923453e-06    # (m^_d^2)_{12}
  1  3     2.65132577e-03    # (m^_d^2)_{13}
  2  1    -2.55923453e-06    # (m^_d^2)_{21}
  2  2     9.52923625e+05    # (m^_d^2)_{22}
  2  3    -4.27384873e-01    # (m^_d^2)_{23}
  3  1     2.65132577e-03    # (m^_d^2)_{31}
  3  2    -4.27384873e-01    # (m^_d^2)_{32}
  3  3     9.43297041e+05    # (m^_d^2)_{33}
Block msu2 Q= 8.76220364e+02 # super CKM squark mass^2 matrix - DRbar
  1  1     9.61896033e+05    # (m^_u^2)_{11}
  1  2    -1.30649168e-08    # (m^_u^2)_{12}
  1  3    -1.17178052e-05    # (m^_u^2)_{13}
  2  1    -1.30649168e-08    # (m^_u^2)_{21}
  2  2     9.61890610e+05    # (m^_u^2)_{22}
  2  3    -5.70313788e-02    # (m^_u^2)_{23}
  3  1    -1.17178052e-05    # (m^_u^2)_{31}
  3  2    -5.70313788e-02    # (m^_u^2)_{32}
  3  3     6.55128792e+05    # (m^_u^2)_{33}
Block mse2 Q= 8.76220364e+02 # super MNS slepton mass^2 matrix - DRbar
  1  1     4.91948225e+04    # (m^_e^2)_{11}
  1  2    -3.28954932e-16    # (m^_e^2)_{12}
  1  3     0.00000000e+00    # (m^_e^2)_{13}
  2  1    -3.28954932e-16    # (m^_e^2)_{21}
  2  2     4.92029933e+04    # (m^_e^2)_{22}
  2  3     0.00000000e+00    # (m^_e^2)_{23}
  3  1     0.00000000e+00    # (m^_e^2)_{31}
  3  2     0.00000000e+00    # (m^_e^2)_{32}
  3  3     4.77771052e+04    # (m^_e^2)_{33}
Block tu Q= 8.76220364e+02   # super CKM trilinear matrix - DRbar
  1  1    -8.38404424e-03    # (T^_u)_{11}
  1  2    -1.80746600e-08    # (T^_u)_{12}
  1  3    -8.04343250e-08    # (T^_u)_{13}
  2  1    -8.27952718e-06    # (T^_u)_{21}
  2  2    -3.84053716e+00    # (T^_u)_{22}
  2  3    -3.91129992e-04    # (T^_u)_{23}
  3  1    -1.11163612e-02    # (T^_u)_{31}
  3  2    -1.17984336e-01    # (T^_u)_{32}
  3  3    -7.60422959e+02    # (T^_u)_{33}
Block td Q= 8.76220364e+02   # super CKM trilinear matrix - DRbar
  1  1    -1.97008293e-01    # (T^_d)_{11}
  1  2    -2.91217926e-06    # (T^_d)_{12}
  1  3     6.92114591e-05    # (T^_d)_{13}
  2  1    -6.37623749e-05    # (T^_d)_{21}
  2  2    -4.31307551e+00    # (T^_d)_{22}
  2  3    -1.11566172e-02    # (T^_d)_{23}
  3  1     6.59728724e-02    # (T^_d)_{31}
  3  2    -4.85706083e-01    # (T^_d)_{32}
  3  3    -1.75998782e+02    # (T^_d)_{33}
Block te Q= 8.76220364e+02   # super CKM trilinear matrix - DRbar
  1  1    -8.30057270e-03    # (T^_e)_{11}
  1  2    -8.22670134e-22    # (T^_e)_{12}
  1  3     0.00000000e+00    # (T^_e)_{13}
  2  1    -3.96736609e-24    # (T^_e)_{21}
  2  2    -1.71623188e+00    # (T^_e)_{22}
  2  3     0.00000000e+00    # (T^_e)_{23}
  3  1     0.00000000e+00    # (T^_e)_{31}
  3  2     0.00000000e+00    # (T^_e)_{32}
  3  3    -2.96754931e+01    # (T^_e)_{33}
Block VCKM Q= 8.76220364e+02 # DRbar CKM mixing matrix
  1  1     9.73840718e-01    # CKM_{11} matrix element
  1  2     2.27197409e-01    # CKM_{12} matrix element
  1  3     3.94887731e-03    # CKM_{13} matrix element
  2  1    -2.27161573e-01    # CKM_{21} matrix element
  2  2     9.72961269e-01    # CKM_{22} matrix element
  2  3     4.17610937e-02    # CKM_{23} matrix element
  3  1     5.64590762e-03    # CKM_{31} matrix element
  3  2    -4.15656867e-02    # CKM_{32} matrix element
  3  3     9.99119821e-01    # CKM_{33} matrix element
Block msoft Q= 8.76220364e+02 # MSSM DRbar SUSY breaking parameters
     1     2.10406720e+02     # M_1(Q)
     2     3.89202300e+02     # M_2(Q)
     3     1.11364053e+03     # M_3(Q)
    21     1.08623296e+05     # mH1^2(Q)
    22    -3.80244762e+05     # mH2^2(Q)
Block USQMIX  # super CKM squark mass^2 matrix
  1  1     2.22383864e-05   # (USQMIX)_{11}
  1  2     2.35484423e-04   # (USQMIX)_{12}
  1  3     4.29694410e-01   # (USQMIX)_{13}
  1  4     1.33103342e-10   # (USQMIX)_{14}
  1  5     6.46283255e-07   # (USQMIX)_{15}
  1  6     9.02974340e-01   # (USQMIX)_{16}
  2  1     1.63629419e-04   # (USQMIX)_{21}
  2  2     1.73195146e-03   # (USQMIX)_{22}
  2  3     9.02972821e-01   # (USQMIX)_{23}
  2  4     1.03901297e-08   # (USQMIX)_{24}
  2  5     5.03902989e-05   # (USQMIX)_{25}
  2  6    -4.29694143e-01   # (USQMIX)_{26}
  3  1     1.60883242e-07   # (USQMIX)_{31}
  3  2     8.86171480e-03   # (USQMIX)_{32}
  3  3    -6.05327602e-05   # (USQMIX)_{33}
  3  4     2.48110045e-08   # (USQMIX)_{34}
  3  5     9.99960732e-01   # (USQMIX)_{35}
  3  6     2.57787297e-05   # (USQMIX)_{36}
  4  1     1.93461050e-05   # (USQMIX)_{41}
  4  2     1.31383590e-10   # (USQMIX)_{42}
  4  3    -1.24816301e-08   # (USQMIX)_{43}
  4  4     1.00000000e+00   # (USQMIX)_{44}
  4  5    -2.48171484e-08   # (USQMIX)_{45}
  4  6     5.31570173e-09   # (USQMIX)_{46}
  5  1     1.87878167e-01   # (USQMIX)_{51}
  5  2     9.82152219e-01   # (USQMIX)_{52}
  5  3    -1.66453478e-03   # (USQMIX)_{53}
  5  4    -3.63507938e-06   # (USQMIX)_{54}
  5  5    -8.70403933e-03   # (USQMIX)_{55}
  5  6     5.31340966e-04   # (USQMIX)_{56}
  6  1     9.82192327e-01   # (USQMIX)_{61}
  6  2    -1.87870790e-01   # (USQMIX)_{62}
  6  3     1.58238992e-04   # (USQMIX)_{63}
  6  4    -1.90015276e-05   # (USQMIX)_{64}
  6  5     1.66477559e-03   # (USQMIX)_{65}
  6  6    -5.04966886e-05   # (USQMIX)_{66}
Block DSQMIX  # super CKM squark mass^2 matrix
  1  1     4.59225485e-03   # (DSQMIX)_{11}
  1  2    -3.38095964e-02   # (DSQMIX)_{12}
  1  3     9.74056246e-01   # (DSQMIX)_{13}
  1  4     9.71588542e-07   # (DSQMIX)_{14}
  1  5    -1.56628792e-04   # (DSQMIX)_{15}
  1  6     2.23719082e-01   # (DSQMIX)_{16}
  2  1    -1.78771875e-03   # (DSQMIX)_{21}
  2  2     1.31631645e-02   # (DSQMIX)_{22}
  2  3    -2.23387565e-01   # (DSQMIX)_{23}
  2  4    -2.43266051e-06   # (DSQMIX)_{24}
  2  5     3.92324953e-04   # (DSQMIX)_{25}
  2  6     9.74639101e-01   # (DSQMIX)_{26}
  3  1     1.97141546e-06   # (DSQMIX)_{31}
  3  2     4.52076635e-03   # (DSQMIX)_{32}
  3  3     4.02967230e-04   # (DSQMIX)_{33}
  3  4     5.56447172e-06   # (DSQMIX)_{34}
  3  5     9.99989631e-01   # (DSQMIX)_{35}
  3  6    -3.71221583e-04   # (DSQMIX)_{36}
  4  1     2.07140382e-04   # (DSQMIX)_{41}
  4  2     6.48167658e-08   # (DSQMIX)_{42}
  4  3    -2.50183162e-06   # (DSQMIX)_{43}
  4  4     9.99999979e-01   # (DSQMIX)_{44}
  4  5    -5.56336728e-06   # (DSQMIX)_{45}
  4  6     2.30384825e-06   # (DSQMIX)_{46}
  5  1    -1.38066928e-01   # (DSQMIX)_{51}
  5  2     9.89735749e-01   # (DSQMIX)_{52}
  5  3     3.62249420e-02   # (DSQMIX)_{53}
  5  4     2.86129772e-05   # (DSQMIX)_{54}
  5  5    -4.49070938e-03   # (DSQMIX)_{55}
  5  6    -5.31572745e-03   # (DSQMIX)_{56}
  6  1     9.90410620e-01   # (DSQMIX)_{61}
  6  2     1.38153365e-01   # (DSQMIX)_{62}
  6  3     1.30246492e-04   # (DSQMIX)_{63}
  6  4    -2.05166109e-04   # (DSQMIX)_{64}
  6  5    -6.26576524e-04   # (DSQMIX)_{65}
  6  6    -1.91035430e-05   # (DSQMIX)_{66}
Block RVLMIX  # charged higgs-slepton mixing matrix 
  1 1    0.00000000e+00   # C_{11}
  1 2    0.00000000e+00   # C_{12}
  1 3    0.00000000e+00   # C_{13}
  1 4    0.00000000e+00   # C_{14}
  1 5    1.45634857e-01   # C_{15}
  1 6    0.00000000e+00   # C_{16}
  1 7    0.00000000e+00   # C_{17}
  1 8    9.89338409e-01   # C_{18}
  2 1   -9.25566439e-29   # C_{21}
  2 2    1.33126812e-27   # C_{22}
  2 3    4.22675641e-05   # C_{23}
  2 4    1.19910702e-18   # C_{24}
  2 5    0.00000000e+00   # C_{25}
  2 6    9.99999999e-01   # C_{26}
  2 7    1.11721310e-16   # C_{27}
  2 8    0.00000000e+00   # C_{28}
  3 1   -8.26433026e-13   # C_{31}
  3 2    1.18871914e-11   # C_{32}
  3 3   -3.64561744e-21   # C_{33}
  3 4    8.73978543e-03   # C_{34}
  3 5    0.00000000e+00   # C_{35}
  3 6   -1.11727523e-16   # C_{36}
  3 7    9.99961807e-01   # C_{37}
  3 8    0.00000000e+00   # C_{38}
  4 1   -1.23994522e-26   # C_{41}
  4 2   -5.85607468e-27   # C_{42}
  4 3    9.99999999e-01   # C_{43}
  4 4   -2.46416357e-19   # C_{44}
  4 5    0.00000000e+00   # C_{45}
  4 6   -4.22675641e-05   # C_{46}
  4 7    1.07683442e-21   # C_{47}
  4 8    0.00000000e+00   # C_{48}
  5 1    2.37761598e-12   # C_{51}
  5 2    1.08394115e-12   # C_{52}
  5 3    2.46406946e-19   # C_{53}
  5 4    9.99961807e-01   # C_{54}
  5 5    0.00000000e+00   # C_{55}
  5 6   -2.22651363e-19   # C_{56}
  5 7   -8.73978543e-03   # C_{57}
  5 8    0.00000000e+00   # C_{58}
  6 1    0.00000000e+00   # C_{61}
  6 2    0.00000000e+00   # C_{62}
  6 3    0.00000000e+00   # C_{63}
  6 4    0.00000000e+00   # C_{64}
  6 5    9.89338409e-01   # C_{65}
  6 6    0.00000000e+00   # C_{66}
  6 7    0.00000000e+00   # C_{67}
  6 8   -1.45634857e-01   # C_{68}
  7 1    9.94700973e-01   # C_{71}
  7 2    1.02810376e-01   # C_{72}
  7 3    1.29352018e-26   # C_{73}
  7 4   -2.47985930e-12   # C_{74}
  7 5    0.00000000e+00   # C_{75}
  7 6   -9.82188733e-32   # C_{76}
  7 7   -3.78413894e-13   # C_{77}
  7 8    0.00000000e+00   # C_{78}
Block RVHMIX  # CP-even neutral scalar mixing matrix 
  1 1    1.05903065e-01   # curlyN_{11}
  1 2    9.94376458e-01   # curlyN_{12}
  1 3    3.02458743e-25   # curlyN_{13}
  1 4   -5.79944177e-11   # curlyN_{14}
  1 5    0.00000000e+00   # curlyN_{15}
  2 1    0.00000000e+00   # curlyN_{21}
  2 2    0.00000000e+00   # curlyN_{22}
  2 3    0.00000000e+00   # curlyN_{23}
  2 4    0.00000000e+00   # curlyN_{24}
  2 5    1.00000000e+00   # curlyN_{25}
  3 1    8.75793795e-12   # curlyN_{31}
  3 2    5.73896584e-11   # curlyN_{32}
  3 3    2.46456715e-19   # curlyN_{33}
  3 4    1.00000000e+00   # curlyN_{34}
  3 5    0.00000000e+00   # curlyN_{35}
  4 1   -4.56383676e-26   # curlyN_{41}
  4 2   -2.99323049e-25   # curlyN_{42}
  4 3    1.00000000e+00   # curlyN_{43}
  4 4   -2.46456715e-19   # curlyN_{44}
  4 5    0.00000000e+00   # curlyN_{45}
  5 1    9.94376458e-01   # curlyN_{51}
  5 2   -1.05903065e-01   # curlyN_{52}
  5 3    1.36818418e-26   # curlyN_{53}
  5 4   -2.63094662e-12   # curlyN_{54}
  5 5    0.00000000e+00   # curlyN_{55}
Block RVAMIX  # CP-odd neutral scalar mixing matrix 
  1 1    0.00000000e+00   # curlyN~_{11}
  1 2    0.00000000e+00   # curlyN~_{12}
  1 3    0.00000000e+00   # curlyN~_{13}
  1 4    0.00000000e+00   # curlyN~_{14}
  1 5    1.00000000e+00   # curlyN~_{15}
  2 1   -6.56521153e-12   # curlyN~_{21}
  2 2    5.68142654e-11   # curlyN~_{22}
  2 3    2.46456715e-19   # curlyN~_{23}
  2 4    1.00000000e+00   # curlyN~_{24}
  2 5    0.00000000e+00   # curlyN~_{25}
  3 1    3.42651021e-26   # curlyN~_{31}
  3 2   -2.96194694e-25   # curlyN~_{32}
  3 3    1.00000000e+00   # curlyN~_{33}
  3 4   -2.46456715e-19   # curlyN~_{34}
  3 5    0.00000000e+00   # curlyN~_{35}
  4 1    9.94700756e-01   # curlyN~_{41}
  4 2    1.02812483e-01   # curlyN~_{42}
  4 3   -3.63084114e-27   # curlyN~_{43}
  4 4    6.89205168e-13   # curlyN~_{44}
  4 5    0.00000000e+00   # curlyN~_{45}
