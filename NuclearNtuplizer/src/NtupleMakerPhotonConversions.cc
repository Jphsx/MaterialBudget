/* ****************************************** */
/*                                            */
/* Tracker Material with Nuclear Interactions */
/*                                            */
/*               Nicola Pozzobon              */
/*                    2013                    */
/*                                            */
/* ****************************************** */

#include "MaterialBudget/NuclearNtuplizer/interface/NtupleMakerPhotonConversions.h"



/* Constructors and Destructors */
NtupleMakerPhotonConversions::NtupleMakerPhotonConversions( const edm::ParameterSet& )
{

  // data members for consumes:
  recoVertexToken                  = consumes<reco::VertexCollection>(edm::InputTag("offlinePrimaryVertices"));
  addPileupInfoToken               = consumes<std::vector<PileupSummaryInfo>>(edm::InputTag("addPileupInfo"));
  offlineBeamSpotToken             = consumes<reco::BeamSpot>(edm::InputTag("offlineBeamSpot"));
  particleFlowDisplacedVertexToken = consumes< reco::PFDisplacedVertexCollection >(edm::InputTag("particleFlowDisplacedVertex"));

  edm::InputTag trackingParticlesTag ("mix","MergedTrackTruth");
  trackingParticlesToken           = consumes< TrackingVertexCollection > (trackingParticlesTag);

}

