# -*- coding: utf-8 -*-
import FWCore.ParameterSet.Config as cms


process = cms.Process('niReRECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('CommonTools.ParticleFlow.EITopPAG_cff')
process.load('Configuration.StandardSequences.AlCaRecoStreams_cff')
process.load('DQMOffline.Configuration.DQMOffline_cff')

### Import real conditions
from Configuration.StandardSequences.FrontierConditions_GlobalTag_cff import *
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')

#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '102X_dataRun2_Prompt_v6', '')

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2018_realistic', '')

#### Additional stuff
##process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
process.load('RecoParticleFlow/PFTracking/particleFlowDisplacedVertex_cff')
process.load('RecoParticleFlow/PFTracking/particleFlowDisplacedVertexCandidate_cff')
process.particleFlowDisplacedVertex.primaryVertexCut = cms.double(1.3)
process.particleFlowDisplacedVertexCandidate.primaryVertexCut = cms.double(1.3)


### Define source
process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
 'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_0.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_1.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_10.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_100.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_101.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_102.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_103.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_104.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_105.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_106.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_107.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_108.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_109.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_11.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_110.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_111.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_112.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_113.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_114.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_115.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_116.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_117.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_118.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_119.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_12.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_120.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_121.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_122.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_123.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_124.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_125.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_126.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_127.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_128.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_129.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_13.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_130.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_131.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_132.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_133.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_134.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_135.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_136.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_137.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_138.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_139.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_14.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_140.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_141.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_142.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_143.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_144.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_145.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_146.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_147.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_148.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_149.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_15.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_150.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_151.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_152.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_153.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_154.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_155.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_156.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_157.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_158.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_159.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_16.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_160.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_161.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_162.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_163.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_164.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_165.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_166.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_167.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_169.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_17.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_170.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_171.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_172.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_173.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_174.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_175.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_176.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_177.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_178.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_179.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_18.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_180.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_181.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_182.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_183.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_184.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_185.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_186.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_187.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_188.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_189.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_19.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_190.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_191.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_192.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_193.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_194.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_195.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_196.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_197.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_198.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_199.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_2.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_20.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_200.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_201.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_202.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_203.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_204.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_205.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_206.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_207.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_208.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_209.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_21.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_210.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_211.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_212.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_213.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_214.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_215.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_216.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_217.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_218.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_219.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_22.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_220.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_221.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_222.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_223.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_224.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_225.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_226.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_227.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_228.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_229.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_23.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_230.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_231.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_232.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_233.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_234.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_235.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_236.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_237.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_238.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_239.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_24.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_240.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_241.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_242.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_243.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_25.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_26.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_27.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_28.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_29.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_3.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_30.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_31.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_32.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_33.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_34.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_35.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_36.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_37.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_38.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_39.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_4.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_40.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_41.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_42.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_43.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_44.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_45.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_46.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_47.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_48.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_49.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_50.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_51.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_52.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_53.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_54.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_55.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_56.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_57.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_58.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_59.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_6.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_60.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_61.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_62.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_63.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_64.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_65.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_66.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_67.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_68.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_69.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_7.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_70.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_71.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_72.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_73.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_74.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_75.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_76.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_77.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_78.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_79.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_8.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_80.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_81.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_82.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_83.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_84.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_85.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_86.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_87.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_88.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_89.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_9.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_90.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_91.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_92.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_93.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_94.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_95.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_96.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_97.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_98.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion100GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_99.root'
  ),
  secondaryFileNames = cms.untracked.vstring(
  )
)

process.options = cms.untracked.PSet(

)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100000) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.source.duplicateCheckMode = cms.untracked.string("noDuplicateCheck")
# Output definition

process.AODoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AOD'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string('file:step_niPFrereco_inAOD.root'),
    outputCommands = process.FEVTEventContent.outputCommands
)


### Define number of events to be processed (-1 means all)
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1001) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#process.source.duplicateCheckMode = cms.untracked.string("noDuplicateCheck")

### Define text output
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
#process.MessageLogger = cms.Service("MessageLogger",
#  destinations = cms.untracked.vstring('MyNtupleMaker.log'), ### Output filename
#    default = cms.untracked.PSet( reportEvery = cms.untracked.int32(1000) ),
#)

### Define Ntuplizer
#process.MyNtupleMaking = cms.EDAnalyzer("NtupleMakerNuclearInteractions",
process.MyNtupleMaking = cms.EDAnalyzer("NtupleMakerPhotonConversions",
   RealData  = cms.bool(False),
)

#### Root output
process.TFileService = cms.Service("TFileService",
  fileName = cms.string("Run2018_iteractive_MCPC.root" )
)

#process.out = cms.OutputModule("PoolOutputModule",
#  outputCommands = cms.untracked.vstring ('keep *'),
#  fileName = cms.untracked.string('myOutputFileMC.root')
#)

# Path and EndPath definitions
process.niReReconstruction_step = cms.Path(process.particleFlowDisplacedVertexCandidate
                                           +process.particleFlowDisplacedVertex
                                           +process.MyNtupleMaking
                                           )

process.AODoutput_step = cms.EndPath(process.AODoutput)
### Schedule definition
process.schedule = cms.Schedule(process.niReReconstruction_step)
#process.schedule = cms.Schedule(process.niReReconstruction_step,process.AODoutput_step)
