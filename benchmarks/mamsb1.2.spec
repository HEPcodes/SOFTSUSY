# SOFTSUSY3.4.1 SLHA compliant output
# B.C. Allanach, Comput. Phys. Commun. 143 (2002) 305-331, hep-ph/0104145
Block SPINFO          # Program information
     1    SOFTSUSY    # spectrum calculator
     2    3.4.1       # version number
Block MODSEL  # Select model
     1    3   # amsb
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
     1    3.75000000e+02   # m0
     2    5.00000000e+04   # m3/2
Block EXTPAR               # scale of SUSY breaking BCs
     0    2.44371560e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=7.12004234e-04
# MX=2.44371560e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03946733e+01   # MW
        25     1.14135982e+02   # h0
        35     8.96368446e+02   # H0
        36     8.96183707e+02   # A0
        37     9.00008584e+02   # H+
   1000021    -1.08704793e+03   # ~g
   1000022     1.64196051e+02   # ~neutralino(1)
   1000023     4.56142716e+02   # ~neutralino(2)
   1000024     1.64369658e+02   # ~chargino(1)
   1000025    -8.62661161e+02   # ~neutralino(3)
   1000035     8.69335027e+02   # ~neutralino(4)
   1000037     8.68132096e+02   # ~chargino(2)
   1000039     5.00000000e+04   # ~gravitino
   1000001     1.07982086e+03   # ~d_L
   1000002     1.07706753e+03   # ~u_L
   1000003     1.07981436e+03   # ~s_L
   1000004     1.07706100e+03   # ~c_L
   1000005     9.39010536e+02   # ~b_1
   1000006     7.80252248e+02   # ~t_1
   1000011     3.23425782e+02   # ~e_L
   1000012     3.13391566e+02   # ~nue_L
   1000013     3.23411683e+02   # ~mu_L
   1000014     3.13377037e+02   # ~numu_L
   1000015     2.87173933e+02   # ~stau_1
   1000016     3.08921938e+02   # ~nu_tau_L
   2000001     1.09077192e+03   # ~d_R
   2000002     1.08264424e+03   # ~u_R
   2000003     1.09076494e+03   # ~s_R
   2000004     1.08263828e+03   # ~c_R
   2000005     1.07629662e+03   # ~b_2
   2000006     9.78135324e+02   # ~t_2
   2000011     3.13331928e+02   # ~e_R
   2000013     3.13302741e+02   # ~mu_R
   2000015     3.34581654e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.06403276e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1    -5.33049203e-03   # N_{1,1}
  1  2     9.95025018e-01   # N_{1,2}
  1  3    -9.57782868e-02   # N_{1,3}
  1  4     2.68946115e-02   # N_{1,4}
  2  1     9.96224842e-01   # N_{2,1}
  2  2     1.36033005e-02   # N_{2,2}
  2  3     7.34665750e-02   # N_{2,3}
  2  4    -4.42004161e-02   # N_{2,4}
  3  1    -2.12449275e-02   # N_{3,1}
  3  2     4.85996028e-02   # N_{3,2}
  3  3     7.04737409e-01   # N_{3,3}
  3  4     7.07482803e-01   # N_{3,4}
  4  1    -8.40018043e-02   # N_{4,1}
  4  2     8.58967015e-02   # N_{4,2}
  4  3     6.99123999e-01   # N_{4,3}
  4  4    -7.04834085e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.90904464e-01   # U_{1,1}
  1  2    -1.34567248e-01   # U_{1,2}
  2  1     1.34567248e-01   # U_{2,1}
  2  2     9.90904464e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.99283037e-01   # V_{1,1}
  1  2    -3.78604262e-02   # V_{1,2}
  2  1     3.78604262e-02   # V_{2,1}
  2  2     9.99283037e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1    -4.03390377e-01   # F_{11}
  1  2     9.15027980e-01   # F_{12}
  2  1     9.15027980e-01   # F_{21}
  2  2     4.03390377e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.98279023e-01   # F_{11}
  1  2     5.86429283e-02   # F_{12}
  2  1    -5.86429283e-02   # F_{21}
  2  2     9.98279023e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     5.86358956e-01   # F_{11}
  1  2     8.10051341e-01   # F_{12}
  2  1     8.10051341e-01   # F_{21}
  2  2    -5.86358956e-01   # F_{22}
Block gauge Q= 8.41434018e+02  # SM gauge couplings
     1     3.62168686e-01   # g'(Q)MSSM DRbar
     2     6.44985532e-01   # g(Q)MSSM DRbar
     3     1.06272964e+00   # g3(Q)MSSM DRbar
Block yu Q= 8.41434018e+02  
  3  3     8.63492319e-01   # Yt(Q)MSSM DRbar
Block yd Q= 8.41434018e+02  
  3  3     1.49003285e-01   # Yb(Q)MSSM DRbar
Block ye Q= 8.41434018e+02  
  3  3     9.93740932e-02   # Ytau(Q)MSSM DRbar
Block hmix Q= 8.41434018e+02 # Higgs mixing parameters
     1     8.61466211e+02    # mu(Q)MSSM DRbar
     2     9.67927802e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.44429936e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     8.03315701e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 8.41434018e+02  # MSSM DRbar SUSY breaking parameters
     1     4.65558577e+02      # M_1(Q)
     2     1.59472715e+02      # M_2(Q)
     3    -1.03437804e+03      # M_3(Q)
    21     4.93849046e+04      # mH1^2(Q)
    22    -7.27137831e+05      # mH2^2(Q)
    31     3.19021335e+02      # meL(Q)
    32     3.19007050e+02      # mmuL(Q)
    33     3.14811022e+02      # mtauL(Q)
    34     3.06006578e+02      # meR(Q)
    35     3.05976779e+02      # mmuR(Q)
    36     2.97154052e+02      # mtauR(Q)
    41     1.04655482e+03      # mqL1(Q)
    42     1.04654811e+03      # mqL2(Q)
    43     9.07851272e+02      # mqL3(Q)
    44     1.05268651e+03      # muR(Q)
    45     1.05268036e+03      # mcR(Q)
    46     7.69256759e+02      # mtR(Q)
    47     1.06023132e+03      # mdR(Q)
    48     1.06022409e+03      # msR(Q)
    49     1.04519260e+03      # mbR(Q)
Block au Q= 8.41434018e+02  
  1  1     1.62907548e+03      # Au(Q)MSSM DRbar
  2  2     1.62906176e+03      # Ac(Q)MSSM DRbar
  3  3     9.24488810e+02      # At(Q)MSSM DRbar
Block ad Q= 8.41434018e+02  
  1  1     2.30319906e+03      # Ad(Q)MSSM DRbar
  2  2     2.30318635e+03      # As(Q)MSSM DRbar
  3  3     2.05129936e+03      # Ab(Q)MSSM DRbar
Block ae Q= 8.41434018e+02  
  1  1     4.90567467e+02      # Ae(Q)MSSM DRbar
  2  2     4.90535724e+02      # Amu(Q)MSSM DRbar
  3  3     4.81170016e+02      # Atau(Q)MSSM DRbar
