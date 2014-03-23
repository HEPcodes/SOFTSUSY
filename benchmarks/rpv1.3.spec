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
     1    1.50000000e+02   # m0
     2    6.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.48286593e+16   # MX scale
Block RVLAMLLEIN           # input LLE couplings at MSUSY
  1 2 1   1.00000000e-02   # lambda_{121}
  2 1 1  -1.00000000e-02   # lambda_{211}
# SOFTSUSY-specific non SLHA information:
# MIXING=1 Desired accuracy=1.00000000e-03 Achieved accuracy=3.56558591e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.05225405e+01   # MW
        25     1.15947498e+02   # CP even neutral scalar
        35     4.21951075e+02   # CP even neutral scalar
        36     4.21951075e+02   # CP odd neutral scalar
        37     2.66771256e+02   # charged scalar
   1000021     1.35744015e+03   # ~g
   1000022     2.49015414e+02   # ~neutralino(1)
   1000023     4.69722662e+02   # ~neutralino(2)
   1000024     4.69789147e+02   # ~chargino(1)
   1000025    -7.53619424e+02   # ~neutralino(3)
   1000035     7.65731223e+02   # ~neutralino(4)
   1000037     7.65982251e+02   # ~chargino(2)
   1000011     2.73878954e+02   # charged scalar
   1000013     2.73890281e+02   # charged scalar
   1000015     4.30188527e+02   # charged scalar
   2000011     4.30629726e+02   # charged scalar
   2000013     4.30632306e+02   # charged scalar
   2000015     8.50008627e+02   # charged scalar
   1000012     4.23122842e+02   # CP even neutral scalar
   1000014     4.23126762e+02   # CP even neutral scalar
   1000016     8.45973128e+02   # CP even neutral scalar
   1000017     4.23122842e+02   # CP odd neutral scalar
   1000018     4.23126762e+02   # CP odd neutral scalar
   1000019     8.45973128e+02   # CP odd neutral scalar
   1000001     1.14378737e+03   # ~d_1
   1000003     1.18489447e+03   # ~d_2
   1000005     1.19388598e+03   # ~d_3
   2000001     1.19388986e+03   # ~d_4
   2000003     1.24721803e+03   # ~d_5
   2000005     1.24724061e+03   # ~d_6
   1000002     9.61172665e+02   # ~u_1
   1000004     1.17171728e+03   # ~u_2
   1000006     1.19828774e+03   # ~u_3
   2000002     1.19829331e+03   # ~u_4
   2000004     1.24485496e+03   # ~u_5
   2000006     1.24486016e+03   # ~u_6
        12     2.21677199e-42   # Mnu1 inverted hierarchy output
        14     1.99775647e-14   # Mnu2 inverted hierarchy output
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
  2 2   -3.96486039e-15   # N_{22}
  2 3    0.00000000e+00   # N_{23}
  2 4   -6.29961604e-24   # N_{24}
  2 5   -2.89492584e-24   # N_{25}
  2 6   -3.63779025e-24   # N_{26}
  2 7   -9.43465003e-28   # N_{27}
  3 1    3.96486039e-15   # N_{31}
  3 2    1.00000000e+00   # N_{32}
  3 3    0.00000000e+00   # N_{33}
  3 4   -4.18382787e-10   # N_{34}
  3 5    4.35245839e-10   # N_{35}
  3 6   -2.44695641e-09   # N_{36}
  3 7    3.79534048e-12   # N_{37}
  4 1    8.85494390e-24   # N_{41}
  4 2    5.94179398e-10   # N_{42}
  4 3    0.00000000e+00   # N_{43}
  4 4    9.97021253e-01   # N_{44}
  4 5   -1.26348540e-02   # N_{45}
  4 6    7.00588552e-02   # N_{46}
  4 7   -2.96772520e-02   # N_{47}
  5 1   -9.56584693e-25   # N_{51}
  5 2   -8.39824169e-10   # N_{52}
  5 3    0.00000000e+00   # N_{53}
  5 4    2.81359532e-02   # N_{54}
  5 5    9.77193623e-01   # N_{55}
  5 6   -1.74023111e-01   # N_{56}
  5 7    1.18393190e-01   # N_{57}
  6 1    9.21330383e-24   # N_{61}
  6 2    1.69195509e-09   # N_{62}
  6 3    0.00000000e+00   # N_{63}
  6 4   -2.79193034e-02   # N_{64}
  6 5    4.04942765e-02   # N_{65}
  6 6    7.04527464e-01   # N_{66}
  6 7    7.07970182e-01   # N_{67}
  7 1   -8.85662823e-24   # N_{71}
  7 2   -1.55917522e-09   # N_{72}
  7 3    0.00000000e+00   # N_{73}
  7 4    6.61626984e-02   # N_{74}
  7 5   -2.08070172e-01   # N_{75}
  7 6   -6.84433171e-01   # N_{76}
  7 7    6.95615221e-01   # N_{77}
