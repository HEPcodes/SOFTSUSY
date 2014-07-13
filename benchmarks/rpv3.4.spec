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
     1    1.62500000e+02   # m0
     2    6.50000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.44231976e+16   # MX scale
Block RVLAMUDDIN          # input LQD couplings at MSUSY
  1 2 3   1.00000000e-04   # lambda''_{123}
  1 3 2  -1.00000000e-04   # lambda''_{132}
# SOFTSUSY-specific non SLHA information:
# MIXING=1 Desired accuracy=1.00000000e-03 Achieved accuracy=4.55911624e-04
# MX=1.44231976e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.05328025e+01   # MW
        25     1.16441263e+02   # CP even neutral scalar
        35     4.57304266e+02   # CP even neutral scalar
        36     4.57304266e+02   # CP odd neutral scalar
        37     2.88870968e+02   # charged scalar
   1000021     1.46181369e+03   # ~g
   1000022     2.70955436e+02   # ~neutralino(1)
   1000023     5.11113793e+02   # ~neutralino(2)
   1000024     5.11196489e+02   # ~chargino(1)
   1000025    -8.08759418e+02   # ~neutralino(3)
   1000035     8.20357769e+02   # ~neutralino(4)
   1000037     8.20581862e+02   # ~chargino(2)
   1000011     2.96043438e+02   # charged scalar
   1000013     2.96065649e+02   # charged scalar
   1000015     4.64695891e+02   # charged scalar
   2000011     4.65532981e+02   # charged scalar
   2000013     4.65534696e+02   # charged scalar
   2000015     9.13993126e+02   # charged scalar
   1000012     4.58575474e+02   # CP even neutral scalar
   1000014     4.58579681e+02   # CP even neutral scalar
   1000016     9.10230963e+02   # CP even neutral scalar
   1000017     4.58575474e+02   # CP odd neutral scalar
   1000018     4.58579681e+02   # CP odd neutral scalar
   1000019     9.10230963e+02   # CP odd neutral scalar
   1000001     1.23129154e+03   # ~d_1
   1000003     1.27438234e+03   # ~d_2
   1000005     1.28413172e+03   # ~d_3
   2000001     1.28413576e+03   # ~d_4
   2000003     1.34205871e+03   # ~d_5
   2000005     1.34208317e+03   # ~d_6
   1000002     1.03757779e+03   # ~u_1
   1000004     1.25609512e+03   # ~u_2
   1000006     1.28907551e+03   # ~u_3
   2000002     1.28908109e+03   # ~u_4
   2000004     1.33987579e+03   # ~u_5
   2000006     1.33988176e+03   # ~u_6
        12     0.00000000e+00   # Mnu1 inverted hierarchy output
        14     0.00000000e+00   # Mnu2 inverted hierarchy output
        16     0.00000000e+00   # Mnu3 inverted hierarchy output
Block RVNMIX  # neutrino-neutralino mixing matrix 
  1 1    0.00000000e+00   # N_{11}
  1 2    0.00000000e+00   # N_{12}
  1 3    0.00000000e+00   # N_{13}
  1 4    0.00000000e+00   # N_{14}
  1 5    0.00000000e+00   # N_{15}
  1 6    0.00000000e+00   # N_{16}
  1 7    0.00000000e+00   # N_{17}
  2 1    0.00000000e+00   # N_{21}
  2 2    0.00000000e+00   # N_{22}
  2 3    0.00000000e+00   # N_{23}
  2 4    0.00000000e+00   # N_{24}
  2 5    0.00000000e+00   # N_{25}
  2 6    0.00000000e+00   # N_{26}
  2 7    0.00000000e+00   # N_{27}
  3 1    0.00000000e+00   # N_{31}
  3 2    0.00000000e+00   # N_{32}
  3 3    0.00000000e+00   # N_{33}
  3 4    0.00000000e+00   # N_{34}
  3 5    0.00000000e+00   # N_{35}
  3 6    0.00000000e+00   # N_{36}
  3 7    0.00000000e+00   # N_{37}
  4 1    0.00000000e+00   # N_{41}
  4 2    0.00000000e+00   # N_{42}
  4 3    0.00000000e+00   # N_{43}
  4 4    0.00000000e+00   # N_{44}
  4 5    0.00000000e+00   # N_{45}
  4 6    0.00000000e+00   # N_{46}
  4 7    0.00000000e+00   # N_{47}
  5 1    0.00000000e+00   # N_{51}
  5 2    0.00000000e+00   # N_{52}
  5 3    0.00000000e+00   # N_{53}
  5 4    0.00000000e+00   # N_{54}
  5 5    0.00000000e+00   # N_{55}
  5 6    0.00000000e+00   # N_{56}
  5 7    0.00000000e+00   # N_{57}
  6 1    0.00000000e+00   # N_{61}
  6 2    0.00000000e+00   # N_{62}
  6 3    0.00000000e+00   # N_{63}
  6 4    0.00000000e+00   # N_{64}
  6 5    0.00000000e+00   # N_{65}
  6 6    0.00000000e+00   # N_{66}
  6 7    0.00000000e+00   # N_{67}
  7 1    0.00000000e+00   # N_{71}
  7 2    0.00000000e+00   # N_{72}
  7 3    0.00000000e+00   # N_{73}
  7 4    0.00000000e+00   # N_{74}
  7 5    0.00000000e+00   # N_{75}
  7 6    0.00000000e+00   # N_{76}
  7 7    0.00000000e+00   # N_{77}
