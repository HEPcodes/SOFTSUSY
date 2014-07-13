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
     3    1.00000000e+01   # tanb, DRbar, Feynman gauge
     4    1.00000000e+00   # sign(mu)
     1    2.50000000e+02   # m0
     2    6.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.79640155e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.10522664e-04
# MX=1.79640155e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03941529e+01   # MW
        25     1.16111790e+02   # h0
        35     8.71238461e+02   # H0
        36     8.70999048e+02   # A0
        37     8.74942998e+02   # H+
   1000021     1.35966333e+03   # ~g
   1000022     2.48142177e+02   # ~neutralino(1)
   1000023     4.69490823e+02   # ~neutralino(2)
   1000024     4.69553686e+02   # ~chargino(1)
   1000025    -7.45757016e+02   # ~neutralino(3)
   1000035     7.58194824e+02   # ~neutralino(4)
   1000037     7.58435724e+02   # ~chargino(2)
   1000001     1.26232744e+03   # ~d_L
   1000002     1.25998342e+03   # ~u_L
   1000003     1.26232432e+03   # ~s_L
   1000004     1.25998030e+03   # ~c_L
   1000005     1.15391575e+03   # ~b_1
   1000006     9.66350546e+02   # ~t_1
   1000011     4.75467734e+02   # ~e_L
   1000012     4.68672708e+02   # ~nue_L
   1000013     4.75463062e+02   # ~mu_L
   1000014     4.68667970e+02   # ~numu_L
   1000015     3.32171114e+02   # ~stau_1
   1000016     4.67065109e+02   # ~nu_tau_L
   2000001     1.20942982e+03   # ~d_R
   2000002     1.21380016e+03   # ~u_R
   2000003     1.20942657e+03   # ~s_R
   2000004     1.21379681e+03   # ~c_R
   2000005     1.20456884e+03   # ~b_2
   2000006     1.19225859e+03   # ~t_2
   2000011     3.38923366e+02   # ~e_R
   2000013     3.38910061e+02   # ~mu_R
   2000015     4.75570960e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05842776e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96958089e-01   # N_{1,1}
  1  2    -1.26834066e-02   # N_{1,2}
  1  3     7.07619631e-02   # N_{1,3}
  1  4    -3.01072089e-02   # N_{1,4}
  2  1     2.87254912e-02   # N_{2,1}
  2  2     9.76042922e-01   # N_{2,2}
  2  3    -1.77865367e-01   # N_{2,3}
  2  4     1.21979393e-01   # N_{2,4}
  3  1    -2.81046143e-02   # N_{3,1}
  3  2     4.07279204e-02   # N_{3,2}
  3  3     7.04490996e-01   # N_{3,3}
  3  4     7.07985737e-01   # N_{3,4}
  4  1    -6.67798253e-02   # N_{4,1}
  4  2     2.13355531e-01   # N_{4,2}
  4  3     6.83409901e-01   # N_{4,3}
  4  4    -6.94960992e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.67163612e-01   # U_{1,1}
  1  2    -2.54154573e-01   # U_{1,2}
  2  1     2.54154573e-01   # U_{2,1}
  2  2     9.67163612e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.84594284e-01   # V_{1,1}
  1  2    -1.74854497e-01   # V_{1,2}
  2  1     1.74854497e-01   # V_{2,1}
  2  2     9.84594284e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.76439943e-01   # F_{11}
  1  2     9.26441023e-01   # F_{12}
  2  1     9.26441023e-01   # F_{21}
  2  2    -3.76439943e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.85010143e-01   # F_{11}
  1  2     1.72496430e-01   # F_{12}
  2  1    -1.72496430e-01   # F_{21}
  2  2     9.85010143e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.17748962e-01   # F_{11}
  1  2     9.93043394e-01   # F_{12}
  2  1     9.93043394e-01   # F_{21}
  2  2    -1.17748962e-01   # F_{22}
Block gauge Q= 1.04161501e+03  # SM gauge couplings
     1     3.62710173e-01   # g'(Q)MSSM DRbar
     2     6.41986408e-01   # g(Q)MSSM DRbar
     3     1.05179421e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.04161501e+03  
  3  3     8.55317363e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.04161501e+03  
  3  3     1.34154842e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.04161501e+03  
  3  3     1.00403704e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.04161501e+03 # Higgs mixing parameters
     1     7.40241584e+02    # mu(Q)MSSM DRbar
     2     9.65267332e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43896715e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     7.85375209e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.04161501e+03  # MSSM DRbar SUSY breaking parameters
     1     2.53210585e+02      # M_1(Q)
     2     4.67952573e+02      # M_2(Q)
     3     1.31890250e+03      # M_3(Q)
    21     1.95212836e+05      # mH1^2(Q)
    22    -5.27291852e+05      # mH2^2(Q)
    31     4.68054896e+02      # meL(Q)
    32     4.68050140e+02      # mmuL(Q)
    33     4.66612157e+02      # mtauL(Q)
    34     3.32675956e+02      # meR(Q)
    35     3.32662390e+02      # mmuR(Q)
    36     3.28540511e+02      # mtauR(Q)
    41     1.21952881e+03      # mqL1(Q)
    42     1.21952563e+03      # mqL2(Q)
    43     1.12139974e+03      # mqL3(Q)
    44     1.17420462e+03      # muR(Q)
    45     1.17420122e+03      # mcR(Q)
    46     9.60716955e+02      # mtR(Q)
    47     1.16867958e+03      # mdR(Q)
    48     1.16867628e+03      # msR(Q)
    49     1.16264372e+03      # mbR(Q)
Block au Q= 1.04161501e+03  
  1  1    -1.34254407e+03      # Au(Q)MSSM DRbar
  2  2    -1.34253809e+03      # Ac(Q)MSSM DRbar
  3  3    -1.03867334e+03      # At(Q)MSSM DRbar
Block ad Q= 1.04161501e+03  
  1  1    -1.63918618e+03      # Ad(Q)MSSM DRbar
  2  2    -1.63918064e+03      # As(Q)MSSM DRbar
  3  3    -1.53252273e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.04161501e+03  
  1  1    -3.56270146e+02      # Ae(Q)MSSM DRbar
  2  2    -3.56263815e+02      # Amu(Q)MSSM DRbar
  3  3    -3.54350484e+02      # Atau(Q)MSSM DRbar