Block RVUMIX  # lepton-chargino mixing matrix U
  1 1    1.00000000e+00   # U_{11}
  1 2    5.42101086e-20   # U_{12}
  1 3    0.00000000e+00   # U_{13}
  1 4    1.59872935e-24   # U_{14}
  1 5   -2.83050136e-23   # U_{15}
  2 1    6.29691302e-32   # U_{21}
  2 2   -1.00000000e+00   # U_{22}
  2 3    0.00000000e+00   # U_{23}
  2 4   -2.97900733e-10   # U_{24}
  2 5    4.43311981e-09   # U_{25}
  3 1    0.00000000e+00   # U_{31}
  3 2    0.00000000e+00   # U_{32}
  3 3    1.00000000e+00   # U_{33}
  3 4    0.00000000e+00   # U_{34}
  3 5    0.00000000e+00   # U_{35}
  4 1   -8.59434963e-24   # U_{41}
  4 2   -1.39206826e-09   # U_{42}
  4 3    0.00000000e+00   # U_{43}
  4 4    9.68520978e-01   # U_{44}
  4 5   -2.48931948e-01   # U_{45}
  5 1    2.70157960e-23   # U_{51}
  5 2    4.21941252e-09   # U_{52}
  5 3    0.00000000e+00   # U_{53}
  5 4    2.48931948e-01   # U_{54}
  5 5    9.68520978e-01   # U_{55}
Block RVVMIX  # lepton-chargino mixing matrix V
  1 1    1.00000000e+00   # V_{11}
  1 2    3.20923843e-17   # V_{12}
  1 3    0.00000000e+00   # V_{13}
  1 4    0.00000000e+00   # V_{14}
  1 5    9.99110282e-46   # V_{15}
  2 1   -3.20923843e-17   # V_{21}
  2 2   -1.00000000e+00   # V_{22}
  2 3    0.00000000e+00   # V_{23}
  2 4   -4.89994791e-13   # V_{24}
  2 5    1.72589708e-12   # V_{25}
  3 1    0.00000000e+00   # V_{31}
  3 2    0.00000000e+00   # V_{32}
  3 3    1.00000000e+00   # V_{33}
  3 4    0.00000000e+00   # V_{34}
  3 5    0.00000000e+00   # V_{35}
  4 1   -2.47238293e-29   # V_{41}
  4 2   -7.70395528e-13   # V_{42}
  4 3    0.00000000e+00   # V_{43}
  4 4    9.86053939e-01   # V_{44}
  4 5   -1.66426051e-01   # V_{45}
  5 1    5.19986393e-29   # V_{51}
  5 2    1.62027972e-12   # V_{52}
  5 3    0.00000000e+00   # V_{53}
  5 4    1.66426051e-01   # V_{54}
  5 5    9.86053939e-01   # V_{55}
Block gauge Q= 1.03489143e+03  # SM gauge couplings
     1     3.63063539e-01   # g'(Q)MSSM DRbar
     2     6.41438383e-01   # g(Q)MSSM DRbar
     3     1.05565102e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.03489143e+03   # diagonal Up Yukawa matrix
  1  1     7.29101734e-06    # YU_{11}(Q)MSSM DRbar
  2  2     3.33981871e-03    # YU_{22}(Q)MSSM DRbar
  3  3     8.51711336e-01    # YU_{33}(Q)MSSM DRbar