/* Begin Job */
void NtupleMakerPhotonConversions::beginJob()
{

  /// Initialize Event Number etc...
  isRealData = true;
  eventNumber = 0;
  runNumber = 0;
  lumiSection = 0;

  /// Initialize Primary Vertices
  numberOfPV = 0;
  PV_x = new std::vector< double >;
  PV_y = new std::vector< double >;
  PV_z = new std::vector< double >;
  PV_xError = new std::vector< double >;
  PV_yError = new std::vector< double >;
  PV_zError = new std::vector< double >;
  PV_isFake = new std::vector< bool >;

  /// Initialize PileUp
  numberOfMC_PUInfo = 0;
  MC_PUInfo_bunchCrossing = new std::vector< unsigned int >;
  MC_PUInfo_numberOfInteractions = new std::vector< unsigned int >;

  /// Initialize BeamSpot
  BS_x = 0;
  BS_y = 0;
  BS_z = 0;
  BS_zSigma = 0;
  BS_dxdy = 0;
  BS_dydz = 0;
  BS_xWidth = 0;
  BS_yWidth = 0;

  /// Initialize Tracking Vertices
  numberOfMC_TrkV = 0;
  MC_TrkV_isNuclearInteraction = new std::vector< bool >;
  MC_TrkV_isKaonDecay = new std::vector< bool >;
  MC_TrkV_isConversion = new std::vector< bool >;
  MC_TrkV_x = new std::vector< double >;
  MC_TrkV_y = new std::vector< double >;
  MC_TrkV_z = new std::vector< double >;
  MC_TrkV_momentumInc_pt = new std::vector< double >;
  MC_TrkV_momentumInc_phi = new std::vector< double >;
  MC_TrkV_momentumInc_theta = new std::vector< double >;
  MC_TrkV_Inc_charge = new std::vector< double >;
  MC_TrkV_Inc_pdgId = new std::vector< int >;
  MC_TrkV_momentumOut_pt = new std::vector< double >;
  MC_TrkV_momentumOut_phi = new std::vector< double >;
  MC_TrkV_momentumOut_theta = new std::vector< double >;
  MC_TrkV_momentumOut_mass = new std::vector< double >;
  MC_TrkV_numberOfChargedParticles_0p2 = new std::vector< unsigned int >;
  MC_TrkV_numberOfChargedParticles_0p5 = new std::vector< unsigned int >;
  MC_TrkV_numberOfChargedParticles_1p0 = new std::vector< unsigned int >;
  MC_TrkV_numberOfChargedParticles_Out0p2 = new std::vector< unsigned int >;
  MC_TrkV_numberOfChargedParticles_Out0p5 = new std::vector< unsigned int >;
  MC_TrkV_numberOfChargedParticles_Out1p0 = new std::vector< unsigned int >;
  MC_TrkV_isAssociatedPF = new std::vector< bool >;
  MC_TrkV_associationPFDVIdx = new std::vector< unsigned int >;
  MC_TrkV_associationPFDV_deltaR2d= new std::vector< double >;
  MC_TrkV_associationPFDV_deltaR3d= new std::vector< double >;
  MC_TrkV_associationPFDV_deltaR3dPerpendicular= new std::vector< double >;
  MC_TrkV_associationPFDV_deltaR3dParallel= new std::vector< double >;
/*
  MC_TrkV_associationDeltaPt = new std::vector< double >;
  MC_TrkV_associationDeltaPhi = new std::vector< double >;
  MC_TrkV_associationDeltaTheta = new std::vector< double >;
  MC_TrkV_associationDeltaX = new std::vector< double >;
  MC_TrkV_associationDeltaY = new std::vector< double >;
  MC_TrkV_associationDeltaZ = new std::vector< double >;
  MC_TrkV_associationIsNuclear = new std::vector< bool >;
  MC_TrkV_associationIsNuclearLoose = new std::vector< bool >;
  MC_TrkV_associationIsNuclearKink = new std::vector< bool >;
  MC_TrkV_associationIsK0 = new std::vector< bool >;
  MC_TrkV_associationIsLambda = new std::vector< bool >;
  MC_TrkV_associationIsLambdaBar = new std::vector< bool >;
  MC_TrkV_associationIsKPlusLoose = new std::vector< bool >;
  MC_TrkV_associationIsKMinusLoose = new std::vector< bool >;
  MC_TrkV_associationIsConversionLoose = new std::vector< bool >;
  MC_TrkV_associationIsLooper = new std::vector< bool >;
  MC_TrkV_associationIsFake = new std::vector< bool >;
  MC_TrkV_associationIsTherePrimaryTrack = new std::vector< bool >;
  MC_TrkV_associationIsThereMergedTrack = new std::vector< bool >;
*/

  /// Initialize Displaced Vertices
  numberOfPFDV = 0;
  PFDV_x = new std::vector< double >;
  PFDV_y = new std::vector< double >;
  PFDV_z = new std::vector< double >;
  PFDV_momentumInc_pt = new std::vector< double >;
  PFDV_Inc_charge = new std::vector< double >;
  PFDV_momentumInc_phi = new std::vector< double >;
  PFDV_momentumInc_theta = new std::vector< double >;
  PFDV_momentumOut_pt = new std::vector< double >;
  PFDV_momentumOut_phi = new std::vector< double >;
  PFDV_momentumOut_theta = new std::vector< double >;
  PFDV_momentumOut_mass = new std::vector< double >;
  PFDV_momentumOut_numberOfTracks = new std::vector< unsigned int >;
  PFDV_numberOfTracks_0p0 = new std::vector< unsigned int >;
  PFDV_numberOfTracks_0p2 = new std::vector< unsigned int >;
  PFDV_numberOfTracks_0p5 = new std::vector< unsigned int >;
  PFDV_numberOfTracks_1p0 = new std::vector< unsigned int >;
  PFDV_numberOfTracks_Out0p0 = new std::vector< unsigned int >;
  PFDV_numberOfTracks_Out0p2 = new std::vector< unsigned int >;
  PFDV_numberOfTracks_Out0p5 = new std::vector< unsigned int >;
  PFDV_numberOfTracks_Out1p0 = new std::vector< unsigned int >;
  PFDV_isNuclear = new std::vector< bool >;
  PFDV_isNuclearLoose = new std::vector< bool >;
  PFDV_isNuclearKink = new std::vector< bool >;
  PFDV_isK0 = new std::vector< bool >;
  PFDV_isLambda = new std::vector< bool >;
  PFDV_isLambdaBar = new std::vector< bool >;
  PFDV_isKPlusLoose = new std::vector< bool >;
  PFDV_isKMinusLoose = new std::vector< bool >;
  PFDV_isConversionLoose = new std::vector< bool >;
  PFDV_isLooper = new std::vector< bool >;
  PFDV_isFake = new std::vector< bool >;
  PFDV_isTherePrimaryTrack = new std::vector< bool >;
  PFDV_isThereMergedTrack = new std::vector< bool >;
  PFDV_isAssociatedMC = new std::vector< bool >;
  PFDV_deltaR3d_Associated = new std::vector< double >;
  PFDV_deltaR2d_Associated = new std::vector< double >;
  PFDV_associationMC_TrkVIdx = new std::vector< unsigned int >;
  PFDV_vTrack_algo = new std::vector< std::vector< int > >;
  PFDV_vTrack_pt = new std::vector< std::vector< double > >;
  PFDV_vTrack_eta = new std::vector< std::vector< double > >;
  PFDV_vTrack_phi = new std::vector< std::vector< double > >;
  PFDV_vTrack_chi2 = new std::vector< std::vector< double > >;
  PFDV_vTrack_normalizedChi2 = new std::vector< std::vector< double > >;
  //PFDV_vTrack_isHighPurity = new std::vector< std::vector< bool > >;
  PFDV_vTrack_rho = new std::vector< std::vector< double > >;
  PFDV_vTrack_numberOfValidHits = new std::vector< std::vector< unsigned int > >;
  PFDV_vTrack_numberOfExpectedOuterHits = new std::vector< std::vector< unsigned int > >;
  PFDV_vTrack_closestDxyPVIdx = new std::vector< std::vector< unsigned int > >;
  PFDV_vTrack_closestDxyPVIdx_dxy = new std::vector< std::vector< double > >;
  PFDV_vTrack_closestDxyPVIdx_dz = new std::vector< std::vector< double > >;
  PFDV_vTrack_closestDzPVIdx = new std::vector< std::vector< unsigned int > >;
  PFDV_vTrack_closestDzPVIdx_dxy = new std::vector< std::vector< double > >;
  PFDV_vTrack_closestDzPVIdx_dz = new std::vector< std::vector< double > >;

  // TFileService
  edm::Service< TFileService > fs;

  /// Tree
  outputTree = fs->make<TTree>("NuclearInteractionsTree","NuclearInteractionsTree");

  /// Branches for Event Number etc...
  outputTree->Branch( "isRealData", &isRealData, "isRealData/O" ); // O = boolean Bool_t
  outputTree->Branch( "eventNumber", &eventNumber, "eventNumber/i" ); // i = 32 bit unsigned int UInt_t
  outputTree->Branch( "runNumber", &runNumber, "runNumber/i" );
  outputTree->Branch( "lumiSection", &lumiSection, "lumiSection/i" );

  /// Branches for Primary Vertices
  outputTree->Branch( "numberOfPV", &numberOfPV, "numberOfPV/i" );
  outputTree->Branch( "PV_x", "std::vector< double >", &PV_x );
  outputTree->Branch( "PV_y", "std::vector< double >", &PV_y );
  outputTree->Branch( "PV_z", "std::vector< double >", &PV_z );
  outputTree->Branch( "PV_xError", "std::vector< double >", &PV_xError );
  outputTree->Branch( "PV_yError", "std::vector< double >", &PV_yError );
  outputTree->Branch( "PV_zError", "std::vector< double >", &PV_zError );
  outputTree->Branch( "PV_isFake", "std::vector< bool >", &PV_isFake );

  /// Branches for PileUp
  outputTree->Branch( "numberOfMC_PUInfo", &numberOfMC_PUInfo, "numberOfMC_PUInfo/i" );
  outputTree->Branch( "MC_PUInfo_bunchCrossing", "std::vector< unsigned int >", &MC_PUInfo_bunchCrossing );
  outputTree->Branch( "MC_PUInfo_numberOfInteractions", "std::vector< unsigned int >", MC_PUInfo_numberOfInteractions );

  /// Branches for BeamSpot
  outputTree->Branch( "BS_x", &BS_x, "BS_x/D" ); // D = 64 bit floating point Double_t
  outputTree->Branch( "BS_y", &BS_y, "BS_y/D" );
  outputTree->Branch( "BS_z", &BS_z, "BS_z/D" );
  outputTree->Branch( "BS_zSigma", &BS_zSigma, "BS_zSigma/D" );
  outputTree->Branch( "BS_dxdy", &BS_dxdy, "BS_dxdy/D" );
  outputTree->Branch( "BS_dydz", &BS_dydz, "BS_dydz/D" );
  outputTree->Branch( "BS_xWidth", &BS_xWidth, "BS_xWidth/D" );
  outputTree->Branch( "BS_yWidth", &BS_yWidth, "BS_yWidth/D" );

  /// Branches for Tracking Vertices
  outputTree->Branch( "numberOfMC_TrkV", &numberOfMC_TrkV, "numberOfMC_TrkV/i" );
  outputTree->Branch( "MC_TrkV_isNuclearInteraction", "std::vector< bool >", &MC_TrkV_isNuclearInteraction );
  outputTree->Branch( "MC_TrkV_isKaonDecay", "std::vector< bool >", &MC_TrkV_isKaonDecay );
  outputTree->Branch( "MC_TrkV_isConversion", "std::vector< bool >", &MC_TrkV_isConversion );
  outputTree->Branch( "MC_TrkV_x", "std::vector< double >", &MC_TrkV_x );
  outputTree->Branch( "MC_TrkV_y", "std::vector< double >", &MC_TrkV_y );
  outputTree->Branch( "MC_TrkV_z", "std::vector< double >", &MC_TrkV_z );
  outputTree->Branch( "MC_TrkV_momentumInc_pt", "std::vector< double >", &MC_TrkV_momentumInc_pt );
  outputTree->Branch( "MC_TrkV_Inc_charge", "std::vector< double >", &MC_TrkV_Inc_charge );
  outputTree->Branch( "MC_TrkV_Inc_pdgId", "std::vector< int >", &MC_TrkV_Inc_pdgId );
  outputTree->Branch( "MC_TrkV_momentumInc_phi", "std::vector< double >", &MC_TrkV_momentumInc_phi );
  outputTree->Branch( "MC_TrkV_momentumInc_theta", "std::vector< double >", &MC_TrkV_momentumInc_theta );
  outputTree->Branch( "MC_TrkV_momentumOut_pt", "std::vector< double >", &MC_TrkV_momentumOut_pt );
  outputTree->Branch( "MC_TrkV_momentumOut_phi", "std::vector< double >", &MC_TrkV_momentumOut_phi );
  outputTree->Branch( "MC_TrkV_momentumOut_theta", "std::vector< double >", &MC_TrkV_momentumOut_theta );
  outputTree->Branch( "MC_TrkV_momentumOut_mass", "std::vector< double >", &MC_TrkV_momentumOut_mass );
  outputTree->Branch( "MC_TrkV_numberOfChargedParticles_0p2", "std::vector< unsigned int >", &MC_TrkV_numberOfChargedParticles_0p2 );
  outputTree->Branch( "MC_TrkV_numberOfChargedParticles_0p5", "std::vector< unsigned int >", &MC_TrkV_numberOfChargedParticles_0p5 );
  outputTree->Branch( "MC_TrkV_numberOfChargedParticles_1p0", "std::vector< unsigned int >", &MC_TrkV_numberOfChargedParticles_1p0 );
  outputTree->Branch( "MC_TrkV_numberOfChargedParticles_Out0p2", "std::vector< unsigned int >", &MC_TrkV_numberOfChargedParticles_Out0p2 );
  outputTree->Branch( "MC_TrkV_numberOfChargedParticles_Out0p5", "std::vector< unsigned int >", &MC_TrkV_numberOfChargedParticles_Out0p5 );
  outputTree->Branch( "MC_TrkV_numberOfChargedParticles_Out1p0", "std::vector< unsigned int >", &MC_TrkV_numberOfChargedParticles_Out1p0 );
  outputTree->Branch( "MC_TrkV_isAssociatedPF", "std::vector< bool >", &MC_TrkV_isAssociatedPF );
  outputTree->Branch( "MC_TrkV_associationPFDVIdx", "std::vector< unsigned int >", &MC_TrkV_associationPFDVIdx );
  outputTree->Branch( "MC_TrkV_associationPFDV_deltaR2d", "std::vector< double >", &MC_TrkV_associationPFDV_deltaR2d );
  outputTree->Branch( "MC_TrkV_associationPFDV_deltaR3d", "std::vector< double >", &MC_TrkV_associationPFDV_deltaR3d );
  outputTree->Branch( "MC_TrkV_associationPFDV_deltaR3dPerpendicular", "std::vector< double >", &MC_TrkV_associationPFDV_deltaR3dPerpendicular );
  outputTree->Branch( "MC_TrkV_associationPFDV_deltaR3dParallel", "std::vector< double >", &MC_TrkV_associationPFDV_deltaR3dParallel );
/*
  outputTree->Branch( "MC_TrkV_associationDeltaPt", "std::vector< double >", &MC_TrkV_associationDeltaPt );
  outputTree->Branch( "MC_TrkV_associationDeltaPhi", "std::vector< double >", &MC_TrkV_associationDeltaPhi );
  outputTree->Branch( "MC_TrkV_associationDeltaTheta", "std::vector< double >", &MC_TrkV_associationDeltaTheta );
  outputTree->Branch( "MC_TrkV_associationDeltaX", "std::vector< double >", &MC_TrkV_associationDeltaX );
  outputTree->Branch( "MC_TrkV_associationDeltaY", "std::vector< double >", &MC_TrkV_associationDeltaY );
  outputTree->Branch( "MC_TrkV_associationDeltaZ", "std::vector< double >", &MC_TrkV_associationDeltaZ );
  outputTree->Branch( "MC_TrkV_associationIsNuclear", "std::vector< bool >", &MC_TrkV_associationIsNuclear );
  outputTree->Branch( "MC_TrkV_associationIsNuclearLoose", "std::vector< bool >", &MC_TrkV_associationIsNuclearLoose );
  outputTree->Branch( "MC_TrkV_associationIsNuclearKink", "std::vector< bool >", &MC_TrkV_associationIsNuclearKink );
  outputTree->Branch( "MC_TrkV_associationIsK0", "std::vector< bool >", &MC_TrkV_associationIsK0 );
  outputTree->Branch( "MC_TrkV_associationIsLambda", "std::vector< bool >", &MC_TrkV_associationIsLambda );
  outputTree->Branch( "MC_TrkV_associationIsLambdaBar", "std::vector< bool >", &MC_TrkV_associationIsLambdaBar );
  outputTree->Branch( "MC_TrkV_associationIsKPlusLoose", "std::vector< bool >", &MC_TrkV_associationIsKPlusLoose );
  outputTree->Branch( "MC_TrkV_associationIsKMinusLoose", "std::vector< bool >", &MC_TrkV_associationIsKMinusLoose );
  outputTree->Branch( "MC_TrkV_associationIsConversionLoose", "std::vector< bool >", &MC_TrkV_associationIsConversionLoose );
  outputTree->Branch( "MC_TrkV_associationIsLooper", "std::vector< bool >", &MC_TrkV_associationIsLooper );
  outputTree->Branch( "MC_TrkV_associationIsFake", "std::vector< bool >", &MC_TrkV_associationIsFake );
  outputTree->Branch( "MC_TrkV_associationIsTherePrimaryTrack", "std::vector< bool >", &MC_TrkV_associationIsTherePrimaryTrack );
  outputTree->Branch( "MC_TrkV_associationIsThereMergedTrack", "std::vector< bool >", &MC_TrkV_associationIsThereMergedTrack );
*/

  /// Branches for Displaced Vertices
  outputTree->Branch( "numberOfPFDV", &numberOfPFDV, "numberOfPFDV/i" );
  outputTree->Branch( "PFDV_x", "std::vector< double >", &PFDV_x );
  outputTree->Branch( "PFDV_y", "std::vector< double >", &PFDV_y );
  outputTree->Branch( "PFDV_z", "std::vector< double >", &PFDV_z );
  outputTree->Branch( "PFDV_momentumInc_pt", "std::vector< double >", &PFDV_momentumInc_pt );
  outputTree->Branch( "PFDV_Inc_charge", "std::vector< double >", &PFDV_Inc_charge );
  outputTree->Branch( "PFDV_momentumInc_phi", "std::vector< double >", &PFDV_momentumInc_phi );
  outputTree->Branch( "PFDV_momentumInc_theta", "std::vector< double >", &PFDV_momentumInc_theta );
  outputTree->Branch( "PFDV_momentumOut_pt", "std::vector< double >", &PFDV_momentumOut_pt );
  outputTree->Branch( "PFDV_momentumOut_phi", "std::vector< double >", &PFDV_momentumOut_phi );
  outputTree->Branch( "PFDV_momentumOut_theta", "std::vector< double >", &PFDV_momentumOut_theta );
  outputTree->Branch( "PFDV_momentumOut_mass", "std::vector< double >", &PFDV_momentumOut_mass );
  outputTree->Branch( "PFDV_momentumOut_numberOfTracks", "std::vector< unsigned int >", &PFDV_momentumOut_numberOfTracks );
  outputTree->Branch( "PFDV_numberOfTracks_0p0", "std::vector< unsigned int >", &PFDV_numberOfTracks_0p0 );
  outputTree->Branch( "PFDV_numberOfTracks_0p2", "std::vector< unsigned int >", &PFDV_numberOfTracks_0p2 );
  outputTree->Branch( "PFDV_numberOfTracks_0p5", "std::vector< unsigned int >", &PFDV_numberOfTracks_0p5 );
  outputTree->Branch( "PFDV_numberOfTracks_1p0", "std::vector< unsigned int >", &PFDV_numberOfTracks_1p0 );
  outputTree->Branch( "PFDV_numberOfTracks_Out0p0", "std::vector< unsigned int >", &PFDV_numberOfTracks_Out0p0 );
  outputTree->Branch( "PFDV_numberOfTracks_Out0p2", "std::vector< unsigned int >", &PFDV_numberOfTracks_Out0p2 );
  outputTree->Branch( "PFDV_numberOfTracks_Out0p5", "std::vector< unsigned int >", &PFDV_numberOfTracks_Out0p5 );
  outputTree->Branch( "PFDV_numberOfTracks_Out1p0", "std::vector< unsigned int >", &PFDV_numberOfTracks_Out1p0 );
  outputTree->Branch( "PFDV_isNuclear", "std::vector< bool >", &PFDV_isNuclear );
  outputTree->Branch( "PFDV_isNuclearLoose", "std::vector< bool >", &PFDV_isNuclearLoose );
  outputTree->Branch( "PFDV_isNuclearKink", "std::vector< bool >", &PFDV_isNuclearKink );
  outputTree->Branch( "PFDV_isK0", "std::vector< bool >", &PFDV_isK0 );
  outputTree->Branch( "PFDV_isLambda", "std::vector< bool >", &PFDV_isLambda );
  outputTree->Branch( "PFDV_isLambdaBar", "std::vector< bool >", &PFDV_isLambdaBar );
  outputTree->Branch( "PFDV_isKPlusLoose", "std::vector< bool >", &PFDV_isKPlusLoose );
  outputTree->Branch( "PFDV_isKMinusLoose", "std::vector< bool >", &PFDV_isKMinusLoose );
  outputTree->Branch( "PFDV_isConversionLoose", "std::vector< bool >", &PFDV_isConversionLoose );
  outputTree->Branch( "PFDV_isLooper", "std::vector< bool >", &PFDV_isLooper );
  outputTree->Branch( "PFDV_isFake", "std::vector< bool >", &PFDV_isFake );
  outputTree->Branch( "PFDV_isTherePrimaryTrack", "std::vector< bool >", &PFDV_isTherePrimaryTrack );
  outputTree->Branch( "PFDV_isThereMergedTrack", "std::vector< bool >", &PFDV_isThereMergedTrack );
  outputTree->Branch( "PFDV_isAssociatedMC", "std::vector< bool >", &PFDV_isAssociatedMC );
  outputTree->Branch( "PFDV_deltaR3d_Associated", "std::vector< double >", &PFDV_deltaR3d_Associated );
  outputTree->Branch( "PFDV_deltaR2d_Associated", "std::vector< double >", &PFDV_deltaR2d_Associated );
  outputTree->Branch( "PFDV_associationMC_TrkVIdx", "std::vector< unsigned int >", &PFDV_associationMC_TrkVIdx );
  outputTree->Branch( "PFDV_vTrack_algo", "std::vector< std::vector< int > >", &PFDV_vTrack_algo );
  outputTree->Branch( "PFDV_vTrack_pt", "std::vector< std::vector< double > >", &PFDV_vTrack_pt );
  outputTree->Branch( "PFDV_vTrack_eta", "std::vector< std::vector< double > >", &PFDV_vTrack_eta );
  outputTree->Branch( "PFDV_vTrack_phi", "std::vector< std::vector< double > >", &PFDV_vTrack_phi );
  outputTree->Branch( "PFDV_vTrack_chi2", "std::vector< std::vector< double > >", &PFDV_vTrack_chi2 );
  outputTree->Branch( "PFDV_vTrack_normalizedChi2", "std::vector< std::vector< double > >", &PFDV_vTrack_normalizedChi2 );
  outputTree->Branch( "PFDV_vTrack_rho", "std::vector< std::vector< double > >", &PFDV_vTrack_rho );
  outputTree->Branch( "PFDV_vTrack_numberOfValidHits", "std::vector< std::vector< unsigned int > >", &PFDV_vTrack_numberOfValidHits );
  outputTree->Branch( "PFDV_vTrack_numberOfExpectedOuterHits", "std::vector< std::vector< unsigned int > >", &PFDV_vTrack_numberOfExpectedOuterHits );
  outputTree->Branch( "PFDV_vTrack_closestDxyPVIdx", "std::vector< std::vector< unsigned int > >", &PFDV_vTrack_closestDxyPVIdx );
  outputTree->Branch( "PFDV_vTrack_closestDxyPVIdx_dxy", "std::vector< std::vector< double > >", &PFDV_vTrack_closestDxyPVIdx_dxy );
  outputTree->Branch( "PFDV_vTrack_closestDxyPVIdx_dz", "std::vector< std::vector< double > >", &PFDV_vTrack_closestDxyPVIdx_dz );
  outputTree->Branch( "PFDV_vTrack_closestDzPVIdx", "std::vector< std::vector< unsigned int > >", &PFDV_vTrack_closestDzPVIdx );
  outputTree->Branch( "PFDV_vTrack_closestDzPVIdx_dxy", "std::vector< std::vector< double > >", &PFDV_vTrack_closestDzPVIdx_dxy );
  outputTree->Branch( "PFDV_vTrack_closestDzPVIdx_dz", "std::vector< std::vector< double > >", &PFDV_vTrack_closestDzPVIdx_dz );
  //outputTree->Branch( "PFDV_vTrack_isHighPurity", "std::vector< std::vector< bool > >", &PFDV_vTrack_isHighPurity );
}

