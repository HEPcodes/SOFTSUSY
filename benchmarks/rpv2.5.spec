# SOFTSUSY3.4.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
# B.C. Allanach and M.A. Bernhardt, Comput. Phys. Commun. 181 (2010) 232,
# arXiv:0903.1805
# B.C. Allanach, M. Hanussek and C.H. Kom, arXiv:1109.3735
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.1       # version number
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
     1    5.00000000e+01   # m0
     2    6.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.46222160e+16   # MX scale
Block RVLAMLQDIN           # input LLE couplings at MSUSY
  1 1 2   1.00000000e-03   # lambda'_{112}
# SOFTSUSY-specific non SLHA information:
# MIXING=1 Desired accuracy=1.00000000e-03 Achieved accuracy=3.57797868e-04
# MX=1.46222160e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.05220003e+01   # MW
        25     1.15932665e+02   # CP even neutral scalar
        35     3.97929146e+02   # CP even neutral scalar
        36     3.97929146e+02   # CP odd neutral scalar
        37     2.27188035e+02   # charged scalar
   1000021     1.35583766e+03   # ~g
   1000022     2.48582023e+02   # ~neutralino(1)
   1000023     4.69257885e+02   # ~neutralino(2)
   1000024     4.69324411e+02   # ~chargino(1)
   1000025    -7.53672033e+02   # ~neutralino(3)
   1000035     7.65770202e+02   # ~neutralino(4)
   1000037     7.66023515e+02   # ~chargino(2)
   1000011     2.34806682e+02   # charged scalar
   1000013     2.34830221e+02   # charged scalar
   1000015     4.06599475e+02   # charged scalar
   2000011     4.06905716e+02   # charged scalar
   2000013     4.06910333e+02   # charged scalar
   2000015     8.38381473e+02   # charged scalar
   1000012     3.98974609e+02   # CP even neutral scalar
   1000014     3.98976849e+02   # CP even neutral scalar
   1000016     8.34300985e+02   # CP even neutral scalar
   1000017     3.98974609e+02   # CP odd neutral scalar
   1000018     3.98976849e+02   # CP odd neutral scalar
   1000019     8.34300985e+02   # CP odd neutral scalar
   1000001     1.13781863e+03   # ~d_1
   1000003     1.17687267e+03   # ~d_2
   1000005     1.18546074e+03   # ~d_3
   2000001     1.18546486e+03   # ~d_4
   2000003     1.23923628e+03   # ~d_5
   2000005     1.23925857e+03   # ~d_6
   1000002     9.56915970e+02   # ~u_1
   1000004     1.16648344e+03   # ~u_2
   1000006     1.18988770e+03   # ~u_3
   2000002     1.18989322e+03   # ~u_4
   2000004     1.23685611e+03   # ~u_5
   2000006     1.23686104e+03   # ~u_6
        12     0.00000000e+00   # Mnu1 inverted hierarchy output
        14     5.40002621e-23   # Mnu2 inverted hierarchy output
        16     0.00000000e+00   # Mnu3 inverted hierarchy output
