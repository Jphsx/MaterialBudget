# -*- coding: utf-8 -*-
import FWCore.ParameterSet.Config as cms

process = cms.Process("MyNtupleMaker")

### Import real conditions
from Configuration.StandardSequences.FrontierConditions_GlobalTag_cff import *
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2018_realistic', '')


### Define source
process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_0.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_1.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_10.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_100.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_102.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_103.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_104.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_105.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_106.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_107.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_108.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_109.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_11.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_110.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_111.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_112.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_114.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_115.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_116.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_117.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_118.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_119.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_12.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_120.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_121.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_122.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_123.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_124.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_125.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_126.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_127.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_128.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_129.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_13.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_130.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_131.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_132.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_133.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_134.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_135.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_136.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_137.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_139.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_14.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_140.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_141.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_142.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_143.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_145.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_146.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_147.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_148.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_149.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_15.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_150.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_151.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_152.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_153.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_154.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_155.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_156.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_157.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_158.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_159.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_16.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_160.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_161.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_162.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_163.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_164.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_166.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_167.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_169.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_17.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_170.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_171.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_172.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_173.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_174.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_175.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_176.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_177.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_178.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_179.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_18.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_180.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_181.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_182.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_183.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_184.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_185.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_186.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_187.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_188.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_189.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_19.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_190.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_191.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_192.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_193.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_194.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_195.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_2.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_20.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_21.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_22.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_23.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_24.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_26.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_27.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_28.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_29.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_3.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_30.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_32.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_33.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_34.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_35.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_36.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_37.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_38.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_39.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_4.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_40.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_41.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_43.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_45.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_46.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_47.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_48.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_49.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_5.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_50.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_51.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_52.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_53.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_55.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_57.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_58.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_6.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_61.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_62.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_63.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_64.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_65.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_66.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_67.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_68.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_69.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_7.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_70.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_71.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_72.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_73.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_74.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_75.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_76.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_77.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_78.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_79.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_8.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_80.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_81.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_82.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_83.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_84.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_85.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_86.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_87.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_88.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_89.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_9.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_90.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_91.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_92.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_93.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_94.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_95.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_96.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_97.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_98.root',
'file:/eos/cms/store/group/dpg_tracker_strip/tracker/MaterialBudget/NI/PionGun2018/CMSSW_10_1_6_Pion50GeV_RECO/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_99.root'

  ),
  secondaryFileNames = cms.untracked.vstring(
  )
)


### Define number of events to be processed (-1 means all)
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source.duplicateCheckMode = cms.untracked.string("noDuplicateCheck")

### Define text output
process.MessageLogger = cms.Service("MessageLogger",
  destinations = cms.untracked.vstring('MyNtupleMaker.log'), ### Output filename
    default = cms.untracked.PSet( reportEvery = cms.untracked.int32(10000) ),
)

### Define Ntuplizer
process.MyNtupleMaking = cms.EDAnalyzer("NtupleMakerNuclearInteractions",
#process.MyNtupleMaking = cms.EDAnalyzer("NI",
   RealData  = cms.bool(False),
)

### Root output
process.TFileService = cms.Service("TFileService",
  fileName = cms.string('Ntuple_Pi10GeV_1016.root' )
)

process.out = cms.OutputModule("PoolOutputModule",
  outputCommands = cms.untracked.vstring ('keep *'),
  fileName = cms.untracked.string('myOutputFileMC.root')
)

process.ana_step = cms.Path( process.MyNtupleMaking )

#process.e = cms.EndPath(process.out)

### Schedule definition
#process.schedule = cms.Schedule(process.ana_step, process.e)
process.schedule = cms.Schedule(process.ana_step)