/* End Job */
void NtupleMakerPhotonConversions::endJob()
{

}

/* Analyze */
void NtupleMakerPhotonConversions::analyze( const edm::Event& iEvent, const edm::EventSetup& iSetup )
{
  /// Get Event Number etc...
  isRealData = iEvent.isRealData();
  eventNumber = iEvent.id().event();
  runNumber = iEvent.run();
  lumiSection = iEvent.id().luminosityBlock();
  //std::cout << "*** TEST: runNumber = " << runNumber  << " eventNumber = " << eventNumber << std::endl;

  /// Prepare Primary Vertices
  PV_x->clear();
  PV_y->clear();
  PV_z->clear();
  PV_xError->clear();
  PV_yError->clear();
  PV_zError->clear();
  PV_isFake->clear();

  /// Get Primary Vertices
  edm::Handle< reco::VertexCollection > primaryVerticesHandle;
  //iEvent.getByLabel( "offlinePrimaryVertices", primaryVerticesHandle );
  iEvent.getByToken( recoVertexToken, primaryVerticesHandle );

  numberOfPV = primaryVerticesHandle->size();

  for ( unsigned int i = 0; i < primaryVerticesHandle->size(); i++ )
  {
    PV_x->push_back( primaryVerticesHandle->at(i).x() );
    PV_y->push_back( primaryVerticesHandle->at(i).y() );
    PV_z->push_back( primaryVerticesHandle->at(i).z() );
    PV_xError->push_back( primaryVerticesHandle->at(i).xError() );
    PV_yError->push_back( primaryVerticesHandle->at(i).yError() );
    PV_zError->push_back( primaryVerticesHandle->at(i).zError() );
    PV_isFake->push_back( primaryVerticesHandle->at(i).isFake() );
  }

  /// Prepare PileUp
  MC_PUInfo_bunchCrossing->clear();
  MC_PUInfo_numberOfInteractions->clear();
  if ( !isRealData )
  {
    /// Get PileUp
    edm::Handle< std::vector< PileupSummaryInfo > > pileUpInfoHandle;
    //iEvent.getByLabel( edm::InputTag("addPileupInfo"), pileUpInfoHandle );
    iEvent.getByToken( addPileupInfoToken, pileUpInfoHandle );

    numberOfMC_PUInfo = pileUpInfoHandle->size();

    for ( unsigned int i = 0; i < pileUpInfoHandle->size(); i++ )
    {
      MC_PUInfo_bunchCrossing->push_back( pileUpInfoHandle->at(i).getBunchCrossing() );
      MC_PUInfo_numberOfInteractions->push_back( pileUpInfoHandle->at(i).getPU_NumInteractions() );
    }
  }

  /// Get BeamSpot
  edm::Handle< reco::BeamSpot > beamSpotHandle;
  //iEvent.getByLabel( "offlineBeamSpot", beamSpotHandle );
  iEvent.getByToken( offlineBeamSpotToken, beamSpotHandle );

  if ( beamSpotHandle.isValid() )
  {
    reco::BeamSpot beamSpot = *beamSpotHandle;

    BS_x = beamSpot.x0();
    BS_y = beamSpot.y0();
    BS_z = beamSpot.z0();
    BS_zSigma = beamSpot.sigmaZ();
    BS_dxdy = beamSpot.dxdz();
    BS_dydz = beamSpot.dydz();
    BS_xWidth = beamSpot.BeamWidthX();
    BS_yWidth = beamSpot.BeamWidthY();
  }

  /// Prepare for PF stuff
  /// Get PF Displaced vertices
  edm::Handle< reco::PFDisplacedVertexCollection > displacedVtxHandle;
  //iEvent.getByLabel( edm::InputTag("particleFlowDisplacedVertex"), displacedVtxHandle );
  iEvent.getByToken( particleFlowDisplacedVertexToken, displacedVtxHandle );

  /// Prepare for MC stuff
  MC_TrkV_isNuclearInteraction->clear();
  MC_TrkV_isKaonDecay->clear();
  MC_TrkV_isConversion->clear();
  MC_TrkV_x->clear();
  MC_TrkV_y->clear();
  MC_TrkV_z->clear();
  MC_TrkV_momentumInc_pt->clear();
  MC_TrkV_Inc_charge->clear();
  MC_TrkV_Inc_pdgId->clear();
  MC_TrkV_momentumInc_phi->clear();
  MC_TrkV_momentumInc_theta->clear();
  MC_TrkV_momentumOut_pt->clear();
  MC_TrkV_momentumOut_phi->clear();
  MC_TrkV_momentumOut_theta->clear();
  MC_TrkV_momentumOut_mass->clear();
  MC_TrkV_numberOfChargedParticles_0p2->clear();
  MC_TrkV_numberOfChargedParticles_0p5->clear();
  MC_TrkV_numberOfChargedParticles_1p0->clear();
  MC_TrkV_numberOfChargedParticles_Out0p2->clear();
  MC_TrkV_numberOfChargedParticles_Out0p5->clear();
  MC_TrkV_numberOfChargedParticles_Out1p0->clear();
  MC_TrkV_isAssociatedPF->clear();
  MC_TrkV_associationPFDVIdx->clear();
  MC_TrkV_associationPFDV_deltaR2d->clear();
  MC_TrkV_associationPFDV_deltaR3d->clear();
  MC_TrkV_associationPFDV_deltaR3dPerpendicular->clear();
  MC_TrkV_associationPFDV_deltaR3dParallel->clear();
/*
  MC_TrkV_associationDeltaPt->clear();
  MC_TrkV_associationDeltaPhi->clear();
  MC_TrkV_associationDeltaTheta->clear();
  MC_TrkV_associationDeltaX->clear();
  MC_TrkV_associationDeltaY->clear();
  MC_TrkV_associationDeltaZ->clear();
  MC_TrkV_associationIsNuclear->clear();
  MC_TrkV_associationIsNuclearLoose->clear();
  MC_TrkV_associationIsNuclearKink->clear();
  MC_TrkV_associationIsK0->clear();
  MC_TrkV_associationIsLambda->clear();
  MC_TrkV_associationIsLambdaBar->clear();
  MC_TrkV_associationIsKPlusLoose->clear();
  MC_TrkV_associationIsKMinusLoose->clear();
  MC_TrkV_associationIsConversionLoose->clear();
  MC_TrkV_associationIsLooper->clear();
  MC_TrkV_associationIsFake->clear();
  MC_TrkV_associationIsTherePrimaryTrack->clear();
  MC_TrkV_associationIsThereMergedTrack->clear();
*/
  /// Get Tracking Vertices
  edm::Handle< TrackingVertexCollection > trackingVtxHandle;

  bool isGoodSimulation = false;
  if ( !isRealData )
    //isGoodSimulation = iEvent.getByLabel( "mix", "MergedTrackTruth", trackingVtxHandle );
    isGoodSimulation = iEvent.getByToken( trackingParticlesToken, trackingVtxHandle );

  if ( isGoodSimulation )
  {
    numberOfMC_TrkV = 0;

    for ( unsigned int i = 0; i < trackingVtxHandle->size(); i++ )
    {
      TrackingVertex thisVtx = trackingVtxHandle->at(i);

      /// Check the Vertex is Nucl Int
      if ( thisVtx.nSourceTracks() < 1 )
        continue;

      bool isThisNuclearInteraction = isNuclearInteraction( thisVtx );
      bool isThisKaonDecay = isKaonDecay( thisVtx );
      bool isThisConversion = isConversion( thisVtx );

      // select only Nuclear Interection vertex candicate
      //if ( !isThisNuclearInteraction && !isThisKaonDecay && !isThisConversion )
      if ( !isThisNuclearInteraction )
        continue;

      numberOfMC_TrkV++;
      MC_TrkV_isNuclearInteraction->push_back( isThisNuclearInteraction );
      MC_TrkV_isKaonDecay->push_back( isThisKaonDecay );
      MC_TrkV_isConversion->push_back( isThisConversion );

      /// Inbound and outbound momenta
      math::XYZVectorD thisSimMomentumInc = (*thisVtx.sourceTracks_begin())->momentum();
      math::XYZTLorentzVectorD thisSimMomentumOut( 0, 0, 0, 0 );

      unsigned int nTrackingParticles_0p2 = 0;
      unsigned int nTrackingParticles_0p5 = 0;
      unsigned int nTrackingParticles_1p0 = 0;
      unsigned int nTrackingParticles_Out0p2 = 0;
      unsigned int nTrackingParticles_Out0p5 = 0;
      unsigned int nTrackingParticles_Out1p0 = 0;
      TrackingParticleRefVector::iterator trackDaughter;
      for ( trackDaughter = thisVtx.daughterTracks_begin();
            trackDaughter != thisVtx.daughterTracks_end();
            ++trackDaughter )
      {
        if ( (*trackDaughter)->charge() == 0 ) //reject neutral particles
        continue;

        if ( fabs((*trackDaughter)->eta()) > 2.5 ) //reject particle out of detector acceptence in eta
        continue;

        if( (*trackDaughter)->pt() > 0.2 ){
        thisSimMomentumOut += (*trackDaughter)->p4();
        nTrackingParticles_0p2++;
        nTrackingParticles_Out0p2++;
        }
        if( (*trackDaughter)->pt() > 0.5 ){
        nTrackingParticles_0p5++;
        nTrackingParticles_Out0p5++;
        }
        if( (*trackDaughter)->pt() > 1.0 ){
        nTrackingParticles_1p0++;
        nTrackingParticles_Out1p0++;
        }
      }

      MC_TrkV_x->push_back( thisVtx.position().x() );
      MC_TrkV_y->push_back( thisVtx.position().y() );
      MC_TrkV_z->push_back( thisVtx.position().z() );
      MC_TrkV_momentumInc_pt->push_back( sqrt( thisSimMomentumInc.Perp2() ) );
      MC_TrkV_momentumInc_phi->push_back( thisSimMomentumInc.Phi() );
      MC_TrkV_momentumInc_theta->push_back( thisSimMomentumInc.Theta() );
      MC_TrkV_momentumOut_pt->push_back( sqrt( thisSimMomentumOut.Perp2() ) );
      MC_TrkV_momentumOut_phi->push_back( thisSimMomentumOut.Phi() );
      MC_TrkV_momentumOut_theta->push_back( thisSimMomentumOut.Theta() );
      MC_TrkV_momentumOut_mass->push_back( thisSimMomentumOut.mass() );


      //calculate Radius of Sim vertex
      double R_SimVer = sqrt( thisVtx.position().x()*thisVtx.position().x() + thisVtx.position().y()*thisVtx.position().y() );

      int NumberOfPrimaryTracks = 0;
      double Source_Charge = -10;
      int Source_pdgId = 0;
   
      TrackingParticleRefVector::iterator trackSource;
      for ( trackSource = thisVtx.sourceTracks_begin();
            trackSource != thisVtx.sourceTracks_end();
            ++trackSource )
      {
        NumberOfPrimaryTracks++;
        //std::cout << "PDG ID of Primary Particle = " << (*trackSource)->pdgId() << std::endl;
        Source_Charge = (*trackSource)->charge();
        Source_pdgId = (*trackSource)->pdgId();

        if ( (*trackSource)->charge() == 0 )
        continue;
        // request  R_SimVer > 12. to have possibity to reconstruct charged tracker at least at Pixel region
        if( (*trackSource)->pt() > 0.2 && R_SimVer > 12. ) nTrackingParticles_0p2++;
        if( (*trackSource)->pt() > 0.5 && R_SimVer > 12.) nTrackingParticles_0p5++;
        if( (*trackSource)->pt() > 1.0 && R_SimVer > 12.) nTrackingParticles_1p0++;
      }
      if( NumberOfPrimaryTracks != 1 ) std::cout << " ERROR! CHECK: unusual size for MC of sorce Tracks = " << NumberOfPrimaryTracks << std::endl;
 
      MC_TrkV_numberOfChargedParticles_0p2->push_back( nTrackingParticles_0p2 );
      MC_TrkV_numberOfChargedParticles_0p5->push_back( nTrackingParticles_0p5 );
      MC_TrkV_numberOfChargedParticles_1p0->push_back( nTrackingParticles_1p0 );
      MC_TrkV_numberOfChargedParticles_Out0p2->push_back( nTrackingParticles_Out0p2 );
      MC_TrkV_numberOfChargedParticles_Out0p5->push_back( nTrackingParticles_Out0p5 );
      MC_TrkV_numberOfChargedParticles_Out1p0->push_back( nTrackingParticles_Out1p0 );
      MC_TrkV_Inc_charge->push_back(Source_Charge);
      MC_TrkV_Inc_pdgId->push_back(Source_pdgId);

      double deltaR  = 999;
      double deltaZ  = 999;
      double deltaPt = 999; deltaPt = deltaPt;
      double deltaPhi = 999; deltaPhi = deltaPhi;
      double deltaTheta = 999; deltaTheta = deltaTheta;
      double deltaX = 999;
      double deltaY = 999;

      double distance3D_Ass = 900.; //Start with a big value
      double deltaR_Ass     = 900.; //Start with a big value
      double distance3DParallel_Ass = 900.; //Start with a big value
      double distance3DPerpendicular_Ass = 900.; //Start with a big value
      deltaR_Ass = deltaR_Ass;
   //      bool assoc = false;
      unsigned int iAssociationIndexLast = 0;
      iAssociationIndexLast = iAssociationIndexLast;

      bool foundAssociated = false;

      unsigned int jAssociationCounter = 0;
      unsigned int jAssociationCounterLast = 0;

      /// Match with Particle Flow Displaced Vertices
      for ( unsigned int j = 0; j < displacedVtxHandle->size(); j++ )
      {
        reco::PFDisplacedVertex thisDisplacedVtx = displacedVtxHandle->at(j);

        if ( thisDisplacedVtx.isFake() )
          continue;

        // make assosication only with Nuclear Interection reco vertices
        if ( !(thisDisplacedVtx.isNucl()) )
          continue;

        jAssociationCounter++;

        /// Calculate all possible forms of distance
        const math::XYZTLorentzVector thisRecMomentumInc = thisDisplacedVtx.primaryMomentum("PI", false, 0.0);

        deltaPt = sqrt(thisSimMomentumInc.Perp2()) - sqrt(thisRecMomentumInc.Perp2());
        //deltaPhi = thisSimMomentumInc.Phi() - thisRecMomentumInc.Phi();
        deltaPhi = reco::deltaPhi( thisSimMomentumInc.Phi(), thisRecMomentumInc.Phi() );
        deltaTheta = thisSimMomentumInc.Theta() - thisRecMomentumInc.Theta();
        deltaX = thisVtx.position().x() - thisDisplacedVtx.position().x();
        deltaY = thisVtx.position().y() - thisDisplacedVtx.position().y();
        deltaZ = thisVtx.position().z() - thisDisplacedVtx.position().z();
        deltaR  = sqrt(thisVtx.position().perp2()) - sqrt(thisDisplacedVtx.position().perp2());
        double distance3D = sqrt(deltaX*deltaX + deltaY*deltaY + deltaZ*deltaZ);
        double distance3DPer = VectorPerpendicularR(thisVtx, thisDisplacedVtx); //Sim, PF vextecise
        double distance3DPar = VectorParallelR     (thisVtx, thisDisplacedVtx);


        ///// Apply Selection
        //bool isAssociated = true;
        //// very-very loose cut of 20 cm for future test:
        //if (distance3D > 20.) isAssociated = false;
       // if ( !( ( fabs(thisVtx.position().eta()) < 1.2 && ( deltaR < -1.0 || deltaR > 3.0 ) ) ||
       //         ( fabs(thisVtx.position().eta()) >= 1.2 && ( deltaR < -2.0 || deltaR > 6.0 ) ) ) )
       //   isAssociated = false;

       // else if ( !( ( fabs(thisVtx.position().eta()) < 1.4 && fabs(deltaTheta) > 0.2 ) ||
       //              ( fabs(thisVtx.position().eta()) >= 1.4 && fabs(deltaTheta) > 0.1 ) ) )
       //   isAssociated = false;

       // else if ( !( ( fabs(thisVtx.position().eta()) < 1.4 && fabs(deltaPhi) > 0.04 ) ||
       //              ( fabs(thisVtx.position().eta()) >= 1.4 && fabs(deltaPhi) > 0.08 ) ) )
       //   isAssociated = false;

        //reject if we don't find association or if our new dR is large then previous

        //if ( distance3D < distance3D_Ass ){
        if ( distance3DPer < distance3DPerpendicular_Ass ){
           distance3D_Ass = distance3D;
           foundAssociated = true;
      	   iAssociationIndexLast = j;
           jAssociationCounterLast = jAssociationCounter;
        }
        if (deltaR < deltaR_Ass) deltaR_Ass = deltaR;
        if (distance3DPer < distance3DPerpendicular_Ass) distance3DPerpendicular_Ass = distance3DPer;
        if (distance3DPar < distance3DParallel_Ass) distance3DParallel_Ass = distance3DPar;
      }

      /// Do what is needed in case of association
      if ( foundAssociated )
      {
        MC_TrkV_isAssociatedPF->push_back( true );
        MC_TrkV_associationPFDVIdx->push_back( jAssociationCounterLast ); /// This will match the association in the output ntuple
        MC_TrkV_associationPFDV_deltaR2d->push_back( deltaR_Ass ); /// deltaR 2d: xy
        MC_TrkV_associationPFDV_deltaR3d->push_back( distance3D_Ass ); /// deltaR 3d: xyz
        MC_TrkV_associationPFDV_deltaR3dPerpendicular->push_back( distance3DPerpendicular_Ass ); /// deltaR 3d: Perpendicular to vertex
        MC_TrkV_associationPFDV_deltaR3dParallel->push_back( distance3DParallel_Ass ); /// deltaR 3d: Parallel to vertex

/*
        MC_TrkV_associationDeltaPt->push_back( deltaPt );
        MC_TrkV_associationDeltaPhi->push_back( deltaPhi );
        MC_TrkV_associationDeltaTheta->push_back( deltaTheta );
        MC_TrkV_associationDeltaX->push_back( deltaX );
        MC_TrkV_associationDeltaY->push_back( deltaY );
        MC_TrkV_associationDeltaZ->push_back( deltaZ );

        MC_TrkV_associationIsNuclear->push_back( displacedVtxHandle->at( iAssociationIndexLast ).isNucl() ); 
        MC_TrkV_associationIsNuclearLoose->push_back( displacedVtxHandle->at( iAssociationIndexLast ).isNucl_Loose() );
        MC_TrkV_associationIsNuclearKink->push_back( displacedVtxHandle->at( iAssociationIndexLast ).isNuclKink() );
        MC_TrkV_associationIsK0->push_back( displacedVtxHandle->at( iAssociationIndexLast ).isK0() );
        MC_TrkV_associationIsLambda->push_back( displacedVtxHandle->at( iAssociationIndexLast ).isLambda() );
        MC_TrkV_associationIsLambdaBar->push_back( displacedVtxHandle->at( iAssociationIndexLast ).isLambdaBar() );
        MC_TrkV_associationIsKPlusLoose->push_back( displacedVtxHandle->at( iAssociationIndexLast ).isKplus_Loose() );
        MC_TrkV_associationIsKMinusLoose->push_back( displacedVtxHandle->at( iAssociationIndexLast ).isKminus_Loose() );
        MC_TrkV_associationIsConversionLoose->push_back( displacedVtxHandle->at( iAssociationIndexLast ).isConvLoose() );
        MC_TrkV_associationIsLooper->push_back( displacedVtxHandle->at( iAssociationIndexLast ).isLooper() );
        MC_TrkV_associationIsFake->push_back( displacedVtxHandle->at( iAssociationIndexLast ).isFake() );
        MC_TrkV_associationIsTherePrimaryTrack->push_back( displacedVtxHandle->at( iAssociationIndexLast ).isTherePrimaryTracks() );
        MC_TrkV_associationIsThereMergedTrack->push_back( displacedVtxHandle->at( iAssociationIndexLast ).isThereMergedTracks() );
*/
      }
      else
      {
        MC_TrkV_isAssociatedPF->push_back( false );
        MC_TrkV_associationPFDVIdx->push_back( 0 );
        MC_TrkV_associationPFDV_deltaR2d->push_back( deltaR_Ass ); /// deltaR 2d: xy
        MC_TrkV_associationPFDV_deltaR3d->push_back( distance3D_Ass ); /// deltaR 3d: xyz
        MC_TrkV_associationPFDV_deltaR3dPerpendicular->push_back( distance3DPerpendicular_Ass ); /// deltaR 3d: Perpendicular to vertex
        MC_TrkV_associationPFDV_deltaR3dParallel->push_back( distance3DParallel_Ass ); /// deltaR 3d: Parallel to vertex
/*
        MC_TrkV_associationDeltaPt->push_back( 0.0 );
        MC_TrkV_associationDeltaPhi->push_back( 0.0 );
        MC_TrkV_associationDeltaTheta->push_back( 0.0 );
        MC_TrkV_associationDeltaX->push_back( 0.0 );
        MC_TrkV_associationDeltaY->push_back( 0.0 );
        MC_TrkV_associationDeltaZ->push_back( 0.0 );

        MC_TrkV_associationIsNuclear->push_back( false ); 
        MC_TrkV_associationIsNuclearLoose->push_back( false );
        MC_TrkV_associationIsNuclearKink->push_back( false );
        MC_TrkV_associationIsK0->push_back( false );
        MC_TrkV_associationIsLambda->push_back( false );
        MC_TrkV_associationIsLambdaBar->push_back( false );
        MC_TrkV_associationIsKPlusLoose->push_back( false );
        MC_TrkV_associationIsKMinusLoose->push_back( false );
        MC_TrkV_associationIsConversionLoose->push_back( false );
        MC_TrkV_associationIsLooper->push_back( false );
        MC_TrkV_associationIsFake->push_back( false );
        MC_TrkV_associationIsTherePrimaryTrack->push_back( false );
        MC_TrkV_associationIsThereMergedTrack->push_back( false );
*/
      }
    }
  }

  /// From now on, everything is purely reco

  /// Prepare PF Displaced Vertices
  PFDV_x->clear();
  PFDV_y->clear();
  PFDV_z->clear();
  PFDV_momentumInc_pt->clear();
  PFDV_Inc_charge->clear();
  PFDV_momentumInc_phi->clear();
  PFDV_momentumInc_theta->clear();
  PFDV_momentumOut_pt->clear();
  PFDV_momentumOut_phi->clear();
  PFDV_momentumOut_theta->clear();
  PFDV_momentumOut_mass->clear();
  PFDV_momentumOut_numberOfTracks->clear();
  PFDV_numberOfTracks_0p0->clear();
  PFDV_numberOfTracks_0p2->clear();
  PFDV_numberOfTracks_0p5->clear();
  PFDV_numberOfTracks_1p0->clear();
  PFDV_numberOfTracks_Out0p0->clear();
  PFDV_numberOfTracks_Out0p2->clear();
  PFDV_numberOfTracks_Out0p5->clear();
  PFDV_numberOfTracks_Out1p0->clear();
  PFDV_isNuclear->clear();
  PFDV_isNuclearLoose->clear();
  PFDV_isNuclearKink->clear();
  PFDV_isK0->clear();
  PFDV_isLambda->clear();
  PFDV_isLambdaBar->clear();
  PFDV_isKPlusLoose->clear();
  PFDV_isKMinusLoose->clear();
  PFDV_isConversionLoose->clear();
  PFDV_isLooper->clear();
  PFDV_isFake->clear();
  PFDV_isTherePrimaryTrack->clear();
  PFDV_isThereMergedTrack->clear();
  PFDV_isAssociatedMC->clear();
  PFDV_deltaR3d_Associated->clear();
  PFDV_deltaR2d_Associated->clear();
  PFDV_associationMC_TrkVIdx->clear();
  PFDV_vTrack_algo->clear();
  PFDV_vTrack_pt->clear();
  PFDV_vTrack_eta->clear();
  PFDV_vTrack_phi->clear();
  PFDV_vTrack_chi2->clear();
  PFDV_vTrack_normalizedChi2->clear();
  //PFDV_vTrack_isHighPurity->clear();
  PFDV_vTrack_rho->clear();
  PFDV_vTrack_numberOfValidHits->clear();
  PFDV_vTrack_numberOfExpectedOuterHits->clear();
  PFDV_vTrack_closestDxyPVIdx->clear();
  PFDV_vTrack_closestDxyPVIdx_dxy->clear();
  PFDV_vTrack_closestDxyPVIdx_dz->clear();
  PFDV_vTrack_closestDzPVIdx->clear();
  PFDV_vTrack_closestDzPVIdx_dxy->clear();
  PFDV_vTrack_closestDzPVIdx_dz->clear();

  numberOfPFDV = 0;
  int NumberOfLooseNuclearVertex = 0;
  int NumberOfNuclearVertex = 0;
  bool FlagLess3TracksFromVertex = false; FlagLess3TracksFromVertex = FlagLess3TracksFromVertex; 

  for ( unsigned int i = 0; i < displacedVtxHandle->size(); i++ )
  {
    reco::PFDisplacedVertex thisDisplacedVtx = displacedVtxHandle->at(i);

    if ( thisDisplacedVtx.isFake() )
      continue;
    // select only Nuclear Interection vetices with high quality
    if (!(thisDisplacedVtx.isNucl()) )
      continue;

    numberOfPFDV++;

    PFDV_x->push_back( thisDisplacedVtx.position().x() );
    PFDV_y->push_back( thisDisplacedVtx.position().y() );
    PFDV_z->push_back( thisDisplacedVtx.position().z() );

    /// Inbound and outbound momenta
    const math::XYZTLorentzVector thisRecMomentumInc = thisDisplacedVtx.primaryMomentum("PI", false, 0.0);
    const math::XYZTLorentzVector thisRecMomentumOut = thisDisplacedVtx.secondaryMomentum("PI", true, 0.0);

    PFDV_momentumInc_pt->push_back( sqrt( thisRecMomentumInc.Perp2() ) );
    PFDV_momentumInc_phi->push_back( thisRecMomentumInc.Phi() );
    PFDV_momentumInc_theta->push_back( thisRecMomentumInc.Theta() );
    PFDV_momentumOut_pt->push_back( sqrt( thisRecMomentumOut.Perp2() ) );
    PFDV_momentumOut_phi->push_back( thisRecMomentumOut.Phi() );
    PFDV_momentumOut_theta->push_back( thisRecMomentumOut.Theta() );
    PFDV_momentumOut_mass->push_back( thisRecMomentumOut.mass() );
    PFDV_momentumOut_numberOfTracks->push_back( thisDisplacedVtx.nSecondaryTracks() );

    PFDV_isNuclear->push_back( thisDisplacedVtx.isNucl() ); 
    PFDV_isNuclearLoose->push_back( thisDisplacedVtx.isNucl_Loose() );
    PFDV_isNuclearKink->push_back( thisDisplacedVtx.isNucl_Kink() );
    PFDV_isK0->push_back( thisDisplacedVtx.isK0() );
    PFDV_isLambda->push_back( thisDisplacedVtx.isLambda() );
    PFDV_isLambdaBar->push_back( thisDisplacedVtx.isLambdaBar() );
    PFDV_isKPlusLoose->push_back( thisDisplacedVtx.isKplus_Loose() );
    PFDV_isKMinusLoose->push_back( thisDisplacedVtx.isKminus_Loose() );
    PFDV_isConversionLoose->push_back( thisDisplacedVtx.isConv_Loose() );
    PFDV_isLooper->push_back( thisDisplacedVtx.isLooper() );
    PFDV_isFake->push_back( thisDisplacedVtx.isFake() );
    PFDV_isTherePrimaryTrack->push_back( thisDisplacedVtx.isTherePrimaryTracks() );
    PFDV_isThereMergedTrack->push_back( thisDisplacedVtx.isThereMergedTracks() );

    if(PFDV_isNuclear)NumberOfNuclearVertex++;
    if(PFDV_isNuclearLoose)NumberOfLooseNuclearVertex++;
  
    /// Find association with Tracking Vertices
    double deltaR  = 999;
    double deltaZ  = 999;
    double deltaPt = 999;  deltaPt =  deltaPt;
    double deltaPhi = 999; deltaPhi = deltaPhi;
    double deltaTheta = 999; deltaTheta = deltaTheta;
    double deltaX = 999;
    double deltaY = 999;

    double distance3D_Ass = 900.; //Start with a big value
    double deltaR_Ass = 900.; //Start with a big value
    //    bool assoc = false;

    bool foundAssociated = false;
   
    unsigned int iAssociationIndexLast = 0; iAssociationIndexLast = iAssociationIndexLast;

    unsigned int jAssociationCounter = 0;
    unsigned int jAssociationCounterLast = 0;

    if ( isGoodSimulation )
    {

      for ( unsigned int j = 0; j < trackingVtxHandle->size(); j++ )
      {
        TrackingVertex thisVtx = trackingVtxHandle->at(j);

        /// Check the Vertex is Nucl Int
        if ( thisVtx.nSourceTracks() < 1 )
          continue;
        // Extra Check the Vertex is Nuclear Interection
        if ( ! (isNuclearInteraction( thisVtx )) )
          continue;
        jAssociationCounter++;

        /// Calculate all possible forms of distance
        const math::XYZTLorentzVector thisRecMomentumInc = thisDisplacedVtx.primaryMomentum("PI", false, 0.0);
        math::XYZVectorD thisSimMomentumInc = (*thisVtx.sourceTracks_begin())->momentum();

        deltaPt = sqrt(thisSimMomentumInc.Perp2()) - sqrt(thisRecMomentumInc.Perp2());
        //deltaPhi = thisSimMomentumInc.Phi() - thisRecMomentumInc.Phi();
        deltaPhi = reco::deltaPhi( thisSimMomentumInc.Phi(), thisRecMomentumInc.Phi() );
        deltaTheta = thisSimMomentumInc.Theta() - thisRecMomentumInc.Theta();
        deltaX = thisVtx.position().x() - thisDisplacedVtx.position().x();
        deltaY = thisVtx.position().y() - thisDisplacedVtx.position().y();
        deltaZ = thisVtx.position().z() - thisDisplacedVtx.position().z();
        deltaR  = sqrt(thisVtx.position().perp2()) - sqrt(thisDisplacedVtx.position().perp2());
        double distance3D = sqrt(deltaX*deltaX + deltaY*deltaY + deltaZ*deltaZ);

        /// Apply Selection
        bool isAssociated = true;

        // very-very loose cut of  distance3D_Ass for future test:
        if (distance3D > distance3D_Ass) isAssociated = false;
 
       // if ( !( ( fabs(thisVtx.position().eta()) < 1.2 && ( deltaR < -1.0 || deltaR > 3.0 ) ) ||
       //         ( fabs(thisVtx.position().eta()) >= 1.2 && ( deltaR < -2.0 || deltaR > 6.0 ) ) ) )
       //   isAssociated = false;

       // else if ( !( ( fabs(thisVtx.position().eta()) < 1.4 && fabs(deltaTheta) > 0.2 ) ||
       //              ( fabs(thisVtx.position().eta()) >= 1.4 && fabs(deltaTheta) > 0.1 ) ) )
       //   isAssociated = false;

       // else if ( !( ( fabs(thisVtx.position().eta()) < 1.4 && fabs(deltaPhi) > 0.04 ) ||
       //              ( fabs(thisVtx.position().eta()) >= 1.4 && fabs(deltaPhi) > 0.08 ) ) )
       //   isAssociated = false;

        //reject if we don't find association or if our new dR is large then previous
        if ( !isAssociated  || (distance3D > distance3D_Ass) )
          continue;

        distance3D_Ass = distance3D;
        deltaR_Ass = deltaR;
        foundAssociated = true;
	iAssociationIndexLast = j;
        jAssociationCounterLast = jAssociationCounter;
      }
    }

    /// Do what is needed in case of association
    /// Note that if we are running on reco, foundAssociated == false, hence we can do this
    if ( foundAssociated )
    {
      PFDV_isAssociatedMC->push_back( true );
      PFDV_deltaR2d_Associated->push_back( deltaR_Ass );
      PFDV_deltaR3d_Associated->push_back( distance3D_Ass );
      PFDV_associationMC_TrkVIdx->push_back( jAssociationCounterLast ); /// This will match the association in the output ntuple
    }
    else // don't find assosication
    {
      PFDV_isAssociatedMC->push_back( false );
      PFDV_deltaR2d_Associated->push_back( deltaR_Ass );
      PFDV_deltaR3d_Associated->push_back( distance3D_Ass );
      PFDV_associationMC_TrkVIdx->push_back( 0 );
    }

    /// Tracks
    std::vector< int > vTrack_algo;                                vTrack_algo.clear();
    std::vector< double > vTrack_pt;                               vTrack_pt.clear();
    std::vector< double > vTrack_eta;                              vTrack_eta.clear();
    std::vector< double > vTrack_phi;                              vTrack_phi.clear();
    std::vector< double > vTrack_chi2;                             vTrack_chi2.clear();
    std::vector< double > vTrack_normalizedChi2;                   vTrack_normalizedChi2.clear();
    //std::vector< bool > vTrack_isHighPurity;                       vTrack_isHighPurity.clear();
    std::vector< double > vTrack_rho;                              vTrack_rho.clear();
    std::vector< unsigned int > vTrack_numberOfValidHits;          vTrack_numberOfValidHits.clear();
    std::vector< unsigned int > vTrack_numberOfExpectedOuterHits;  vTrack_numberOfExpectedOuterHits.clear();
    std::vector< unsigned int > vTrack_closestDxyPVIdx;            vTrack_closestDxyPVIdx.clear();
    std::vector< double > vTrack_closestDxyPVIdx_dxy;              vTrack_closestDxyPVIdx_dxy.clear();
    std::vector< double > vTrack_closestDxyPVIdx_dz;               vTrack_closestDxyPVIdx_dz.clear();
    std::vector< unsigned int > vTrack_closestDzPVIdx;             vTrack_closestDzPVIdx.clear();
    std::vector< double > vTrack_closestDzPVIdx_dxy;               vTrack_closestDzPVIdx_dxy.clear();
    std::vector< double > vTrack_closestDzPVIdx_dz;                vTrack_closestDzPVIdx_dz.clear();

    unsigned int nTrackingParticles_PFDV_0p0 = 0;
    unsigned int nTrackingParticles_PFDV_0p2 = 0;
    unsigned int nTrackingParticles_PFDV_0p5 = 0;
    unsigned int nTrackingParticles_PFDV_1p0 = 0;
    unsigned int nTrackingParticles_PFDV_Out0p0 = 0;
    unsigned int nTrackingParticles_PFDV_Out0p2 = 0;
    unsigned int nTrackingParticles_PFDV_Out0p5 = 0;
    unsigned int nTrackingParticles_PFDV_Out1p0 = 0;
    double Source_Charge = -10.;

    reco::Vertex::trackRef_iterator trackDisplacedVertex;
    for ( trackDisplacedVertex = thisDisplacedVtx.tracks_begin();
          trackDisplacedVertex != thisDisplacedVtx.tracks_end();
          ++trackDisplacedVertex )
    {
 

        int QualityTrack = 0;
        bool Flag_SecondaryTrack = false;
        if( thisDisplacedVtx.isPrimaryTrack((*trackDisplacedVertex))) QualityTrack = 1; 
        if( thisDisplacedVtx.isMergedTrack((*trackDisplacedVertex))) QualityTrack = 1; 
        if( thisDisplacedVtx.isSecondaryTrack((*trackDisplacedVertex))){
            QualityTrack = 1;
            Flag_SecondaryTrack = true;
        } 
        if( QualityTrack == 0) std::cout << "Error: Track is not Primary, not Merged, not Secondary, it is rejected, see code" << std::endl;
        if( QualityTrack == 0) continue; //reject unknow type of tracks

        if(thisDisplacedVtx.isPrimaryTrack((*trackDisplacedVertex)) || thisDisplacedVtx.isMergedTrack((*trackDisplacedVertex))) 
          Source_Charge = (*trackDisplacedVertex)->charge();
        if ( (*trackDisplacedVertex)->charge() == 0 ) //reject nuetral particles
        continue;

        if( fabs((*trackDisplacedVertex)->charge()) > 2.5) continue;// reject particle out of detector acceptence 

        nTrackingParticles_PFDV_0p0++;
        if(Flag_SecondaryTrack) nTrackingParticles_PFDV_Out0p0++;

        if( (*trackDisplacedVertex)->pt() > 0.2 ) nTrackingParticles_PFDV_0p2++;
        if( (*trackDisplacedVertex)->pt() > 0.5 ) nTrackingParticles_PFDV_0p5++;
        if( (*trackDisplacedVertex)->pt() > 1.0 ) nTrackingParticles_PFDV_1p0++;
 
        if(Flag_SecondaryTrack) {
           if( (*trackDisplacedVertex)->pt() > 0.2 ) nTrackingParticles_PFDV_Out0p2++;
           if( (*trackDisplacedVertex)->pt() > 0.5 ) nTrackingParticles_PFDV_Out0p5++;
           if( (*trackDisplacedVertex)->pt() > 1.0 ) nTrackingParticles_PFDV_Out1p0++;
        }
      /// New Track!
      vTrack_pt.push_back( (*trackDisplacedVertex)->pt() );
      vTrack_algo.push_back( (*trackDisplacedVertex)->algo() );
      vTrack_eta.push_back( (*trackDisplacedVertex)->eta() );
      vTrack_phi.push_back( (*trackDisplacedVertex)->phi() );
      vTrack_chi2.push_back( (*trackDisplacedVertex)->chi2() );
      vTrack_normalizedChi2.push_back( (*trackDisplacedVertex)->normalizedChi2() );
      //vTrack_isHighPurity.push_back( (*trackDisplacedVertex)->quality((*trackDisplacedVertex)->qualityByName("HighPurity") ) ); // high purity
      // rho doesn't exit if you reconstruct PF Displaced vertex from AOD
      //std::cout << "TEST: (*trackDisplacedVertex)->innerPosition().Rho() = " << (*trackDisplacedVertex)->innerPosition().Rho() << std::endl;
      //vTrack_rho.push_back( (*trackDisplacedVertex)->innerPosition().Rho() );
      vTrack_numberOfValidHits.push_back( (*trackDisplacedVertex)->numberOfValidHits() );
      vTrack_numberOfExpectedOuterHits.push_back( 0 );//(*trackDisplacedVertex)->trackerExpectedHitsOuter().numberOfHits() );
 
      /// Look for closest PV
      double minDxy = 1000.;
      double dzMinDxy = 1000.;
      unsigned int jClosestPVDxy = 0;

      double minDz = 1000.;
      double dxyMinDz = 1000.;
      unsigned int jClosestPVDz = 0;

      for ( unsigned int j = 0; j < primaryVerticesHandle->size(); j++ )
      {
        double thisPVDxy = (*trackDisplacedVertex)->dxy( primaryVerticesHandle->at(j).position() );
        double thisPVDz = (*trackDisplacedVertex)->dz( primaryVerticesHandle->at(j).position() );

        if ( thisPVDxy < minDxy )
        {
          minDxy = thisPVDxy;
          dzMinDxy = thisPVDz;
          jClosestPVDxy = j;
        }
        if ( thisPVDz < minDz )
        {
          minDz = thisPVDz;
          dxyMinDz = thisPVDxy;
          jClosestPVDz = j;
        }
      }

      vTrack_closestDxyPVIdx.push_back( jClosestPVDxy );
      vTrack_closestDxyPVIdx_dxy.push_back( minDxy );
      vTrack_closestDxyPVIdx_dz.push_back( dzMinDxy );
      vTrack_closestDzPVIdx.push_back( jClosestPVDz );
      vTrack_closestDzPVIdx_dz.push_back( minDz );
      vTrack_closestDzPVIdx_dxy.push_back( dxyMinDz );
    }

    if(nTrackingParticles_PFDV_0p0 < 3) thisDisplacedVtx.Dump();
    if(nTrackingParticles_PFDV_0p0 < 3) FlagLess3TracksFromVertex = true;
    PFDV_numberOfTracks_0p0->push_back( nTrackingParticles_PFDV_0p0 );
    PFDV_numberOfTracks_0p2->push_back( nTrackingParticles_PFDV_0p2 );
    PFDV_numberOfTracks_0p5->push_back( nTrackingParticles_PFDV_0p5 );
    PFDV_numberOfTracks_1p0->push_back( nTrackingParticles_PFDV_1p0 );
    PFDV_numberOfTracks_Out0p0->push_back( nTrackingParticles_PFDV_Out0p0 );
    PFDV_numberOfTracks_Out0p2->push_back( nTrackingParticles_PFDV_Out0p2 );
    PFDV_numberOfTracks_Out0p5->push_back( nTrackingParticles_PFDV_Out0p5 );
    PFDV_numberOfTracks_Out1p0->push_back( nTrackingParticles_PFDV_Out1p0 );

    PFDV_Inc_charge->push_back( Source_Charge );

    PFDV_vTrack_algo->push_back( vTrack_algo );
    PFDV_vTrack_pt->push_back( vTrack_pt );
    PFDV_vTrack_eta->push_back( vTrack_eta );
    PFDV_vTrack_phi->push_back( vTrack_phi );
    PFDV_vTrack_chi2->push_back( vTrack_chi2 );
    PFDV_vTrack_normalizedChi2->push_back( vTrack_normalizedChi2 );
    //PFDV_vTrack_isHighPurity->push_back( vTrack_isHighPurity );
    PFDV_vTrack_rho->push_back( vTrack_rho );
    PFDV_vTrack_numberOfValidHits->push_back( vTrack_numberOfValidHits );
    PFDV_vTrack_numberOfExpectedOuterHits->push_back( vTrack_numberOfExpectedOuterHits );
    PFDV_vTrack_closestDxyPVIdx->push_back( vTrack_closestDxyPVIdx );
    PFDV_vTrack_closestDxyPVIdx_dxy->push_back( vTrack_closestDxyPVIdx_dxy );
    PFDV_vTrack_closestDxyPVIdx_dz->push_back( vTrack_closestDxyPVIdx_dz );
    PFDV_vTrack_closestDzPVIdx->push_back( vTrack_closestDzPVIdx );
    PFDV_vTrack_closestDzPVIdx_dxy->push_back( vTrack_closestDzPVIdx_dxy );
    PFDV_vTrack_closestDzPVIdx_dz->push_back( vTrack_closestDzPVIdx_dz );
  }

//if (NumberOfLooseNuclearVertex > 0) std:cout << "NumberOfLooseNuclearVertex = " << NumberOfLooseNuclearVertex << " NumberOfNuclearVertex = " << NumberOfNuclearVertex << std::endl;
if (FlagLess3TracksFromVertex) std::cout << "NumberOfLooseNuclearVertex = " << NumberOfLooseNuclearVertex << " NumberOfNuclearVertex = " << NumberOfNuclearVertex << std::endl;

  /// Fill Output Tree for MC all the time, for Data if we have RECO NI vertex
 if( (!isRealData) || (isRealData && numberOfPFDV > 0) )  outputTree->Fill();
}