Block RVNMIX  # neutrino-neutralino mixing matrix 
  1 1    0.00000000e+00   # N_{11}
  1 2    1.00000000e+00   # N_{12}
  1 3    0.00000000e+00   # N_{13}
  1 4    0.00000000e+00   # N_{14}
  1 5    0.00000000e+00   # N_{15}
  1 6    0.00000000e+00   # N_{16}
  1 7    0.00000000e+00   # N_{17}
  2 1    0.00000000e+00   # N_{21}
  2 2    0.00000000e+00   # N_{22}
  2 3    1.00000000e+00   # N_{23}
  2 4    0.00000000e+00   # N_{24}
  2 5    0.00000000e+00   # N_{25}
  2 6    0.00000000e+00   # N_{26}
  2 7    0.00000000e+00   # N_{27}
  3 1    1.00000000e+00   # N_{31}
  3 2    0.00000000e+00   # N_{32}
  3 3    0.00000000e+00   # N_{33}
  3 4   -1.38250270e-13   # N_{34}
  3 5    1.60517989e-13   # N_{35}
  3 6   -5.86148328e-13   # N_{36}
  3 7    2.25772858e-15   # N_{37}
  4 1    1.80971687e-13   # N_{41}
  4 2    0.00000000e+00   # N_{42}
  4 3    0.00000000e+00   # N_{43}
  4 4    9.97025616e-01   # N_{44}
  4 5   -1.26302741e-02   # N_{45}
  4 6    7.00135446e-02   # N_{46}
  4 7   -2.96395095e-02   # N_{47}
  5 1   -2.55154860e-13   # N_{51}
  5 2    0.00000000e+00   # N_{52}
  5 3    0.00000000e+00   # N_{53}
  5 4    2.81031533e-02   # N_{54}
  5 5    9.77243927e-01   # N_{55}
  5 6   -1.73860395e-01   # N_{56}
  5 7    1.18224713e-01   # N_{57}
  6 1    4.00999424e-13   # N_{61}
  6 2    0.00000000e+00   # N_{62}
  6 3    0.00000000e+00   # N_{63}
  6 4   -2.79140677e-02   # N_{64}
  6 5    4.04956543e-02   # N_{65}
  6 6    7.04526856e-01   # N_{66}
  6 7    7.07970915e-01   # N_{67}
  7 1   -3.60276046e-13   # N_{71}
  7 2    0.00000000e+00   # N_{72}
  7 3    0.00000000e+00   # N_{73}
  7 4    6.61130726e-02   # N_{74}
  7 5   -2.07833792e-01   # N_{75}
  7 6   -6.84479785e-01   # N_{76}
  7 7    6.95644737e-01   # N_{77}
Block RVUMIX  # lepton-chargino mixing matrix U
  1 1    1.00000000e+00   # U_{11}
  1 2    0.00000000e+00   # U_{12}
  1 3    0.00000000e+00   # U_{13}
  1 4    1.56283011e-13   # U_{14}
  1 5   -1.44908260e-14   # U_{15}
  2 1    0.00000000e+00   # U_{21}
  2 2    1.00000000e+00   # U_{22}
  2 3    0.00000000e+00   # U_{23}
  2 4    0.00000000e+00   # U_{24}
  2 5    0.00000000e+00   # U_{25}
  3 1    0.00000000e+00   # U_{31}
  3 2    0.00000000e+00   # U_{32}
  3 3    1.00000000e+00   # U_{33}
  3 4    0.00000000e+00   # U_{34}
  3 5    0.00000000e+00   # U_{35}
  4 1   -1.54972007e-13   # U_{41}
  4 2    0.00000000e+00   # U_{42}
  4 3    0.00000000e+00   # U_{43}
  4 4    9.68535024e-01   # U_{44}
  4 5   -2.48877292e-01   # U_{45}
  5 1   -2.48604200e-14   # U_{51}
  5 2    0.00000000e+00   # U_{52}
  5 3    0.00000000e+00   # U_{53}
  5 4    2.48877292e-01   # U_{54}
  5 5    9.68535024e-01   # U_{55}
Block RVVMIX  # lepton-chargino mixing matrix V
  1 1    1.00000000e+00   # V_{11}
  1 2    0.00000000e+00   # V_{12}
  1 3    0.00000000e+00   # V_{13}
  1 4    1.24303023e-18   # V_{14}
  1 5   -4.37802809e-18   # V_{15}
  2 1    0.00000000e+00   # V_{21}
  2 2    1.00000000e+00   # V_{22}
  2 3    0.00000000e+00   # V_{23}
  2 4    0.00000000e+00   # V_{24}
  2 5    0.00000000e+00   # V_{25}
  3 1    0.00000000e+00   # V_{31}
  3 2    0.00000000e+00   # V_{32}
  3 3    1.00000000e+00   # V_{33}
  3 4    0.00000000e+00   # V_{34}
  3 5    0.00000000e+00   # V_{35}
  4 1   -1.95409300e-18   # V_{41}
  4 2    0.00000000e+00   # V_{42}
  4 3    0.00000000e+00   # V_{43}
  4 4    9.86062836e-01   # V_{44}
  4 5   -1.66373324e-01   # V_{45}
  5 1    4.11020372e-18   # V_{51}
  5 2    0.00000000e+00   # V_{52}
  5 3    0.00000000e+00   # V_{53}
  5 4    1.66373324e-01   # V_{54}
  5 5    9.86062836e-01   # V_{55}