Block RVUMIX  # lepton-chargino mixing matrix U
  1 1    1.00000000e+00   # U_{11}
  1 2    0.00000000e+00   # U_{12}
  1 3    0.00000000e+00   # U_{13}
  1 4    0.00000000e+00   # U_{14}
  1 5    0.00000000e+00   # U_{15}
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
  4 1    0.00000000e+00   # U_{41}
  4 2    0.00000000e+00   # U_{42}
  4 3    0.00000000e+00   # U_{43}
  4 4    9.71641882e-01   # U_{44}
  4 5   -2.36457296e-01   # U_{45}
  5 1    0.00000000e+00   # U_{51}
  5 2    0.00000000e+00   # U_{52}
  5 3    0.00000000e+00   # U_{53}
  5 4    2.36457296e-01   # U_{54}
  5 5    9.71641882e-01   # U_{55}
Block RVVMIX  # lepton-chargino mixing matrix V
  1 1    1.00000000e+00   # V_{11}
  1 2    0.00000000e+00   # V_{12}
  1 3    0.00000000e+00   # V_{13}
  1 4    0.00000000e+00   # V_{14}
  1 5    0.00000000e+00   # V_{15}
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
  4 1    0.00000000e+00   # V_{41}
  4 2    0.00000000e+00   # V_{42}
  4 3    0.00000000e+00   # V_{43}
  4 4    9.87158788e-01   # V_{44}
  4 5   -1.59742068e-01   # V_{45}
  5 1    0.00000000e+00   # V_{51}
  5 2    0.00000000e+00   # V_{52}
  5 3    0.00000000e+00   # V_{53}
  5 4    1.59742068e-01   # V_{54}
  5 5    9.87158788e-01   # V_{55}
Block gauge Q= 1.11357587e+03  # SM gauge couplings
     1     3.63221828e-01   # g'(Q)MSSM DRbar
     2     6.41038973e-01   # g(Q)MSSM DRbar
     3     1.05189667e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.11357587e+03   # diagonal Up Yukawa matrix
  1  1     7.27333626e-06    # YU_{11}(Q)MSSM DRbar
  2  2     3.33171959e-03    # YU_{22}(Q)MSSM DRbar
  3  3     8.49071074e-01    # YU_{33}(Q)MSSM DRbar
Block yd Q= 1.11357587e+03   # diagonal down Yukawa matrix
  1  1     1.39727804e-04    # YD_{11}(Q)MSSM DRbar
  2  2     3.05936692e-03    # YD_{22}(Q)MSSM DRbar
  3  3     1.33195086e-01    # YD_{33}(Q)MSSM DRbar
Block ye Q= 1.11357587e+03   # diagonal lepton Yukawa matrix
  1  1     2.78105567e-05    # YE_{11}(Q)MSSM DRbar
  2  2     5.75034989e-03    # YE_{22}(Q)MSSM DRbar
  3  3     1.00130664e-01    # YE_{33}(Q)MSSM DRbar