/* Additional methods */
bool NtupleMakerPhotonConversions::isNuclearInteraction( const TrackingVertex& v ) const
{
  /// Geometric constraints
  if ( v.position().rho() > 120 || fabs(v.position().z())> 150 || v.position().rho() < 2 )
    return false;

  /// Vertex Mother classification
  bool bK = false;
  bool bK0s = false;
  bool bLambda = false;
  bool bGamma = false;

  TrackingVertex::tp_iterator simMother;
  TrackingVertex::tp_iterator simDaughter;

  for ( simMother = v.sourceTracks_begin();
        simMother != v.sourceTracks_end();
        ++simMother)
  {
    if ((**simMother).pdgId() == 11 || (**simMother).pdgId() == -11)
      return false;

    bGamma = ((**simMother).pdgId() == 22);
    bK0s = ((**simMother).pdgId() == 310 || (**simMother).pdgId() == -310);
    bLambda = ((**simMother).pdgId() == 3122 || (**simMother).pdgId() == -3122);
    bK = ((**simMother).pdgId() == 321 || (**simMother).pdgId() == -321);
  }

  /// Prepare list of Vertex Daughters
  std::vector< int > pdgIds;

  for ( simDaughter = v.daughterTracks_begin();
        simDaughter != v.daughterTracks_end();
        ++simDaughter)
  {
    pdgIds.push_back((**simDaughter).pdgId());
  }

  /// Define decays and reject them
  bool bK0sDecay = bK0s &&
                   v.nDaughterTracks() == 2 &&
                   ( (pdgIds[0] == 211 && pdgIds[1] == -211) ||
                     (pdgIds[0] == -211 && pdgIds[1] == 211) );
  if ( bK0sDecay )
    return false;

  bool bLambdaDecay = bLambda &&
                      v.nDaughterTracks() == 2 &&
                      ( (pdgIds[0] == -211 && pdgIds[1] == 2212) ||
                        (pdgIds[0] == 2212 && pdgIds[1] == -211) ||
                        (pdgIds[0] == 211 && pdgIds[1] == -2212) ||
                        (pdgIds[0] == -2212 && pdgIds[1] == 211) );
  if ( bLambdaDecay )
    return false;

  if ( bGamma )
    return false;

  bool bKDecay = bK &&
                 ( pdgIds[0] == 13 || pdgIds[0] == -13 ) &&
                 v.nDaughterTracks() == 1;
  if ( bKDecay )
    return false;

  /// Default means all exceptions failed
  return true;
}

