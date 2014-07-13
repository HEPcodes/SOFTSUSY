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
     1    1.50000000e+02   # m0
     2    6.00000000e+02   # m12
     5    0.00000000e+00   # A0
Block EXTPAR               # scale of SUSY breaking BCs
     0    1.76385201e+16   # MX scale
# SOFTSUSY-specific non SLHA information:
# MIXING=0 Desired accuracy=1.00000000e-03 Achieved accuracy=1.11811082e-04
# MX=1.76385201e+16 GeV
Block MASS                      # Mass spectrum
# PDG code     mass             particle
        24     8.03945127e+01   # MW
        25     1.16085538e+02   # h0
        35     8.48771730e+02   # H0
        36     8.48539246e+02   # A0
        37     8.52560795e+02   # H+
   1000021     1.35667047e+03   # ~g
   1000022     2.47689437e+02   # ~neutralino(1)
   1000023     4.68638798e+02   # ~neutralino(2)
   1000024     4.68701489e+02   # ~chargino(1)
   1000025    -7.45754923e+02   # ~neutralino(3)
   1000035     7.58164563e+02   # ~neutralino(4)
   1000037     7.58410390e+02   # ~chargino(2)
   1000001     1.24670820e+03   # ~d_L
   1000002     1.24433108e+03   # ~u_L
   1000003     1.24670519e+03   # ~s_L
   1000004     1.24432805e+03   # ~c_L
   1000005     1.14235049e+03   # ~b_1
   1000006     9.58226056e+02   # ~t_1
   1000011     4.31793770e+02   # ~e_L
   1000012     4.24323005e+02   # ~nue_L
   1000013     4.31789896e+02   # ~mu_L
   1000014     4.24319066e+02   # ~numu_L
   1000015     2.66970894e+02   # ~stau_1
   1000016     4.22941428e+02   # ~nu_tau_L
   2000001     1.19293706e+03   # ~d_R
   2000002     1.19736463e+03   # ~u_R
   2000003     1.19293391e+03   # ~s_R
   2000004     1.19736140e+03   # ~c_R
   2000005     1.18847716e+03   # ~b_2
   2000006     1.18197126e+03   # ~t_2
   2000011     2.74085057e+02   # ~e_R
   2000013     2.74072675e+02   # ~mu_R
   2000015     4.32299994e+02   # ~stau_2
Block alpha                     # Effective Higgs mixing parameter
          -1.05966214e-01       # alpha
Block nmix                  # neutralino mixing matrix
  1  1     9.96966162e-01   # N_{1,1}
  1  2    -1.26748339e-02   # N_{1,2}
  1  3     7.06798313e-02   # N_{1,3}
  1  4    -3.00363358e-02   # N_{1,4}
  2  1     2.86652975e-02   # N_{2,1}
  2  2     9.76134591e-01   # N_{2,2}
  2  3    -1.77579258e-01   # N_{2,3}
  2  4     1.21676490e-01   # N_{2,4}
  3  1    -2.80967600e-02   # N_{3,1}
  3  2     4.07347858e-02   # N_{3,2}
  3  3     7.04489163e-01   # N_{3,3}
  3  4     7.07987477e-01   # N_{3,4}
  4  1    -6.66884115e-02   # N_{4,1}
  4  2     2.12934934e-01   # N_{4,2}
  4  3     6.83494687e-01   # N_{4,3}
  4  4    -6.95015383e-01   # N_{4,4}
Block Umix                  # chargino U mixing matrix 
  1  1     9.67359948e-01   # U_{1,1}
  1  2    -2.53406258e-01   # U_{1,2}
  2  1     2.53406258e-01   # U_{2,1}
  2  2     9.67359948e-01   # U_{2,2}
Block Vmix                  # chargino V mixing matrix 
  1  1     9.84730707e-01   # V_{1,1}
  1  2    -1.74084564e-01   # V_{1,2}
  2  1     1.74084564e-01   # V_{2,1}
  2  2     9.84730707e-01   # V_{2,2}
