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
     1    1.75000000e+02   # m0
     2    7.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.40621856e+16   # MX scale
Block RVLAMLLEIN           # input LLE couplings at MSUSY
  1 2 1   1.00000000e-02   # lambda_{121}
  2 1 1  -1.00000000e-02   # lambda_{211}
# SOFTSUSY-specific non SLHA information:
# MIXING=1 Desired accuracy=1.00000000e-03 Achieved accuracy=5.67638418e-04
# MX=1.40621856e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.05426556e+01   # MW
        25     1.16886473e+02   # CP even neutral scalar
        35     4.92554846e+02   # CP even neutral scalar
        36     4.92554846e+02   # CP odd neutral scalar
        37     3.10963041e+02   # charged scalar
   1000021     1.56566807e+03   # ~g
   1000022     2.92951601e+02   # ~neutralino(1)
   1000023     5.52497109e+02   # ~neutralino(2)
   1000024     5.52592404e+02   # ~chargino(1)
   1000025    -8.63383724e+02   # ~neutralino(3)
   1000035     8.74528261e+02   # ~neutralino(4)
   1000037     8.74730734e+02   # ~chargino(2)
   1000011     3.18205580e+02   # charged scalar
   1000013     3.18222012e+02   # charged scalar
   1000015     4.99202611e+02   # charged scalar
   2000011     5.00388734e+02   # charged scalar
   2000013     5.00389673e+02   # charged scalar
   2000015     9.77496821e+02   # charged scalar
   1000012     4.93901288e+02   # CP even neutral scalar
   1000014     4.93905783e+02   # CP even neutral scalar
   1000016     9.73969867e+02   # CP even neutral scalar
   1000017     4.93901288e+02   # CP odd neutral scalar
   1000018     4.93905783e+02   # CP odd neutral scalar
   1000019     9.73969867e+02   # CP odd neutral scalar
   1000001     1.31831507e+03   # ~d_1
   1000003     1.36333406e+03   # ~d_2
   1000005     1.37381652e+03   # ~d_3
   2000001     1.37382072e+03   # ~d_4
   2000003     1.43636543e+03   # ~d_5
   2000005     1.43639175e+03   # ~d_6
   1000002     1.11345679e+03   # ~u_1
   1000004     1.34024510e+03   # ~u_2
   1000006     1.37929825e+03   # ~u_3
   2000002     1.37930388e+03   # ~u_4
   2000004     1.43433797e+03   # ~u_5
   2000006     1.43434465e+03   # ~u_6
        12     8.74234978e-43   # Mnu1 inverted hierarchy output
        14     1.69283248e-14   # Mnu2 inverted hierarchy output
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
  2 2   -9.61552644e-15   # N_{22}
  2 3    0.00000000e+00   # N_{23}
  2 4   -6.76143706e-24   # N_{24}
  2 5   -1.66448591e-24   # N_{25}
  2 6   -1.61297765e-23   # N_{26}
  2 7    6.81911848e-28   # N_{27}
  3 1    9.61552644e-15   # N_{31}
  3 2    1.00000000e+00   # N_{32}
  3 3    0.00000000e+00   # N_{33}
  3 4   -3.53296024e-10   # N_{34}
  3 5    3.67566978e-10   # N_{35}
  3 6   -2.41631970e-09   # N_{36}
  3 7    2.78557391e-12   # N_{37}
  4 1    1.25675311e-23   # N_{41}
  4 2    5.04249294e-10   # N_{42}
  4 3    0.00000000e+00   # N_{43}
  4 4    9.97721237e-01   # N_{44}
  4 5   -9.63700932e-03   # N_{45}
  4 6    6.13090923e-02   # N_{46}
  4 7   -2.64699222e-02   # N_{47}
  5 1   -7.83544924e-24   # N_{51}
  5 2   -7.35065075e-10   # N_{52}
  5 3    0.00000000e+00   # N_{53}
  5 4    2.21015415e-02   # N_{54}
  5 5    9.81059330e-01   # N_{55}
  5 6   -1.58076234e-01   # N_{56}
  5 7    1.09754346e-01   # N_{57}
  6 1    2.74273386e-23   # N_{61}
  6 2    1.68052376e-09   # N_{62}
  6 3    0.00000000e+00   # N_{63}
  6 4   -2.42168061e-02   # N_{64}
  6 5    3.49882657e-02   # N_{65}
  6 6    7.05168077e-01   # N_{66}
  6 7    7.07762213e-01   # N_{67}
  7 1   -2.61652272e-23   # N_{71}
  7 2   -1.57473302e-09   # N_{72}
  7 3    0.00000000e+00   # N_{73}
  7 4    5.89694980e-02   # N_{74}
  7 5   -1.90277533e-01   # N_{75}
  7 6   -6.88470102e-01   # N_{76}
  7 7    6.97370760e-01   # N_{77}