bool NtupleMakerPhotonConversions::isKaonDecay( const TrackingVertex& v ) const
{
  /// Vertex Mother classification
  bool bKPlus = false;
  bool bKMinus = false;

  TrackingVertex::tp_iterator simMother;
  TrackingVertex::tp_iterator simDaughter;

  for ( simMother = v.sourceTracks_begin();
        simMother != v.sourceTracks_end();
        ++simMother)
  {
    bKPlus = bKPlus || (**simMother).pdgId() == 321;
    bKMinus = bKMinus || (**simMother).pdgId() == -321;
  }

  /// Prepare list of Vertex Daughters
  std::vector< int > pdgIds;
  int i = -1;
  for ( simDaughter = v.daughterTracks_begin();
        simDaughter != v.daughterTracks_end();
        ++simDaughter)
  {
    pdgIds.push_back((**simDaughter).pdgId());
    i++;
  }

  bKPlus = bKPlus && pdgIds[0]==-13;
  bKMinus = bKMinus && pdgIds[0]==13;

  if (bKPlus || bKMinus)
    return true;

  return false;
}

bool NtupleMakerPhotonConversions::isConversion( const TrackingVertex& v ) const
{
  /// Geometric constraints
  if ( v.position().rho() > 120 || fabs(v.position().z())> 150 || v.position().rho() < 2 )
    return false;

  /// Vertex Mother classification
  TrackingVertex::tp_iterator simMother;
  for ( simMother = v.sourceTracks_begin();
        simMother != v.sourceTracks_end();
        ++simMother)
  {
    if ( (**simMother).pdgId() == 22 )
      return true;
  }

  return false;
}