Block gauge Q= 1.03033262e+03  # SM gauge couplings
     1     3.63109774e-01   # g'(Q)MSSM DRbar
     2     6.41501677e-01   # g(Q)MSSM DRbar
     3     1.05584083e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.03033262e+03   # diagonal Up Yukawa matrix
  1  1     7.29208539e-06    # YU_{11}(Q)MSSM DRbar
  2  2     3.34030790e-03    # YU_{22}(Q)MSSM DRbar
  3  3     8.51789046e-01    # YU_{33}(Q)MSSM DRbar
Block yd Q= 1.03033262e+03   # diagonal down Yukawa matrix
  1  1     1.40211725e-04    # YD_{11}(Q)MSSM DRbar
  2  2     3.06996086e-03    # YD_{22}(Q)MSSM DRbar
  3  3     1.33688831e-01    # YD_{33}(Q)MSSM DRbar
Block ye Q= 1.03033262e+03   # diagonal lepton Yukawa matrix
  1  1     2.78419961e-05    # YE_{11}(Q)MSSM DRbar
  2  2     5.75685001e-03    # YE_{22}(Q)MSSM DRbar
  3  3     1.00178531e-01    # YE_{33}(Q)MSSM DRbar
Block hmix Q= 1.03033262e+03 # Higgs mixing parameters
     1     7.48344976e+02    # mu(Q)MSSM DRbar
     2     9.65652190e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44381401e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     7.21974075e+05    # mA^2(Q)MSSM DRbar
Block RVLAMLLE Q= 1.03033262e+03 # non-zero R-Parity violating LLE couplings 
  1 2 2   -2.68148659e-21   # lambda_{122}
  1 3 3   -4.66648691e-20   # lambda_{133}
  2 1 2    2.68148659e-21   # lambda_{212}
  3 1 3    4.66648691e-20   # lambda_{313}
Block RVLAMLQD Q= 1.03033262e+03 # non-zero R-Parity violating LQD couplings 
  1 1 1   -1.34819706e-22   # lambda'_{111}
  1 1 2    9.99999869e-04   # lambda'_{112}
  1 1 3   -1.13785676e-17   # lambda'_{113}
  1 2 1    1.19409919e-28   # lambda'_{121}
  1 2 2   -3.11888282e-15   # lambda'_{122}
  1 2 3    1.96496571e-23   # lambda'_{123}
  1 3 1   -2.81807744e-27   # lambda'_{131}
  1 3 2    7.31398118e-14   # lambda'_{132}
  1 3 3   -6.15644969e-20   # lambda'_{133}
Block RVLAMUDD Q= 1.03033262e+03 # non-zero R-Parity violating UDD couplings 
Block RVTLLE Q= 1.03033262e+03 # non-zero R-Parity violating LLE soft terms 
  1 2 2   -3.76766460e-17   # T_{122}
  1 3 3   -6.55676518e-16   # T_{133}
  2 1 2    3.76766460e-17   # T_{212}
  3 1 3    6.55676518e-16   # T_{313}
Block RVTLQD Q= 1.03033262e+03 # non-zero R-Parity violating LQD soft terms 
  1 1 1   -1.34297272e-18   # T'_{111}
  1 1 2    3.05474212e-07   # T'_{112}
  1 1 3   -8.15400546e-14   # T'_{113}
  1 2 1    4.91718637e-24   # T'_{121}
  1 2 2    6.64489947e-12   # T'_{122}
  1 2 3    7.95672174e-19   # T'_{123}
  1 3 1   -1.15035114e-22   # T'_{131}
  1 3 2   -1.55794180e-10   # T'_{132}
  1 3 3   -8.15171871e-16   # T'_{133}