Block yd Q= 1.03489143e+03   # diagonal down Yukawa matrix
  1  1     1.40183302e-04    # YD_{11}(Q)MSSM DRbar
  2  2     3.06933860e-03    # YD_{22}(Q)MSSM DRbar
  3  3     1.33715369e-01    # YD_{33}(Q)MSSM DRbar
Block ye Q= 1.03489143e+03   # diagonal lepton Yukawa matrix
  1  1     2.78403799e-05    # YE_{11}(Q)MSSM DRbar
  2  2     5.75650492e-03    # YE_{22}(Q)MSSM DRbar
  3  3     1.00175219e-01    # YE_{33}(Q)MSSM DRbar
Block hmix Q= 1.03489143e+03 # Higgs mixing parameters
     1     7.48240426e+02    # mu(Q)MSSM DRbar
     2     9.65595802e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44376812e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     7.41838984e+05    # mA^2(Q)MSSM DRbar
Block RVLAMLLE Q= 1.03489143e+03 # non-zero R-Parity violating LLE couplings 
  1 2 1    9.99999971e-03   # lambda_{121}
  1 2 2    5.68035831e-31   # lambda_{122}
  1 3 3    3.28053910e-30   # lambda_{133}
  2 1 1   -9.99999971e-03   # lambda_{211}
  2 1 2   -5.68035831e-31   # lambda_{212}
  2 3 3   -4.94371056e-16   # lambda_{233}
  3 1 3   -3.28053910e-30   # lambda_{313}
  3 2 3    4.94371056e-16   # lambda_{323}
Block RVLAMLQD Q= 1.03489143e+03 # non-zero R-Parity violating LQD couplings 
  1 1 1    4.59309445e-33   # lambda'_{111}
  1 1 2   -2.74264858e-37   # lambda'_{112}
  1 1 3    2.76999371e-34   # lambda'_{113}
  1 2 1   -1.25265124e-38   # lambda'_{121}
  1 2 2    1.00566612e-31   # lambda'_{122}
  1 2 3   -2.03930180e-33   # lambda'_{123}
  1 3 1    2.93671047e-37   # lambda'_{131}
  1 3 2   -4.73373396e-35   # lambda'_{132}
  1 3 3    4.37991239e-30   # lambda'_{133}
  2 1 1   -6.92170644e-19   # lambda'_{211}
  2 1 2    4.13312365e-23   # lambda'_{212}
  2 1 3   -4.17433214e-20   # lambda'_{213}
  2 2 1    1.88772360e-24   # lambda'_{221}
  2 2 2   -1.51551981e-17   # lambda'_{222}
  2 2 3    3.07319220e-19   # lambda'_{223}
  2 3 1   -4.42557144e-23   # lambda'_{231}
  2 3 2    7.13365448e-21   # lambda'_{232}
  2 3 3   -6.60044519e-16   # lambda'_{233}
Block RVLAMUDD Q= 1.03489143e+03 # non-zero R-Parity violating UDD couplings 
Block RVTLLE Q= 1.03489143e+03 # non-zero R-Parity violating LLE soft terms 
  1 2 1    2.40819610e-07   # T_{121}
  1 2 2   -4.67018210e-28   # T_{122}
  1 3 3   -3.47677093e-27   # T_{133}
  2 1 1   -2.40819610e-07   # T_{211}
  2 1 2    4.67018210e-28   # T_{212}
  2 3 3    5.23949041e-13   # T_{233}
  3 1 3    3.47677093e-27   # T_{313}
  3 2 3   -5.23949041e-13   # T_{323}
