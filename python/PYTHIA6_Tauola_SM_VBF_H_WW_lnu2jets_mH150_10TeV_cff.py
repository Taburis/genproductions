import FWCore.ParameterSet.Config as cms

from Configuration.GenProduction.PythiaUESettings_cfi import *
from GeneratorInterface.Pythia6Interface.TauolaSettings_cff import *
#################################################
source = cms.Source("PythiaSource",					       
    pythiaHepMCVerbosity = cms.untracked.bool(False),			       
    maxEventsToPrint = cms.untracked.int32(0),				       
    pythiaPylistVerbosity = cms.untracked.int32(0),			       
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.untracked.double(10000.0),	
    crossSection = cms.untracked.double(55000000000.),
    ##### add Tauola to Pythia
    ExternalGenerators = cms.PSet(
           Tauola = cms.untracked.PSet(
                       TauolaPolar,
                       TauolaDefaultInputCards
           ),
           parameterSets = cms.vstring('Tauola')
    ),
    UseExternalGenerators = cms.untracked.bool(True),
    #################################################
    PythiaParameters = cms.PSet(					       
	pythiaUESettingsBlock,
	processParameters = cms.vstring(
            'MSEL=0            ! User defined processes',
            'MSUB(102)=0       ! gg->H',
            'MSUB(123)=1       ! qq-ZZqq->Hqq',
            'MSUB(124)=1       ! qq-WWqq->Hqq',
	    'PMAS(23,1)=91.188 ! Z mass',
	    'PMAS(24,1)=80.450 ! W mass',
	    'PMAS(25,1)=150.0  ! mass of Higgs',
# Higgs boson decays
            'MDME(210,1)=0    ! Higgs decay into dd', 		       
            'MDME(211,1)=0    ! Higgs decay into uu', 		       
            'MDME(212,1)=0    ! Higgs decay into ss', 		       
            'MDME(213,1)=0    ! Higgs decay into cc', 		       
            'MDME(214,1)=0    ! Higgs decay into bb', 		       
            'MDME(215,1)=0    ! Higgs decay into tt', 		       
            'MDME(216,1)=0    ! Higgs decay into', 		       
            'MDME(217,1)=0    ! Higgs decay into Higgs decay', 	       
            'MDME(218,1)=0    ! Higgs decay into e e', 	       
            'MDME(219,1)=0    ! Higgs decay into mu mu', 
            'MDME(220,1)=0    ! Higgs decay into tau tau', 	       
            'MDME(221,1)=0    ! Higgs decay into Higgs decay', 	       
            'MDME(222,1)=0    ! Higgs decay into g g', 		       
            'MDME(223,1)=0    ! Higgs decay into gam gam', 	       
            'MDME(224,1)=0    ! Higgs decay into gam Z', 	       
            'MDME(225,1)=0    ! Higgs decay into Z Z', 		       
# Higgs->WW
            'MDME(226,1)=1    ! Higgs decay into W W',
# W boson decays
            'MDME(190,1)=4    ! W decay into dbar u', 
            'MDME(191,1)=4    ! W decay into dbar c', 
            'MDME(192,1)=4    ! W decay into dbar t', 
            'MDME(194,1)=4    ! W decay into sbar u', 
            'MDME(195,1)=4    ! W decay into sbar c', 
            'MDME(196,1)=4    ! W decay into sbar t', 
            'MDME(198,1)=4    ! W decay into bbar u', 
            'MDME(199,1)=4    ! W decay into bbar c', 
            'MDME(200,1)=4    ! W decay into bbar t', 
            'MDME(206,1)=5    ! W decay into e+ nu_e', 
            'MDME(207,1)=5    ! W decay into mu+ nu_mu', 
            'MDME(208,1)=5    ! W decay into tau+ nu_tau', ),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 'processParameters')
    )									       
)									       
configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string('$Source: /local/projects/CMSSW/rep/CMSSW/Configuration/GenProduction/python/PYTHIA6_Tauola_SM_VBF_H_WW_lnu2jets_mH150_10TeV_cff.py,v $'),
    annotation = cms.untracked.string('PYTHIA6 Tauola SM VBF H->WW->l nu 2jets at 10TeV with mH=150 GeV')
)