Block stopmix               # stop mixing matrix
  1  1     3.84605344e-01   # F_{11}
  1  2     9.23081106e-01   # F_{12}
  2  1     9.23081106e-01   # F_{21}
  2  2    -3.84605344e-01   # F_{22}
Block sbotmix               # sbottom mixing matrix
  1  1     9.81379084e-01   # F_{11}
  1  2     1.92080955e-01   # F_{12}
  2  1    -1.92080955e-01   # F_{21}
  2  2     9.81379084e-01   # F_{22}
Block staumix               # stau mixing matrix
  1  1     1.18064696e-01   # F_{11}
  1  2     9.93005905e-01   # F_{12}
  2  1     9.93005905e-01   # F_{21}
  2  2    -1.18064696e-01   # F_{22}
Block gauge Q= 1.03281016e+03  # SM gauge couplings
     1     3.62766869e-01   # g'(Q)MSSM DRbar
     2     6.42082770e-01   # g(Q)MSSM DRbar
     3     1.05212450e+00   # g3(Q)MSSM DRbar
Block yu Q= 1.03281016e+03  
  3  3     8.55437341e-01   # Yt(Q)MSSM DRbar
Block yd Q= 1.03281016e+03  
  3  3     1.34149952e-01   # Yb(Q)MSSM DRbar
Block ye Q= 1.03281016e+03  
  3  3     1.00418885e-01   # Ytau(Q)MSSM DRbar
Block hmix Q= 1.03281016e+03 # Higgs mixing parameters
     1     7.40337510e+02    # mu(Q)MSSM DRbar
     2     9.65379664e+00    # tan beta(Q)MSSM DRbar Feynman gauge
     3     2.43912205e+02    # higgs vev(Q)MSSM DRbar Feynman gauge
     4     7.46256614e+05    # mA^2(Q)MSSM DRbar
Block msoft Q= 1.03281016e+03  # MSSM DRbar SUSY breaking parameters
     1     2.53206999e+02      # M_1(Q)
     2     4.67936390e+02      # M_2(Q)
     3     1.31909528e+03      # M_3(Q)
    21     1.56952988e+05      # mH1^2(Q)
    22    -5.28306366e+05      # mH2^2(Q)
    31     4.23672759e+02      # meL(Q)
    32     4.23668817e+02      # mmuL(Q)
    33     4.22477126e+02      # mtauL(Q)
    34     2.66158977e+02      # meR(Q)
    35     2.66146213e+02      # mmuR(Q)
    36     2.62264162e+02      # mtauR(Q)
    41     1.20403493e+03      # mqL1(Q)
    42     1.20403185e+03      # mqL2(Q)
    43     1.11028577e+03      # mqL3(Q)
    44     1.15796862e+03      # muR(Q)
    45     1.15796533e+03      # mcR(Q)
    46     9.54084703e+02      # mtR(Q)
    47     1.15234619e+03      # mdR(Q)
    48     1.15234299e+03      # msR(Q)
    49     1.14650404e+03      # mbR(Q)
Block au Q= 1.03281016e+03  
  1  1    -1.34291478e+03      # Au(Q)MSSM DRbar
  2  2    -1.34290880e+03      # Ac(Q)MSSM DRbar
  3  3    -1.03903333e+03      # At(Q)MSSM DRbar
Block ad Q= 1.03281016e+03  
  1  1    -1.63958307e+03      # Ad(Q)MSSM DRbar
  2  2    -1.63957754e+03      # As(Q)MSSM DRbar
  3  3    -1.53291832e+03      # Ab(Q)MSSM DRbar
Block ae Q= 1.03281016e+03  
  1  1    -3.56261220e+02      # Ae(Q)MSSM DRbar
  2  2    -3.56254890e+02      # Amu(Q)MSSM DRbar
  3  3    -3.54341625e+02      # Atau(Q)MSSM DRbar