Block hmix Q= 1.11357587e+03 # Higgs mixing parameters
     1     8.03344479e+02    # mu(Q)MSSM DRbar
     2     9.64757519e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44326239e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     8.58533567e+05    # mA^2(Q)MSSM DRbar
Block RVLAMLLE Q= 1.11357587e+03 # non-zero R-Parity violating LLE couplings 
Block RVLAMLQD Q= 1.11357587e+03 # non-zero R-Parity violating LQD couplings 
Block RVLAMUDD Q= 1.11357587e+03 # non-zero R-Parity violating UDD couplings 
  1 1 2   -7.96793187e-21   # lambda''_{112}
  1 1 3   -7.89983541e-24   # lambda''_{113}
  1 2 1    7.96793187e-21   # lambda''_{121}
  1 2 3    9.99999824e-05   # lambda''_{123}
  1 3 1    7.89983541e-24   # lambda''_{131}
  1 3 2   -9.99999824e-05   # lambda''_{132}
  2 1 2   -1.35960050e-26   # lambda''_{212}
  2 1 3   -1.32666549e-29   # lambda''_{213}
  2 2 1    1.35960050e-26   # lambda''_{221}
  2 2 3   -6.80024391e-16   # lambda''_{223}
  2 3 1    1.32666549e-29   # lambda''_{231}
  2 3 2    6.80024391e-16   # lambda''_{232}
  3 1 2    3.15490416e-25   # lambda''_{312}
  3 1 3    3.07835376e-28   # lambda''_{313}
  3 2 1   -3.15490416e-25   # lambda''_{321}
  3 2 3    1.59386900e-14   # lambda''_{323}
  3 3 1   -3.07835376e-28   # lambda''_{331}
  3 3 2   -1.59386900e-14   # lambda''_{332}
Block RVTLLE Q= 1.11357587e+03 # non-zero R-Parity violating LLE soft terms 
Block RVTLQD Q= 1.11357587e+03 # non-zero R-Parity violating LQD soft terms 
Block RVTUDD Q= 1.11357587e+03 # non-zero R-Parity violating UDD soft terms 
  1 1 2   -5.56865552e-17   # T''_{112}
  1 1 3   -5.48019201e-20   # T''_{113}
  1 2 1    5.56865552e-17   # T''_{121}
  1 2 3    4.92446693e-08   # T''_{123}
  1 3 1    5.48019201e-20   # T''_{131}
  1 3 2   -4.92446693e-08   # T''_{132}
  2 1 2    2.13768787e-22   # T''_{212}
  2 1 3    2.08433368e-25   # T''_{213}
  2 2 1   -2.13768787e-22   # T''_{221}
  2 2 3    1.54785565e-12   # T''_{223}
  2 3 1   -2.08433368e-25   # T''_{231}
  2 3 2   -1.54785565e-12   # T''_{232}
  3 1 2   -4.94687158e-21   # T''_{312}
  3 1 3   -4.82301196e-24   # T''_{313}
  3 2 1    4.94687158e-21   # T''_{321}
  3 2 3   -3.61395242e-11   # T''_{323}
  3 3 1    4.82301196e-24   # T''_{331}
  3 3 2    3.61395242e-11   # T''_{332}
Block RVKAPPA Q= 1.11357587e+03 # R-Parity violating kappa 
     1    0.00000000e+00   # kappa_{1}
     2    0.00000000e+00   # kappa_{2}
     3    0.00000000e+00   # kappa_{3}
Block RVD Q= 1.11357587e+03 # R-Parity violating D 
     1    0.00000000e+00   # D_{1}
     2    0.00000000e+00   # D_{2}
     3    0.00000000e+00   # D_{3}
Block RVSNVEV Q= 1.11357587e+03 # sneutrino VEVs D 
     1    0.00000000e+00   # SneutrinoVev_{1}
     2    0.00000000e+00   # SneutrinoVev_{2}
     3    0.00000000e+00   # SneutrinoVev_{3}
Block RVM2LH1 Q= 1.11357587e+03 # M2LH1 
     1    0.00000000e+00   # M2LH1_{1}
     2    0.00000000e+00   # M2LH1_{2}
     3    0.00000000e+00   # M2LH1_{3}