Block RVUMIX  # lepton-chargino mixing matrix U
  1 1    1.00000000e+00   # U_{11}
  1 2    5.42101086e-20   # U_{12}
  1 3    0.00000000e+00   # U_{13}
  1 4   -1.28544662e-24   # U_{14}
  1 5    2.29489518e-23   # U_{15}
  2 1   -5.37954244e-32   # U_{21}
  2 2   -1.00000000e+00   # U_{22}
  2 3    0.00000000e+00   # U_{23}
  2 4   -2.57012748e-10   # U_{24}
  2 5    4.67377044e-09   # U_{25}
  3 1    0.00000000e+00   # U_{31}
  3 2    0.00000000e+00   # U_{32}
  3 3    1.00000000e+00   # U_{33}
  3 4    0.00000000e+00   # U_{34}
  3 5    0.00000000e+00   # U_{35}
  4 1    6.42710378e-24   # U_{41}
  4 2   -1.30426843e-09   # U_{42}
  4 3    0.00000000e+00   # U_{43}
  4 4    9.74246163e-01   # U_{44}
  4 5   -2.25487058e-01   # U_{45}
  5 1   -2.20683204e-23   # U_{51}
  5 2    4.49544987e-09   # U_{52}
  5 3    0.00000000e+00   # U_{53}
  5 4    2.25487058e-01   # U_{54}
  5 5    9.74246163e-01   # U_{55}
Block RVVMIX  # lepton-chargino mixing matrix V
  1 1    1.00000000e+00   # V_{11}
  1 2   -1.12757026e-17   # V_{12}
  1 3    0.00000000e+00   # V_{13}
  1 4    0.00000000e+00   # V_{14}
  1 5    1.12314123e-45   # V_{15}
  2 1    1.12757026e-17   # V_{21}
  2 2   -1.00000000e+00   # V_{22}
  2 3    0.00000000e+00   # V_{23}
  2 4   -3.67572232e-13   # V_{24}
  2 5    1.51875356e-12   # V_{25}
  3 1    0.00000000e+00   # V_{31}
  3 2    0.00000000e+00   # V_{32}
  3 3    1.00000000e+00   # V_{33}
  3 4    0.00000000e+00   # V_{34}
  3 5    0.00000000e+00   # V_{35}
  4 1    6.72887331e-30   # V_{41}
  4 2   -5.96758673e-13   # V_{42}
  4 3    0.00000000e+00   # V_{43}
  4 4    9.88104606e-01   # V_{44}
  4 5   -1.53783249e-01   # V_{45}
  5 1   -1.62839293e-29   # V_{51}
  5 2    1.44416094e-12   # V_{52}
  5 3    0.00000000e+00   # V_{53}
  5 4    1.53783249e-01   # V_{54}
  5 5    9.88104606e-01   # V_{55}
Block gauge Q= 1.19186980e+03  # SM gauge couplings
     1     3.63368511e-01   # g'(Q)MSSM DRbar
     2     6.40671560e-01   # g(Q)MSSM DRbar
     3     1.04845220e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.19186980e+03   # diagonal Up Yukawa matrix
  1  1     7.25709146e-06    # YU_{11}(Q)MSSM DRbar
  2  2     3.32427839e-03    # YU_{22}(Q)MSSM DRbar
  3  3     8.46649125e-01    # YU_{33}(Q)MSSM DRbar