Block RVTUDD Q= 1.03033262e+03 # non-zero R-Parity violating UDD soft terms 
Block RVKAPPA Q= 1.03033262e+03 # R-Parity violating kappa 
     1   -3.54202207e-16   # kappa_{1}
     2    0.00000000e+00   # kappa_{2}
     3    0.00000000e+00   # kappa_{3}
Block RVD Q= 1.03033262e+03 # R-Parity violating D 
     1   -4.95278867e-12   # D_{1}
     2    0.00000000e+00   # D_{2}
     3    0.00000000e+00   # D_{3}
Block RVSNVEV Q= 1.03033262e+03 # sneutrino VEVs D 
     1   -1.58854492e-10   # SneutrinoVev_{1}
     2    0.00000000e+00   # SneutrinoVev_{2}
     3    0.00000000e+00   # SneutrinoVev_{3}
Block RVM2LH1 Q= 1.03033262e+03 # M2LH1 
     1    1.56320635e-11   # M2LH1_{1}
     2    0.00000000e+00   # M2LH1_{2}
     3    0.00000000e+00   # M2LH1_{3}
Block UPMNS Q= 9.11876000e+01 # neutrino mixing matrix (inverted  hierarchy)
  1  1     0.00000000e+00   # UPMNS_{11} matrix element
  1  2     1.00000000e+00   # UPMNS_{12} matrix element
  1  3     0.00000000e+00   # UPMNS_{13} matrix element
  2  1     0.00000000e+00   # UPMNS_{21} matrix element
  2  2     0.00000000e+00   # UPMNS_{22} matrix element
  2  3     1.00000000e+00   # UPMNS_{23} matrix element
  3  1     1.00000000e+00   # UPMNS_{31} matrix element
  3  2     0.00000000e+00   # UPMNS_{32} matrix element
  3  3     0.00000000e+00   # UPMNS_{33} matrix element
Block msq2 Q= 1.03033262e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.43111172e+06    # (m_Q^2)_{11}
  1  2     4.80677447e+01    # (m_Q^2)_{12}
  1  3    -1.13695757e+03    # (m_Q^2)_{13}
  2  1     4.80677447e+01    # (m_Q^2)_{21}
  2  2     1.43076371e+06    # (m_Q^2)_{22}
  2  3     8.37050809e+03    # (m_Q^2)_{23}
  3  1    -1.13695757e+03    # (m_Q^2)_{31}
  3  2     8.37050809e+03    # (m_Q^2)_{32}
  3  3     1.22307123e+06    # (m_Q^2)_{33}
Block msl2 Q= 1.03033262e+03 # super MNS slepton mass^2 matrix - DRbar
  1  1     1.58687829e+05    # (m_L^2)_{11}
  1  2     0.00000000e+00    # (m_L^2)_{12}
  1  3     0.00000000e+00    # (m_L^2)_{13}
  2  1     0.00000000e+00    # (m_L^2)_{21}
  2  2     1.58686072e+05    # (m_L^2)_{22}
  2  3     0.00000000e+00    # (m_L^2)_{23}
  3  1     0.00000000e+00    # (m_L^2)_{31}
  3  2     0.00000000e+00    # (m_L^2)_{32}
  3  3     1.57862134e+05    # (m_L^2)_{33}
Block msd2 Q= 1.03033262e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.31010357e+06    # (m_d^2)_{11}
  1  2    -3.62428992e-06    # (m_d^2)_{12}
  1  3     3.58121018e-03    # (m_d^2)_{13}
  2  1    -3.62428992e-06    # (m_d^2)_{21}
  2  2     1.31009578e+06    # (m_d^2)_{22}
  2  3    -5.77265603e-01    # (m_d^2)_{23}
  3  1     3.58121018e-03    # (m_d^2)_{31}
  3  2    -5.77265603e-01    # (m_d^2)_{32}
  3  3     1.29715952e+06    # (m_d^2)_{33}