Block UPMNS Q= 9.11876000e+01 # neutrino mixing matrix (inverted  hierarchy)
  1  1     0.00000000e+00   # UPMNS_{11} matrix element
  1  2     0.00000000e+00   # UPMNS_{12} matrix element
  1  3     0.00000000e+00   # UPMNS_{13} matrix element
  2  1     0.00000000e+00   # UPMNS_{21} matrix element
  2  2     0.00000000e+00   # UPMNS_{22} matrix element
  2  3     0.00000000e+00   # UPMNS_{23} matrix element
  3  1     0.00000000e+00   # UPMNS_{31} matrix element
  3  2     0.00000000e+00   # UPMNS_{32} matrix element
  3  3     0.00000000e+00   # UPMNS_{33} matrix element
Block msq2 Q= 1.11357587e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.68009329e+06    # (m_Q^2)_{11}
  1  2     5.71964521e+01    # (m_Q^2)_{12}
  1  3    -1.35337743e+03    # (m_Q^2)_{13}
  2  1     5.71964521e+01    # (m_Q^2)_{21}
  2  2     1.67967883e+06    # (m_Q^2)_{22}
  2  3     9.96383546e+03    # (m_Q^2)_{23}
  3  1    -1.35337743e+03    # (m_Q^2)_{31}
  3  2     9.96383546e+03    # (m_Q^2)_{32}
  3  3     1.43245826e+06    # (m_Q^2)_{33}
Block msl2 Q= 1.11357587e+03 # super MNS slepton mass^2 matrix - DRbar
  1  1     2.08862112e+05    # (m_L^2)_{11}
  1  2     0.00000000e+00    # (m_L^2)_{12}
  1  3     0.00000000e+00    # (m_L^2)_{13}
  2  1     0.00000000e+00    # (m_L^2)_{21}
  2  2     2.08858286e+05    # (m_L^2)_{22}
  2  3     0.00000000e+00    # (m_L^2)_{23}
  3  1     0.00000000e+00    # (m_L^2)_{31}
  3  2     0.00000000e+00    # (m_L^2)_{32}
  3  3     2.07703786e+05    # (m_L^2)_{33}
Block msd2 Q= 1.11357587e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.53858114e+06    # (m_d^2)_{11}
  1  2    -3.96499697e-06    # (m_d^2)_{12}
  1  3     4.10067872e-03    # (m_d^2)_{13}
  2  1    -3.96499697e-06    # (m_d^2)_{21}
  2  2     1.53857271e+06    # (m_d^2)_{22}
  2  3    -6.61016943e-01    # (m_d^2)_{23}
  3  1     4.10067872e-03    # (m_d^2)_{31}
  3  2    -6.61016943e-01    # (m_d^2)_{32}
  3  3     1.52330956e+06    # (m_d^2)_{33}
Block msu2 Q= 1.11357587e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.55379264e+06    # (m_u^2)_{11}
  1  2     2.12405155e-03    # (m_u^2)_{12}
  1  3    -7.11355134e-05    # (m_u^2)_{13}
  2  1     2.12405155e-03    # (m_u^2)_{21}
  2  2     1.55378394e+06    # (m_u^2)_{22}
  2  3    -8.65983870e-02    # (m_u^2)_{23}
  3  1    -7.11355134e-05    # (m_u^2)_{31}
  3  2    -8.65983870e-02    # (m_u^2)_{32}
  3  3     1.06149469e+06    # (m_u^2)_{33}
Block mse2 Q= 1.11357587e+03 # super MNS slepton mass^2 matrix - DRbar
  1  1     8.29341528e+04    # (m_e^2)_{11}
  1  2     0.00000000e+00    # (m_e^2)_{12}
  1  3     0.00000000e+00    # (m_e^2)_{13}
  2  1     0.00000000e+00    # (m_e^2)_{21}
  2  2     8.29263527e+04    # (m_e^2)_{22}
  2  3     0.00000000e+00    # (m_e^2)_{23}
  3  1     0.00000000e+00    # (m_e^2)_{31}
  3  2     0.00000000e+00    # (m_e^2)_{32}
  3  3     8.05720495e+04    # (m_e^2)_{33}