Block yd Q= 1.19186980e+03   # diagonal down Yukawa matrix
  1  1     1.39309983e-04    # YD_{11}(Q)MSSM DRbar
  2  2     3.05022006e-03    # YD_{22}(Q)MSSM DRbar
  3  3     1.32730384e-01    # YD_{33}(Q)MSSM DRbar
Block ye Q= 1.19186980e+03   # diagonal lepton Yukawa matrix
  1  1     2.77831098e-05    # YE_{11}(Q)MSSM DRbar
  2  2     5.74466194e-03    # YE_{22}(Q)MSSM DRbar
  3  3     1.00070417e-01    # YE_{33}(Q)MSSM DRbar
Block hmix Q= 1.19186980e+03 # Higgs mixing parameters
     1     8.57899403e+02    # mu(Q)MSSM DRbar
     2     9.63988323e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44281567e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     9.82729707e+05    # mA^2(Q)MSSM DRbar
Block RVLAMLLE Q= 1.19186980e+03 # non-zero R-Parity violating LLE couplings 
  1 2 1    9.99999965e-03   # lambda_{121}
  1 2 2   -2.42108788e-31   # lambda_{122}
  1 3 3   -1.39966515e-30   # lambda_{133}
  2 1 1   -9.99999965e-03   # lambda_{211}
  2 1 2    2.42108788e-31   # lambda_{212}
  2 3 3   -6.00346869e-16   # lambda_{233}
  3 1 3    1.39966515e-30   # lambda_{313}
  3 2 3    6.00346869e-16   # lambda_{323}
Block RVLAMLQD Q= 1.19186980e+03 # non-zero R-Parity violating LQD couplings 
  1 1 1   -1.94960536e-33   # lambda'_{111}
  1 1 2    1.21923948e-37   # lambda'_{112}
  1 1 3   -1.22929158e-34   # lambda'_{113}
  1 2 1    5.56863835e-39   # lambda'_{121}
  1 2 2   -4.26869932e-32   # lambda'_{122}
  1 2 3    9.05018921e-34   # lambda'_{123}
  1 3 1   -1.30549656e-37   # lambda'_{131}
  1 3 2    2.10435250e-35   # lambda'_{132}
  1 3 3   -1.85693986e-30   # lambda'_{133}
  2 1 1   -8.36228166e-19   # lambda'_{211}
  2 1 2    5.22958893e-23   # lambda'_{212}
  2 1 3   -5.27270445e-20   # lambda'_{213}
  2 2 1    2.38851268e-24   # lambda'_{221}
  2 2 2   -1.83093804e-17   # lambda'_{222}
  2 2 3    3.88182704e-19   # lambda'_{223}
  2 3 1   -5.59956462e-23   # lambda'_{231}
  2 3 2    9.02603508e-21   # lambda'_{232}
  2 3 3   -7.96481929e-16   # lambda'_{233}
Block RVLAMUDD Q= 1.19186980e+03 # non-zero R-Parity violating UDD couplings 
Block RVTLLE Q= 1.19186980e+03 # non-zero R-Parity violating LLE soft terms 
  1 2 1    3.42872019e-07   # T_{121}
  1 2 2    2.30584335e-28   # T_{122}
  1 3 3    1.71837466e-27   # T_{133}
  2 1 1   -3.42872019e-07   # T_{211}
  2 1 2   -2.30584335e-28   # T_{212}
  2 3 3    7.37056998e-13   # T_{233}
  3 1 3   -1.71837466e-27   # T_{313}
  3 2 3   -7.37056998e-13   # T_{323}