double NtupleMakerPhotonConversions::VectorParallelR( const TrackingVertex& VecSim, const reco::PFDisplacedVertex& VecPF) const
{
// find Parallel of dR between vectors

double dVecX = VecSim.position().x() - VecPF.position().x(); 
double dVecY = VecSim.position().y() - VecPF.position().y(); 
double dVecZ = VecSim.position().z() - VecPF.position().Z(); 
double dR_par = VecSim.position().x()*dVecX + VecSim.position().y()*dVecY + VecSim.position().z()*dVecZ;
double abs_vec = sqrt(VecSim.position().x()*VecSim.position().x() + VecSim.position().y()*VecSim.position().y() + VecSim.position().z()*VecSim.position().z());

if (abs_vec > 0) dR_par = fabs(dR_par/abs_vec);
else dR_par = 1000.;

return dR_par;

}

double NtupleMakerPhotonConversions::VectorPerpendicularR( const TrackingVertex& VecSim, const reco::PFDisplacedVertex& VecPF) const
{
// find Perpendicular of dR between vectors

double dVecX = VecSim.position().x() - VecPF.position().x(); 
double dVecY = VecSim.position().y() - VecPF.position().y(); 
double dVecZ = VecSim.position().z() - VecPF.position().Z(); 
double dR_perX = VecSim.position().y()*dVecZ -VecSim.position().z()*dVecY; 
double dR_perY = VecSim.position().z()*dVecX -VecSim.position().x()*dVecZ; 
double dR_perZ = VecSim.position().x()*dVecY -VecSim.position().y()*dVecX; 
double abs_vec = sqrt(VecSim.position().x()*VecSim.position().x() + VecSim.position().y()*VecSim.position().y() + VecSim.position().z()*VecSim.position().z());

double dR_per = sqrt(dR_perX*dR_perX + dR_perY*dR_perY + dR_perZ*dR_perZ);

if (abs_vec > 0) dR_per = dR_per/abs_vec;
else dR_per = 1000.;

return dR_per;
}


/// Define this as a plug-in
DEFINE_FWK_MODULE( NtupleMakerPhotonConversions );