Block tu Q= 1.11357587e+03   # super CKM trilinear matrix - DRbar
  1  1    -1.05228004e-02    # (T_u)_{11}
  1  2    -2.00335772e-08    # (T_u)_{12}
  1  3    -1.09419856e-07    # (T_u)_{13}
  2  1    -1.00362654e-05    # (T_u)_{21}
  2  2    -4.82025068e+00    # (T_u)_{22}
  2  3    -4.73655765e-04    # (T_u)_{23}
  3  1    -1.34049431e-02    # (T_u)_{31}
  3  2    -1.42276505e-01    # (T_u)_{32}
  3  3    -9.56522868e+02    # (T_u)_{33}
Block td Q= 1.11357587e+03   # super CKM trilinear matrix - DRbar
  1  1    -2.45765590e-01    # (T_d)_{11}
  1  2    -3.58052263e-06    # (T_d)_{12}
  1  3     8.51646329e-05    # (T_d)_{13}
  2  1    -7.83959416e-05    # (T_d)_{21}
  2  2    -5.38052908e+00    # (T_d)_{22}
  2  3    -1.37282378e-02    # (T_d)_{23}
  3  1     8.10310789e-02    # (T_d)_{31}
  3  2    -5.96568039e-01    # (T_d)_{32}
  3  3    -2.19328224e+02    # (T_d)_{33}
Block te Q= 1.11357587e+03   # super CKM trilinear matrix - DRbar
  1  1    -1.06234129e-02    # (T_e)_{11}
  1  2     0.00000000e+00    # (T_e)_{12}
  1  3     0.00000000e+00    # (T_e)_{13}
  2  1     0.00000000e+00    # (T_e)_{21}
  2  2    -2.19654951e+00    # (T_e)_{22}
  2  3     0.00000000e+00    # (T_e)_{23}
  3  1     0.00000000e+00    # (T_e)_{31}
  3  2     0.00000000e+00    # (T_e)_{32}
  3  3    -3.80447572e+01    # (T_e)_{33}
Block VCKM Q= 1.11357587e+03 # DRbar CKM mixing matrix
  1  1     9.73840749e-01    # CKM_{11} matrix element
  1  2     2.27197341e-01    # CKM_{12} matrix element
  1  3     3.94503067e-03    # CKM_{13} matrix element
  2  1    -2.27161574e-01    # CKM_{21} matrix element
  2  2     9.72963011e-01    # CKM_{22} matrix element
  2  3     4.17204801e-02    # CKM_{23} matrix element
  3  1     5.64041322e-03    # CKM_{31} matrix element
  3  2    -4.15252630e-02    # CKM_{32} matrix element
  3  3     9.99121533e-01    # CKM_{33} matrix element
Block msoft Q= 1.11357587e+03 # MSSM DRbar SUSY breaking parameters
     1     2.76747225e+02     # M_1(Q)
     2     5.08650721e+02     # M_2(Q)
     3     1.42150525e+03     # M_3(Q)
    21     1.83211100e+05     # mH1^2(Q)
    22    -6.00033934e+05     # mH2^2(Q)