Block RVTLQD Q= 1.19186980e+03 # non-zero R-Parity violating LQD soft terms 
  1 1 1    5.27235367e-30   # T'_{111}
  1 1 2    9.21669364e-34   # T'_{112}
  1 1 3   -9.29863686e-31   # T'_{113}
  1 2 1    4.20956625e-35   # T'_{121}
  1 2 2    1.15430339e-28   # T'_{122}
  1 2 3    6.84580878e-30   # T'_{123}
  1 3 1   -9.92272093e-34   # T'_{131}
  1 3 2    1.59946245e-31   # T'_{132}
  1 3 3    4.79150402e-27   # T'_{133}
  2 1 1    2.26143882e-15   # T'_{211}
  2 1 2    3.95322477e-19   # T'_{212}
  2 1 3   -3.98837217e-16   # T'_{213}
  2 2 1    1.80556740e-20   # T'_{221}
  2 2 2    4.95108385e-14   # T'_{222}
  2 2 3    2.93630492e-15   # T'_{223}
  2 3 1   -4.25605431e-19   # T'_{231}
  2 3 2    6.86041573e-17   # T'_{232}
  2 3 3    2.05519155e-12   # T'_{233}
Block RVTUDD Q= 1.19186980e+03 # non-zero R-Parity violating UDD soft terms 
Block RVKAPPA Q= 1.19186980e+03 # R-Parity violating kappa 
     1   -1.19978295e-26   # kappa_{1}
     2   -5.14613039e-12   # kappa_{2}
     3    0.00000000e+00   # kappa_{3}
Block RVD Q= 1.19186980e+03 # R-Parity violating D 
     1    8.40291366e-24   # D_{1}
     2    3.60426673e-09   # D_{2}
     3    0.00000000e+00   # D_{3}
Block RVSNVEV Q= 1.19186980e+03 # sneutrino VEVs D 
     1   -4.64121735e-22   # SneutrinoVev_{1}
     2   -1.89966820e-07   # SneutrinoVev_{2}
     3    0.00000000e+00   # SneutrinoVev_{3}
Block RVM2LH1 Q= 1.19186980e+03 # M2LH1 
     1   -1.58021775e-23   # M2LH1_{1}
     2   -6.77803203e-09   # M2LH1_{2}
     3    0.00000000e+00   # M2LH1_{3}
Block UPMNS Q= 9.11876000e+01 # neutrino mixing matrix (inverted  hierarchy)
  1  1     1.00000000e+00   # UPMNS_{11} matrix element
  1  2     9.61563551e-15   # UPMNS_{12} matrix element
  1  3     0.00000000e+00   # UPMNS_{13} matrix element
  2  1    -9.61563551e-15   # UPMNS_{21} matrix element
  2  2     1.00000000e+00   # UPMNS_{22} matrix element
  2  3     0.00000000e+00   # UPMNS_{23} matrix element
  3  1     0.00000000e+00   # UPMNS_{31} matrix element
  3  2     0.00000000e+00   # UPMNS_{32} matrix element
  3  3     1.00000000e+00   # UPMNS_{33} matrix element
Block msq2 Q= 1.19186980e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.92557670e+06    # (m_Q^2)_{11}
  1  2     6.53482668e+01    # (m_Q^2)_{12}
  1  3    -1.54666611e+03    # (m_Q^2)_{13}
  2  1     6.53482668e+01    # (m_Q^2)_{21}
  2  2     1.92510319e+06    # (m_Q^2)_{22}
  2  3     1.13868672e+04    # (m_Q^2)_{23}
  3  1    -1.54666611e+03    # (m_Q^2)_{31}
  3  2     1.13868672e+04    # (m_Q^2)_{32}
  3  3     1.64253199e+06    # (m_Q^2)_{33}
Block msl2 Q= 1.19186980e+03 # super MNS slepton mass^2 matrix - DRbar
  1  1     2.41553986e+05    # (m_L^2)_{11}
  1  2     1.05615311e-23    # (m_L^2)_{12}
  1  3     0.00000000e+00    # (m_L^2)_{13}
  2  1     1.05615311e-23    # (m_L^2)_{21}
  2  2     2.41549582e+05    # (m_L^2)_{22}
  2  3     0.00000000e+00    # (m_L^2)_{23}
  3  1     0.00000000e+00    # (m_L^2)_{31}
  3  2     0.00000000e+00    # (m_L^2)_{32}
  3  3     2.40231969e+05    # (m_L^2)_{33}