Block RVTLQD Q= 1.03489143e+03 # non-zero R-Parity violating LQD soft terms 
  1 1 1   -1.08005380e-29   # T'_{111}
  1 1 2   -1.93551645e-33   # T'_{112}
  1 1 3    1.95628071e-30   # T'_{113}
  1 2 1   -8.84013832e-35   # T'_{121}
  1 2 2   -2.36461374e-28   # T'_{122}
  1 2 3   -1.44024588e-29   # T'_{123}
  1 3 1    2.08362349e-33   # T'_{131}
  1 3 2   -3.35863273e-31   # T'_{132}
  1 3 3   -9.82367386e-27   # T'_{133}
  2 1 1    1.62762903e-15   # T'_{211}
  2 1 2    2.91677617e-19   # T'_{212}
  2 1 3   -2.94806760e-16   # T'_{213}
  2 2 1    1.33218732e-20   # T'_{221}
  2 2 2    3.56344653e-14   # T'_{222}
  2 2 3    2.17041563e-15   # T'_{223}
  2 3 1   -3.13997005e-19   # T'_{231}
  2 3 2    5.06137804e-17   # T'_{232}
  2 3 3    1.48041717e-12   # T'_{233}
Block RVTUDD Q= 1.03489143e+03 # non-zero R-Parity violating UDD soft terms 
Block RVKAPPA Q= 1.03489143e+03 # R-Parity violating kappa 
     1    2.45007055e-26   # kappa_{1}
     2   -3.69221010e-12   # kappa_{2}
     3    0.00000000e+00   # kappa_{3}
Block RVD Q= 1.03489143e+03 # R-Parity violating D 
     1   -1.48145177e-23   # D_{1}
     2    2.23256612e-09   # D_{2}
     3    0.00000000e+00   # D_{3}
Block RVSNVEV Q= 1.03489143e+03 # sneutrino VEVs D 
     1    1.31317465e-21   # SneutrinoVev_{1}
     2   -1.92962409e-07   # SneutrinoVev_{2}
     3    0.00000000e+00   # SneutrinoVev_{3}
Block RVM2LH1 Q= 1.03489143e+03 # M2LH1 
     1    2.72956070e-23   # M2LH1_{1}
     2   -4.11347871e-09   # M2LH1_{2}
     3    0.00000000e+00   # M2LH1_{3}
Block UPMNS Q= 9.11876000e+01 # neutrino mixing matrix (inverted  hierarchy)
  1  1     1.00000000e+00   # UPMNS_{11} matrix element
  1  2     3.96454996e-15   # UPMNS_{12} matrix element
  1  3     0.00000000e+00   # UPMNS_{13} matrix element
  2  1    -3.96454996e-15   # UPMNS_{21} matrix element
  2  2     1.00000000e+00   # UPMNS_{22} matrix element
  2  3     0.00000000e+00   # UPMNS_{23} matrix element
  3  1     0.00000000e+00   # UPMNS_{31} matrix element
  3  2     0.00000000e+00   # UPMNS_{32} matrix element
  3  3     1.00000000e+00   # UPMNS_{33} matrix element
Block msq2 Q= 1.03489143e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.45009297e+06    # (m^_Q^2)_{11}
  1  2     4.95330450e+01    # (m^_Q^2)_{12}
  1  3    -1.17171565e+03    # (m^_Q^2)_{13}
  2  1     4.95330450e+01    # (m^_Q^2)_{21}
  2  2     1.44973404e+06    # (m^_Q^2)_{22}
  2  3     8.62640366e+03    # (m^_Q^2)_{23}
  3  1    -1.17171565e+03    # (m^_Q^2)_{31}
  3  2     8.62640366e+03    # (m^_Q^2)_{32}
  3  3     1.23573128e+06    # (m^_Q^2)_{33}
Block msl2 Q= 1.03489143e+03 # super MNS slepton mass^2 matrix - DRbar
  1  1     1.78484272e+05    # (m^_L^2)_{11}
  1  2    -2.00036870e-23    # (m^_L^2)_{12}
  1  3     0.00000000e+00    # (m^_L^2)_{13}
  2  1    -2.00036870e-23    # (m^_L^2)_{21}
  2  2     1.78480986e+05    # (m^_L^2)_{22}
  2  3     0.00000000e+00    # (m^_L^2)_{23}
  3  1     0.00000000e+00    # (m^_L^2)_{31}
  3  2     0.00000000e+00    # (m^_L^2)_{32}
  3  3     1.77499697e+05    # (m^_L^2)_{33}