Block msu2 Q= 1.03033262e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.32307267e+06    # (m_u^2)_{11}
  1  2    -1.76240771e-08    # (m_u^2)_{12}
  1  3    -1.57355202e-05    # (m_u^2)_{13}
  2  1    -1.76240771e-08    # (m_u^2)_{21}
  2  2     1.32306532e+06    # (m_u^2)_{22}
  2  3    -7.65839437e-02    # (m_u^2)_{23}
  3  1    -1.57355202e-05    # (m_u^2)_{31}
  3  2    -7.65839437e-02    # (m_u^2)_{32}
  3  3     9.09447908e+05    # (m_u^2)_{33}
Block mse2 Q= 1.03033262e+03 # super MNS slepton mass^2 matrix - DRbar
  1  1     5.08063265e+04    # (m_e^2)_{11}
  1  2     0.00000000e+00    # (m_e^2)_{12}
  1  3     0.00000000e+00    # (m_e^2)_{13}
  2  1     0.00000000e+00    # (m_e^2)_{21}
  2  2     5.08007351e+04    # (m_e^2)_{22}
  2  3     0.00000000e+00    # (m_e^2)_{23}
  3  1     0.00000000e+00    # (m_e^2)_{31}
  3  2     0.00000000e+00    # (m_e^2)_{32}
  3  3     4.91157108e+04    # (m_e^2)_{33}
Block tu Q= 1.03033262e+03   # super CKM trilinear matrix - DRbar
  1  1    -9.81938954e-03    # (T_u)_{11}
  1  2    -2.04890375e-08    # (T_u)_{12}
  1  3    -9.19313305e-08    # (T_u)_{13}
  2  1    -9.38549185e-06    # (T_u)_{21}
  2  2    -4.49803445e+00    # (T_u)_{22}
  2  3    -4.47028281e-04    # (T_u)_{23}
  3  1    -1.26659770e-02    # (T_u)_{31}
  3  2    -1.34426973e-01    # (T_u)_{32}
  3  3    -8.91977211e+02    # (T_u)_{33}
Block td Q= 1.03033262e+03   # super CKM trilinear matrix - DRbar
  1  1    -2.29766958e-01    # (T_d)_{11}
  1  2    -3.36193895e-06    # (T_d)_{12}
  1  3     7.99440675e-05    # (T_d)_{13}
  2  1    -7.36099510e-05    # (T_d)_{21}
  2  2    -5.03026769e+00    # (T_d)_{22}
  2  3    -1.28866892e-02    # (T_d)_{23}
  3  1     7.60808267e-02    # (T_d)_{31}
  3  2    -5.60123133e-01    # (T_d)_{32}
  3  3    -2.05049459e+02    # (T_d)_{33}
Block te Q= 1.03033262e+03   # super CKM trilinear matrix - DRbar
  1  1    -9.85264970e-03    # (T_e)_{11}
  1  2     0.00000000e+00    # (T_e)_{12}
  1  3     0.00000000e+00    # (T_e)_{13}
  2  1     0.00000000e+00    # (T_e)_{21}
  2  2    -2.03718045e+00    # (T_e)_{22}
  2  3     0.00000000e+00    # (T_e)_{23}
  3  1     0.00000000e+00    # (T_e)_{31}
  3  2     0.00000000e+00    # (T_e)_{32}
  3  3    -3.52607702e+01    # (T_e)_{33}