Block msd2 Q= 1.19186980e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.76179271e+06    # (m_d^2)_{11}
  1  2    -4.48398472e-06    # (m_d^2)_{12}
  1  3     4.63905802e-03    # (m_d^2)_{13}
  2  1    -4.48398472e-06    # (m_d^2)_{21}
  2  2     1.76178311e+06    # (m_d^2)_{22}
  2  3    -7.47802739e-01    # (m_d^2)_{23}
  3  1     4.63905802e-03    # (m_d^2)_{31}
  3  2    -7.47802739e-01    # (m_d^2)_{32}
  3  3     1.74439387e+06    # (m_d^2)_{33}
Block msu2 Q= 1.19186980e+03 # super CKM squark mass^2 matrix - DRbar
  1  1     1.77945151e+06    # (m_u^2)_{11}
  1  2    -2.26331772e-08    # (m_u^2)_{12}
  1  3    -2.00249842e-05    # (m_u^2)_{13}
  2  1    -2.26331772e-08    # (m_u^2)_{21}
  2  2     1.77944156e+06    # (m_u^2)_{22}
  2  3    -9.74677859e-02    # (m_u^2)_{23}
  3  1    -2.00249842e-05    # (m_u^2)_{31}
  3  2    -9.74677859e-02    # (m_u^2)_{32}
  3  3     1.21672215e+06    # (m_u^2)_{33}
Block mse2 Q= 1.19186980e+03 # super MNS slepton mass^2 matrix - DRbar
  1  1     9.60842087e+04    # (m_e^2)_{11}
  1  2     2.78891205e-16    # (m_e^2)_{12}
  1  3     0.00000000e+00    # (m_e^2)_{13}
  2  1     2.78891205e-16    # (m_e^2)_{21}
  2  2     9.60999625e+04    # (m_e^2)_{22}
  2  3     0.00000000e+00    # (m_e^2)_{23}
  3  1     0.00000000e+00    # (m_e^2)_{31}
  3  2     0.00000000e+00    # (m_e^2)_{32}
  3  3     9.33878024e+04    # (m_e^2)_{33}
Block tu Q= 1.19186980e+03   # super CKM trilinear matrix - DRbar
  1  1    -1.12213067e-02    # (T_u)_{11}
  1  2    -2.31369482e-08    # (T_u)_{12}
  1  3    -1.02828238e-07    # (T_u)_{13}
  2  1    -1.05984329e-05    # (T_u)_{21}
  2  2    -5.14021983e+00    # (T_u)_{22}
  2  3    -5.00035434e-04    # (T_u)_{23}
  3  1    -1.41348218e-02    # (T_u)_{31}
  3  2    -1.50023895e-01    # (T_u)_{32}
  3  3    -1.02065610e+03    # (T_u)_{33}
Block td Q= 1.19186980e+03   # super CKM trilinear matrix - DRbar
  1  1    -2.61635220e-01    # (T_d)_{11}
  1  2    -3.79610308e-06    # (T_d)_{12}
  1  3     9.03127447e-05    # (T_d)_{13}
  2  1    -8.31161408e-05    # (T_d)_{21}
  2  2    -5.72796675e+00    # (T_d)_{22}
  2  3    -1.45581044e-02    # (T_d)_{23}
  3  1     8.58879363e-02    # (T_d)_{31}
  3  2    -6.32325341e-01    # (T_d)_{32}
  3  3    -2.33430210e+02    # (T_d)_{33}
Block te Q= 1.19186980e+03   # super CKM trilinear matrix - DRbar
  1  1    -1.13906052e-02    # (T_e)_{11}
  1  2     4.97099997e-22    # (T_e)_{12}
  1  3     0.00000000e+00    # (T_e)_{13}
  2  1     2.41187414e-24    # (T_e)_{21}
  2  2    -2.35512866e+00    # (T_e)_{22}
  2  3     0.00000000e+00    # (T_e)_{23}
  3  1     0.00000000e+00    # (T_e)_{31}
  3  2     0.00000000e+00    # (T_e)_{32}
  3  3    -4.08076207e+01    # (T_e)_{33}