Block msd2 Q= 1.03489143e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.32925056e+06    # (m^_d^2)_{11}
  1  2    -3.46745054e-06    # (m^_d^2)_{12}
  1  3     3.58976864e-03    # (m^_d^2)_{13}
  2  1    -3.46745054e-06    # (m^_d^2)_{21}
  2  2     1.32924326e+06    # (m^_d^2)_{22}
  2  3    -5.78659604e-01    # (m^_d^2)_{23}
  3  1     3.58976864e-03    # (m^_d^2)_{31}
  3  2    -5.78659604e-01    # (m^_d^2)_{32}
  3  3     1.31598173e+06    # (m^_d^2)_{33}
Block msu2 Q= 1.03489143e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.34219773e+06    # (m^_u^2)_{11}
  1  2    -1.75388493e-08    # (m^_u^2)_{12}
  1  3    -1.56607749e-05    # (m^_u^2)_{13}
  2  1    -1.75388493e-08    # (m^_u^2)_{21}
  2  2     1.34219019e+06    # (m^_u^2)_{22}
  2  3    -7.62243037e-02    # (m^_u^2)_{23}
  3  1    -1.56607749e-05    # (m^_u^2)_{31}
  3  2    -7.62243037e-02    # (m^_u^2)_{32}
  3  3     9.16080119e+05    # (m^_u^2)_{33}
Block mse2 Q= 1.03489143e+03 # super MNS slepton mass^2 matrix - DRbar
  1  1     7.07066938e+04    # (m^_e^2)_{11}
  1  2    -5.89345086e-16    # (m^_e^2)_{12}
  1  3     0.00000000e+00    # (m^_e^2)_{13}
  2  1    -5.89345086e-16    # (m^_e^2)_{21}
  2  2     7.07183560e+04    # (m^_e^2)_{22}
  2  3     0.00000000e+00    # (m^_e^2)_{23}
  3  1     0.00000000e+00    # (m^_e^2)_{31}
  3  2     0.00000000e+00    # (m^_e^2)_{32}
  3  3     6.86985610e+04    # (m^_e^2)_{33}
Block tu Q= 1.03489143e+03   # super CKM trilinear matrix - DRbar
  1  1    -9.81756537e-03    # (T^_u)_{11}
  1  2    -2.06581999e-08    # (T^_u)_{12}
  1  3    -9.18602324e-08    # (T^_u)_{13}
  2  1    -9.46298154e-06    # (T^_u)_{21}
  2  2    -4.49719924e+00    # (T^_u)_{22}
  2  3    -4.46696026e-04    # (T^_u)_{23}
  3  1    -1.26582969e-02    # (T^_u)_{31}
  3  2    -1.34351232e-01    # (T^_u)_{32}
  3  3    -8.91813349e+02    # (T^_u)_{33}
Block td Q= 1.03489143e+03   # super CKM trilinear matrix - DRbar
  1  1    -2.29717270e-01    # (T^_d)_{11}
  1  2    -3.36158576e-06    # (T^_d)_{12}
  1  3     7.99374392e-05    # (T^_d)_{13}
  2  1    -7.36022546e-05    # (T^_d)_{21}
  2  2    -5.02917957e+00    # (T^_d)_{22}
  2  3    -1.28856238e-02    # (T^_d)_{23}
  3  1     7.61050495e-02    # (T^_d)_{31}
  3  2    -5.60301482e-01    # (T^_d)_{32}
  3  3    -2.05084613e+02    # (T^_d)_{33}
Block te Q= 1.03489143e+03   # super CKM trilinear matrix - DRbar
  1  1    -9.85333723e-03    # (T^_e)_{11}
  1  2    -1.22597396e-21    # (T^_e)_{12}
  1  3     0.00000000e+00    # (T^_e)_{13}
  2  1    -5.93743980e-24    # (T^_e)_{21}
  2  2    -2.03728230e+00    # (T^_e)_{22}
  2  3     0.00000000e+00    # (T^_e)_{23}
  3  1     0.00000000e+00    # (T^_e)_{31}
  3  2     0.00000000e+00    # (T^_e)_{32}
  3  3    -3.52630473e+01    # (T^_e)_{33}
