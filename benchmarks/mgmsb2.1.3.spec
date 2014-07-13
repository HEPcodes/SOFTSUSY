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
     1    9.00000000e+04   # lambda
     2    1.00000000e+05   # M_mess
     5    1.00000000e+00   # N5
     6    1.00000000e+00   # cgrav
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=4.58424141e-04
# MX=1.00000000e+05 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.04035163e+01   # MW
        25     1.12330757e+02   # h0
        35     4.62228211e+02   # H0
        36     4.61894379e+02   # A0
        37     4.69154434e+02   # H+
   1000021     8.64571967e+02   # ~g
   1000022     1.45061837e+02   # ~neutralino(1)
   1000023     2.65582335e+02   # ~neutralino(2)
   1000024     2.64827284e+02   # ~chargino(1)
   1000025    -3.68263070e+02   # ~neutralino(3)
   1000035     4.01172255e+02   # ~neutralino(4)
   1000037     4.01215929e+02   # ~chargino(2)
   1000039     2.13300000e-09   # ~gravitino
   1000001     1.03056735e+03   # ~d_L
   1000002     1.02767033e+03   # ~u_L
   1000003     1.03056594e+03   # ~s_L
   1000004     1.02766892e+03   # ~c_L
   1000005     9.76794331e+02   # ~b_1
   1000006     9.13291045e+02   # ~t_1
   1000011     3.17799507e+02   # ~e_L
   1000012     3.07429997e+02   # ~nue_L
   1000013     3.17798149e+02   # ~mu_L
   1000014     3.07428595e+02   # ~numu_L
   1000015     1.52908206e+02   # ~stau_1
   1000016     3.06808241e+02   # ~nu_tau_L
   2000001     9.85001523e+02   # ~d_R
   2000002     9.87536577e+02   # ~u_R
   2000003     9.84999568e+02   # ~s_R
   2000004     9.87535577e+02   # ~c_R
   2000005     9.93416264e+02   # ~b_2
   2000006     1.00616379e+03   # ~t_2
   2000011     1.58936647e+02   # ~e_R
   2000013     1.58931158e+02   # ~mu_R
   2000015     3.19080462e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -7.59172832e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.83917922e-01   # N_{1,1}
  1  2    -4.32799884e-02   # N_{1,2}
  1  3     1.57612111e-01   # N_{1,3}
  1  4    -7.20471268e-02   # N_{1,4}
  2  1     1.21887587e-01   # N_{2,1}
  2  2     8.64324234e-01   # N_{2,2}
  2  3    -3.88777285e-01   # N_{2,3}
  2  4     2.94854637e-01   # N_{2,4}
  3  1    -5.62204288e-02   # N_{3,1}
  3  2     7.93596566e-02   # N_{3,2}
  3  3     6.97354147e-01   # N_{3,3}
  3  4     7.10097530e-01   # N_{3,4}
  4  1    -1.17848221e-01   # N_{4,1}
  4  2     4.94744890e-01   # N_{4,2}
  4  3     5.81126354e-01   # N_{4,3}
  4  4    -6.35319960e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     8.23299367e-01   # U_{1,1}
  1  2    -5.67607393e-01   # U_{1,2}
  2  1     5.67607393e-01   # U_{2,1}
  2  2     8.23299367e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.02289061e-01   # V_{1,1}
  1  2    -4.31131593e-01   # V_{1,2}
  2  1     4.31131593e-01   # V_{2,1}
  2  2     9.02289061e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.77254710e-01   # F_{11}
  1  2     9.60796454e-01   # F_{12}
  2  1     9.60796454e-01   # F_{21}
  2  2    -2.77254710e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     4.75871826e-01   # F_{11}
  1  2     8.79514642e-01   # F_{12}
  2  1     8.79514642e-01   # F_{21}
  2  2    -4.75871826e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.22978484e-01   # F_{11}
  1  2     9.92409337e-01   # F_{12}
  2  1     9.92409337e-01   # F_{21}
  2  2    -1.22978484e-01   # F_{22}
Block gauge Q= 9.37893547e+02  # SM gauge couplings
     1     3.62940588e-01   # g'(Q)MSSM DRbar
     2     6.44931690e-01   # g(Q)MSSM DRbar
     3     1.06542075e+00   # g3(Q)MSSM DRbar
Block yu Q= 9.37893547e+02  
  3  3     8.66418661e-01   # Yt(Q)MSSM DRbar
Block yd Q= 9.37893547e+02  
  3  3     2.04695665e-01   # Yb(Q)MSSM DRbar
Block ye Q= 9.37893547e+02  
  3  3     1.51484292e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 9.37893547e+02 # Higgs mixing parameters
     1     3.59449592e+02    # mu(Q)MSSM DRbar
     2     1.45087715e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43642970e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     2.36653936e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 9.37893547e+02  # MSSM DRbar SUSY breaking parameters
     1     1.51689603e+02      # M_1(Q)
     2     2.86308742e+02      # M_2(Q)
     3     7.85300409e+02      # M_3(Q)
    21     8.47411689e+04      # mH1^2(Q)
    22    -1.13696850e+05      # mH2^2(Q)
    31     3.11339120e+02      # meL(Q)
    32     3.11337731e+02      # mmuL(Q)
    33     3.10913521e+02      # mtauL(Q)
    34     1.48353910e+02      # meR(Q)
    35     1.48348023e+02      # mmuR(Q)
    36     1.46539562e+02      # mtauR(Q)
    41     1.00167356e+03      # mqL1(Q)
    42     1.00167210e+03      # mqL2(Q)
    43     9.66803001e+02      # mqL3(Q)
    44     9.60964115e+02      # muR(Q)
    45     9.60963080e+02      # mcR(Q)
    46     8.89691746e+02      # mtR(Q)
    47     9.57082741e+02      # mdR(Q)
    48     9.57080711e+02      # msR(Q)
    49     9.53123601e+02      # mbR(Q)
Block au Q= 9.37893547e+02  
  1  1    -2.41594358e+02      # Au(Q)MSSM DRbar
  2  2    -2.41594013e+02      # Ac(Q)MSSM DRbar
  3  3    -2.27470379e+02      # At(Q)MSSM DRbar
Block ad Q= 9.37893547e+02  
  1  1    -2.57312918e+02      # Ad(Q)MSSM DRbar
  2  2    -2.57312436e+02      # As(Q)MSSM DRbar
  3  3    -2.51992763e+02      # Ab(Q)MSSM DRbar
Block ae Q= 9.37893547e+02  
  1  1    -2.43963619e+01      # Ae(Q)MSSM DRbar
  2  2    -2.43961814e+01      # Amu(Q)MSSM DRbar
  3  3    -2.43410615e+01      # Atau(Q)MSSM DRbar