Block VCKM Q= 1.19186980e+03 # DRbar CKM mixing matrix
  1  1     9.73840758e-01    # CKM_{11} matrix element
  1  2     2.27197322e-01    # CKM_{12} matrix element
  1  3     3.94396208e-03    # CKM_{13} matrix element
  2  1    -2.27161574e-01    # CKM_{21} matrix element
  2  2     9.72963495e-01    # CKM_{22} matrix element
  2  3     4.17091978e-02    # CKM_{23} matrix element
  3  1     5.63888691e-03    # CKM_{31} matrix element
  3  2    -4.15140335e-02    # CKM_{32} matrix element
  3  3     9.99122009e-01    # CKM_{33} matrix element
Block msoft Q= 1.19186980e+03 # MSSM DRbar SUSY breaking parameters
     1     2.99009029e+02     # M_1(Q)
     2     5.48580705e+02     # M_2(Q)
     3     1.52309965e+03     # M_3(Q)
    21     2.12337345e+05     # mH1^2(Q)
    22    -6.82558913e+05     # mH2^2(Q)
Block USQMIX  # super CKM squark mass^2 matrix
  1  1     1.80493682e-05   # (USQMIX)_{11}
  1  2     1.91119019e-04   # (USQMIX)_{12}
  1  3     3.52453868e-01   # (USQMIX)_{13}
  1  4     9.32084438e-11   # (USQMIX)_{14}
  1  5     4.52695621e-07   # (USQMIX)_{15}
  1  6     9.35829169e-01   # (USQMIX)_{16}
  2  1     1.23685152e-04   # (USQMIX)_{21}
  2  2     1.30903304e-03   # (USQMIX)_{22}
  2  3     9.35828289e-01   # (USQMIX)_{23}
  2  4     2.46335757e-09   # (USQMIX)_{24}
  2  5     1.19444876e-05   # (USQMIX)_{25}
  2  6    -3.52453806e-01   # (USQMIX)_{26}
  3  1     1.05783966e-07   # (USQMIX)_{31}
  3  2     6.03110350e-03   # (USQMIX)_{32}
  3  3    -1.91319273e-05   # (USQMIX)_{33}
  3  4     1.68306691e-08   # (USQMIX)_{34}
  3  5     9.99981813e-01   # (USQMIX)_{35}
  3  6     5.49007667e-06   # (USQMIX)_{36}
  4  1     1.31657140e-05   # (USQMIX)_{41}
  4  2     1.29449272e-10   # (USQMIX)_{42}
  4  3    -3.94577541e-09   # (USQMIX)_{43}
  4  4     1.00000000e+00   # (USQMIX)_{44}
  4  5    -1.68332304e-08   # (USQMIX)_{45}
  4  6     1.13252018e-09   # (USQMIX)_{46}
  5  1     1.30479699e-01   # (USQMIX)_{51}
  5  2     9.91432060e-01   # (USQMIX)_{52}
  5  3    -1.29718499e-03   # (USQMIX)_{53}
  5  4    -1.71809284e-06   # (USQMIX)_{54}
  5  5    -5.97957829e-03   # (USQMIX)_{55}
  5  6     2.83560273e-04   # (USQMIX)_{56}
  6  1     9.91450973e-01   # (USQMIX)_{61}
  6  2    -1.30477378e-01   # (USQMIX)_{62}
  6  3     4.75532091e-05   # (USQMIX)_{63}
  6  4    -1.30531297e-05   # (USQMIX)_{64}
  6  5     7.86832966e-04   # (USQMIX)_{65}
  6  6    -1.03854680e-05   # (USQMIX)_{66}