Block VCKM Q= 1.03489143e+03 # DRbar CKM mixing matrix
  1  1     9.73840740e-01    # CKM_{11} matrix element
  1  2     2.27197361e-01    # CKM_{12} matrix element
  1  3     3.94619356e-03    # CKM_{13} matrix element
  2  1    -2.27161573e-01    # CKM_{21} matrix element
  2  2     9.72962485e-01    # CKM_{22} matrix element
  2  3     4.17327580e-02    # CKM_{23} matrix element
  3  1     5.64207422e-03    # CKM_{31} matrix element
  3  2    -4.15374835e-02    # CKM_{32} matrix element
  3  3     9.99121016e-01    # CKM_{33} matrix element
Block msoft Q= 1.03489143e+03 # MSSM DRbar SUSY breaking parameters
     1     2.54555704e+02     # M_1(Q)
     2     4.68774275e+02     # M_2(Q)
     3     1.31943048e+03     # M_3(Q)
    21     1.56210841e+05     # mH1^2(Q)
    22    -5.22073305e+05     # mH2^2(Q)
Block USQMIX  # super CKM squark mass^2 matrix
  1  1     1.99821472e-05   # (USQMIX)_{11}
  1  2     2.11587915e-04   # (USQMIX)_{12}
  1  3     3.88159600e-01   # (USQMIX)_{13}
  1  4     1.09796427e-10   # (USQMIX)_{14}
  1  5     5.33186640e-07   # (USQMIX)_{15}
  1  6     9.21592144e-01   # (USQMIX)_{16}
  2  1     1.36275495e-04   # (USQMIX)_{21}
  2  2     1.44228818e-03   # (USQMIX)_{22}
  2  3     9.21591078e-01   # (USQMIX)_{23}
  2  4     3.99567902e-09   # (USQMIX)_{24}
  2  5     1.93749377e-05   # (USQMIX)_{25}
  2  6    -3.88159485e-01   # (USQMIX)_{26}
  3  1     1.29420141e-07   # (USQMIX)_{31}
  3  2     7.18536465e-03   # (USQMIX)_{32}
  3  3    -2.82032631e-05   # (USQMIX)_{33}
  3  4     2.05205214e-08   # (USQMIX)_{34}
  3  5     9.99974184e-01   # (USQMIX)_{35}
  3  6     9.65053316e-06   # (USQMIX)_{36}
  4  1     1.56857648e-05   # (USQMIX)_{41}
  4  2     1.35112282e-10   # (USQMIX)_{42}
  4  3    -5.81647587e-09   # (USQMIX)_{43}
  4  4     1.00000000e+00   # (USQMIX)_{44}
  4  5    -2.05242354e-08   # (USQMIX)_{45}
  4  6     1.99054606e-09   # (USQMIX)_{46}
  5  1     1.47404805e-01   # (USQMIX)_{51}
  5  2     9.89049634e-01   # (USQMIX)_{52}
  5  3    -1.41540580e-03   # (USQMIX)_{53}
  5  4    -2.31244556e-06   # (USQMIX)_{54}
  5  5    -7.10692827e-03   # (USQMIX)_{55}
  5  6     3.65878471e-04   # (USQMIX)_{56}
  6  1     9.89076238e-01   # (USQMIX)_{61}
  6  2    -1.47401044e-01   # (USQMIX)_{62}
  6  3     7.61226232e-05   # (USQMIX)_{63}
  6  4    -1.55143751e-05   # (USQMIX)_{64}
  6  5     1.05903192e-03   # (USQMIX)_{65}
  6  6    -1.96658348e-05   # (USQMIX)_{66}