Block VCKM Q= 1.03033262e+03 # DRbar CKM mixing matrix
  1  1     9.73840738e-01    # CKM_{11} matrix element
  1  2     2.27197366e-01    # CKM_{12} matrix element
  1  3     3.94627307e-03    # CKM_{13} matrix element
  2  1    -2.27161577e-01    # CKM_{21} matrix element
  2  2     9.72962448e-01    # CKM_{22} matrix element
  2  3     4.17335975e-02    # CKM_{23} matrix element
  3  1     5.64218794e-03    # CKM_{31} matrix element
  3  2    -4.15383190e-02    # CKM_{32} matrix element
  3  3     9.99120981e-01    # CKM_{33} matrix element
Block msoft Q= 1.03033262e+03 # MSSM DRbar SUSY breaking parameters
     1     2.54573203e+02     # M_1(Q)
     2     4.68778469e+02     # M_2(Q)
     3     1.31944417e+03     # M_3(Q)
    21     1.37070459e+05     # mH1^2(Q)
    22    -5.22726225e+05     # mH2^2(Q)
Block USQMIX  # super CKM squark mass^2 matrix
  1  1     2.01365059e-05   # (USQMIX)_{11}
  1  2     2.13209931e-04   # (USQMIX)_{12}
  1  3     3.92332040e-01   # (USQMIX)_{13}
  1  4     1.13197343e-10   # (USQMIX)_{14}
  1  5     5.49670219e-07   # (USQMIX)_{15}
  1  6     9.19823638e-01   # (USQMIX)_{16}
  2  1     1.38618314e-04   # (USQMIX)_{21}
  2  2     1.46699839e-03   # (USQMIX)_{22}
  2  3     9.19822536e-01   # (USQMIX)_{23}
  2  4     4.63706386e-09   # (USQMIX)_{24}
  2  5     2.24839608e-05   # (USQMIX)_{25}
  2  6    -3.92331914e-01   # (USQMIX)_{26}
  3  1     1.21007133e-07   # (USQMIX)_{31}
  3  2     7.17361138e-03   # (USQMIX)_{32}
  3  3    -3.11764371e-05   # (USQMIX)_{33}
  3  4     1.96804975e-08   # (USQMIX)_{34}
  3  5     9.99974269e-01   # (USQMIX)_{35}
  3  6     1.10373022e-05   # (USQMIX)_{36}
  4  1     1.56601956e-05   # (USQMIX)_{41}
  4  2     1.23010971e-10   # (USQMIX)_{42}
  4  3    -6.42992640e-09   # (USQMIX)_{43}
  4  4     1.00000000e+00   # (USQMIX)_{44}
  4  5    -1.96840070e-08   # (USQMIX)_{45}
  4  6     2.27664488e-09   # (USQMIX)_{46}
  5  1     1.47041842e-01   # (USQMIX)_{51}
  5  2     9.89103704e-01   # (USQMIX)_{52}
  5  3    -1.43717761e-03   # (USQMIX)_{53}
  5  4    -2.30297544e-06   # (USQMIX)_{54}
  5  5    -7.09569496e-03   # (USQMIX)_{55}
  5  6     3.80515423e-04   # (USQMIX)_{56}
  6  1     9.89130263e-01   # (USQMIX)_{61}
  6  2    -1.47038104e-01   # (USQMIX)_{62}
  6  3     7.67551081e-05   # (USQMIX)_{63}
  6  4    -1.54899340e-05   # (USQMIX)_{64}
  6  5     1.05470428e-03   # (USQMIX)_{65}
  6  6    -2.03101012e-05   # (USQMIX)_{66}