Block DSQMIX  # super CKM squark mass^2 matrix
  1  1     4.68313659e-03   # (DSQMIX)_{11}
  1  2    -3.44785703e-02   # (DSQMIX)_{12}
  1  3     9.83563689e-01   # (DSQMIX)_{13}
  1  4     7.73567932e-07   # (DSQMIX)_{14}
  1  5    -1.24706359e-04   # (DSQMIX)_{15}
  1  6     1.77177172e-01   # (DSQMIX)_{16}
  2  1    -1.34849158e-03   # (DSQMIX)_{21}
  2  2     9.92852067e-03   # (DSQMIX)_{22}
  2  3    -1.76932263e-01   # (DSQMIX)_{23}
  2  4    -1.33286458e-06   # (DSQMIX)_{24}
  2  5     2.14939745e-04   # (DSQMIX)_{25}
  2  6     9.84172004e-01   # (DSQMIX)_{26}
  3  1     1.24617252e-06   # (DSQMIX)_{31}
  3  2     3.12814219e-03   # (DSQMIX)_{32}
  3  3     2.72636374e-04   # (DSQMIX)_{33}
  3  4     3.17225693e-06   # (DSQMIX)_{34}
  3  5     9.99995050e-01   # (DSQMIX)_{35}
  3  6    -2.00937082e-04   # (DSQMIX)_{36}
  4  1     1.43288773e-04   # (DSQMIX)_{41}
  4  2     4.69652171e-08   # (DSQMIX)_{42}
  4  3    -1.69207502e-06   # (DSQMIX)_{43}
  4  4     9.99999990e-01   # (DSQMIX)_{44}
  4  5    -3.17188626e-06   # (DSQMIX)_{45}
  4  6     1.24665310e-06   # (DSQMIX)_{46}
  5  1    -1.34800110e-01   # (DSQMIX)_{51}
  5  2     9.90206153e-01   # (DSQMIX)_{52}
  5  3     3.60190126e-02   # (DSQMIX)_{53}
  5  4     1.93245363e-05   # (DSQMIX)_{54}
  5  5    -3.10791627e-03   # (DSQMIX)_{55}
  5  6    -3.69799749e-03   # (DSQMIX)_{56}
  6  1     9.90860817e-01   # (DSQMIX)_{61}
  6  2     1.34887512e-01   # (DSQMIX)_{62}
  6  3     1.07098781e-05   # (DSQMIX)_{63}
  6  4    -1.41986890e-04   # (DSQMIX)_{64}
  6  5    -4.23186887e-04   # (DSQMIX)_{65}
  6  6    -1.09766530e-06   # (DSQMIX)_{66}
Block RVLMIX  # charged higgs-slepton mixing matrix 
  1 1    0.00000000e+00   # C_{11}
  1 2    0.00000000e+00   # C_{12}
  1 3    0.00000000e+00   # C_{13}
  1 4    0.00000000e+00   # C_{14}
  1 5    1.03620781e-01   # C_{15}
  1 6    0.00000000e+00   # C_{16}
  1 7    0.00000000e+00   # C_{17}
  1 8    9.94616878e-01   # C_{18}
  2 1    7.50417737e-30   # C_{21}
  2 2   -1.13952345e-28   # C_{22}
  2 3    2.95254474e-05   # C_{23}
  2 4   -1.64686071e-19   # C_{24}
  2 5    0.00000000e+00   # C_{25}
  2 6    1.00000000e+00   # C_{26}
  2 7   -1.56996088e-17   # C_{27}
  2 8    0.00000000e+00   # C_{28}
  3 1   -4.94920487e-13   # C_{31}
  3 2    7.51608058e-12   # C_{32}
  3 3    1.30634742e-22   # C_{33}
  3 4    6.10541544e-03   # C_{34}
  3 5    0.00000000e+00   # C_{35}
  3 6    1.57003217e-17   # C_{36}
  3 7    9.99981362e-01   # C_{37}
  3 8    0.00000000e+00   # C_{38}
  4 1    3.07967799e-27   # C_{41}
  4 2    1.36833567e-27   # C_{42}
  4 3    1.00000000e+00   # C_{43}
  4 4    1.09009694e-19   # C_{44}
  4 5    0.00000000e+00   # C_{45}
  4 6   -2.95254474e-05   # C_{46}
  4 7   -3.32631387e-22   # C_{47}
  4 8    0.00000000e+00   # C_{48}
  5 1    1.26017103e-12   # C_{51}
  5 2    5.42100712e-13   # C_{52}
  5 3   -1.09007661e-19   # C_{53}
  5 4    9.99981362e-01   # C_{54}
  5 5    0.00000000e+00   # C_{55}
  5 6    6.88335860e-20   # C_{56}
  5 7   -6.10541544e-03   # C_{57}
  5 8    0.00000000e+00   # C_{58}
  6 1    0.00000000e+00   # C_{61}
  6 2    0.00000000e+00   # C_{62}
  6 3    0.00000000e+00   # C_{63}
  6 4    0.00000000e+00   # C_{64}
  6 5    9.94616878e-01   # C_{65}
  6 6    0.00000000e+00   # C_{66}
  6 7    0.00000000e+00   # C_{67}
  6 8   -1.03620781e-01   # C_{68}
  7 1    9.94662497e-01   # C_{71}
  7 2    1.03181961e-01   # C_{72}
  7 3   -3.20428493e-27   # C_{73}
  7 4   -1.31108480e-12   # C_{74}
  7 5    0.00000000e+00   # C_{75}
  7 6   -1.48853463e-31   # C_{76}
  7 7   -2.75245499e-13   # C_{77}
  7 8    0.00000000e+00   # C_{78}
