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
     1    1.20000000e+03   # m0
     2    4.50000000e+02   # m12
     5   -5.00000000e+02   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.08987554e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=3.61923489e-04
# MX=2.08987554e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03908426e+01   # MW
        25     1.16883625e+02   # h0
        35     9.42611623e+02   # H0
        36     9.42714781e+02   # A0
        37     9.46289805e+02   # H+
   1000021     1.10074825e+03   # ~g
   1000022     1.88515057e+02   # ~neutralino(1)
   1000023     3.60118037e+02   # ~neutralino(2)
   1000024     3.60225365e+02   # ~chargino(1)
   1000025    -6.19936649e+02   # ~neutralino(3)
   1000035     6.30471480e+02   # ~neutralino(4)
   1000037     6.31569413e+02   # ~chargino(2)
   1000001     1.50618543e+03   # ~d_L
   1000002     1.50421660e+03   # ~u_L
   1000003     1.50613363e+03   # ~s_L
   1000004     1.50416473e+03   # ~c_L
   1000005     1.18353800e+03   # ~b_1
   1000006     9.83201365e+02   # ~t_1
   1000011     1.23341739e+03   # ~e_L
   1000012     1.23051510e+03   # ~nue_L
   1000013     1.23311569e+03   # ~mu_L
   1000014     1.23021277e+03   # ~numu_L
   1000015     9.95319279e+02   # ~stau_1
   1000016     1.13133953e+03   # ~nu_tau_L
   2000001     1.48466388e+03   # ~d_R
   2000002     1.48591540e+03   # ~u_R
   2000003     1.48456487e+03   # ~s_R
   2000004     1.48590864e+03   # ~c_R
   2000005     1.31119352e+03   # ~b_2
   2000006     1.21427214e+03   # ~t_2
   2000011     1.21108628e+03   # ~e_R
   2000013     1.21046948e+03   # ~mu_R
   2000015     1.13747921e+03   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -2.59229884e-02       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96172173e-01   # N_{1,1}
  1  2    -1.28120353e-02   # N_{1,2}
  1  3     8.20639133e-02   # N_{1,3}
  1  4    -2.72464249e-02   # N_{1,4}
  2  1     3.11334713e-02   # N_{2,1}
  2  2     9.75153639e-01   # N_{2,2}
  2  3    -1.88398664e-01   # N_{2,3}
  2  4     1.12303297e-01   # N_{2,4}
  3  1    -3.78231235e-02   # N_{3,1}
  3  2     5.54565252e-02   # N_{3,2}
  3  3     7.02897315e-01   # N_{3,3}
  3  4     7.08116763e-01   # N_{3,4}
  4  1    -7.23955805e-02   # N_{4,1}
  4  2     2.14092984e-01   # N_{4,2}
  4  3     6.80960221e-01   # N_{4,3}
  4  4    -6.96574656e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.63201444e-01   # U_{1,1}
  1  2    -2.68780540e-01   # U_{1,2}
  2  1     2.68780540e-01   # U_{2,1}
  2  2     9.63201444e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.86988764e-01   # V_{1,1}
  1  2    -1.60789241e-01   # V_{1,2}
  2  1     1.60789241e-01   # V_{2,1}
  2  2     9.86988764e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     2.95766265e-01   # F_{11}
  1  2     9.55260340e-01   # F_{12}
  2  1     9.55260340e-01   # F_{21}
  2  2    -2.95766265e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.84274166e-01   # F_{11}
  1  2     1.76647573e-01   # F_{12}
  2  1    -1.76647573e-01   # F_{21}
  2  2     9.84274166e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.51205242e-01   # F_{11}
  1  2     9.88502390e-01   # F_{12}
  2  1     9.88502390e-01   # F_{21}
  2  2    -1.51205242e-01   # F_{22}
Block gauge Q= 1.06741336e+03  # SM gauge couplings
     1     3.62258151e-01   # g'(Q)MSSM DRbar
     2     6.41713950e-01   # g(Q)MSSM DRbar
     3     1.05405435e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.06741336e+03  
  3  3     8.54178464e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.06741336e+03  
  3  3     5.16039088e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.06741336e+03  
  3  3     4.12907242e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.06741336e+03 # Higgs mixing parameters
     1     6.12073843e+02    # mu(Q)MSSM DRbar
     2     3.92070985e+01    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43605010e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     1.07011120e+06    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.06741336e+03  # MSSM DRbar SUSY breaking parameters
     1     1.90398290e+02      # M_1(Q)
     2     3.52809263e+02      # M_2(Q)
     3     9.97157401e+02      # M_3(Q)
    21     5.37971781e+05      # mH1^2(Q)
    22    -3.57908460e+05      # mH2^2(Q)
    31     1.23047107e+03      # meL(Q)
    32     1.23016953e+03      # mmuL(Q)
    33     1.13380797e+03      # mtauL(Q)
    34     1.20893263e+03      # meR(Q)
    35     1.20831564e+03      # mmuR(Q)
    36     1.00058292e+03      # mtauR(Q)
    41     1.47876400e+03      # mqL1(Q)
    42     1.47871129e+03      # mqL2(Q)
    43     1.16481742e+03      # mqL3(Q)
    44     1.46164022e+03      # muR(Q)
    45     1.46163334e+03      # mcR(Q)
    46     9.68009056e+02      # mtR(Q)
    47     1.45972932e+03      # mdR(Q)
    48     1.45962840e+03      # msR(Q)
    49     1.28511226e+03      # mbR(Q)
Block au Q= 1.06741336e+03  
  1  1    -1.35325057e+03      # Au(Q)MSSM DRbar
  2  2    -1.35321702e+03      # Ac(Q)MSSM DRbar
  3  3    -9.19240853e+02      # At(Q)MSSM DRbar
Block ad Q= 1.06741336e+03  
  1  1    -1.56519443e+03      # Ad(Q)MSSM DRbar
  2  2    -1.56510902e+03      # As(Q)MSSM DRbar
  3  3    -1.29432821e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.06741336e+03  
  1  1    -5.92623426e+02      # Ae(Q)MSSM DRbar
  2  2    -5.92318829e+02      # Amu(Q)MSSM DRbar
  3  3    -4.97371800e+02      # Atau(Q)MSSM DRbar