Block DSQMIX  # super CKM squark mass^2 matrix
  1  1     4.61403972e-03   # (DSQMIX)_{11}
  1  2    -3.39698869e-02   # (DSQMIX)_{12}
  1  3     9.77350264e-01   # (DSQMIX)_{13}
  1  4     9.02884404e-07   # (DSQMIX)_{14}
  1  5    -1.45554324e-04   # (DSQMIX)_{15}
  1  6     2.08832942e-01   # (DSQMIX)_{16}
  2  1    -1.58561564e-03   # (DSQMIX)_{21}
  2  2     1.16746575e-02   # (DSQMIX)_{22}
  2  3    -2.08545975e-01   # (DSQMIX)_{23}
  2  4    -1.88625874e-06   # (DSQMIX)_{24}
  2  5     3.04202466e-04   # (DSQMIX)_{25}
  2  6     9.77941548e-01   # (DSQMIX)_{26}
  3  1     1.59641857e-06   # (DSQMIX)_{31}
  3  2     3.70195896e-03   # (DSQMIX)_{32}
  3  3     3.38090912e-04   # (DSQMIX)_{33}
  3  4     4.06314504e-06   # (DSQMIX)_{34}
  3  5     9.99993050e-01   # (DSQMIX)_{35}
  3  6    -2.83155386e-04   # (DSQMIX)_{36}
  4  1     1.69615840e-04   # (DSQMIX)_{41}
  4  2     5.78281358e-08   # (DSQMIX)_{42}
  4  3    -2.09855042e-06   # (DSQMIX)_{43}
  4  4     9.99999986e-01   # (DSQMIX)_{44}
  4  5    -4.06245110e-06   # (DSQMIX)_{45}
  4  6     1.75687462e-06   # (DSQMIX)_{46}
  5  1    -1.36834807e-01   # (DSQMIX)_{51}
  5  2     9.89923604e-01   # (DSQMIX)_{52}
  5  3     3.59849466e-02   # (DSQMIX)_{53}
  5  4     2.32203488e-05   # (DSQMIX)_{54}
  5  5    -3.67786581e-03   # (DSQMIX)_{55}
  5  6    -4.36462878e-03   # (DSQMIX)_{56}
  6  1     9.90581851e-01   # (DSQMIX)_{61}
  6  2     1.36920790e-01   # (DSQMIX)_{62}
  6  3     8.45829552e-05   # (DSQMIX)_{63}
  6  4    -1.68028164e-04   # (DSQMIX)_{64}
  6  5    -5.08490878e-04   # (DSQMIX)_{65}
  6  6    -1.02536251e-05   # (DSQMIX)_{66}
Block RVLMIX  # charged higgs-slepton mixing matrix 
  1 1    0.00000000e+00   # C_{11}
  1 2    0.00000000e+00   # C_{12}
  1 3    0.00000000e+00   # C_{13}
  1 4    0.00000000e+00   # C_{14}
  1 5    1.21372854e-01   # C_{15}
  1 6    0.00000000e+00   # C_{16}
  1 7    0.00000000e+00   # C_{17}
  1 8    9.92606987e-01   # C_{18}
  2 1    0.00000000e+00   # C_{21}
  2 2    0.00000000e+00   # C_{22}
  2 3    0.00000000e+00   # C_{23}
  2 4    7.19151616e-03   # C_{24}
  2 5    0.00000000e+00   # C_{25}
  2 6    0.00000000e+00   # C_{26}
  2 7    9.99974141e-01   # C_{27}
  2 8    0.00000000e+00   # C_{28}
  3 1   -4.09741471e-18   # C_{31}
  3 2    5.23343982e-17   # C_{32}
  3 3    3.47844709e-05   # C_{33}
  3 4    0.00000000e+00   # C_{34}
  3 5    0.00000000e+00   # C_{35}
  3 6    9.99999999e-01   # C_{36}
  3 7    0.00000000e+00   # C_{37}
  3 8    0.00000000e+00   # C_{38}
  4 1    1.37830108e-15   # C_{41}
  4 2    6.93923892e-16   # C_{42}
  4 3    9.99999999e-01   # C_{43}
  4 4    0.00000000e+00   # C_{44}
  4 5    0.00000000e+00   # C_{45}
  4 6   -3.47844709e-05   # C_{46}
  4 7    0.00000000e+00   # C_{47}
  4 8    0.00000000e+00   # C_{48}
  5 1    0.00000000e+00   # C_{51}
  5 2    0.00000000e+00   # C_{52}
  5 3    0.00000000e+00   # C_{53}
  5 4    9.99974141e-01   # C_{54}
  5 5    0.00000000e+00   # C_{55}
  5 6    0.00000000e+00   # C_{56}
  5 7   -7.19151616e-03   # C_{57}
  5 8    0.00000000e+00   # C_{58}
  6 1    0.00000000e+00   # C_{61}
  6 2    0.00000000e+00   # C_{62}
  6 3    0.00000000e+00   # C_{63}
  6 4    0.00000000e+00   # C_{64}
  6 5    9.92606987e-01   # C_{65}
  6 6    0.00000000e+00   # C_{66}
  6 7    0.00000000e+00   # C_{67}
  6 8   -1.21372854e-01   # C_{68}
  7 1    9.94680728e-01   # C_{71}
  7 2    1.03006066e-01   # C_{72}
  7 3   -1.44244793e-15   # C_{73}
  7 4    0.00000000e+00   # C_{74}
  7 5    0.00000000e+00   # C_{75}
  7 6   -1.26496625e-18   # C_{76}
  7 7    0.00000000e+00   # C_{77}
  7 8    0.00000000e+00   # C_{78}