Block USQMIX  # super CKM squark mass^2 matrix
  1  1     1.89784762e-05   # (USQMIX)_{11}
  1  2     2.00958491e-04   # (USQMIX)_{12}
  1  3     3.69638753e-01   # (USQMIX)_{13}
  1  4     1.86855868e-10   # (USQMIX)_{14}
  1  5     4.89773339e-07   # (USQMIX)_{15}
  1  6     9.29175523e-01   # (USQMIX)_{16}
  2  1     1.28996069e-04   # (USQMIX)_{21}
  2  2     1.36524029e-03   # (USQMIX)_{22}
  2  3     9.29174565e-01   # (USQMIX)_{23}
  2  4     2.83290541e-09   # (USQMIX)_{24}
  2  5     1.47663038e-05   # (USQMIX)_{25}
  2  6    -3.69638670e-01   # (USQMIX)_{26}
  3  1     1.14489739e-07   # (USQMIX)_{31}
  3  2     6.55940659e-03   # (USQMIX)_{32}
  3  3    -2.27094311e-05   # (USQMIX)_{33}
  3  4    -1.47598728e-04   # (USQMIX)_{34}
  3  5     9.99978476e-01   # (USQMIX)_{35}
  3  6     7.08838346e-06   # (USQMIX)_{36}
  4  1     1.43191295e-05   # (USQMIX)_{41}
  4  2     9.68516953e-07   # (USQMIX)_{42}
  4  3    -7.87044206e-09   # (USQMIX)_{43}
  4  4     9.99999989e-01   # (USQMIX)_{44}
  4  5     1.47595548e-04   # (USQMIX)_{45}
  4  6     2.35013637e-09   # (USQMIX)_{46}
  5  1     1.37464211e-01   # (USQMIX)_{51}
  5  2     9.90484457e-01   # (USQMIX)_{52}
  5  3    -1.34740390e-03   # (USQMIX)_{53}
  5  4    -1.96872550e-06   # (USQMIX)_{54}
  5  5    -6.49717901e-03   # (USQMIX)_{55}
  5  6     3.18993290e-04   # (USQMIX)_{56}
  6  1     9.90506726e-01   # (USQMIX)_{61}
  6  2    -1.37461303e-01   # (USQMIX)_{62}
  6  3     5.89039616e-05   # (USQMIX)_{63}
  6  4    -1.41831279e-05   # (USQMIX)_{64}
  6  5     9.01569920e-04   # (USQMIX)_{65}
  6  6    -1.39348492e-05   # (USQMIX)_{66}
Block DSQMIX  # super CKM squark mass^2 matrix
  1  1     4.66675447e-03   # (DSQMIX)_{11}
  1  2    -3.43579819e-02   # (DSQMIX)_{12}
  1  3     9.81838890e-01   # (DSQMIX)_{13}
  1  4     8.13926024e-07   # (DSQMIX)_{14}
  1  5    -1.31212377e-04   # (DSQMIX)_{15}
  1  6     1.86521120e-01   # (DSQMIX)_{16}
  2  1    -1.43455471e-03   # (DSQMIX)_{21}
  2  2     1.05622711e-02   # (DSQMIX)_{22}
  2  3    -1.86259375e-01   # (DSQMIX)_{23}
  2  4    -1.51064637e-06   # (DSQMIX)_{24}
  2  5     2.43612025e-04   # (DSQMIX)_{25}
  2  6     9.82442755e-01   # (DSQMIX)_{26}
  3  1     1.36666870e-06   # (DSQMIX)_{31}
  3  2     3.39480575e-03   # (DSQMIX)_{32}
  3  3     2.95813368e-04   # (DSQMIX)_{33}
  3  4     3.56709417e-06   # (DSQMIX)_{34}
  3  5     9.99994168e-01   # (DSQMIX)_{35}
  3  6    -2.28377158e-04   # (DSQMIX)_{36}
  4  1     1.55508945e-04   # (DSQMIX)_{41}
  4  2     5.02765899e-08   # (DSQMIX)_{42}
  4  3    -1.83602798e-06   # (DSQMIX)_{43}
  4  4     9.99999988e-01   # (DSQMIX)_{44}
  4  5    -3.56663141e-06   # (DSQMIX)_{45}
  4  6     1.41697096e-06   # (DSQMIX)_{46}
  5  1    -1.35316160e-01   # (DSQMIX)_{51}
  5  2     9.90132494e-01   # (DSQMIX)_{52}
  5  3     3.60520703e-02   # (DSQMIX)_{53}
  5  4     2.10529337e-05   # (DSQMIX)_{54}
  5  5    -3.37272201e-03   # (DSQMIX)_{55}
  5  6    -4.00665430e-03   # (DSQMIX)_{56}
  6  1     9.90790430e-01   # (DSQMIX)_{61}
  6  2     1.35403422e-01   # (DSQMIX)_{62}
  6  3     2.94989681e-05   # (DSQMIX)_{63}
  6  4    -1.54085170e-04   # (DSQMIX)_{64}
  6  5    -4.61034010e-04   # (DSQMIX)_{65}
  6  6    -3.27553719e-06   # (DSQMIX)_{66}