Block DSQMIX  # super CKM squark mass^2 matrix
  1  1     4.64689962e-03   # (DSQMIX)_{11}
  1  2    -3.42118313e-02   # (DSQMIX)_{12}
  1  3     9.79756820e-01   # (DSQMIX)_{13}
  1  4     8.59566314e-07   # (DSQMIX)_{14}
  1  5    -1.38569916e-04   # (DSQMIX)_{15}
  1  6     1.97191562e-01   # (DSQMIX)_{16}
  2  1    -1.53409166e-03   # (DSQMIX)_{21}
  2  2     1.12952677e-02   # (DSQMIX)_{22}
  2  3    -1.96910265e-01   # (DSQMIX)_{23}
  2  4    -1.73703208e-06   # (DSQMIX)_{24}
  2  5     2.80123986e-04   # (DSQMIX)_{25}
  2  6     9.80355207e-01   # (DSQMIX)_{26}
  3  1     1.51746793e-06   # (DSQMIX)_{31}
  3  2     3.70701226e-03   # (DSQMIX)_{32}
  3  3     3.23880285e-04   # (DSQMIX)_{33}
  3  4     4.07004452e-06   # (DSQMIX)_{34}
  3  5     9.99993042e-01   # (DSQMIX)_{35}
  3  6    -2.63390292e-04   # (DSQMIX)_{36}
  4  1     1.69819511e-04   # (DSQMIX)_{41}
  4  2     5.41781453e-08   # (DSQMIX)_{42}
  4  3    -2.01038149e-06   # (DSQMIX)_{43}
  4  4     9.99999986e-01   # (DSQMIX)_{44}
  4  5    -4.06944973e-06   # (DSQMIX)_{45}
  4  6     1.63431986e-06   # (DSQMIX)_{46}
  5  1    -1.35982778e-01   # (DSQMIX)_{51}
  5  2     9.90036980e-01   # (DSQMIX)_{52}
  5  3     3.60945153e-02   # (DSQMIX)_{53}
  5  4     2.31036079e-05   # (DSQMIX)_{54}
  5  5    -3.68273958e-03   # (DSQMIX)_{55}
  5  6    -4.36875376e-03   # (DSQMIX)_{56}
  6  1     9.90699101e-01   # (DSQMIX)_{61}
  6  2     1.36069852e-01   # (DSQMIX)_{62}
  6  3     5.38229379e-05   # (DSQMIX)_{63}
  6  4    -1.68249351e-04   # (DSQMIX)_{64}
  6  5    -5.05937948e-04   # (DSQMIX)_{65}
  6  6    -6.51035563e-06   # (DSQMIX)_{66}
Block RVLMIX  # charged higgs-slepton mixing matrix 
  1 1    0.00000000e+00   # C_{11}
  1 2    0.00000000e+00   # C_{12}
  1 3    0.00000000e+00   # C_{13}
  1 4    0.00000000e+00   # C_{14}
  1 5    1.21293705e-01   # C_{15}
  1 6    0.00000000e+00   # C_{16}
  1 7    0.00000000e+00   # C_{17}
  1 8    9.92616662e-01   # C_{18}
  2 1   -3.98272219e-29   # C_{21}
  2 2    5.89725029e-28   # C_{22}
  2 3    3.48109003e-05   # C_{23}
  2 4    6.97367387e-19   # C_{24}
  2 5    0.00000000e+00   # C_{25}
  2 6    9.99999999e-01   # C_{26}
  2 7    6.47906959e-17   # C_{27}
  2 8    0.00000000e+00   # C_{28}
  3 1   -6.22475425e-13   # C_{31}
  3 2    9.21760566e-12   # C_{32}
  3 3   -1.13840075e-21   # C_{33}
  3 4    7.19821241e-03   # C_{34}
  3 5    0.00000000e+00   # C_{35}
  3 6   -6.47940372e-17   # C_{36}
  3 7    9.99974093e-01   # C_{37}
  3 8    0.00000000e+00   # C_{38}
  4 1   -1.14439978e-26   # C_{41}
  4 2   -5.22410949e-27   # C_{42}
  4 3    9.99999999e-01   # C_{43}
  4 4   -3.10356942e-19   # C_{44}
  4 5    0.00000000e+00   # C_{45}
  4 6   -3.48109003e-05   # C_{46}
  4 7    1.11690610e-21   # C_{47}
  4 8    0.00000000e+00   # C_{48}
  5 1    1.68125525e-12   # C_{51}
  5 2    7.42066221e-13   # C_{52}
  5 3    3.10348901e-19   # C_{53}
  5 4    9.99974093e-01   # C_{54}
  5 5    0.00000000e+00   # C_{55}
  5 6   -2.30982932e-19   # C_{56}
  5 7   -7.19821241e-03   # C_{57}
  5 8    0.00000000e+00   # C_{58}
  6 1    0.00000000e+00   # C_{61}
  6 2    0.00000000e+00   # C_{62}
  6 3    0.00000000e+00   # C_{63}
  6 4    0.00000000e+00   # C_{64}
  6 5    9.92616662e-01   # C_{65}
  6 6    0.00000000e+00   # C_{66}
  6 7    0.00000000e+00   # C_{67}
  6 8   -1.21293705e-01   # C_{68}
  7 1    9.94680111e-01   # C_{71}
  7 2    1.03012020e-01   # C_{72}
  7 3    1.19207200e-26   # C_{73}
  7 4   -1.75108560e-12   # C_{74}
  7 5    0.00000000e+00   # C_{75}
  7 6    2.60895831e-31   # C_{76}
  7 7   -3.17763797e-13   # C_{77}
  7 8    0.00000000e+00   # C_{78}