Block RVHMIX  # CP-even neutral scalar mixing matrix 
  1 1    1.05270866e-01   # curlyN_{11}
  1 2    9.94443585e-01   # curlyN_{12}
  1 3   -3.51528567e-14   # curlyN_{13}
  1 4    0.00000000e+00   # curlyN_{14}
  1 5    0.00000000e+00   # curlyN_{15}
  2 1    0.00000000e+00   # curlyN_{21}
  2 2    0.00000000e+00   # curlyN_{22}
  2 3    0.00000000e+00   # curlyN_{23}
  2 4    0.00000000e+00   # curlyN_{24}
  2 5    1.00000000e+00   # curlyN_{25}
  3 1    0.00000000e+00   # curlyN_{31}
  3 2    0.00000000e+00   # curlyN_{32}
  3 3    0.00000000e+00   # curlyN_{33}
  3 4    1.00000000e+00   # curlyN_{34}
  3 5    0.00000000e+00   # curlyN_{35}
  4 1    5.59169905e-15   # curlyN_{41}
  4 2    3.47573399e-14   # curlyN_{42}
  4 3    1.00000000e+00   # curlyN_{43}
  4 4    0.00000000e+00   # curlyN_{44}
  4 5    0.00000000e+00   # curlyN_{45}
  5 1    9.94443585e-01   # curlyN_{51}
  5 2   -1.05270866e-01   # curlyN_{52}
  5 3   -1.90169397e-15   # curlyN_{53}
  5 4    0.00000000e+00   # curlyN_{54}
  5 5    0.00000000e+00   # curlyN_{55}
Block RVAMIX  # CP-odd neutral scalar mixing matrix 
  1 1    0.00000000e+00   # curlyN~_{11}
  1 2    0.00000000e+00   # curlyN~_{12}
  1 3    0.00000000e+00   # curlyN~_{13}
  1 4    0.00000000e+00   # curlyN~_{14}
  1 5    1.00000000e+00   # curlyN~_{15}
  2 1    0.00000000e+00   # curlyN~_{21}
  2 2    0.00000000e+00   # curlyN~_{22}
  2 3    0.00000000e+00   # curlyN~_{23}
  2 4    1.00000000e+00   # curlyN~_{24}
  2 5    0.00000000e+00   # curlyN~_{25}
  3 1   -3.72355312e-15   # curlyN~_{31}
  3 2    3.57340356e-14   # curlyN~_{32}
  3 3    1.00000000e+00   # curlyN~_{33}
  3 4    0.00000000e+00   # curlyN~_{34}
  3 5    0.00000000e+00   # curlyN~_{35}
  4 1    9.94680732e-01   # curlyN~_{41}
  4 2    1.03006031e-01   # curlyN~_{42}
  4 3    2.29253758e-17   # curlyN~_{43}
  4 4    0.00000000e+00   # curlyN~_{44}
  4 5    0.00000000e+00   # curlyN~_{45}