Block RVHMIX  # CP-even neutral scalar mixing matrix 
  1 1    1.04839867e-01   # curlyN_{11}
  1 2    9.94489116e-01   # curlyN_{12}
  1 3   -6.54041898e-26   # curlyN_{13}
  1 4   -2.67697514e-11   # curlyN_{14}
  1 5    0.00000000e+00   # curlyN_{15}
  2 1    0.00000000e+00   # curlyN_{21}
  2 2    0.00000000e+00   # curlyN_{22}
  2 3    0.00000000e+00   # curlyN_{23}
  2 4    0.00000000e+00   # curlyN_{24}
  2 5    1.00000000e+00   # curlyN_{25}
  3 1    4.55793242e-12   # curlyN_{31}
  3 2    2.64375929e-11   # curlyN_{32}
  3 3   -1.09070488e-19   # curlyN_{33}
  3 4    1.00000000e+00   # curlyN_{34}
  3 5    0.00000000e+00   # curlyN_{35}
  4 1    1.11348472e-26   # curlyN_{41}
  4 2    6.45957131e-26   # curlyN_{42}
  4 3    1.00000000e+00   # curlyN_{43}
  4 4    1.09070488e-19   # curlyN_{44}
  4 5    0.00000000e+00   # curlyN_{45}
  5 1    9.94489116e-01   # curlyN_{51}
  5 2   -1.04839867e-01   # curlyN_{52}
  5 3   -4.30108628e-27   # curlyN_{53}
  5 4   -1.76110047e-12   # curlyN_{54}
  5 5    0.00000000e+00   # curlyN_{55}
Block RVAMIX  # CP-odd neutral scalar mixing matrix 
  1 1    0.00000000e+00   # curlyN~_{11}
  1 2    0.00000000e+00   # curlyN~_{12}
  1 3    0.00000000e+00   # curlyN~_{13}
  1 4    0.00000000e+00   # curlyN~_{14}
  1 5    1.00000000e+00   # curlyN~_{15}
  2 1   -2.81743519e-12   # curlyN~_{21}
  2 2    2.72996825e-11   # curlyN~_{22}
  2 3   -1.09070488e-19   # curlyN~_{23}
  2 4    1.00000000e+00   # curlyN~_{24}
  2 5    0.00000000e+00   # curlyN~_{25}
  3 1   -6.88502102e-27   # curlyN~_{31}
  3 2    6.66970668e-26   # curlyN~_{32}
  3 3    1.00000000e+00   # curlyN~_{33}
  3 4    1.09070488e-19   # curlyN~_{34}
  3 5    0.00000000e+00   # curlyN~_{35}
  4 1    9.94662501e-01   # curlyN~_{41}
  4 2    1.03181920e-01   # curlyN~_{42}
  4 3   -3.36576234e-29   # curlyN~_{43}
  4 4   -1.44365363e-14   # curlyN~_{44}
  4 5    0.00000000e+00   # curlyN~_{45}