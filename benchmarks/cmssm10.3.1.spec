# SOFTSUSY3.4.0 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.0       # version number
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
     1    3.00000000e+02   # m0
     2    4.50000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.02230635e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=5.21267488e-04
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03968306e+01   # MW
        25     1.14247220e+02   # h0
        35     7.06800881e+02   # H0
        36     7.06477383e+02   # A0
        37     7.11367523e+02   # H+
   1000021     1.04852555e+03   # ~g
   1000022     1.83393594e+02   # ~neutralino(1)
   1000023     3.46114082e+02   # ~neutralino(2)
   1000024     3.46085364e+02   # ~chargino(1)
   1000025    -5.79635363e+02   # ~neutralino(3)
   1000035     5.94170370e+02   # ~neutralino(4)
   1000037     5.94534555e+02   # ~chargino(2)
   1000001     9.96863763e+02   # ~d_L
   1000002     9.93856773e+02   # ~u_L
   1000003     9.96861168e+02   # ~s_L
   1000004     9.93854168e+02   # ~c_L
   1000005     9.05366771e+02   # ~b_1
   1000006     7.47234066e+02   # ~t_1
   1000011     4.27902215e+02   # ~e_L
   1000012     4.20330576e+02   # ~nue_L
   1000013     4.27897426e+02   # ~mu_L
   1000014     4.20325706e+02   # ~numu_L
   1000015     3.40314891e+02   # ~stau_1
   1000016     4.18756993e+02   # ~nu_tau_L
   2000001     9.58873207e+02   # ~d_R
   2000002     9.61498003e+02   # ~u_R
   2000003     9.58870518e+02   # ~s_R
   2000004     9.61495224e+02   # ~c_R
   2000005     9.55091030e+02   # ~b_2
   2000006     9.49936836e+02   # ~t_2
   2000011     3.46576596e+02   # ~e_R
   2000013     3.46564621e+02   # ~mu_R
   2000015     4.28318102e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06819944e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.94898504e-01   # N_{1,1}
  1  2    -2.10724201e-02   # N_{1,2}
  1  3     9.12628658e-02   # N_{1,3}
  1  4    -3.74701089e-02   # N_{1,4}
  2  1     4.51542161e-02   # N_{2,1}
  2  2     9.66234632e-01   # N_{2,2}
  2  3    -2.11860371e-01   # N_{2,3}
  2  4     1.39523891e-01   # N_{2,4}
  3  1    -3.66373645e-02   # N_{3,1}
  3  2     5.34644296e-02   # N_{3,2}
  3  3     7.02663329e-01   # N_{3,3}
  3  4     7.08564396e-01   # N_{3,4}
  4  1    -8.24364417e-02   # N_{4,1}
  4  2     2.51173534e-01   # N_{4,2}
  4  3     6.73090275e-01   # N_{4,3}
  4  4    -6.90699335e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.52611100e-01   # U_{1,1}
  1  2    -3.04190883e-01   # U_{1,2}
  2  1     3.04190883e-01   # U_{2,1}
  2  2     9.52611100e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.79558072e-01   # V_{1,1}
  1  2    -2.01161583e-01   # V_{1,2}
  2  1     2.01161583e-01   # V_{2,1}
  2  2     9.79558072e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     4.24986170e-01   # F_{11}
  1  2     9.05199843e-01   # F_{12}
  2  1     9.05199843e-01   # F_{21}
  2  2    -4.24986170e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.84457019e-01   # F_{11}
  1  2     1.75625674e-01   # F_{12}
  2  1    -1.75625674e-01   # F_{21}
  2  2     9.84457019e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.57090061e-01   # F_{11}
  1  2     9.87584281e-01   # F_{12}
  2  1     9.87584281e-01   # F_{21}
  2  2    -1.57090061e-01   # F_{22}
Block gauge Q= 8.16307778e+02  # SM gauge couplings
     1     3.62094176e-01   # g'(Q)MSSM DRbar
     2     6.43255451e-01   # g(Q)MSSM DRbar
     3     1.06501876e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.16307778e+02  
  3  3     8.64179140e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.16307778e+02  
  3  3     1.36027163e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.16307778e+02  
  3  3     1.00473584e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.16307778e+02 # Higgs mixing parameters
     1     5.73788052e+02    # mu(Q)MSSM DRbar
     2     9.68146304e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44175943e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     5.16298702e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.16307778e+02  # MSSM DRbar SUSY breaking parameters
     1     1.87573067e+02      # M_1(Q)
     2     3.48988557e+02      # M_2(Q)
     3     1.00878372e+03      # M_3(Q)
    21     1.62329944e+05      # mH1^2(Q)
    22    -3.18361323e+05      # mH2^2(Q)
    31     4.22482194e+02      # meL(Q)
    32     4.22477332e+02      # mmuL(Q)
    33     4.21013837e+02      # mtauL(Q)
    34     3.42012304e+02      # meR(Q)
    35     3.42000171e+02      # mmuR(Q)
    36     3.38334188e+02      # mtauR(Q)
    41     9.62551130e+02      # mqL1(Q)
    42     9.62548471e+02      # mqL2(Q)
    43     8.78997635e+02      # mqL3(Q)
    44     9.30280357e+02      # muR(Q)
    45     9.30277525e+02      # mcR(Q)
    46     7.48587868e+02      # mtR(Q)
    47     9.26410750e+02      # mdR(Q)
    48     9.26408006e+02      # msR(Q)
    49     9.21348551e+02      # mbR(Q)
Block au Q= 8.16307778e+02  
  1  1    -1.03670532e+03      # Au(Q)MSSM DRbar
  2  2    -1.03670065e+03      # Ac(Q)MSSM DRbar
  3  3    -7.98466915e+02      # At(Q)MSSM DRbar
Block ad Q= 8.16307778e+02  
  1  1    -1.27001389e+03      # Ad(Q)MSSM DRbar
  2  2    -1.27000956e+03      # As(Q)MSSM DRbar
  3  3    -1.18634929e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.16307778e+02  
  1  1    -2.70595287e+02      # Ae(Q)MSSM DRbar
  2  2    -2.70590397e+02      # Amu(Q)MSSM DRbar
  3  3    -2.69119755e+02      # Atau(Q)MSSM DRbar