Block RVHMIX  # CP-even neutral scalar mixing matrix 
  1 1    1.05215133e-01   # curlyN_{11}
  1 2    9.94449484e-01   # curlyN_{12}
  1 3    2.55593243e-25   # curlyN_{13}
  1 4   -3.75580512e-11   # curlyN_{14}
  1 5    0.00000000e+00   # curlyN_{15}
  2 1    0.00000000e+00   # curlyN_{21}
  2 2    0.00000000e+00   # curlyN_{22}
  2 3    0.00000000e+00   # curlyN_{23}
  2 4    0.00000000e+00   # curlyN_{24}
  2 5    1.00000000e+00   # curlyN_{25}
  3 1    6.28669894e-12   # curlyN_{31}
  3 2    3.71025336e-11   # curlyN_{32}
  3 3    3.10434820e-19   # curlyN_{33}
  3 4    1.00000000e+00   # curlyN_{34}
  3 5    0.00000000e+00   # curlyN_{35}
  4 1   -4.27829867e-26   # curlyN_{41}
  4 2   -2.52505017e-25   # curlyN_{42}
  4 3    1.00000000e+00   # curlyN_{43}
  4 4   -3.10434820e-19   # curlyN_{44}
  4 5    0.00000000e+00   # curlyN_{45}
  5 1    9.94449484e-01   # curlyN_{51}
  5 2   -1.05215133e-01   # curlyN_{52}
  5 3    1.59774412e-26   # curlyN_{53}
  5 4   -2.34805651e-12   # curlyN_{54}
  5 5    0.00000000e+00   # curlyN_{55}
Block RVAMIX  # CP-odd neutral scalar mixing matrix 
  1 1    0.00000000e+00   # curlyN~_{11}
  1 2    0.00000000e+00   # curlyN~_{12}
  1 3    0.00000000e+00   # curlyN~_{13}
  1 4    0.00000000e+00   # curlyN~_{14}
  1 5    1.00000000e+00   # curlyN~_{15}
  2 1   -3.95494309e-12   # curlyN~_{21}
  2 2    3.83018531e-11   # curlyN~_{22}
  2 3    3.10434820e-19   # curlyN~_{23}
  2 4    1.00000000e+00   # curlyN~_{24}
  2 5    0.00000000e+00   # curlyN~_{25}
  3 1    2.69170803e-26   # curlyN~_{31}
  3 2   -2.60660665e-25   # curlyN~_{32}
  3 3    1.00000000e+00   # curlyN~_{33}
  3 4   -3.10434820e-19   # curlyN~_{34}
  3 5    0.00000000e+00   # curlyN~_{35}
  4 1    9.94680115e-01   # curlyN~_{41}
  4 2    1.03011985e-01   # curlyN~_{42}
  4 3    7.72845308e-29   # curlyN~_{43}
  4 4   -1.16466805e-14   # curlyN~_{44}
  4 5    0.00000000e+00   # curlyN~_{45}
