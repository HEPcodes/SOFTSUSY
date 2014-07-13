# SOFTSUSY3.4.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.1       # version number
Block MODSEL  # Select model
     1    1   # sugra
Block SMINPUTS             # Standard Model inputs
     1    1.27934000e+02   # alpha_em^(-1)(MZ) SM MSbar
     2    1.16637000e-05   # G_Fermi
     3    1.17200000e-01   # alpha_s(MZ)MSbar
     4    9.11876000e+01   # MZ(pole)
     5    4.25000000e+00   # mb(mb)
     6    1.73300000e+02   # Mtop(pole)
     7    1.77700000e+00   # Mtau(pole)
Block MINPAR               # SUSY breaking input parameters
     3    4.00000000e+01   # tanb, DRbar, Feynman gauge
     4    1.00000000e+00   # sign(mu)
     1    6.00000000e+02   # m0
     2    5.00000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.95484588e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=6.15446208e-04
# MX=1.95484588e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03905670e+01   # MW
        25     1.17107153e+02   # h0
        35     6.90336687e+02   # H0
        36     6.90341169e+02   # A0
        37     6.95398074e+02   # H+
   1000021     1.17095730e+03   # ~g
   1000022     2.08190426e+02   # ~neutralino(1)
   1000023     3.97021924e+02   # ~neutralino(2)
   1000024     3.97146977e+02   # ~chargino(1)
   1000025    -6.97382074e+02   # ~neutralino(3)
   1000035     7.05942221e+02   # ~neutralino(4)
   1000037     7.07082422e+02   # ~chargino(2)
   1000001     1.20234533e+03   # ~d_L
   1000002     1.19986753e+03   # ~u_L
   1000003     1.20230821e+03   # ~s_L
   1000004     1.19983033e+03   # ~c_L
   1000005     9.90205830e+02   # ~b_1
   1000006     8.35838071e+02   # ~t_1
   1000011     6.86803082e+02   # ~e_L
   1000012     6.81870394e+02   # ~nue_L
   1000013     6.86624690e+02   # ~mu_L
   1000014     6.81690814e+02   # ~numu_L
   1000015     4.70422797e+02   # ~stau_1
   1000016     6.20872127e+02   # ~nu_tau_L
   2000001     1.16514039e+03   # ~d_R
   2000002     1.16787298e+03   # ~u_R
   2000003     1.16506751e+03   # ~s_R
   2000004     1.16786827e+03   # ~c_R
   2000005     1.06487772e+03   # ~b_2
   2000006     1.05017244e+03   # ~t_2
   2000011     6.29304511e+02   # ~e_R
   2000013     6.28911732e+02   # ~mu_R
   2000015     6.38876624e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.60194914e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.97049954e-01   # N_{1,1}
  1  2    -1.03713191e-02   # N_{1,2}
  1  3     7.22797171e-02   # N_{1,3}
  1  4    -2.36530815e-02   # N_{1,4}
  2  1     2.44479444e-02   # N_{2,1}
  2  2     9.81285814e-01   # N_{2,2}
  2  3    -1.64902067e-01   # N_{2,3}
  2  4     9.63730127e-02   # N_{2,4}
  3  1    -3.37027542e-02   # N_{3,1}
  3  2     4.95635255e-02   # N_{3,2}
  3  3     7.03696622e-01   # N_{3,3}
  3  4     7.07967970e-01   # N_{3,4}
  4  1    -6.44811011e-02   # N_{4,1}
  4  2     1.85779558e-01   # N_{4,2}
  4  3     6.87309258e-01   # N_{4,3}
  4  4    -6.99238248e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.71992359e-01   # U_{1,1}
  1  2    -2.35012455e-01   # U_{1,2}
  2  1     2.35012455e-01   # U_{2,1}
  2  2     9.71992359e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.90449744e-01   # V_{1,1}
  1  2    -1.37874233e-01   # V_{1,2}
  2  1     1.37874233e-01   # V_{2,1}
  2  2     9.90449744e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.28706721e-01   # F_{11}
  1  2     9.03443716e-01   # F_{12}
  2  1     9.03443716e-01   # F_{21}
  2  2    -4.28706721e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     8.95923016e-01   # F_{11}
  1  2     4.44209352e-01   # F_{12}
  2  1    -4.44209352e-01   # F_{21}
  2  2     8.95923016e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     2.91473337e-01   # F_{11}
  1  2     9.56578953e-01   # F_{12}
  2  1     9.56578953e-01   # F_{21}
  2  2    -2.91473337e-01   # F_{22}
Block gauge Q= 9.09333190e+02  # SM gauge couplings
     1     3.62083264e-01   # g'(Q)MSSM DRbar
     2     6.41966876e-01   # g(Q)MSSM DRbar
     3     1.05866867e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.09333190e+02  
  3  3     8.55107033e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.09333190e+02  
  3  3     4.96876333e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.09333190e+02  
  3  3     4.23717356e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.09333190e+02 # Higgs mixing parameters
     1     6.92877718e+02    # mu(Q)MSSM DRbar
     2     3.92246336e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43959928e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     6.09330342e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.09333190e+02  # MSSM DRbar SUSY breaking parameters
     1     2.10820318e+02      # M_1(Q)
     2     3.91199462e+02      # M_2(Q)
     3     1.11446147e+03      # M_3(Q)
    21     6.27368880e+03      # mH1^2(Q)
    22    -4.71938083e+05      # mH2^2(Q)
    31     6.83025331e+02      # meL(Q)
    32     6.82845992e+02      # mmuL(Q)
    33     6.24207520e+02      # mtauL(Q)
    34     6.26405348e+02      # meR(Q)
    35     6.26011173e+02      # mmuR(Q)
    36     4.86800849e+02      # mtauR(Q)
    41     1.16778442e+03      # mqL1(Q)
    42     1.16774599e+03      # mqL2(Q)
    43     9.77878765e+02      # mqL3(Q)
    44     1.13584983e+03      # muR(Q)
    45     1.13584497e+03      # mcR(Q)
    46     8.39350987e+02      # mtR(Q)
    47     1.13206924e+03      # mdR(Q)
    48     1.13199395e+03      # msR(Q)
    49     1.01998498e+03      # mbR(Q)
Block au Q= 9.09333190e+02  
  1  1    -1.47786115e+03      # Au(Q)MSSM DRbar
  2  2    -1.47782490e+03      # Ac(Q)MSSM DRbar
  3  3    -1.01692010e+03      # At(Q)MSSM DRbar
Block ad Q= 9.09333190e+02  
  1  1    -1.71622418e+03      # Ad(Q)MSSM DRbar
  2  2    -1.71613188e+03      # As(Q)MSSM DRbar
  3  3    -1.43761792e+03      # Ab(Q)MSSM DRbar
Block ae Q= 9.09333190e+02  
  1  1    -6.22569703e+02      # Ae(Q)MSSM DRbar
  2  2    -6.22256224e+02      # Amu(Q)MSSM DRbar
  3  3    -5.19334611e+02      # Atau(Q)MSSM DRbar
