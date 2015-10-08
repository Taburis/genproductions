import FWCore.ParameterSet.Config as cms


### if you want to keep the reco::GenParticle information instead of using it from HepMC,
### you can include these next few lines
process.output.outputCommands.append('keep recoGenParticles_*_*_*')


process.genParticles = cms.EDProducer("GenParticleProducer",
                          src = cms.InputTag("generator")
)

process.generator = cms.EDFilter("AMPTGeneratorFilter",
                                 diquarky = cms.double(0.0),
                                 diquarkx = cms.double(0.0),
                                 diquarkpx = cms.double(7.0),
                                 ntmax = cms.int32(150),
                                 dpcoal = cms.double(1000000.0),
                                 diquarkembedding = cms.int32(0),
                                 maxmiss = cms.int32(1000),
                                 ktkick = cms.int32(1),
                                 mu = cms.double(2.265),
                                 quenchingpar = cms.double(2.0),
                                 popcornpar = cms.double(1.0),
                                 drcoal = cms.double(1000000.0),
                                 amptmode = cms.int32(4), 
                                 izpc = cms.int32(0),
                                 popcornmode = cms.bool(True),
                                 minijetpt = cms.double(-7.0),
                                 ks0decay = cms.bool(False),
                                 alpha = cms.double(0.33),
                                 dt = cms.double(0.2),
                                 rotateEventPlane = cms.bool(True),
                                 shadowingmode = cms.bool(True),
                                 diquarkpy = cms.double(0.0),
                                 deuteronfactor = cms.int32(1),
                                 stringFragB = cms.double(0.15),
                                 quenchingmode = cms.bool(False),
                                 stringFragA = cms.double(0.55),
                                 deuteronmode = cms.int32(0),
                                 doInitialAndFinalRadiation = cms.int32(3),
                                 phidecay = cms.bool(True),
                                 deuteronxsec = cms.int32(1),
                                 pthard = cms.double(2.0),
                                 firstRun = cms.untracked.uint32(1),
                                 frame = cms.string('CMS'),
                                 targ = cms.string('A'),
                                 izp = cms.int32(82),
                                 bMin = cms.double(0),
                                 firstEvent = cms.untracked.uint32(1),
                                 izt = cms.int32(82),
                                 proj = cms.string('A'),
                                 comEnergy = cms.double(5020.0),
                                 iat = cms.int32(208),
                                 bMax = cms.double(30),
                                 iap = cms.int32(208)
                                 )

