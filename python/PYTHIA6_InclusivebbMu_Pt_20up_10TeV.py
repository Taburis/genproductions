import FWCore.ParameterSet.Config as cms

from Configuration.GenProduction.PythiaUESettings_cfi import *
source = cms.Source("PythiaSource",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.0025),
    comEnergy = cms.untracked.double(10000.0),
    crossSection = cms.untracked.double(497200000.),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('MSEL=1         ! QCD',
                                        'CKIN(3)=20     ! pthat min.'),
 
       
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)

muFilter = cms.EDFilter("MCSingleParticleFilter",
                             MinPt = cms.untracked.vdouble(5,5),        # > 5 GeV pT
                             MinEta = cms.untracked.vdouble(-2.5,-2.5), # |eta| < 2.5
                             MaxEta = cms.untracked.vdouble(2.5,2.5),
                             ParticleID = cms.untracked.vint32(13,-13), # mu+ or mu-
                             Status = cms.untracked.vint32(1,1)         # final state
)

bbFilter = cms.EDFilter("MCSingleParticleFilter",
                        ParticleID = cms.untracked.vint32(5,-5),
                        Status = cms.untracked.vint32(2,2)
                       )  
configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.3 $'),
    annotation = cms.untracked.string('PYTHIA6-Inclusive bb->mu pthat20up at 10TeV with Muon preselection (pt > 5 |eta| < 2.5)')
)

ProductionFilterSequence = cms.Sequence(bbFilter * muFilter)