Block RVLMIX  # charged higgs-slepton mixing matrix 
  1 1    0.00000000e+00   # C_{11}
  1 2    0.00000000e+00   # C_{12}
  1 3    0.00000000e+00   # C_{13}
  1 4    0.00000000e+00   # C_{14}
  1 5    1.11812899e-01   # C_{15}
  1 6    0.00000000e+00   # C_{16}
  1 7    0.00000000e+00   # C_{17}
  1 8    9.93729277e-01   # C_{18}
  2 1    0.00000000e+00   # C_{21}
  2 2    0.00000000e+00   # C_{22}
  2 3    0.00000000e+00   # C_{23}
  2 4    6.60813883e-03   # C_{24}
  2 5    0.00000000e+00   # C_{25}
  2 6    0.00000000e+00   # C_{26}
  2 7    9.99978166e-01   # C_{27}
  2 8    0.00000000e+00   # C_{28}
  3 1    0.00000000e+00   # C_{31}
  3 2    0.00000000e+00   # C_{32}
  3 3    3.19622299e-05   # C_{33}
  3 4    0.00000000e+00   # C_{34}
  3 5    0.00000000e+00   # C_{35}
  3 6    9.99999999e-01   # C_{36}
  3 7    0.00000000e+00   # C_{37}
  3 8    0.00000000e+00   # C_{38}
  4 1    0.00000000e+00   # C_{41}
  4 2    0.00000000e+00   # C_{42}
  4 3    9.99999999e-01   # C_{43}
  4 4    0.00000000e+00   # C_{44}
  4 5    0.00000000e+00   # C_{45}
  4 6   -3.19622299e-05   # C_{46}
  4 7    0.00000000e+00   # C_{47}
  4 8    0.00000000e+00   # C_{48}
  5 1    0.00000000e+00   # C_{51}
  5 2    0.00000000e+00   # C_{52}
  5 3    0.00000000e+00   # C_{53}
  5 4    9.99978166e-01   # C_{54}
  5 5    0.00000000e+00   # C_{55}
  5 6    0.00000000e+00   # C_{56}
  5 7   -6.60813883e-03   # C_{57}
  5 8    0.00000000e+00   # C_{58}
  6 1    0.00000000e+00   # C_{61}
  6 2    0.00000000e+00   # C_{62}
  6 3    0.00000000e+00   # C_{63}
  6 4    0.00000000e+00   # C_{64}
  6 5    9.93729277e-01   # C_{65}
  6 6    0.00000000e+00   # C_{66}
  6 7    0.00000000e+00   # C_{67}
  6 8   -1.11812899e-01   # C_{68}
  7 1    9.94670936e-01   # C_{71}
  7 2    1.03100573e-01   # C_{72}
  7 3    0.00000000e+00   # C_{73}
  7 4    0.00000000e+00   # C_{74}
  7 5    0.00000000e+00   # C_{75}
  7 6    0.00000000e+00   # C_{76}
  7 7    0.00000000e+00   # C_{77}
  7 8    0.00000000e+00   # C_{78}
Block RVHMIX  # CP-even neutral scalar mixing matrix 
  1 1    1.05000972e-01   # curlyN_{11}
  1 2    9.94472119e-01   # curlyN_{12}
  1 3    0.00000000e+00   # curlyN_{13}
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
  4 1    0.00000000e+00   # curlyN_{41}
  4 2    0.00000000e+00   # curlyN_{42}
  4 3    1.00000000e+00   # curlyN_{43}
  4 4    0.00000000e+00   # curlyN_{44}
  4 5    0.00000000e+00   # curlyN_{45}
  5 1    9.94472119e-01   # curlyN_{51}
  5 2   -1.05000972e-01   # curlyN_{52}
  5 3    0.00000000e+00   # curlyN_{53}
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
  3 1    0.00000000e+00   # curlyN~_{31}
  3 2    0.00000000e+00   # curlyN~_{32}
  3 3    1.00000000e+00   # curlyN~_{33}
  3 4    0.00000000e+00   # curlyN~_{34}
  3 5    0.00000000e+00   # curlyN~_{35}
  4 1    9.94670940e-01   # curlyN~_{41}
  4 2    1.03100536e-01   # curlyN~_{42}
  4 3    0.00000000e+00   # curlyN~_{43}
  4 4    0.00000000e+00   # curlyN~_{44}
  4 5    0.00000000e+00   # curlyN~_{45}
